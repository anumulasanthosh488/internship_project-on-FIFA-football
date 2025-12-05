🏆 Football FIFA Management API

A FastAPI + JSON Server based football data management system


---

📌 Project Overview

The Football FIFA Management API is a backend project designed to manage football-related data such as Players, Teams, and Matches.
It uses:

JSON Server → as a mock database

FastAPI → to build the REST API

Python Requests → to interact with the JSON database


This project demonstrates:

CRUD Operations

API Routing

Service Layer Architecture

Backend Development Skills required for internships



---

🚀 Features

✔ Players Module

Add Player

Fetch All Players

Update Player

Delete Player


✔ Teams Module

Add Team

Fetch All Teams

Update Team

Delete Team


✔ Matches Module

Add Match

Fetch All Matches

Update Match

Delete Match



---

🛠 Tech Stack

Component	Technology

Backend Framework	FastAPI (Python)
Mock Database	JSON Server
API Client	Python Requests
Data Format	JSON



---

📂 Project Structure

Football-FIFA-API/
│
├── apis/
│   ├── player_api.py
│   ├── team_api.py
│   └── match_api.py
│
├── services/
│   ├── player_service.py
│   ├── team_service.py
│   └── match_service.py
│
├── db.json
├── main.py
└── README.md


---

📄 db.json (Database)

Your data includes:

Players

Teams

Matches


JSON Server reads data from db.json and exposes endpoints at:

http://localhost:3000/


---

⚙️ How to Run the Project

1️⃣ Install JSON Server

npm install -g json-server

2️⃣ Start JSON Server

json-server --watch db.json

3️⃣ Install FastAPI + Uvicorn

pip install fastapi uvicorn requests

4️⃣ Run FastAPI Application

uvicorn main:app --reload


---

🌐 API Endpoints

🔹 Players

Method	Endpoint	Description

GET	/players/	Get all players
POST	/players/	Add player
PUT	/players/{id}	Update player
DELETE	/players/{id}	Delete player


🔹 Teams

Method	Endpoint	Description

GET	/teams/	Get all teams
POST	/teams/	Add team
PUT	/teams/{id}	Update team
DELETE	/teams/{id}	Delete team


🔹 Matches

Method	Endpoint	Description

GET	/matches/	Get all matches
POST	/matches/	Add match
PUT	/matches/{id}	Update match
DELETE	/matches/{id}	Delete match



---

🧠 Concept of the Project

The project simulates a football management backend system.
It provides REST APIs to manage:

Football players

Teams

Match results


The architecture follows:

JSON Server → Data Layer

Services → Request Layer

FastAPI Routers → API Layer



---

📌 Usage Examples (Python)

Get All Players:

players = get_players()
print(players)

Add New Player:

add_player({"id": 4, "name": "Neymar", "age": 33})


---

🎯 Why This Project?

Demonstrates backend development skills

Shows real REST API development

Implements clean architecture

Perfect for internship/project submission



---

📝 Conclusion

The Football FIFA Management API is a complete backend application built using FastAPI and JSON Server.
It showcases CRUD operations, API routing, modular architecture, and practical football data handling—making it ideal for academic and internship projects.
