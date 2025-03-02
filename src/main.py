from fastapi import FastAPI

app = FastAPI()

@app.get("/api/v1")
def index():
    return {"message": "Customer API"}


@app.get("/api/v1/customers")
def get_customers():
    pass

@app.get("/api/v1/customers/{customer_id}")
def get_customer(customer_id: int):
    pass

@app.post("/api/v1/customers")
def create_customer():
    pass    

@app.put("/api/v1/customers/{customer_id}")
def update_customer(customer_id: int):
    pass

@app.patch("/api/v1/customers/{customer_id}")
def patch_customer(customer_id: int):
    pass

@app.delete("/api/v1/customers/{customer_id}")
def delete_customer(customer_id: int):
    pass

