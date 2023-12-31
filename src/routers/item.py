from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from src.models.item import Item
from src.schemas.item import Item as ItemCreate, ItemOrm

from src.db import session_factory

router = APIRouter()


@router.post("/items", response_model=ItemOrm)
async def create_item(item_data: ItemCreate, db: Session = Depends(session_factory)):
    """
    Itemを一件Insertするためのエンドポイント
    """

    item = Item(**item_data.model_dump())
    # データの追加
    db.add(item)
    # データの登録
    db.commit()
    # 一時データのリフレッシュ
    db.refresh(item)

    return item


@router.post("/item_list", response_model=List[ItemOrm])
async def create_item_list(
    item_data_list: List[ItemCreate], db: Session = Depends(session_factory)
):
    """
    複数まとめてItemをInsertするためのエンドポイント
    """

    item_list = [
        Item(
            name=item.name,
            description=item.description,
        )
        for item in item_data_list
    ]
    db.add_all(item_list)
    db.commit()
    return item_list


@router.get("/items", response_model=List[ItemOrm])
async def get_items(db: Session = Depends(session_factory)):
    """
    Itemを全件取得するためのエンドポイント
    """

    items = db.scalars(select(Item)).all()

    return items


@router.get("/items/{item_id}", response_model=ItemOrm)
async def get_item(item_id: int, db: Session = Depends(session_factory)):
    """
    ID指定したItemを取得するエンドポイント
    """

    item = db.scalar(select(Item).where(Item.id == item_id))
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item
