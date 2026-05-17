from abc import ABC, abstractmethod
from app.domain.entities.audit_log import AuditLog

class Audit_LogRepository(ABC):
    @abstractmethod
    def save(self, audit_log: AuditLog) -> AuditLog:
        pass
    @abstractmethod
    def find_all(self, skip: int = 0, limit: int = 10) -> list[AuditLog]:
        pass
    @abstractmethod
    def find_by_checksum(self, checksum: str) -> list[AuditLog]: 
        pass