from pydantic import BaseModel, ConfigDict


class ApiPostBaseResponse(BaseModel):
    post_user: str = None
    text: str = None
    date: str = None
    url: str = None


class ApiPostCreateRequest(ApiPostBaseResponse):
    pass


class ApiPostUpdateRequest(ApiPostBaseResponse):
    pass


class ApiPostResponse(ApiPostBaseResponse):
    id: int = None
    group_id: int = None
    user_id: int = None
    answer_id: int = None

    model_config = ConfigDict(
        from_attributes=True,
    )
