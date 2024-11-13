from database.session import Session
from sqlalchemy import select, func
from models.auth import Auth
from models.user import User
import bcrypt


def get_auth(user_id):
  with Session.begin() as session:
    result = session.execute(select(Auth, User).join(Auth.user).where(User.user_id == user_id))
    auth = result.scalars().first()
    return auth

def add_auth(uuid, password):
  with Session.begin() as session:
    session.add(Auth(uuid=uuid, user_password=bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')))
    session.commit()

