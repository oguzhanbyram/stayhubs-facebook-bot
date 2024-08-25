from app.api.deps import SessionDep
from app.models.user import User
from app.schemas.user import ApiUserCreateRequest


def get_user(db: SessionDep, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_users(db: SessionDep):
    return db.query(User).all()


def create_user(db: SessionDep, user: ApiUserCreateRequest):
    db_user = User(email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
