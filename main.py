from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="EMR Backend with NAMASTE + ICD-11 Integration")

# include routes
app.include_router(router)
