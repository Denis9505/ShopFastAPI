import sqlalchemy as sa
from enum import Enum

from database import Base


class AvailabilityEnum(Enum):
    IN_STOCK = 'IN_STOCK'
    NOT_AVAILABLE = 'NOT_AVAILABLE'


class SizeEnum(Enum):
    EXTRA_SMALL = 'XS'
    SMALL = 'S'
    MEDIUM = 'M'
    LARGE = 'L'
    EXTRA_LARGE = 'XL'
    EXTRA_EXTRA_LARGE = 'XXL'


class Product(Base):
    __tablename__ = 'products'
    id = sa.Column(sa.Integer, primary_key=True, index=True, unique=True)
    title = sa.Column(sa.String(50))
    description = sa.Column(sa.String(350))
    size = SizeEnum
    price = sa.Column(sa.Float)
    availability = AvailabilityEnum
    count = sa.Column(sa.Integer)
