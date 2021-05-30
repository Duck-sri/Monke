
from datetime import datetime
import uuid

from .account import Account

class Transaction:

    def __init__(self,from_address,to_address,amount):

        self.from_address:Account = from_address
        self.to_address:Account = to_address
        self.amount = amount
        self.timestamp = datetime.timestamp(datetime.now())
        self.transaction_id = uuid.uuid1().hex



    def __repr__(self) -> str:
        return f" From : {self.from_address}\n To: {self.to_address}\n Amount: {self.amount}\n"

    def __str__(self) -> str:
        return f" From : {self.from_address}\n To: {self.to_address}\n Amount: {self.amount}\n"