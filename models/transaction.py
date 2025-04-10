from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship, backref
from data_base.dbcore import Base
from .user import User


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True)
    amount = Column(Float)
    currency = Column(String)
    exchange_amount = Column(Float)
    date = Column(DateTime)
    user_telegram_id = Column(Integer, ForeignKey("users.telegram_id"))
    user = relationship(
        User, backref=backref("transactions", uselist=True, cascade="delete, all")
    )

    def __str__(self):
        return f"{self.amount} {self.currency} {self.exchange_amount}"

    def to_dict(self):
        return {
            "amount": self.amount,
            "currency": self.currency,
            "exchange_amount": self.exchange_amount,
            "date": self.date.strftime("%Y-%m-%d %H:%M:%S"),
            "user_telegram_id": self.user_telegram_id,
        }
