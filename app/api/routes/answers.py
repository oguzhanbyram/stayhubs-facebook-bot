from fastapi import APIRouter, HTTPException

from app.api.deps import SessionDep
from app.services import answer as answer_service
from app.schemas.answer import (
    ApiAnswerResponse,
    ApiAnswerCreateRequest,
    ApiAnswerUpdateRequest,
)


router = APIRouter(
    prefix="/answers",
    tags=["answers"],
)


@router.post("/", response_model=ApiAnswerResponse)
def create_answer(
    answer: ApiAnswerCreateRequest, session: SessionDep
) -> ApiAnswerResponse:
    return answer_service.create_answer(session, answer)


@router.put("/{answer_id}", response_model=ApiAnswerResponse)
def update_answer(
    answer_id: int, answer: ApiAnswerUpdateRequest, session: SessionDep
) -> ApiAnswerResponse:
    return answer_service.update_answer(session, answer_id, answer)


@router.get("/", response_model=list[ApiAnswerResponse])
def read_answers(session: SessionDep) -> list[ApiAnswerResponse]:
    return answer_service.get_answers(session)


@router.get("/{answer_id}", response_model=ApiAnswerResponse)
def read_answer(answer_id: int, session: SessionDep) -> ApiAnswerResponse:
    db_answer = answer_service.get_answer(session, answer_id=answer_id)
    if db_answer is None:
        raise HTTPException(status_code=404, detail="Answer not found")
    return db_answer


@router.delete("/{answer_id}", response_model=bool)
def delete_answer(answer_id: int, session: SessionDep) -> bool:
    return answer_service.delete_answer(session, answer_id)
