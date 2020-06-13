from fastapi import FastAPI
from src.services.create_basket_service import CreateBasketService
from src.model.repository.basket_writer_repository import FileBasketWriterRepository

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/basket")
def create_basket():
    writer = FileBasketWriterRepository()
    service = CreateBasketService(writer)
    output = service.execute()
    return output


@app.get("/basket/{item_id}")
def get_basket(item_id: int):
    return {"item_id": item_id}


@app.delete("/basket/{item_id}")
def delete_basket(item_id: int):
    return {"item_id": item_id}


@app.post("/basket/{item_id}")
def update_basket(item_id: int):
    return {"item_id": item_id}


@app.post("/basket/{item_id}/add")
def add_product_to_basket(item_id: int):
    return {"item_id": item_id}
