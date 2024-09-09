from pydantic import BaseModel


class BlockBase(BaseModel):
    block_type: str
    parameters: dict | None = None
    parent_id: int


class BlockCreate(BlockBase):
    pass


class Block(BlockBase):
    id: int
    contents: list["Block"] = []

    class Config:
        orm_mode = True
