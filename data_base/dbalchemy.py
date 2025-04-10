from os import path
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy import desc
from sqlalchemy.orm import sessionmaker
from data_base.dbcore import Base

from common.interface import Singleton
from settings import config
from models.transaction import Transaction
from models.user import User


class DBManager(metaclass=Singleton):
    def __init__(self):
        self.engine = create_engine(config.DATABASE)
        session = sessionmaker(bind=self.engine)
        self._session = session()

        db_path = config.DATABASE.replace("sqlite:///", "")
        if not path.exists(db_path):
            Base.metadata.create_all(self.engine)

    def _get_all_transaction(self, user_id):
        result = (
            self._session.query(Transaction)
            .filter_by(user_telegram_id=user_id)
            .order_by(desc(Transaction.date))
            .all()[:10]
        )
        self.close()
        return result

    def _add_transaction(self, user, transaction):
        user_instance = (
            self._session.query(User)
            .filter_by(telegram_id=user.get("telegram_id"))
            .first()
        )
        if not user_instance:
            user_instance = User(
                telegram_id=user.get("telegram_id"),
                first_name=user.get("first_name"),
                last_name=user.get("last_name"),
                is_active=True,
            )
            self._session.add(user_instance)
            self._session.commit()

        transaction = Transaction(
            amount=transaction.get("amount"),
            currency=transaction.get("currency"),
            exchange_amount=transaction.get("exchange_amount"),
            date=datetime.strptime(transaction.get("date"), "%d-%B-%Y %H:%M:%S"),
            user=user_instance,
        )
        self._session.add(transaction)
        self._session.commit()
        self.close()

    def close(self):
        self._session.close()
