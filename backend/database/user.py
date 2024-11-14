from sqlalchemy import select, func
from models.auth import Auth
from models.user import User
import bcrypt
import uuid


def add_user(session, user_id, user_password, user_name):
    user = User(uuid=str(uuid.uuid4()), user_id=user_id, user_name=user_name)
    session.add(user)
    session.add(Auth(uuid=user.uuid, user_password=bcrypt.hashpw(user_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')))
    session.commit()


def get_user(session, uuid):
    return session.execute(select(User).where(User.uuid == uuid)).scalars().first()
