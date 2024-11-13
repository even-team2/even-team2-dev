from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Boolean, CheckConstraint, Integer, ForeignKey, String
from datetime import datetime
from .base import Base


class User(Base):
    __tablename__ = 'user'

    uuid: Mapped[str] = mapped_column(primary_key=True)
    user_id: Mapped[str]
    user_name: Mapped[str]
