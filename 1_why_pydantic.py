# to enhance the code quality using validations specially 1) type validation 2) value validation


from pydantic import BaseModel, Field, ValidationError, EmailStr
from typing import List, Dict, Optional


class Patient(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)  # Field with a minimum length of 1 and maximum length of 100
    email: EmailStr # Validates that the email is in correct format
    age: int  = Field(gt=0, le=120)  # Field with a value greater than 0 and less than or equal to 120
    weight: float = Field(gt=0)  # Field with a value greater than 0
    married: bool = False # Default value is False
    allergies: Optional[List[str]] = None # Optional allows this field to be None
    contact : Dict[str, str] 
    
    
def instert_data(patient : Patient):
    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)  
    print(patient.contact)  
        
        
patient_info = {
    "name": "John Doe", 
    "email": "abc@gmail.com",
    "age": 30,
    "weight": 70.5,
    "married": True,
    "contact": {
        "address": "123 Main St, Springfield",
        "phone": "123-456-7890"}
}

patient1 = Patient(**patient_info)


instert_data(patient1)
