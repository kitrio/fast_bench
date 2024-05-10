from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from jinja2 import Environment
from sqlalchemy import select

from src.database import db_session
from src.models import Config

router = APIRouter()

from jinja2 import FileSystemLoader, select_autoescape

environment = Environment(
    enable_async=True,
    loader=FileSystemLoader("templates"),
    autoescape=select_autoescape(["html"])
)


@router.get('/index')
async def index(
        request: Request,
        db:db_session
):
    
    title = await db.scalar(select(Config.cf_title))
    
    template = environment.get_template("index.html")
    rendered_content = await template.render_async(request=request)
    return HTMLResponse(content=rendered_content)