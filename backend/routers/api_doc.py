from fastapi import APIRouter
from fastapi.openapi.docs import get_swagger_ui_html


router = APIRouter()

@router.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(openapi_url="/openapi.json", title="this is me")

@router.get("/openapi.json", include_in_schema=False)
async def get_openapi_json():
    return app.openapi()
