from models.transaction_class import *
from terminal.terminal.helpers.ddatabase_helpers import get_transactions

def print_transactions():
    transactions = get_transactions()
    for transaction in transactions:
        print("Contract Address: ",transaction["ca"])
        print("Total Amount: ",transaction["total_amount"])
        print("Coin Amount: ",transaction["coin_amount"])
        print("Trades:")
        for trade in transaction["trades"]: 
            print("Tx Address: ",trade["tx_address"])
            print("Amount: ",trade["amount"])
            print("Coin Amount: ",trade["coin_amount"])
            print("Status: ",trade["status"])
