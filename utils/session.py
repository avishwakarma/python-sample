import jwt
from config import JWT_PUBLIC_KEY, JWT_PRIVATE_KEY, JWT_ALGORITHM, JWT_EXPIRY

class Session:
  def user(self, token: str) -> dict:
    payload = jwt.decode(token, JWT_PUBLIC_KEY, algorithms=[JWT_ALGORITHM])
    return payload.user

  def token(self, payload) -> str:
    return jwt.encode(payload, JWT_PRIVATE_KEY, algorithm=JWT_ALGORITHM)