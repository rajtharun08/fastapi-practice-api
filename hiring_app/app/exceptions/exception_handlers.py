from fastapi import Request
from fastapi.responses import JSONResponse
from app.exceptions import HiringAppException

async def hiring_app_exception_handler(request: Request, exc: HiringAppException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "error_type": exc.__class__.__name__,
            "message": exc.message
        }
    )