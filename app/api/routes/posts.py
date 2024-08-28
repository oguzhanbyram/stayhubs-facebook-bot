from fastapi import APIRouter, HTTPException

from app.api.deps import SessionDep
from app.services import post as post_service
from app.schemas.post import (
    ApiPostResponse,
    ApiPostCreateRequest,
    ApiPostUpdateRequest,
)


router = APIRouter(
    prefix="/posts",
    tags=["posts"],
)


@router.post("/", response_model=ApiPostResponse)
def create_post(
    post: ApiPostCreateRequest, session: SessionDep
) -> ApiPostResponse:
    return post_service.create_post(session, post)


@router.put("/{post_id}", response_model=ApiPostResponse)
def update_post(
    post_id: int, post: ApiPostUpdateRequest, session: SessionDep
) -> ApiPostResponse:
    return post_service.update_post(session, post_id, post)


@router.get("/", response_model=list[ApiPostResponse])
def read_posts(session: SessionDep) -> list[ApiPostResponse]:
    return post_service.get_posts(session)


@router.get("/{post_id}", response_model=ApiPostResponse)
def read_post(post_id: int, session: SessionDep) -> ApiPostResponse:
    db_post = post_service.get_post(session, post_id=post_id)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_post


@router.delete("/{post_id}", response_model=bool)
def delete_post(post_id: int, session: SessionDep) -> bool:
    return post_service.delete_post(session, post_id)
