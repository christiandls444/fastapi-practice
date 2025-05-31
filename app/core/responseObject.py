from typing import Any
from app.schemas.responseSchema import responseSchema


def responseObject(
    code: int = 200,
    status: str = "success",
    message: str = "Success",
    data: Any = None
):
    return responseSchema(
        code = code,
        status = status,
        message = message,
        data = data
    )