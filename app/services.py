from app.db import get_mapping

def map_disease_to_codes(disease: str):
    return get_mapping(disease)
