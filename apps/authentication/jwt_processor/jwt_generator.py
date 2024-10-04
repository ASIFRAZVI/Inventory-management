import jwt
from datetime import datetime, timedelta
from inventory_management.settings.config import JWT_SECRET

jwt_secret = JWT_SECRET


def generate_jwt_token(user_id, jwt_secret, expiration_minutes=60):
    payload = {
        "user_id": str(user_id),
        "exp": datetime.utcnow() + timedelta(minutes=expiration_minutes),
    }
    token = jwt.encode(payload, jwt_secret, algorithm="HS256")
    return token


def generate_refresh_token(user_id, jwt_secret, expiration_days=7):
    payload = {
        "user_id": str(user_id),
        "exp": datetime.utcnow() + timedelta(days=expiration_days),
    }
    token = jwt.encode(payload, jwt_secret, algorithm="HS256")
    return token
