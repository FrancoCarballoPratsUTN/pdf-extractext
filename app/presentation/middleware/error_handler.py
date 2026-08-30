from fastapi import Request
from fastapi.responses import JSONResponse

from app.config.logging_config import loger
from app.domain.exceptions.domain_exceptions import ProblemDetailError


async def problem_detail_handler(request: Request, exc: ProblemDetailError):
    """
    Handle ProblemDetailError exceptions and return a JSON response with problem details.
    Args:
        request (Request): The incoming HTTP request.
        exc (ProblemDetailError): The exception instance containing problem details.
    Returns:
        JSONResponse: A JSON response containing the problem details.
    """
    loger.warning(f"ProblemDetailError: {exc.title} - {exc.detail}", extra={"type": exc.type, "status": exc.status, "instance": request.url.path})

    return  JSONResponse(
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
