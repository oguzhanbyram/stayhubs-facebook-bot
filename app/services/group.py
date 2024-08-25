from app.api.deps import SessionDep
from app.models.group import Group
from app.schemas.group import ApiGroupCreateRequest


def get_groups(db: SessionDep) -> list[Group]:
    return db.query(Group).all()


def create_user_group(
    db: SessionDep, group: ApiGroupCreateRequest, user_id: int
) -> Group:
    db_group = Group(**group.dict(), user_id=user_id)
    db.add(db_group)
    db.commit()
    db.refresh(db_group)
    return db_group
