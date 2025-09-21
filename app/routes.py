from fastapi import APIRouter
from app.models import Patient, Condition
from app.services import map_disease_to_codes

router = APIRouter()

patients = {}
conditions = []

@router.post("/patients/")
def create_patient(patient: Patient):
    patients[patient.id] = patient
    return patient

@router.get("/patients/{patient_id}")
def get_patient(patient_id: int):
    return patients.get(patient_id, {"error": "Not found"})

@router.post("/conditions/")
def create_condition(condition: Condition):
    conditions.append(condition)
    return condition

@router.get("/patients/{patient_id}/conditions")
def get_conditions(patient_id: int):
    return [c for c in conditions if c.patient_id == patient_id]

@router.get("/map/{disease}")
def map_codes(disease: str):
    return {
        "disease": disease,
        "codes": map_disease_to_codes(disease)
    }
