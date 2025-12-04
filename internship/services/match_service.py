import requests

base_url = "http://localhost:3000"

def get_matches():
    res = requests.get(f"{base_url}/matches")
    return res.json()

def add_match(match_data):
    res = requests.post(f"{base_url}/matches", json=match_data)
    return res.json()

def update_match(match_id, update_data):
    res = requests.put(f"{base_url}/matches/{match_id}", json=update_data)
    return res.json()

def delete_match(match_id):
    res = requests.delete(f"{base_url}/matches/{match_id}")
    return res.status_code