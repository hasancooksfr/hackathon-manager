# Hackathon Manager
Hackathon Manager is an open-source API used for basic CRUD operations while managing a hackathon.

## Features
The features of this system includes:
- Member Management
- Team Management
- Project Management
- Judgement Management

Details and endpoints of these features can be found at [FEATURES.md](/FEATURES.md)

## Tech Stack
The system is build using **Python** and **FastAPI**. It uses **MongoDB** as database.

## Running the Project
1. Clone the repository
```bash
git clone https://github.com/hasancooksfr/hackathon-manager
cd hackathon-manager
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Configure environment variables
Create an `.env` file:
```env
MONGO_URI=your_mongo_uri_string
```

4. Start the server
```bash
uvicorn main:app --reload
```

The API will be available at:
```
http://127.0.0.1:8000
```

## Database
This system uses  **MongoDB** for data storage.

The system currently uses different collections for different features, including:
```
members
teams
projects
```

## Endpoint prefixes
For each feature, there is an different prefix endpoint:
```
Members: /members
Teams: /teams
Projects: /projects
Judgement: /judgement
```

## License
This project is licenced under MIT License.