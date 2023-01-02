from fastapi_users import FastAPIUsers

from ..models.users import User, get_user_manager
from ..routes.security import auth_backends

fastapi_users = FastAPIUsers[User, int](get_user_manager, auth_backends)

current_active_user = fastapi_users.current_user(active=True)
