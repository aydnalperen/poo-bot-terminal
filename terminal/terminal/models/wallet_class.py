from pysondb import db
class WalletClass():
    def __init__(self, name, address, private_key, buy_amount, gas_limit, buy_gwei, sell_gwei, nonce, approved_tokens):
        self.wallet_name = name
        self.address = address
        self.private_key = private_key
        self.buy_amount = buy_amount
        self.gas_limit = gas_limit
        self.buy_gwei = buy_gwei
        self.sell_gwei = sell_gwei
        self.nonce = nonce
        self.approved_tokens = approved_tokens

    def str(self):
        return self.wallet_name
    def save_to_db(self):
        data = db.getDb("database/wallets.json")
        print(data)
        data.add(self.__dict__)