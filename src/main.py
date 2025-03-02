from fastapi import FastAPI
from src.db import db_connect
from uuid import UUID
import uuid

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
def get_customer(customer_id: UUID):
    conn = db_connect()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM customers where id = %s", (str(customer_id),))
        customer = cursor.fetchone()
    except Exception as e:
        return {"error": str(e)}
    return customer

@app.post("/api/v1/customers")
def create_customer():
    conn = db_connect()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("insert into customers (id, first_name, middle_name, last_name, phone, email) values (%s, %s, %s, %s, %s, %s)", (str(uuid.uuid4()), "a", "b", "c", "1234567890", "abc@gmail.com"))
        conn.commit()
    except Exception as e:
        return {"error": str(e)}
    return {"message": "Customer created"}    

@app.put("/api/v1/customers/{customer_id}")
def update_customer(customer_id: UUID):
    conn = db_connect()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM customers")
        customers = cursor.fetchall()
    except Exception as e:
        return {"error": str(e)}
    return customers

@app.patch("/api/v1/customers/{customer_id}")
def patch_customer(customer_id: UUID):
    conn = db_connect()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM customers")
        customers = cursor.fetchall()
    except Exception as e:
        return {"error": str(e)}
    return customers

@app.delete("/api/v1/customers/{customer_id}")
def delete_customer(customer_id: UUID):
    conn = db_connect()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM customers")
        customers = cursor.fetchall()
    except Exception as e:
        return {"error": str(e)}
    return customers

