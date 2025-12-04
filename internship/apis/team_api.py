from fastapi import APIRouter
from services import team_service

router = APIRouter(prefix="/teams", tags=["Teams"])

@router.get("/")
def get_teams():
    return team_service.get_teams()

@router.post("/")
def add_team(team_data: dict):
    return team_service.add_team(team_data)

@router.put("/{team_id}")
def update_team(team_id: int, update_data: dict):
    return team_service.update_team(team_id, update_data)

@router.delete("/{team_id}")
def delete_team(team_id: int):
    return team_service.delete_team(team_id)