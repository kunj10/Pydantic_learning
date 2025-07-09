# to enhance the code quality using validations specially 1) type validation 2) value validation


from pydantic import BaseModel, Field, EmailStr, field_validator
from typing import List, Dict, Optional


class Patient(BaseModel):
    name: str 
    email: EmailStr 
    age: int 
    weight: float 
    married: bool 
    allergies: Optional[List[str]] 
    contact : Dict[str, str] 
    
    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
      valid_domains = ['hdfc.com', 'icici.com', 'outlook.com']
      domainname = value.split('@')[-1]
      if domainname not in valid_domains:
          raise ValueError('not a valid email domain')
      return value
    
    
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
    "age": 30,
    "weight": 70.5,
    "married": True,
    "allergies": ["pollen", "nuts"],
    "contact": {
        "address": "123 Main St, Springfield",
        "phone": "123-456-7890"}
}

patient1 = Patient(**patient_info)


instert_data(patient1)
