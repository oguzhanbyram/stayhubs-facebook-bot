from fastapi import FastAPI

from app.core.config import settings
from app.api.main import api_router
from app.core.database import init_db

app = FastAPI(
    title=settings.APP_NAME,
    app_name=settings.APP_NAME,
    description=settings.APP_DESCRIPTION,
    version=settings.APP_VERSION,
    license_name=settings.LICENSE_NAME,
    contact={"name": settings.CONTACT_NAME, "email": settings.CONTACT_EMAIL},
)

init_db()

app.include_router(api_router)
