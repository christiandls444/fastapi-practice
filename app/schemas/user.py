from pydantic import BaseModel, ConfigDict

class UserBase(BaseModel):
    id: int
    username: str
    hashed_password: str
    is_admin: bool
    
    model_config = ConfigDict(from_attributes = True)
        
        
        
        
        
        
        
        
        