# Hackathon Manager
Hackathon Manager is an open-source API used for basic CRUD operations while managing a hackathon.

## Features
The features of this system includes:
- Member Management
- Team Management
- Project Management
- Judgement Management

Details and endpoints of these features can be found at [FEATURES.md](/FEATURES.md)

## Screenshots
There are screenshots of top 4 requests I personally like, you can see more info in [FEATURES.md](/FEATURES.md).

![Post Members](/images/post_members.jpg)

![Post Teams](/images/post_teams.png)

![Get All Members](/images/get_all_members.png)

![Get All Teams](/images/get_all_teams.png)

The request URL is blurred because it is hosted URL with my database linked to it, I'll soon unhost it and put the postman collection link!

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