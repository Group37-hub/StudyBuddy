from app import db
import datetime


def reset_db():
    db.drop_all()
    db.create_all()


