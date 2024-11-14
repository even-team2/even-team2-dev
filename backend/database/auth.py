from sqlalchemy import select, func
from models.auth import Auth
from models.user import User
from models.revoked_token import RevokedToken
import bcrypt


def get_auth(session, user_id):
    result = session.execute(select(Auth, User).join(Auth.user).where(User.user_id == user_id))
    auth = result.scalars().first()
    return auth


def add_auth(session, uuid, password):
    session.add(Auth(uuid=uuid, user_password=bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')))
    session.commit()


def is_revoked_token(session, token):
    result = session.execute(select(RevokedToken).where(RevokedToken.token == token))
    return result.scalars().first()


def add_revoked_token(session, token):
    session.add(RevokedToken(token=token))
    session.commit()
