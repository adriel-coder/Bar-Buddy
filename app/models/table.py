from enum import Enum as PyEnum
from sqlalchemy import Enum as SQLAlchemyEnum

from app import db

class TableStatusEnum(PyEnum):
    FREE = 'FREE'
    OCCUPIED = 'OCCUPIED'
    RESERVED = 'RESERVED'
    UNDER_MAINTENANCE = 'UNDER_MAINTENANCE'

class Table(db.Model):
    __tablename__ = 'tables'
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, unique=True, nullable=False)
    status = db.Column(SQLAlchemyEnum(TableStatusEnum), default=TableStatusEnum.FREE, nullable=False)

