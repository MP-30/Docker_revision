from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Test 1: Simple GET request
@app.get("/health")
def read_health():
    return {"status": "up and running", "message": "Docker is working!"}

# Test 2: POST request with data
class Item(BaseModel):
    name: str
    price: float

@app.post("/test-data")
def create_item(item: Item):
    return {"message": f"Received {item.name}", "total_price": item.price * 1.05}

