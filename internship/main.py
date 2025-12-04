# main.py
from fastapi import FastAPI
from apis import player_api, team_api, match_api

app = FastAPI(title="Football FIFA API")

# Attach all routers
app.include_router(player_api.router)
app.include_router(team_api.router)
app.include_router(match_api.router)