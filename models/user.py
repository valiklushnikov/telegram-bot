from sqlalchemy import Column, Integer, String, Boolean
from data_base.dbcore import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    is_active = Column(Boolean)

    def __str__(self):
        return f"{self.telegram_id} {self.first_name}"
