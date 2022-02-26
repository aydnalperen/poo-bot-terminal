from pysondb import db
class ModeClass():
    def __init__(self, name, wallets, max_tax):
        self.mode_name = name
        self.wallets = wallets
        self.max_tax = max_tax

    def str(self):
        return self.mode_name
        
    def save_to_db(self):
        data = db.getDb("database/modes.json")
        data.add(self.__dict__)