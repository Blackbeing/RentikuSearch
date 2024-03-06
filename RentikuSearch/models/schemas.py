from pydantic import BaseModel


class PropertyBase(BaseModel):
    title: str
    description: str
    type: str
    location: str
    price: float


class propertyCreate(PropertyBase):
    pass


class Property(PropertyBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True


class UserBase(BaseModel):
    username: str
    email: str


class UserCreate(UserBase):
    password_hash: str


class User(UserBase):
    id: int

    class Config:
        from_attributes = True
