from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Boolean, CheckConstraint, Integer, ForeignKey, String
from datetime import datetime
from .base import Base


class Auth(Base):
    __tablename__ = 'auth'

    uuid: Mapped[str] = mapped_column(ForeignKey("user.uuid"), primary_key=True)
    user: Mapped["User"] = relationship("User")
    user_password: Mapped[str]
