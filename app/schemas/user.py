from pydantic import BaseModel

class ApiUserBase(BaseModel):
    email: str


class ApiUserCreateRequest(ApiUserBase):
    password: str


class ApiUserResponse(ApiUserBase):
    id: int
    is_active: bool
