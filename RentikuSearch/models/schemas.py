from pydantic import BaseModel


class PropertyBase(BaseModel):
    title: str
    description: str | None
    action: str | None
    price: float
    rent: float
    num_rooms: int
    address: str | None
    latitude: str | None
    longitude: str | None
    region: str | None
    image_url: str | None


class PropertyCreate(PropertyBase):
    owner_id: int


class Property(PropertyBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True


class UserBase(BaseModel):
    username: str
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int

    class Config:
        from_attributes = True
