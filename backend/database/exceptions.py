from typing import Any
from fastapi import HTTPException, status


class ErrorCountExceptions(HTTPException):
    def __init__(self, value: Any) -> None:
        detail = f"Not enough count product = {value}"
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail=detail)
