from fastapi import FastAPI, HTTPException
from fastapi import Response, status
from pydantic import BaseModel, Field

from src.config import BASKET_DB_PATH
from src.model.repository.basket_reader_repository import FileBasketReaderRepository
from src.model.repository.basket_writer_repository import FileBasketWriterRepository
from src.model.repository.product_reader_repository import DictionaryProductReaderRepository
from src.model.repository.discount_reader_repository import DictionaryDiscountReaderRepository
from src.exceptions import BasketFileNotFoundException
from src.exceptions import ProductNotFoundException
from src.services.checkout_basket_service import CheckoutBasketService
from src.services.create_basket_service import CreateBasketService
from src.services.delete_basket_service import DeleteBasketService
from src.services.update_basket_service import UpdateBasketService


app = FastAPI()


class ProductDTOApi(BaseModel):
    """
        DTO object to be treated in update_basket endpoint.
        Acts as part of endpoint definition
    """
    product_code: str
    amount: int = Field(1, gt=0, description="Amount must be greater than zero")


@app.post("/basket", status_code=200)
def create_basket(response: Response):
    writer = FileBasketWriterRepository(BASKET_DB_PATH)
    service = CreateBasketService(writer)
    output = service.execute()
    response.status_code = status.HTTP_201_CREATED
    return output


@app.delete("/basket/{basket_id}")
def delete_basket(basket_id: int):
    writer = FileBasketWriterRepository(BASKET_DB_PATH)
    service = DeleteBasketService(writer)
    try:
        output = service.execute(basket_id)
        return output
    except BasketFileNotFoundException:
        raise HTTPException(status_code=404, detail="Basket not found")


@app.post("/basket/{basket_id}/product")
def update_basket(basket_id: int, product: ProductDTOApi):
    basket_reader = FileBasketReaderRepository(BASKET_DB_PATH)
    basket_writer = FileBasketWriterRepository(BASKET_DB_PATH)
    product_reader = DictionaryProductReaderRepository()
    try:
        service = UpdateBasketService(basket_writer, basket_reader, product_reader)
        output = service.execute(basket_id, product.product_code, product.amount)
        return output
    except BasketFileNotFoundException:
        raise HTTPException(status_code=404, detail="Basket not found")
    except ProductNotFoundException:
        raise HTTPException(status_code=404, detail="Product not found")


@app.get("/basket/{basket_id}")
def get_basket_checkout(basket_id: int):
    basket_reader = FileBasketReaderRepository(BASKET_DB_PATH)
    discount_reader = DictionaryDiscountReaderRepository()
    try:
        service = CheckoutBasketService(basket_reader, discount_reader)
        output = service.execute(basket_id)
        return output
    except BasketFileNotFoundException:
        raise HTTPException(status_code=404, detail="Basket not found")
    except ProductNotFoundException:
        raise HTTPException(status_code=404, detail="Product not found")
