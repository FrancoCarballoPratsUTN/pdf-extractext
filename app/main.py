from fastapi import FastAPI
from app.presentation.routes.document_upload import router as document_upload_router

app = FastAPI()
app.include_router(document_upload_router)
