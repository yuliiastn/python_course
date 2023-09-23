from bank_model import SavingsAccount, CurrentAccount, Bank


def test_add_interest_to_savings_account():
    savings_account = SavingsAccount(1000.0, 'S001', 2.5)
    bank = Bank()
    bank.open_account(savings_account)
    expected_balance = 1000.0 + (1000.0 * (2.5 / 100))
    bank.update()
    assert savings_account.get_balance() == expected_balance


def test_update_sends_overdraft_letter(mocker):
    bank = Bank()
    current_account = CurrentAccount(-100.0, 'C001', 0)
    bank.open_account(current_account)
    mock_send_overdraft_letter = mocker.patch.object(
        current_account, 'send_overdraft_letter'
        )
    bank.update()
    mock_send_overdraft_letter.assert_called()
