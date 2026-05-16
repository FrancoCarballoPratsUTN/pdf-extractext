from app.presentation.middleware.error_handler import problem_detail_handler
from fastapi import FastAPI
from app.domain.exceptions.domain_exceptions import ProblemDetailError
from app.presentation.routes.document_upload import router as document_upload_router
from app.presentation.routes.document_find_by_checksum import router as document_find_by_checksum_router
from app.presentation.routes.document_update import router as document_update_router
from app.presentation.routes.document_delete import router as document_delete_router
from app.presentation.routes.document_save import router as document_save_router
from app.presentation.routes.audit_routes import router as audit_find_router

app = FastAPI()

app.add_exception_handler(ProblemDetailError, problem_detail_handler)
app.include_router(document_upload_router)
app.include_router(document_find_by_checksum_router)
app.include_router(document_update_router)
app.include_router(document_delete_router)
app.include_router(document_save_router)
app.include_router(audit_find_router)