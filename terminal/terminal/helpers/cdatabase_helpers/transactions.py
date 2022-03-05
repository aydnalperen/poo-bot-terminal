from models.transaction_class import *
from helpers.ddatabase_helpers import *

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

def add_to_transactions(trade):
    transaction_address = trade["tx_address"]
    trade.save_trade_to_db()
    
    transactions = get_transactions()
    
    if transactions:
        for transaction in transactions:
            if transaction["tx_address"] == trade.tx_address:
                transaction["trades"].append(trade.__dict__)
                update_transaction_by_id(transaction["id"],transaction)  
    else:
        transaction = TransactionClass(transaction_address)   
        transaction.add_trade(trade)
        transaction.save_transaction_to_db() 
        
def print_current_trades(trades):
    pass
    #for trade in trades:
        
    