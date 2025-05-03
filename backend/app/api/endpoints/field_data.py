from fastapi import APIRouter

router = APIRouter()

@router.post("/")
def submit_field_data():
    return {"status": "Field data submitted"}
