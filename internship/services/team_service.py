import requests

base_url = "http://localhost:3000"

def get_teams():
    res = requests.get(f"{base_url}/teams")
    return res.json()

def add_team(team_data):
    res = requests.post(f"{base_url}/teams", json=team_data)
    return res.json()

def update_team(team_id, update_data):
    res = requests.put(f"{base_url}/teams/{team_id}", json=update_data)
    return res.json()

def delete_team(team_id):
    res = requests.delete(f"{base_url}/teams/{team_id}")
    return res.status_code