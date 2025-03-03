from sqlmodel import SQLModel
from typing import Optional

# Customer model (used for POST, PUT)
# Validates the fields that are passed in the request
# All fields are required except middle_name
class Customer(SQLModel):
    first_name: str
    middle_name: Optional[str] = None
    last_name: str
    phone: str
    email: str

# Customer model (used for PATCH)
# All fields are marked as optional because PATCH request 
# can contain only the fields that need to be updated
class CustomerPatchModel(Customer):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None

"""
Improvements:
- Field validation
- ORM integration like SQLAlchemy
- Custom validation like email, phone etc. validation
"""
