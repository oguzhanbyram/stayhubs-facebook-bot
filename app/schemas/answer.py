import datetime
from pydantic import BaseModel, ConfigDict


class ApiAnswerBaseResponse(BaseModel):
    text: str = None


class ApiAnswerCreateRequest(ApiAnswerBaseResponse):
    pass


class ApiAnswerUpdateRequest(ApiAnswerBaseResponse):
    pass


class ApiAnswerResponse(ApiAnswerBaseResponse):
    id: int = None
    created_at: datetime.datetime = None
    updated_at: datetime.datetime = None
