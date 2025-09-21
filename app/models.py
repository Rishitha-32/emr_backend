from pydantic import BaseModel

class Patient(BaseModel):
    id: int
    name: str
    age: int

class Condition(BaseModel):
    patient_id: int
    disease: str
    namaste_code: str
    icd11_code: str

class CodeMapping(BaseModel):
    disease: str
    namaste: str
    icd11: str
