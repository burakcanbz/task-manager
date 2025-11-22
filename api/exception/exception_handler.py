from sqlalchemy.exc import SQLAlchemyError
from fastapi.responses import JSONResponse
from fastapi import Request

from .app_exception import AppException
from config.logger import logger

async def general_exception_handler(req: Request, error: Exception):
    logger.error(f"Exception occured for request URL: {req.url} \n\t error_code: 500 | error_details: {error}")
    
    return JSONResponse(
        status_code=500,
        content={"error": {"message": "Internal server error", "details": str(error)}}
    )

async def app_exception_handler(req: Request, error: AppException):
    logger.error(
        f"AppException occurred for request URL: {req.url} \n\terror_code: {error.code} | error_details: {error.detail}"
    )
    return JSONResponse(
        status_code=error.status_code,
        content={"error": {"message": "Service error", "details": error.detail}}
    )

async def sqlalchemy_exception_handler(req: Request, error: SQLAlchemyError):
    logger.error(
        f"Database exception occured for request URL: {req.url} \n\terror_code: 500 | error_details: {error}"
    )
    return JSONResponse(
        status_code=500,
        content={"error": {"message": "Database error", "details": str(error)}}
    )

def setup_exception_handlers(app):
    app.add_exception_handler(AppException, app_exception_handler)
    app.add_exception_handler(SQLAlchemyError, sqlalchemy_exception_handler)
    app.add_exception_handler(Exception, general_exception_handler)