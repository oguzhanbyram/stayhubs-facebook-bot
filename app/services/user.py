from typing import Optional
from sqlalchemy import select
from app.api.deps import SessionDep
from app.models.user import User
from app.schemas.user import (
    ApiUserCreateRequest,
    ApiUserUpdateRequest,
    ApiUserFilterQuery,
)


def get_user(db: SessionDep, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_users(db: SessionDep, filters: Optional[ApiUserFilterQuery] = None):
    query = select(User)
    if filters:
        query = query.filter_by(**filters.model_dump(exclude_none=True))
    return db.scalars(query).all()


def create_user(db: SessionDep, user: ApiUserCreateRequest):
    db_user = User(email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: SessionDep, user_id: int, user: ApiUserUpdateRequest):
    db_user = db.query(User).filter(User.id == user_id).first()
    db_user.email = user.email
    db_user.is_active = user.is_active
    db_user.password = user.password
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: SessionDep, user_id: int) -> bool:
    user = db.scalars(select(User).filter_by(id=user_id)).first()
    if user:
        db.delete(user)
        db.commit()
        return True
    return False
