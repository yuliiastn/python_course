from bank_model import Bank, Account


def test_open_account():
    bank = Bank()
    account = Account.create_account('A001')
    bank.open_account(account)
    assert isinstance(account, Account)
    assert account.get_balance() == 0.0
