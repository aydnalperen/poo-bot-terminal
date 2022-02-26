from models.wallet_class import WalletClass
from ..ddatabase_helpers import *
from ..transaction_helpers import *


def create_wallet():
    name = input("Give a name to your wallet and press ENTER: ")
    address = input("Paste the wallet adress here and press ENTER: ")
    private_key = input("Write private key of your wallet and press ENTER: ")
    buy_amount = float(input(
        "Give a buying amount to this wallet and press ENTER: "))
    gas_limit = float(input(
        "Give a gas limit to this wallet and press ENTER: "))
    buy_gwei = float(input(
        "Write the amount of buying gwei and press ENTER: "))
    sell_gwei = float(input(
        "Write the amount of selling gwei and press ENTER: "))

    approved_tokens = []

    nonce = get_nonce(address)
    if nonce is None:
        return "wallet address problem"
    print("\n->Added your wallet.")

    print("WalletClass Name: "+name)
    print("WalletClass Adress: " + address)
    print("Buying Amonut: " + str(buy_amount))
    print("Gas Limit : " + str(gas_limit))
    print("Buying Gwei Limit" + str(buy_gwei))
    print("Selling Gwei Limit" + str(sell_gwei))

    wallet = WalletClass(name, address, private_key, buy_amount,
                         gas_limit, buy_gwei, sell_gwei, nonce, approved_tokens)
    wallet.save_to_db()

    print("New wallet added into database.")


def update_wallet():
    pass


def delete_wallet():
    pass


def print_wallets():
    print("Wallets:")
    wallets = get_wallets()

    at_str = ""

    for i in range(len(wallets)):
        for at in wallets[i]["approved_tokens"]:
            at_str += at

        if(at_str == ""):
            at_str = "There is not approved token yet."

        walletTemp = wallets[i]

        print("- "+str(i+1) + ". Name:" + walletTemp["wallet_name"] + "  Adress:" + walletTemp["address"] + "  Buying Amount:" + walletTemp["buy_amount"] + "  Buying Gwei:" + walletTemp["buy_gwei"]
              + "  Selling Gwei:" + walletTemp["sell_gwei"] + "  Approved Tokens:" + at_str)
