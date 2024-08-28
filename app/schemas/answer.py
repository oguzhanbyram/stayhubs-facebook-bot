from pydantic import BaseModel, ConfigDict


class ApiAnswerBaseResponse(BaseModel):
    text: str = None
    created_at: str = None
    updated_at: str = None


class ApiAnswerCreateRequest(ApiAnswerBaseResponse):
    pass


class ApiAnswerUpdateRequest(ApiAnswerBaseResponse):
    pass


class ApiAnswerResponse(ApiAnswerBaseResponse):
    id: int = None

    model_config = ConfigDict(
        from_attributes=True,
    )
