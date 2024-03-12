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


class PropertyUpdate(BaseModel):
    title: str = None
    description: str | None = None
    action: str | None = None
    price: float = None
    rent: float = None
    num_rooms: int = None
    address: str | None = None
    latitude: str | None = None
    longitude: str | None = None
    region: str | None = None
    image_url: str | None = None

    class Config:
        from_attributes = True


class Property(PropertyBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str
    email: str


class User(UserBase):
    id: int
    email: str

    class Config:
        from_attributes = True


class UserLogin(UserBase):
    password: str


class UserUpdate(BaseModel):
    password: str


class Token(BaseModel):
    access_token: str
