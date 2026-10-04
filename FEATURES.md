# Features of Hackathon Manager

The system consists of different features, this document will explain each feature and how to operate each command.

## Members Management
### Features:
- Create new member
- View all members
- View members with query search
- View member data using memberid
- Update members
- Delete members

### Endpoints:
1. Create new member:
```http
POST /members/
```

Example Body content:
```json
{
    "name": "John Doe",
    "email_id": "johndoe@xyzmail.com",
    "contact_number": 1234567890,
    "slack_id": "ABCD123456",
    "github_id": "johndoe"
}
```
System auto-generates memberid and stores it in the database. Memberid is also returned in the response of this request.

2. Get all members:
```http
GET /members/
```

Returns list of all the members registered in the database. (Only returns a few fields rather than returning full data).

3. Get members with query search
```http
GET /members/search/?name=johndoe
```

Search can be used with fields: `name`, `email_id`, `contact_number`, `slack_id` and/or `github_id`.

4. Get member data using memberid
```http
GET /members/{memberid}
```

Returns full data of member holding the requested memberid.

5. Update member
```http
PUT /members/{memberid}
```

Body should be sent with information that is required to be updated.

6. Delete member
```http
DELETE /members/{memberid}
```

Deletes the database entry with memberid entirely.

## Teams Management
### Features:
- Create a team
- Join a team (add a member to team)
- Leave a team (remove a member from team)
- Update Team information
- Delete Team
- Get all teams
- get teams by query search
- Get team data

### Endpoints:
1. Create a team
```http
POST /teams/
```

Example body content:
```json
{
    "name": "Innovision",
    "leader_id": "MEM0001"
}
```

Creates a team with data provided and adds to database.

2. Add members to team
```http
POST /teams/join/{teamid}?memberid={memberid}
```

Adds the memberid into `team_members` dict in database.


3. Remove members from team
```http
POST /teams/leave/{teamid}?memberid={memberid}
```

Removes the memberid from `team_members` dict in database.

4. Update team information
```http
PUT /teams/{teamid}
```

Updates team information to the data given in request body. (Changes name or leader_id)

5. Delete team
```http
DELETE /teams/{teamid}
```

Deletes the team from database entirely.

6. Get all teams
```http
GET /teams/
```

Returns the list of all the teams in the database. (Only teamid, name and leader_id is returned).

7. Get teams by query search
```http
GET /teams/search/?name=Innvision
```

Returns the list of all the teams in the database matching with the search query. Search can be used with fields: `name` and/or `member_id`.

8. Get team data
```http
GET /teams/{teamid}
```

Returns the full data of team stored in the database including team_members' IDs.

## Project Management
### Features:
- Create a project
- Update a project information
- Delete a project
- Log Devlogs
- Get all projects
- Get projects of a team
- Get project data
- Get project by query search

### Endpoints:
1. Create a project
```http
POST /projects/
```

Example body content:
```json
{
    "teamid": "TEAM0001",
    "name": "Hackathon Manager",
    "description": "A basic CRUD system to manage hackathon"
}
```

Creates a projects under teamid and adds into database.

2. Update project information
```http
PUT /projects/{projectid}
```

Updates project information according to data provided. Only `name` and/or `description` can be updated.

3. Delete project
```http
DELETE /projects/{projectid}
```

Deletes the project from database entirely.

4. Log Devlogs
```http
POST /projects/devlog/{projectid}
```

Example body content:
```json
{
    "memberid": "MEM0001",
    "title": "Added a feature",
    "description": "Feature is add members..."
}
```

Adds a devlog into `devlogs` dict in database under projectid.

5. Get all projects
```http
GET /projects/
```

Returns a list of all the projects in database.

6. Get projects of a team
```http
GET /projects/team/{teamid}
```

Returns a list of all the projects in database under teamid.

7. Get project data
```http
GET /projects/{projectid}
```

Returns the full data of project including devlogs.

8. Get projects by query search
```http
GET /projects/search/?name=ABC
```

Returns a list of projects from database matching with search query.
Search can be made using fields: `name` and/or `status`.

## Judgement System
### Features:
- Approve project
- Reject project
- Mark as changes required in a project

### Endpoints:
1. Approve project
```http
PUT /judgement/approve/{projectid}
```

Example body content:
```json
{
    "reviewer_name": "John Tester",
    "remarks": "Nice project!"
}
```

Updates the project status to `approved`.

2. Reject project
```http
PUT /judgement/reject/{projectid}
```

Example body content:
```json
{
    "reviewer_name": "John Tester",
    "remarks": "Not nice project!"
}
```

Updates the project status to `rejected`.

3. Mark as changes required
```http
PUT /judgement/changes-req/{projectid}
```

Example body content:
```json
{
    "reviewer_name": "John Tester",
    "remarks": "Please fix the xyz function as it returns a 500 internal error."
}
```

Updates the project status to `changes-requested`.