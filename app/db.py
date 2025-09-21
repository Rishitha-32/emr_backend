import pandas as pd

# Load CSVs
namaste_df = pd.read_csv("data/namaste_codes.csv")
icd11_df = pd.read_csv("data/icd11_codes.csv")
mapping_df = pd.read_csv("data/mapping.csv")

def get_namaste_code(disease: str):
    row = namaste_df[namaste_df["disease"] == disease]
    return row.iloc[0]["code"] if not row.empty else None

def get_icd11_code(disease: str):
    row = icd11_df[icd11_df["disease"] == disease]
    return row.iloc[0]["code"] if not row.empty else None

def get_mapping(disease: str):
    row = mapping_df[mapping_df["disease"] == disease]
    if not row.empty:
        return {
            "namaste": row.iloc[0]["namaste_code"],
            "icd11": row.iloc[0]["icd11_code"]
        }
    return None
