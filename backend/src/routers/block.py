import src.schemas.block as schemas
import src.crud.block as crud
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.core.database import get_db

router = APIRouter()


@router.post("/", response_model=schemas.Block)
def create_block(block: schemas.BlockCreate, db: Session = Depends(get_db)):
    return crud.create_block(db=db, block=block)


@router.get("/", response_model=list[schemas.Block])
def read_blocks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    blocks = crud.get_blocks(db, skip=skip, limit=limit)
    return blocks


@router.get("/{block_id}", response_model=schemas.Block)
def read_employee(block_id: int, db: Session = Depends(get_db)):
    db_block = crud.get_block(db, block_id=block_id)
    if db_block is None:
        raise HTTPException(status_code=404, detail="Block not found")
    return db_block


@router.put("/{block_id}", response_model=schemas.Employee)
def update_block(
    block_id: int, block: schemas.BlockCreate, db: Session = Depends(get_db)
):
    db_block = crud.update_block(db, block_id == block_id, block=block)
    if db_block is None:
        raise HTTPException(status_code=404, detail="Block not found")
    return db_block


@router.delete("/{block_id}")
def delete_block(block_id: int, db: Session = Depends(get_db)):
    crud.delete_block(db, block_id=block_id)
    return {"message": "Block deleted successfully"}
