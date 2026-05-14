from fastapi import Request
from fastapi.responses import JSONResponse
from app.domain.exceptions import ProblemDetailError

async def problem_detail_handler(request: Request, exc: ProblemDetailError):
    """
    Transform any exception that inherits from ProblemDetailError
    into a JSON response conforming to RFC 9457.
    """
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