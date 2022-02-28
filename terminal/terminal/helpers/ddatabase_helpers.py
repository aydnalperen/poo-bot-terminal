from pysondb import db
from os import path
def get_wallets():
   data = db.getDb(path.join(path.dirname(__file__)+"/.." + "/database/wallets.json"))
   return data.getAll()

def get_wallet_by_id(id):
   data = db.getDb(path.join(path.dirname(__file__)+"/.." +"/database/wallets.json"))
   return data.getBy({"id":id}) 

def update_wallet_by_id(old_wallet_id,updated_wallet):
    data = db.getDb(path.join(path.dirname(__file__)+"/.." +"/database/wallets.json"))
    data.updateById(old_wallet_id,updated_wallet)
    
def delete_wallet(id):
    data = db.getDb(path.join(path.dirname(__file__)+"/.." +"/database/wallets.json"))
    data.deleteById(id)
    
def get_modes():
    data = db.getDb(path.join(path.dirname(__file__)+"/.." +"/database/modes.json"))
    return data.getAll()

def get_mode_by_id(id):
    data = db.getDb(path.join(path.dirname(__file__)+"/.." +"/database/modes.json"))
    return data.getBy({"id":id}) 

def update_mode_by_id(old_mode_id,updated_mode):
    data = db.getDb(path.join(path.dirname(__file__)+"/.." +"/database/modes.json"))
    data.updateById(old_mode_id,updated_mode)
    
def delete_mode(id):
    data = db.getDb(path.join(path.dirname(__file__)+"/.." +"/database/modes.json"))
    data.deleteById(id)
    
def get_transactions():
    data = db.getDb(path.join(path.dirname(__file__)+"/.." +"/database/transactions.json"))
    return data.getAll()

def get_transactions_by_query(dict):
   data = db.getDb(path.join(path.dirname(__file__)+"/.." +"/database/transactions.json"))
   return data.getBy({"transactions_name":dict["transaction_name"]}) ##will be completed after transaction model is completed


def get_transaction_by_id(id):
   data = db.getDb(path.join(path.dirname(__file__)+"/.." +"/database/transactions.json"))
   return data.getBy({"id":id}) 

def update_transaction(old_object,updated_object):
    data = db.getDb(path.join(path.dirname(__file__)+"/.." +"/database/transactions.json"))
    data.update(old_object, updated_object)
    
def delete_transaction(id):
    data = db.getDb(path.join(path.dirname(__file__)+"/.." +"/database/transactions.json"))
    data.deleteById(id)