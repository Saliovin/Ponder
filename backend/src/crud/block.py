from sqlalchemy.orm import Session

from src.models.block import Block
from src.schemas.block import BlockCreate


def get_block(db: Session, user_id: int):
    return db.query(Block).filter(Block.id == user_id).first()


def get_blocks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Block).offset(skip).limit(limit).all()


def create_block(db: Session, block: BlockCreate):
    db_block = Block(
        block_type=block.block_type,
        parameters=block.parameters,
        parent_id=block.parent_id,
    )
    db.add(db_block)
    db.commit()
    db.refresh(db_block)
    return db_block


def update_block(db: Session, block_id: int, block: BlockCreate):
    db_block = db.query(Block).filter(Block.id == block_id).first()
    if not db_block:
        return None
    for key, value in block:
        setattr(db_block, key, value)
    db.commit()
    db.refresh(db_block)
    return db_block


def delete_block(db: Session, block_id: int):
    db_block = db.query(Block).filter(Block.id == block_id).first()
    if db_block:
        db.delete(db_block)
        db.commit()
