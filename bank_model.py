class Account:
    def __init__(self, balance, account_number):
        self._balance = balance
        self._account_number = account_number

    @classmethod
    def create_account(cls, account_number):
        return cls(0.0, account_number)

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            raise ValueError('Amount must be positive')

    def withdraw(self, amount):
        if amount > 0:
            self._balance -= amount
        else:
            raise ValueError('Amount must be positive')

    def get_balance(self):
        return self._balance

    def get_account_number(self):
        return self._account_number

    def __str__(self):
        return f'Account number: {self._account_number}, balance: {self._balance}'


class SavingsAccount(Account):
    def __init__(self, balance, account_number, interest_rate):
        super().__init__(balance, account_number)
        self.interest_rate = interest_rate

    def add_interest(self, years):
        for _ in range(years):
            interest_earned = self._balance * (self.interest_rate / 100)
            self._balance += interest_earned


class CurrentAccount(Account):

    def __init__(self, balance, account_number, overdraft_limit):
        super().__init__(balance, account_number)
        self.overdraft_limit = overdraft_limit

    def send_overdraft_letter(self):
        return "Sending overdraft letter to current account"

    def update(self):
        if self._balance < 0:
            self.send_overdraft_letter()


class Bank:
    def __init__(self):
        self.accounts = []

    def open_account(self, account):
        self.accounts.append(account)

    def close_account(self, account):
        self.accounts.remove(account)

    def pay_dividend(self, dividend_amount):
        for account in self.accounts:
            account.deposit(dividend_amount)

    def update(self):
        for account in self.accounts:
            if isinstance(account, SavingsAccount):
                account.add_interest(1)
            elif isinstance(account, CurrentAccount):
                if account.get_balance() < 0:
                    account.send_overdraft_letter()

    def __str__(self):
        return f'Bank with {len(self.accounts)} accounts'
