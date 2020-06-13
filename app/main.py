from fastapi import FastAPI, HTTPException
from src.model.repository.basket_writer_repository import FileBasketWriterRepository
from src.exceptions import BasketFileNotFoundException
from src.services.create_basket_service import CreateBasketService
from src.services.delete_basket_service import DeleteBasketService


app = FastAPI()


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


@app.post("/basket/{basket_id}")
def update_basket(basket_id: int):
    return {"item_id": basket_id}


@app.post("/basket/{basket_id}/add")
def add_product_to_basket(basket_id: int):
    return {"item_id": basket_id}
