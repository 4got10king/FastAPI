from typing import Any
from fastapi import HTTPException, status


class DataBase404Exception(HTTPException):
    def __init__(self, value: Any) -> None:
        detail = f"Not found data with key = {value}"
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=detail)


class DataBaseException(HTTPException):
    def __init__(self, message: Any) -> None:
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=message)
