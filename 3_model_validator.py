# to enhance the code quality using validations specially 1) type validation 2) value validation


from pydantic import BaseModel, Field, EmailStr, field_validator, model_validator
from typing import List, Dict, Optional


class Patient(BaseModel):
    name: str 
    email: EmailStr 
    age: int 
    weight: float 
    married: bool 
    allergies: Optional[List[str]] 
    contact : Dict[str, str] 
    
    @model_validator(mode='after')
    def validate_contact(cls, model):
      if model.age>60 and 'emergency' not in model.contact:
          raise ValueError('Emergency contact is required for patients over 60 years old')
      return model
    
    
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
    "email": "abc@hdfc.com",
    "age": 75,
    "weight": 70.5,
    "married": True,
    "allergies": ["pollen", "nuts"],
    "contact": {
        "address": "123 Main St, Springfield",
        "phone": "123-456-7890",
        "emergency": "987-654-3210" }
}

patient1 = Patient(**patient_info)


instert_data(patient1)
