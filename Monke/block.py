from datetime import datetime
from hashlib import sha256
import numpy as np
from typing import List,Union


# my imports
from .transaction import Transaction

class Block:  # transcation

    def __init__(self,transactions:Transaction,prev_hash:str = ''):
        self.timestamp = datetime.timestamp(datetime.now())
        self.transactions:List[Transaction] = list(transactions)
        self.prev_hash = prev_hash
        self.noice = np.random.randint(1,100000)
        self.hash = self.sha_sum_block()

    def __eq__(self,block_b) -> bool: 
        return self.hash == block_b.hash

    def sha_sum_block(self) -> str:
        s = f"{self.timestamp}{str(self.transactions)}{self.prev_hash}{self.noice}"
        h = sha256(s.encode('utf-8')).hexdigest()
        return h


    def __str__(self): return f" Timestamp : {self.timestamp}\n Data : {self.transactions}\n previousHash : {self.prev_hash}\n hash : {self.hash}\n"