from pydantic import BaseModel

class ApiUserBase(BaseModel):
    email: str = None


class ApiUserCreateRequest(ApiUserBase):
    password: str = None

class ApiUserUpdateRequest(ApiUserBase):
    is_active: bool = True
    password: str = None


class ApiUserResponse(ApiUserBase):
    id: int = None
    is_active: bool = True
