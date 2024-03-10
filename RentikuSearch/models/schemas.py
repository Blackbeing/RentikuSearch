from pydantic import BaseModel


class PropertyBase(BaseModel):
    title: str
    description: str
    action: str
    price: float
    rent: float
    num_rooms: int
    address: str
    latitude: str
    longitude: str
    region: str
    image_url: str


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
