from typing import Literal

from sqlalchemy import Enum, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from RentikuSearch.models.base_model import BaseModel
from RentikuSearch.models.database import Base

actions = ["rent", "sell", "lease"]
Actions = Literal["rent", "sell", "lease"]


class User(BaseModel, Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(
        String(50), nullable=False, unique=True
    )
    email: Mapped[str] = mapped_column(String(255), unique=True)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)

    def __repr__(self):
        return "username: {}  email: {}".format(self.username, self.email)


class Property(BaseModel, Base):
    __tablename__ = "properties"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(50), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    action: Mapped[Actions] = mapped_column(
        Enum(*actions, name="action"), nullable=True
    )
    price: Mapped[float] = mapped_column(Float, nullable=True)
    rent: Mapped[float] = mapped_column(Float, nullable=True)
    num_rooms: Mapped[int] = mapped_column(Integer, nullable=True)
    address: Mapped[str] = mapped_column(String(100), nullable=True)
    latitude: Mapped[str] = mapped_column(String(50), nullable=True)
    longitude: Mapped[str] = mapped_column(String(50), nullable=True)
    region: Mapped[str] = mapped_column(String(100), nullable=True)
    image_url: Mapped[int] = mapped_column(String(255), nullable=True)
    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
