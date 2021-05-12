from threading import Lock

class BankAccount:
    def __init__(self):
        self.account = False
        self.balance = 0
        self.lock = Lock()

    def get_balance(self):
        if self.check_account():
            return self.balance
        else:
            raise ValueError('Not available')

    def open(self):
        if self.check_account():
            raise ValueError('Not available')
        else:
            self.account = True

    def deposit(self, amount):
        with self.lock:
            if self.check_account() and self.check_amount(amount):
                self.balance += amount
            else:
                raise ValueError('Not available')

    def withdraw(self, amount):
        with self.lock:
            if (self.check_account() and
                self.check_amount(amount) and
                self.balance >= amount):
                self.balance -= amount
            else:
                raise ValueError('Not available')

    def close(self):
        if self.check_account():
            self.account = False
            self.balance = 0
        else:
            raise ValueError('Not available')

    def check_account(self):
        if self.account == True:
            return True
        return False

    @staticmethod
    def check_amount(amount):
        if amount > 0:
            return True
