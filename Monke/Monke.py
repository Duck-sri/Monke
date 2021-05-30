"""
Welcome to the my Block chain implementation !!

Introducing      -->   Monke, together strong

"""

from datetime import datetime
from hashlib import sha256
from time import time
import numpy as np

class Block:  # transcation


    def __init__(self,index,data:dict,prev_hash:str = ''):
        self.index = index # where on the chain 
        self.timestamp = datetime.timestamp(datetime.now())
        self.data = data
        self.prev_hash = prev_hash
        self.noice = np.random.randint(1,100000)
        self.hash = self.sha_sum_block()

    def __eq__(self,block_b) -> bool: 
        return self.hash == block_b.hash

    def sha_sum_block(self) -> str:
        s = f"{self.timestamp}{str(self.data)}{self.prev_hash}{self.noice}"
        h = sha256(s.encode('utf-8')).hexdigest()
        return h



    
    def __str__(self):
        return f"\
Index : {self.index}\n\
Timestamp : {self.timestamp}\n\
Data : {self.data}\n\
previousHash : {self.prev_hash}\n\
hash : {self.hash}\n"


def sha_sum(string):
    h = sha256(string.encode('utf-8')).hexdigest()
    return h




class BlockChain:

    def __init__(self):
        self.chain = []
        self.difficulty = 4


    @staticmethod
    def create_genesis_block() -> Block:
        return Block(0,{},'')
    
    def get_latest_block(self) -> int :
        if len(self.chain) > 0:
            return self.chain[-1]
        else:
            return self.create_genesis_block()

    def add_block(self,new_block:Block,display:bool = False) -> None:

        if self.proof_of_work(new_block,display):
            new_block.prev_hash = sha_sum(self.get_latest_block().hash)
            new_block.hash = new_block.sha_sum_block() # recalculate the hash 
            self.chain.append(new_block)


    def proof_of_work(self,new_block:Block,display:bool = False) -> bool:

        start = time()
        count = 0
        while( new_block.hash[:self.difficulty] != '0'*self.difficulty):
            new_block.noice = np.random.randint(0,100000)
            new_block.hash = new_block.sha_sum_block()
            count += 1

        end = time()
        if display:
            print(f"Took abt {round(end - start,3) }s  and {count} iterations to generate hash \n")

        return True


    def verify_chain(self) -> bool:
        count = 1
        for curr in self.chain[1:]:

            if curr.sha_sum_block() != curr.hash:
                print(f"Current block has been tampered! pos = {count }")
                return False

            prev = self.chain[count-1]
            if sha_sum(prev.hash) != curr.prev_hash:
                print(f"Either of Blocks {count-1,count} has been tampered !  ")
                return False

            count += 1

        return True

    def __repr__(self):
        res = ''
        for block in self.chain:
            res += str(block) + '\n'

        return res

def main():
    monke: BlockChain = BlockChain()
    monke.difficulty = 4
    for i in range(1,11):
        ape = Block(i,{"amt":i**2,"from":"hi","to":"bye"},'')
        monke.add_block(ape,True)

    # print(monke)
    print(monke.verify_chain(),end='\n\n')


if __name__ == '__main__':
    main()