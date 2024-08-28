import typing
from pydantic import BaseModel,ConfigDict

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


class ApiUserFilterQuery(BaseModel):
    email: typing.Optional[str] = None
    is_active: typing.Optional[bool] = None

    model_config = ConfigDict(
        from_attributes=True,
    )