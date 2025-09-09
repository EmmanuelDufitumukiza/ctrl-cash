from pydantic import BaseModel
from typing import Optional

class Txn(BaseModel):
    id: str
    ts: Optional[str]
    amount: float
    currency: str
    direction: str
    category: str
    counterparty: str
    description: str
