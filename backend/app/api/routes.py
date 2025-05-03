from fastapi import APIRouter
from app.api.endpoints import reports, field_data

router = APIRouter()

router.include_router(reports.router, prefix="/reports", tags=["Reports"])
router.include_router(field_data.router, prefix="/field", tags=["Field Data"])
