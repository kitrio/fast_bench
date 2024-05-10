from fastapi import APIRouter
from src.router.index import router as index_router
router = APIRouter()

router.include_router(index_router, tags='index')