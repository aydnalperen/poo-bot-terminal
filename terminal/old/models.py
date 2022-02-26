class Wallet:
    def __init__(self, name, address, private_key, buy_amount, gas_limit, buy_gwei, sell_gwei, nonce, approved_tokens):
        self.name = name
        self.address = address
        self.private_key = private_key
        self.buy_amount = buy_amount
        self.gas_limit = gas_limit
        self.buy_gwei = buy_gwei
        self.sell_gwei = sell_gwei
        self.nonce = nonce
        self.approved_tokens = approved_tokens
        
    def __str__(self):
        return self.name

class Mode:
    def __init__(self, name, wallets, max_tax):
        self.name = name
        self.wallets = wallets
        self.max_tax = max_tax

    def __str__(self):
        return self.name
