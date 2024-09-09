from sqlalchemy import JSON, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from src.core.database import Base


class Block(Base):
    __tablename__ = "blocks"

    id = Column(Integer, primary_key=True)
    block_type = Column(String)
    parameters = Column(JSON, default={})
    parent_id = Column(Integer, ForeignKey("blocks.id"))

    contents = relationship("Block", back_populates="parent")
    parent = relationship("Block", back_populates="contents", remote_side=[id])
