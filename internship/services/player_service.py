import requests

base_url = "http://localhost:3000"

def get_players():
    res = requests.get(f"{base_url}/players")
    return res.json()

def add_player(player_data):
    res = requests.post(f"{base_url}/players", json=player_data)
    return res.json()

def update_player(player_id, update_data):
    res = requests.put(f"{base_url}/players/{player_id}", json=update_data)
    return res.json()

def delete_player(player_id):
    res = requests.delete(f"{base_url}/players/{player_id}")
    return res.status_code