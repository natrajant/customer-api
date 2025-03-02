from sqlmodel import SQLModel
from typing import Optional

class Customer(SQLModel):
    first_name: str
    middle_name: Optional[str] = None
    last_name: str
    phone: str
    email: str
