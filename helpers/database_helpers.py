import helpers


def get_wallets():
    data = helpers.db.getDb(helpers.path.join(helpers.path.dirname(__file__)+"/.." + "/database/wallets.json"))
    return data.getAll()

def get_wallet_by_id(id):
    data = helpers.db.getDb(helpers.path.join(helpers.path.dirname(__file__)+"/.." +"/database/wallets.json"))
    return data.getBy({"id":id}) 

def update_wallet_by_id(old_wallet_id,updated_wallet):
    data = helpers.db.getDb(helpers.path.join(helpers.path.dirname(__file__)+"/.." +"/database/wallets.json"))
    data.updateById(old_wallet_id,updated_wallet)
    
def delete_wallet(id):
    data = helpers.db.getDb(helpers.path.join(helpers.path.dirname(__file__)+"/.." +"/database/wallets.json"))
    data.deleteById(id)
    
def get_modes():
    data = helpers.db.getDb(helpers.path.join(helpers.path.dirname(__file__)+"/.." +"/database/modes.json"))
    return data.getAll()

def get_mode_by_id(id):
    data = helpers.db.getDb(helpers.path.join(helpers.path.dirname(__file__)+"/.." +"/database/modes.json"))
    return data.getBy({"id":id}) 

def update_mode_by_id(old_mode_id,updated_mode):
    data = helpers.db.getDb(helpers.path.join(helpers.path.dirname(__file__)+"/.." +"/database/modes.json"))
    data.updateById(old_mode_id,updated_mode)
    
def delete_mode(id):
    data = helpers.db.getDb(helpers.path.join(helpers.path.dirname(__file__)+"/.." +"/database/modes.json"))
    data.deleteById(id)
    
def get_transactions():
    data = helpers.db.getDb(helpers.path.join(helpers.path.dirname(__file__)+"/.." +"/database/transactions.json"))
    return data.getAll()

def get_transactions_by_query(dict):
    data = helpers.db.getDb(helpers.path.join(helpers.path.dirname(__file__)+"/.." +"/database/transactions.json"))
    return data.getBy({"transactions_name":dict["transaction_name"]}) ##will be completed after transaction model is completed


def get_transaction_by_id(id):
    data = helpers.db.getDb(helpers.path.join(helpers.path.dirname(__file__)+"/.." +"/database/transactions.json"))
    return data.getBy({"id":id}) 

def update_transaction_by_id(old_object_id,updated_object):
    data = helpers.db.getDb(helpers.path.join(helpers.path.dirname(__file__)+"/.." +"/database/transactions.json"))
    data.updateById(old_object_id, updated_object)
    
def delete_transaction(id):
    data = helpers.db.getDb(helpers.path.join(helpers.path.dirname(__file__)+"/.." +"/database/transactions.json"))
    data.deleteById(id)

def get_default_mode_by_name(name):
    data = helpers.db.getDb(helpers.path.join(helpers.path.dirname(__file__)+"/.." + "/database/default_modes.json"))
    return data.getBy({"mode_name":name})

def get_default_modes():
    data = helpers.db.getDb(helpers.path.join(helpers.path.dirname(__file__)+"/.." + "/database/default_modes.json"))
    return data.getAll()

def get_default_mode_by_id(id):
    data = helpers.db.getDb(helpers.path.join(helpers.path.dirname(__file__)+"/.." + "/database/default_modes.json"))
    return data.getBy({"id":id})

def delete_default_mode(id):
    data = helpers.db.getDb(helpers.path.join(helpers.path.dirname(__file__)+"/.." +"/database/default_modes.json"))
    data.deleteById(id)
    
def update_default_mode_by_id(old_mode_id,updated_mode):
    data = helpers.db.getDb(helpers.path.join(helpers.path.dirname(__file__)+"/.." +"/database/default_modes.json"))
    data.updateById(old_mode_id,updated_mode)

def update_default_mode_by_name(name,updated_mode):
    data = helpers.db.getDb(helpers.path.join(helpers.path.dirname(__file__)+"/.." +"/database/default_modes.json"))
    data.update({"mode_name":name},updated_mode)
def add_default_mode(mode):
    data = helpers.db.getDb(helpers.path.join(helpers.path.dirname(__file__)+"/.." +"/database/default_modes.json"))
    data.add(mode)
    