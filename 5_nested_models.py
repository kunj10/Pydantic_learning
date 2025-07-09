from pydantic import BaseModel

class address(BaseModel):
    
    city: str
    state: str
    zip_code: str

class Patient(BaseModel):
    name: str 
    gender: str
    age: int 
    address: address
    
    
address_info = {
    "city": "Springfield",
    "state": "IL",
    "zip_code": "62701"
}
    
address1 = address(**address_info)

patient = {
    "name": "John Doe",
    "gender" : "male",
    "age": 30,
    "address": address1
}

patient1 = Patient(**patient)


def instert_data(patient : Patient):
    print(patient.name)
    print(patient.gender)
    print(patient.age)
    print(patient.address) 
  
instert_data(patient1)  
    