from fastapi import Request
from fastapi.responses import JSONResponse
from app.domain.exceptions.domain_exceptions import ProblemDetailError

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
