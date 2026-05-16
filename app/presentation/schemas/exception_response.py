from pydantic import BaseModel, HttpUrl

class ProblemDetailsSchema(BaseModel):
    type: HttpUrl
    title: str
    status: int
    detail: str
    instance: str
