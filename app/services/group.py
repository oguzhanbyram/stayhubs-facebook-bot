from fastapi import HTTPException

from app.api.deps import SessionDep
from app.models.group import Group
from app.schemas.group import (
    ApiGroupResponse,
    ApiGroupCreateRequest,
    ApiGroupIsActiveRequest,
)
from app.services.facebook.scraper import FacebookScraper
from app.services import user as user_service


def get_groups(db: SessionDep) -> list[ApiGroupResponse]:
    return db.query(Group).all()


def sync_user_groups(db: SessionDep) -> list[ApiGroupResponse]:
    users = user_service.get_users(db)

    if not users:
        raise HTTPException(status_code=404, detail="No users found")

    scraper = FacebookScraper()

    result = []

    for user in users:
        try:
            scraper.login(user.email, user.password)
            groups = scraper.get_groups()
            for group in groups:
                group = create_user_group(db, group, user.id)
                result.append(group)

            scraper.logout()
        except Exception as e:
            print(f"Error processing user {user.email}: {str(e)}")

    return result


def create_user_group(
    db: SessionDep, group: ApiGroupCreateRequest, user_id: int
) -> ApiGroupResponse:
    db_group = Group(**group.model_dump(), user_id=user_id)
    db.add(db_group)
    db.commit()
    db.refresh(db_group)
    return db_group


def change_group_status(
    db: SessionDep, group_id: int, group: ApiGroupIsActiveRequest
) -> ApiGroupResponse:
    db_group = db.query(Group).filter(Group.id == group_id).first()
    db_group.is_active = group.is_active
    db.commit()
    db.refresh(db_group)
    return db_group
