from fastapi import APIRouter

from app.api.deps import SessionDep
from app.services import group as group_service
from app.schemas.group import ApiGroupResponse, ApiGroupCreateRequest


router = APIRouter(
    prefix="/groups",
    tags=["groups"],
)


@router.post("/users/{user_id}/groups/", response_model=ApiGroupResponse)
def create_group_for_user(
    user_id: int, group: ApiGroupCreateRequest, session: SessionDep
) -> ApiGroupResponse:
    return group_service.create_user_group(db=session, group=group, user_id=user_id)


@router.get("/", response_model=list[ApiGroupResponse])
def read_groups(session: SessionDep) -> list[ApiGroupResponse]:
    groups = group_service.get_groups(session)
    return groups
