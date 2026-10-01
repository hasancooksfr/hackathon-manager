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