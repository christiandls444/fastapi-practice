from app.models.user import User
from sqlalchemy.orm import Session
from typing import List

def fetch_users(db: Session) -> List[User]:
    return db.query(User).all()
