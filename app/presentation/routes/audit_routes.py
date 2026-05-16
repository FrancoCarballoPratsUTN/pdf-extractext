from app.presentation.schemas.exception_response import ProblemDetailsSchema
from app.presentation.schemas.audit_log_response import AuditLogSchema
from fastapi import APIRouter, Depends
from app.domain.use_cases.audit.find_audit_by_checksum_use_case import FindAuditLogsByChecksumUseCase
from app.domain.use_cases.audit.find_audit_use_case import FindAuditLogsUseCase
from app.infrastructure.dependencies.dependencies import get_find_audit_use_case, get_find_audit_by_checksum

router = APIRouter(prefix="/audit")

@router.get("/logs", 
            response_model=list[AuditLogSchema],
            responses={
                200: {"description": "Successfully retrieved audit logs"},
                500: {"model": ProblemDetailsSchema, "description": "Internal server error while retrieving audit logs"}
            }) 
async def get_audit_logs(skip: int = 0, limit: int = 10, use_case: FindAuditLogsUseCase = Depends(get_find_audit_use_case)):
    """Endpoint to retrieve all audit logs with pagination."""
    return use_case.execute(skip, limit)

@router.get("/logs/checksum/{checksum}", 
            response_model=list[AuditLogSchema], 
            responses={
                200: {"description": "Successfully retrieved audit logs"},
                404: {"model": ProblemDetailsSchema, "description": "No audit logs found with the specified checksum"},
                500: {"model": ProblemDetailsSchema, "description": "Internal server error while retrieving audit logs"}
            })
async def get_audit_logs_by_checksum(checksum: str, use_case: FindAuditLogsByChecksumUseCase = Depends(get_find_audit_by_checksum)):
    """Endpoint to retrieve audit logs by document checksum."""
    return use_case.execute(checksum)