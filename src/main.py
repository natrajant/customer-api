from fastapi import FastAPI
from src.db import db_connect


app = FastAPI()

@app.get("/api/v1")
def index():
    return {"message": "Customer API"}


@app.get("/api/v1/customers")
def get_customers():
    conn = db_connect()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM customers")
        customers = cursor.fetchall()
    except Exception as e:
        return {"error": str(e)}
    return customers

@app.get("/api/v1/customers/{customer_id}")
def get_customer(customer_id: int):
    conn = db_connect()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM customers")
        customers = cursor.fetchall()
    except Exception as e:
        return {"error": str(e)}
    return customers

@app.post("/api/v1/customers")
def create_customer():
    conn = db_connect()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM customers")
        customers = cursor.fetchall()
    except Exception as e:
        return {"error": str(e)}
    return customers    

@app.put("/api/v1/customers/{customer_id}")
def update_customer(customer_id: int):
    conn = db_connect()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM customers")
        customers = cursor.fetchall()
    except Exception as e:
        return {"error": str(e)}
    return customers

@app.patch("/api/v1/customers/{customer_id}")
def patch_customer(customer_id: int):
    conn = db_connect()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM customers")
        customers = cursor.fetchall()
    except Exception as e:
        return {"error": str(e)}
    return customers

@app.delete("/api/v1/customers/{customer_id}")
def delete_customer(customer_id: int):
    conn = db_connect()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM customers")
        customers = cursor.fetchall()
    except Exception as e:
        return {"error": str(e)}
    return customers

