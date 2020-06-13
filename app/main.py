from fastapi import FastAPI, HTTPException
from fastapi import Response, status
from pydantic import BaseModel

from src.model.repository.basket_writer_repository import FileBasketWriterRepository
from src.model.repository.product_reader_repository import DictionaryProductReaderRepository
from src.exceptions import BasketFileNotFoundException
from src.exceptions import ProductNotFoundException
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
    amount: int = 1


@app.post("/basket", status_code=200)
def create_basket(response: Response):
    writer = FileBasketWriterRepository()
    service = CreateBasketService(writer)
    output = service.execute()
    response.status_code = status.HTTP_201_CREATED
    return output


@app.get("/basket/{basket_id}")
def get_basket(basket_id: int):
    return {"item_id": basket_id}


@app.delete("/basket/{basket_id}")
def delete_basket(basket_id: int):
    writer = FileBasketWriterRepository()
    service = DeleteBasketService(writer)
    try:
        output = service.execute(basket_id)
        return output
    except BasketFileNotFoundException:
        raise HTTPException(status_code=404, detail="Basket not found")


@app.patch("/basket/{basket_id}")
def update_basket(basket_id: int, product: ProductDTOApi):
    writer = FileBasketWriterRepository()
    reader = DictionaryProductReaderRepository()
    print(product)
    try:
        service = UpdateBasketService(writer, reader)
        service.execute(basket_id, product.product_code, product.amount)
    except BasketFileNotFoundException:
        raise HTTPException(status_code=404, detail="Basket not found")
    except ProductNotFoundException:
        raise HTTPException(status_code=404, detail="Product not found")

    return {"added item_id": basket_id}
