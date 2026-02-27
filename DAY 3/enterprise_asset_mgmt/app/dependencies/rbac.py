from fastapi import Depends, HTTPException, status
from app.services.auth_service import get_current_user

def require_roles(*roles: str): 
    def wrapper(current_user=Depends(get_current_user)): 
        if current_user.role not in roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, 
                detail="Operation not permitted for this role"
            )
        return current_user
    return wrapper 