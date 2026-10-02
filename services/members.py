from database import members_collection

def createMember(member):
    data = member.model_dump()

    last_entry = members_collection.find_one(
        {},
        sort=[("memberid", -1)]
    )

    if last_entry is None:
        memberid = "MEM0001"
    else:
        last_id = int(last_entry['memberid'].replace("MEM", ""))
        memberid = f"MEM{last_id+1:04d}"

    data['memberid'] = memberid
    members_collection.insert_one(
        data
    )

    return True

def getAllMembers():
    data = list(members_collection.find({}, {
        "_id": 0,
        "memberid": 1,
        "name": 1,
        "email_id": 1,
        "slack_id": 1
    }))

    return data

def getMembersByQuery(
    name: str = None,
    email_id: str = None,
    contact_number: int = None,
    slack_id: str = None,
    github_id: str = None
):
    query = {}

    if name:
        query['name'] = name

    if email_id:
        query['email_id'] = email_id

    if contact_number:
        query['contact_number'] = contact_number

    if slack_id:
        query['slack_id'] = slack_id

    if github_id:
        query['github_id'] = github_id

    data = list(
        members_collection.find(
            query,
            {
                "_id": 0,
                "memberid": 1,
                "name": 1,
                "email_id": 1,
                "slack_id": 1
            }
        )
    )

    return data

