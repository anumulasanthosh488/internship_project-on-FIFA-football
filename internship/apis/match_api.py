from fastapi import APIRouter
from services import match_service

router = APIRouter(prefix="/matches", tags=["Matches"])

@router.get("/")
def get_matches():
    return match_service.get_matches()

@router.post("/")
def add_match(match_data: dict):
    return match_service.add_match(match_data)

@router.put("/{match_id}")
def update_match(match_id: int, update_data: dict):
    return match_service.update_match(match_id, update_data)

@router.delete("/{match_id}")
def delete_match(match_id: int):
    return match_service.delete_match(match_id)