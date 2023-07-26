# api_v1/router.py
from fastapi import APIRouter
from . import slack, chatgpt, alert

router = APIRouter()

router.include_router(alert.router)
router.include_router(slack.router)
router.include_router(chatgpt.router)
