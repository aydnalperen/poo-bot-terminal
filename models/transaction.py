from pysondb import db
import helpers

class TransactionClass():
    def __init__(self, ca, trades = [], total_amount = 0, coin_amount = 0,is_over=False):
        self.ca = ca
        self.trades = trades
        self.total_amount = total_amount
        self.coin_amount = coin_amount
        self.is_over = is_over

    # Add trade only when its status is successfull
    def add_trade(self, trade):
        self.trades.append(trade)
        self.total_amount += trade.amount
        self.coin_amount += trade.coin_amount

    # def calculate_pnl(self):
    #     # TODO: (Eren) Get latest price of the coin
    #     return self.coin_amount * (price of the coin) / self.total_amount * 100 - 100

    def save_transaction_to_db(self):
        data = db.getDb("database/transactions.json")
        data.add(self.__dict__)

        

            

class TradeClass():
    def __init__(self, tx_address, amount, coin_amount, status):
        self.tx_address = tx_address
        self.amount = amount
        self.coin_amount = coin_amount
        self.status = status

    def check_status_and_update(self):
        self.status = helpers.get_status(self, self.tx_address)

    def check_coin_amount_and_update(self):
        self.coin_amount = 0 # TODO: (Eren) Get coin amount out from the transaction

    def save_trade_to_db(self):
        data = db.getDb("database/trades.json")
        data.add(self.__dict__)