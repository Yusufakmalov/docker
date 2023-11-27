from pydantic import BaseModel

class CardAddValidator(BaseModel):
    user_id: int
    card_number: int
    balance: float
    exp_date: int
    card_name: str
