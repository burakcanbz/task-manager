from fastapi import HTTPException

class AppException(HTTPException):
    def __init__(self, status_code: int = 400, detail: str = "An error occured", code: str | None = None):
        self.code = code
        super().__init__(status_code=status_code, detail=detail)