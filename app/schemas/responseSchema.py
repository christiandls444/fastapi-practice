from typing import Any, Optional
from pydantic import BaseModel

class responseSchema(BaseModel):
    code: int
    status: str
    message: str
    data: Optional[Any] = None