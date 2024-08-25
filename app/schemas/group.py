from pydantic import BaseModel


class ApiGroupBaseResponse(BaseModel):
    name: str
    group_id: str
    url: str


class ApiGroupCreateRequest(ApiGroupBaseResponse):
    pass


class ApiGroupResponse(ApiGroupBaseResponse):
    id: int
    user_id: int

    class Config:
        from_attributes = True
