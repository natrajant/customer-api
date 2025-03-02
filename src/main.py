from fastapi import FastAPI, HTTPException
from src.db import db_connect
from src.models import Customer, CustomerPatchModel
from uuid import UUID
import uuid
import logging
logging.basicConfig(filename='app.log',level=logging.INFO , format='%(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

app = FastAPI()

@app.get("/api/v1")
def index():
    return {"message": "Customer API"}


@app.get("/api/v1/customers")
def get_customers():
    logger.info("GET /api/v1/customers")
    
    try:
        conn = db_connect()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM customers")
        customers = cursor.fetchall()
    except Exception as e:
        logger.error(f"Error: {str(e)}")    
        return {"error": str(e)}
    return customers

@app.get("/api/v1/customers/{customer_id}")
def get_customer(customer_id: UUID):
    logger.info(f"GET /api/v1/customers/{customer_id}")
    
    try:
        conn = db_connect()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM customers where id = %s", (str(customer_id),))
        customer = cursor.fetchone()
    except Exception as e:
        logger.error(f"Error: {str(e)}")  
        return {"error": str(e)}
    return customer

@app.post("/api/v1/customers")
def create_customer(customer: Customer):
    logger.info(f"POST /api/v1/customers")
    
    try:
        conn = db_connect()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("insert into customers (id, first_name, middle_name, last_name, phone, email) values (%s, %s, %s, %s, %s, %s)", (str(uuid.uuid4()), customer.first_name, customer.middle_name, customer.last_name, customer.phone, customer.email))
        conn.commit()
    except Exception as e:
        logger.error(f"Error: {str(e)}")  
        return {"error": str(e)}
    return {"message": "Customer created"}    

@app.put("/api/v1/customers/{customer_id}")
def update_customer(customer_id: UUID, customer: Customer):
    logger.info(f"PUT /api/v1/customers/{customer_id}")
    try:
        if not get_customer(customer_id):
            logger.error(f"Error: Customer not found")  
            raise HTTPException(status_code=404, detail="Customer not found")
        
        conn = db_connect()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("UPDATE customers SET first_name = %s, middle_name = %s, last_name = %s, email = %s, phone = %s WHERE id = %s", (customer.first_name, customer.middle_name, customer.last_name, customer.email, customer.phone, str(customer_id)))
        conn.commit()
    except Exception as e:
        logger.error(f"Error: {str(e)}")  
        return {"error": str(e)}
    return {"message": "Customer updated"}

@app.patch("/api/v1/customers/{customer_id}")
def patch_customer(customer_id: UUID, customer: CustomerPatchModel):
    logger.info(f"PATCH /api/v1/customers/{customer_id}")
    try:
        if not get_customer(customer_id):
            logger.error(f"Error: Customer not found")  
            raise HTTPException(status_code=404, detail="Customer not found")
        
        conn = db_connect()
        cursor = conn.cursor(dictionary=True)
        # cursor.execute("UPDATE customers SET first_name = %s, middle_name = %s, last_name = %s, email = %s, phone = %s WHERE id = %s", (customer.first_name, customer.middle_name, customer.last_name, customer.email, customer.phone, str(customer_id)))
        if customer.dict(exclude_unset=True).items():
            sql = "UPDATE customers SET "
            fields = []
            for key, value in customer.dict(exclude_unset=True).items():
                fields.append(f"{key} = '{value}'")
            sql += ", ".join(fields)
            sql += f" WHERE id = '{str(customer_id)}'"
            cursor.execute(sql)
            
            conn.commit()
    except Exception as e:
        logger.error(f"Error: {str(e)}")  
        return {"error": str(e)}
    return {"message": "Customer updated"}

@app.delete("/api/v1/customers/{customer_id}")
def delete_customer(customer_id: UUID):
    logger.info(f"DELETE /api/v1/customers/{customer_id}")
    try:
        if not get_customer(customer_id):
            logger.error(f"Error: Customer not found")  
            raise HTTPException(status_code=404, detail="Customer not found")
        
        conn = db_connect()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("delete FROM customers where id = %s", (str(customer_id),))
        conn.commit()
    except Exception as e:
        logger.error(f"Error: {str(e)}")  
        return {"error": str(e)}
    return {"message": "Customer deleted"}
