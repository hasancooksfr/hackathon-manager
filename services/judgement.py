from fastapi import HTTPException
from database import projects_collection

def approveProject(projectid, review):
    review = review.model_dump()

    res = projects_collection.update_one(
        {
            "projectid": projectid
        },
        {
            "$set": {
                "status": "approved",
                **review
            }
        }
    )
    if res.matched_count == 0:
        raise HTTPException(
            status_code=404,
            detail="No records found for projectid."
        )

    return True

def rejectProjectwithRemarks(projectid, review):
    review = review.model_dump()

    res = projects_collection.update_one(
        {
            "projectid": projectid
        },
        {
            "$set": {
                "status": "changes-requested",
                **review
            }
        }
    )
    if res.matched_count == 0:
        raise HTTPException(
            status_code=404,
            detail="No records found for projectid."
        )

    return True