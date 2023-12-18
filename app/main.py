from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "test"}

@app.get("/customers/{customer_id}")
async def read_customer(customer_id: int):
    return {"customer_id": customer_id}

