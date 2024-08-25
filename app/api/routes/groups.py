from fastapi import APIRouter

from app.api.deps import SessionDep
from app.services import group as group_service
from app.schemas.group import ApiGroupResponse


router = APIRouter(
    prefix="/groups",
    tags=["groups"],
)


@router.get("/", response_model=list[ApiGroupResponse])
def read_groups(session: SessionDep) -> list[ApiGroupResponse]:
    return group_service.get_groups(db=session)


@router.get("/sync-from-users", response_model=list[ApiGroupResponse])
def sync_user_groups(session: SessionDep) -> list[ApiGroupResponse]:
    return group_service.sync_user_groups(db=session)
