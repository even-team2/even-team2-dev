from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.exceptions import HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from schemas.response import ErrorResponse
from routers.api_doc import router as api_doc_router
from routers.auth import router as auth_router
from routers.user import router as user_router


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.exception_handler(HTTPException)
async def exception_handler(request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content=jsonable_encoder(ErrorResponse(
            success=False,
            message="fail to process request"))
    )

app.include_router(api_doc_router)
app.include_router(auth_router)
app.include_router(user_router)

