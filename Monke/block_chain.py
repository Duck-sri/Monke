"""
Welcome to the my Block chain implementation !!

Introducing      -->   Monke, together strong

"""
import sys
from time import time
from typing import List

import numpy as np

# my imports
#TODO -- fix these import errors
from .account import Account
from .block import Block
from .transaction import Transaction
from .utils.hash_utils import sha_sum


class BlockChain:

    def __init__(self):
        self.chain:List[Block] = []
        self.difficulty = 2
        self.pending_transactions: List[Transaction] = []  #ttoda add this as a stack or choose not to, it is choosen by miner 
        self.mining_reward = 100


    @staticmethod
    def create_genesis_block() -> Block:
        return Block({},'')
    
    def get_latest_block(self) -> Block :
        if len(self.chain) > 0:
            return self.chain[-1]
        else:
            return self.create_genesis_block()

    def add_block(self,new_block:Block,display:bool = False) -> bool:

        if self.mine_block(new_block,display):
            new_block.prev_hash = sha_sum(self.get_latest_block().hash)
            new_block.hash = new_block.sha_sum_block() # recalculate the hash 
            self.chain.append(new_block)

            #TODO add a p2p arroval logic
            return True


    def proof_of_work(self,new_block:Block,display:bool = False) -> bool:

        start = time()
        count = 0
        while( new_block.hash[:self.difficulty] != '0'*self.difficulty):
            new_block.noice = np.random.randint(0,100000)
            new_block.hash = new_block.sha_sum_block()
            count += 1

        print(f"Block Mined: {new_block.hash}\n")

        end = time()
        if display:
            print(f"Took abt {round(end - start,3) }s  and {count} iterations to generate hash \n")

        return True

    def mine_block(self,new_block:Block,display:bool = False) -> bool :
        return self.proof_of_work(new_block,display)



    def mine_pending_transactions(self,miner_address):
        #TODO considering all transactions are inside one block, need to change later
        block = Block(self.pending_transactions)

        # this may need a new p2p approval
        if self.add_block(block,True):
            self.pending_transactions = [Transaction(None,miner_address,self.mining_reward)]
        else:
            self.pending_transactions = []


    def create_transactions(self,new_transactions) -> None:
        for trans in new_transactions:
            self.pending_transactions.append(trans)


    def get_balance_of_address(self,address) -> float:
        balance = 0.0
        
        for block in self.chain:
            for trans in block.transactions:
                if (address == trans.from_address):
                    balance -= trans.amount
                elif (address == trans.to_address):
                    balance += trans.amount

        return balance

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
    monke.difficulty = 2

    trans = []
    miner = Account("hi")
    ram = Account('ram')
    mahes = Account('mahes')
    trans.append(Transaction(ram.address,mahes.address,1000))
    trans.append(Transaction(mahes.address,ram.address,80))
    trans.append(Transaction(mahes.address,ram.address,80))

    monke.create_transactions(trans)
    monke.mine_pending_transactions(miner.address)

    print(f"Is the chain secure? {monke.verify_chain()}")
    print(f"Ram balance : {monke.get_balance_of_address(ram.address)}")
    print(f"Mahes balance : {monke.get_balance_of_address(mahes.address)}")
    """
    Block can have many transactions in this imple
    """


if __name__ == '__main__':
    main()
