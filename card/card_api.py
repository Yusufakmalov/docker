# make a router
# zapros na dobavleniye karti - async  def add_new_card()
# zapros na polucheniye info ob opredeleniye karti usera


from fastapi import APIRouter
from datetime import datetime

from card import CardAddValidator
from database.cardservice import get_exact_user_cards_db, get_all_transactions_db, validate_card_db, check_card_db, check_card_info, delete_card_db, add_card_db

card_router = APIRouter(prefix='/card', tags=[' work with cards'])

@card_router.get('/get_user_card')
async def get_exact_user_card(card_name: str, card_number: int):
    result = get_exact_user_cards_db(card_number, card_name)

    if result:
        return {'Message': "Successfully done!"}
    else:
        return {'Message': "ERROR!"}

@card_router.get('/transaction')
async def get_all_transactions(card_name: str, card_number: int):
    result = get_all_transactions_db(card_number, card_name)

    if result:
        return {'Message': "Successfully transacted!"}
    else:
        return {'Message': "ERROR!"}

@card_router.get('/validat_card')
async def validate_card(data: CardAddValidator):
    validator = data.model_dump()

    result = validate_card_db(**validator)

    return {'Message': result}

@card_router.put('/add')
async def add_card(card_name: str, card_number: int):
    result = add_card_db(card_number, card_name)

    if result:
        return {'Message': "Successfully Added!"}
    else:
        return {'Message': "ERROR!"}

