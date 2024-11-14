from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Boolean, CheckConstraint, Integer, ForeignKey, String, func
from datetime import datetime
from .base import Base


class RevokedToken(Base):
    __tablename__ = 'revoked_token'

    token: Mapped[str] = mapped_column(primary_key=True)
    revoked_at: Mapped[datetime] = mapped_column(insert_default=func.now())
