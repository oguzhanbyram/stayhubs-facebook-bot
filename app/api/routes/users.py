from fastapi import APIRouter, HTTPException

from app.api.deps import SessionDep
from app.services import user as user_service
from app.schemas.user import ApiUserResponse, ApiUserCreateRequest, ApiUserUpdateRequest


router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.post("/", response_model=ApiUserResponse)
def create_user(user: ApiUserCreateRequest, session: SessionDep) -> ApiUserResponse:
    return user_service.create_user(session, user)


@router.put("/{user_id}", response_model=ApiUserResponse)
def update_user(
    user_id: int, user: ApiUserUpdateRequest, session: SessionDep
) -> ApiUserResponse:
    return user_service.update_user(session, user_id, user)


@router.get("/", response_model=list[ApiUserResponse])
def read_users(session: SessionDep) -> list[ApiUserResponse]:
    users = user_service.get_users(session)
    return users


@router.get("/{user_id}", response_model=ApiUserResponse)
def read_user(user_id: int, session: SessionDep) -> ApiUserResponse:
    db_user = user_service.get_user(session, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.delete("/{user_id}", response_model=bool)
def delete_user(user_id: int, session: SessionDep) -> bool:
    return user_service.delete_user(session, user_id)
