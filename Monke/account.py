
import uuid
from typing import List



class Account:

    def __init__(self,passphrase):
        self.passphrase = passphrase
        # self.amount = 0
        self.address = uuid.uuid1().hex
        self.transactions = []


    
    def __repr__(self) -> str:
        return self.address