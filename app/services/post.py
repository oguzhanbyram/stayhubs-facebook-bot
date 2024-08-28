from sqlalchemy import select
from app.api.deps import SessionDep
from app.models.post import Post
from app.schemas.post import (
    ApiPostCreateRequest,
    ApiPostUpdateRequest,
)


def get_post(db: SessionDep, post_id: int):
    return db.query(Post).filter(Post.id == post_id).first()


def get_posts(db: SessionDep):
    return db.scalars(select(Post)).all()


def create_post(db: SessionDep, post: ApiPostCreateRequest):
    db_post = Post(**post.model_dump())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


def update_post(db: SessionDep, post_id: int, post: ApiPostUpdateRequest):
    db_post = db.query(Post).filter(Post.id == post_id).first()
    db_post.text = post.text
    db.commit()
    db.refresh(db_post)
    return db_post


def delete_post(db: SessionDep, post_id: int) -> bool:
    post = db.scalars(select(Post).filter_by(id=post_id)).first()
    if post:
        db.delete(post)
        db.commit()
        return True
    return False
