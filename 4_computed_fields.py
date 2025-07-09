
from pydantic import BaseModel, Field, EmailStr, computed_field
from typing import List, Dict, Optional


class Patient(BaseModel):
    name: str 
    email: EmailStr 
    age: int 
    weight: float 
    height: float
    married: bool 
    allergies: Optional[List[str]] 
    contact : Dict[str, str] 
    
    @computed_field
    @property
    def bmi(self) -> float:
        if self.height <= 0:
            raise ValueError("Height must be greater than zero to calculate BMI.")
        return round(self.weight / (self.height ** 2), 2)
    
    
def instert_data(patient : Patient):
    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.weight)
    print(patient.height)
    print(patient.bmi)  # Using the computed field
    print(patient.married)
    print(patient.allergies)  
    print(patient.contact)  
        
        
patient_info = {
    "name": "John Doe", 
    "email": "abc@hdfc.com",
    "age": 30,
    "weight": 70.5,
    "height": 1.75,  # Height in meters
    "married": True,
    "allergies": ["pollen", "nuts"],
    "contact": {
        "address": "123 Main St, Springfield",
        "phone": "123-456-7890"}
}

patient1 = Patient(**patient_info)


instert_data(patient1)
