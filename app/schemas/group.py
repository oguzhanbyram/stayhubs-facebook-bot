from pydantic import BaseModel, ConfigDict


class ApiGroupBaseResponse(BaseModel):
    name: str = None
    group_id: str = None
    url: str = None


class ApiGroupCreateRequest(ApiGroupBaseResponse):
    pass


class ApiGroupResponse(ApiGroupBaseResponse):
    id: int = None
    user_id: int = None

    model_config = ConfigDict(
        from_attributes=True,
    )
