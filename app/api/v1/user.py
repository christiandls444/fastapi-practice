from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.schemas.user import UserBase
from app.db.session import get_db
from app.services.user_service import fetch_users

from app.core.responseObject import responseObject

router = APIRouter()

# @router.get("/users", response_model=List[UserBase])
@router.get("/users")
async def get_users(db: Session = Depends(get_db)):
    users = fetch_users(db)
    user_data: List[UserBase] = [UserBase.model_validate(user) for user in users]
    # return fetch_users(db)
    return responseObject(
        code = 200,
        status = "success",
        message = "User list fetched successfully",
        data = user_data 
    )


