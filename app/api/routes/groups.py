from fastapi import APIRouter, HTTPException

from app.api.deps import SessionDep
from app.services import group as group_service
from app.schemas.group import ApiGroupResponse, ApiGroupIsActiveRequest


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


@router.get("/{group_id}", response_model=ApiGroupResponse)
def read_user(group_id: int, session: SessionDep) -> ApiGroupResponse:
    group = group_service.get_group(session, group_id=group_id)
    if group is None:
        raise HTTPException(status_code=404, detail="Group not found")
    return group


@router.put("/change-status/{group_id}", response_model=ApiGroupResponse)
def change_group_status(
    session: SessionDep, group_id: int, group: ApiGroupIsActiveRequest
) -> ApiGroupResponse:
    return group_service.change_group_status(db=session, group_id=group_id, group=group)


@router.delete("/delete/{group_id}", response_model=bool)
def delete_group(session: SessionDep, group_id: int) -> bool:
    return group_service.delete_group(db=session, group_id=group_id)
