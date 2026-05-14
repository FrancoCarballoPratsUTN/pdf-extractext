from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.domain.exceptions.domain_exceptions import ProblemDetailError
from app.presentation.routes.document_upload import router as document_upload_router
from app.presentation.routes.document_find_by_checksum import router as document_find_by_checksum_router
from app.presentation.routes.document_update import router as document_update_router
from app.presentation.routes.document_delete import router as document_delete_router
from app.presentation.routes.document_save import router as document_save_router

app = FastAPI()

@app.exception_handler(ProblemDetailError)
async def problem_detail_handler(request: Request, exc: ProblemDetailError):
    return JSONResponse(
        status_code=exc.status,
        content={
            "type": exc.type,
            "title": exc.title,
            "status": exc.status,
            "detail": exc.detail,
            "instance": request.url.path 
        },
        media_type="application/problem+json"
    )

app.include_router(document_upload_router)
app.include_router(document_find_by_checksum_router)
app.include_router(document_update_router)
app.include_router(document_delete_router)
app.include_router(document_save_router)