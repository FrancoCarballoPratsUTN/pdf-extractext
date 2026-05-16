from abc import ABC, abstractmethod
from app.domain.entities.audit_log import Audit_Log

class Audit_LogRepository(ABC):
    @abstractmethod
    def save(self, audit_log: Audit_Log) -> Audit_Log:
        pass
    @abstractmethod
    def find_all(self, skip: int = 0, limit: int = 10) -> list[Audit_Log]:
        pass
    @abstractmethod
    def find_by_checksum(self, checksum: str) -> list[Audit_Log]: 
        pass