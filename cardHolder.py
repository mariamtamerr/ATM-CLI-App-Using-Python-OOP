


class card_holder():

    def __init__(self,firstname,lastname,card_nmber,pin,balance):
        self.firstname = firstname
        self.lastname = lastname
        self.card_nmber = card_nmber
        self.pin = pin
        self.balance = balance

    # getter to know / return the value of each cardholder

    def get_firstname(self):
        return self.firstname
    
    def get_lastname(self):
        return self.lastname
    
    def get_card_nmber(self):
        return self.card_nmber
    
    def get_pin(self):
        return self.pin
    
    def get_balance(self):
        return self.balance
    
    # ------ setter to change the value depending on each carhdolder

    def set_firstname(self, newValue):
        self.firstname = newValue

    def set_lastname(self, newValue):
        self.lastname = newValue

    def set_card_nmber(self, newValue):
        self.card_nmber = newValue

    def set_pin(self, newValue):
        self.pin = newValue

    def set_balance(self, newValue):
        self.balance = newValue


    # ----------------------------------------------------------------------


    




