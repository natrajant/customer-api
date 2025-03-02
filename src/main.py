from fastapi import FastAPI, HTTPException
from src.db import db_connect
from src.models import Customer
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
def create_customer(customer: Customer):
    conn = db_connect()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("insert into customers (id, first_name, middle_name, last_name, phone, email) values (%s, %s, %s, %s, %s, %s)", (str(uuid.uuid4()), customer.first_name, customer.middle_name, customer.last_name, customer.phone, customer.email))
        conn.commit()
    except Exception as e:
        return {"error": str(e)}
    return {"message": "Customer created"}    

@app.put("/api/v1/customers/{customer_id}")
def update_customer(customer_id: UUID, customer: Customer):
    try:
        if not get_customer(customer_id):
            raise HTTPException(status_code=404, detail="Customer not found")
        
        conn = db_connect()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("UPDATE customers SET first_name = %s, middle_name = %s, last_name = %s, email = %s, phone = %s WHERE id = %s", (customer.first_name, customer.middle_name, customer.last_name, customer.email, customer.phone, str(customer_id)))
        conn.commit()
    except Exception as e:
        return {"error": str(e)}
    return {"message": "Customer updated"}

@app.patch("/api/v1/customers/{customer_id}")
def patch_customer(customer_id: UUID, status_code=200):
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

