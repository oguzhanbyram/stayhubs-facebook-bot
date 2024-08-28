from sqlalchemy import select
from app.api.deps import SessionDep
from app.models.answer import Answer
from app.schemas.answer import (
    ApiAnswerCreateRequest,
    ApiAnswerUpdateRequest,
)


def get_answer(db: SessionDep, answer_id: int):
    return db.query(Answer).filter(Answer.id == answer_id).first()


def get_answers(db: SessionDep):
    return db.scalars(select(Answer)).all()


def create_answer(db: SessionDep, answer: ApiAnswerCreateRequest):
    db_answer = Answer(**answer.model_dump())
    db.add(db_answer)
    db.commit()
    db.refresh(db_answer)
    return db_answer


def update_answer(db: SessionDep, answer_id: int, answer: ApiAnswerUpdateRequest):
    db_answer = db.query(Answer).filter(Answer.id == answer_id).first()
    db_answer.text = answer.text
    db.commit()
    db.refresh(db_answer)
    return db_answer


def delete_answer(db: SessionDep, answer_id: int) -> bool:
    answer = db.scalars(select(Answer).filter_by(id=answer_id)).first()
    if answer:
        db.delete(answer)
        db.commit()
        return True
    return False
