from dataclasses import dataclass
from datetime import datetime
from marshmallow import fields
from suave.assets.bases import Base, BaseSchema


@dataclass
class Equity(Base):

    date: datetime = None
    ticker: str = None
    volume: float = None
    price: float = None


class EquitySchema(BaseSchema):

    date = fields.DateTime()
    ticker = fields.String()
    volume = fields.Float()
    price = fields.Float()

    class Meta:
        dateformat = '%Y-%m-%d %H:%M:%S'
