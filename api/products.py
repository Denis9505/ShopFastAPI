from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from models.products import BaseProduct, CreateProduct
from tables import Product
from database import get_session


router = APIRouter(prefix='/products')


@router.get('/', response_model=List[BaseProduct])
def get_list_products(session: Session = Depends(get_session)):
    products = session.query(Product).all
    return products


@router.post('/', response_model=BaseProduct)
def create_product(item: CreateProduct, session: Session = Depends(get_session)):
    product = Product(**item.dict())
    session.add(product)
    session.commit()
    return product
