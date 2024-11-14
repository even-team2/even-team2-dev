from dotenv import load_dotenv
import os
import jwt
import bcrypt
from datetime import datetime, timedelta
from database.session import Session
from database.auth import is_revoked_token, add_revoked_token


load_dotenv()
JWT_SECRET=os.getenv('JWT_SECRET')

def issue_token(uuid):
    exp = datetime.utcnow() + timedelta(weeks=4)
    token = jwt.encode({'uuid': uuid, 'exp': exp}, JWT_SECRET, algorithm='HS256')
    return token


def verify_token(token):
    try:
        with Session.begin() as session:
            if not is_revoked_token(session, token):
                return jwt.decode(token.encode('utf-8'), JWT_SECRET, algorithms=["HS256"])
    except:
        return None


def verify_password(password, encrypted_password):
    return bcrypt.checkpw(password.encode('utf-8'), encrypted_password.encode('utf-8'))


def revoke_token(token):
    with Session.begin() as session:
        add_revoked_token(session, token)
