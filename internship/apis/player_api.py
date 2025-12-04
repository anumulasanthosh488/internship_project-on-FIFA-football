from fastapi import APIRouter
from services import player_service

router = APIRouter(prefix="/players", tags=["Players"])

@router.get("/")
def get_players():
    return player_service.get_players()

@router.post("/")
def add_player(player_data: dict):
    return player_service.add_player(player_data)

@router.put("/{player_id}")
def update_player(player_id: int, update_data: dict):
    return player_service.update_player(player_id, update_data)

@router.delete("/{player_id}")
def delete_player(player_id: int):
    return player_service.delete_player(player_id)