from datetime import datetime
from database.models import User
from database import get_db

def register_db(name, surname, email, password, city, phone_number):
    db = next(get_db())

    new_user = User(name=name, surname=surname, password=password, email=email, city=city, phone_number=phone_number)
    db.add()
    db.commit()

    return "User successfully registered"


def get_exact_user_db(user_id):
    db = next(get_db())

    checker = db.query(User).filter_by(user_id=user_id).first()

    return checker


def check_user_email_db(email):
    db = next(get_db())

    checker = db.query(User).filter_by(email=email).first()

    if checker:
        return checker
    else:
        return {'message': "Not found"}


def edit_user_db(user_id, edit_type, new_data):
    db = next(get_db())


    exact_user = db.query(User).filter_by(user_id=user_id).first()

    if exact_user:
        if edit_type == 'email':
            exact_user.email = new_data

        elif edit_type == 'password':
            exact_user.password == new_data

        elif edit_type == 'city':
            exact_user.city = new_data

            db.commit()

        return "data successfully change"
    else:
        return 'User not found'

def delete_user_db(user_id):
    db = next(get_db())

    exact_user = db.query(User).filter_by(user_id=user_id).first()

    if exact_user:
        db.delete(exact_user)
        db.commit()

        return "user successfully deleted"
    else:
        return "user not found"




