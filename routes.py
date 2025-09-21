# app/routes.py

from fastapi import APIRouter, HTTPException
from app import db, models, services

router = APIRouter()

# ------------------------
# 1. Get all NAMASTE codes
# ------------------------
@router.get("/namaste")
def get_namaste_codes():
    return db.namaste_data  # from db.py (CSV loaded as dict)


# ------------------------
# 2. Get all ICD-11 codes
# ------------------------
@router.get("/icd11")
def get_icd11_codes():
    return db.icd11_data


# ------------------------
# 3. Search NAMASTE by term
# ------------------------
@router.get("/namaste/search/{term}")
def search_namaste(term: str):
    results = services.search_codes(db.namaste_data, term)
    if not results:
        raise HTTPException(status_code=404, detail="No matching NAMASTE code found")
    return results


# ------------------------
# 4. Search ICD-11 by term
# ------------------------
@router.get("/icd11/search/{term}")
def search_icd11(term: str):
    results = services.search_codes(db.icd11_data, term)
    if not results:
        raise HTTPException(status_code=404, detail="No matching ICD-11 code found")
    return results


# ------------------------
# 5. Get mapping from NAMASTE → ICD-11
# ------------------------
@router.get("/map/{namaste_code}")
def map_to_icd11(namaste_code: str):
    mapping = services.map_code(namaste_code, db.mapping_data)
    if not mapping:
        raise HTTPException(status_code=404, detail="Mapping not found")
    return mapping
