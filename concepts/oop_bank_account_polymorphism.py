"""Problem Statement: Imagine extending the BankAccount class to support different types of accounts,
such as SavingsAccount and CheckingAccount. Each type has its own rules for withdrawals:

* SavingsAccount allows withdrawal only once per month
* CheckingAccount has no such restriction

How would you implement this using polymorphism in Python?
Discuss the advantages of using polymorphism in this scenario and how it enhances flexibility and maintainability in the system."""

from typing import List, Tuple
from pydantic import BaseModel
from uuid import uuid4
from datetime import datetime, timezone, date

from loguru import logger


class BaseBankAccountException(Exception):
    pass


class DepositNotPositive(BaseBankAccountException):
    """Deposit must be positive"""


class WithdrawalNotPositive(BaseBankAccountException):
    """Withdrawal must be positive"""


class WithdrawalAlreadyMadeThisMonth(BaseBankAccountException):
    """Withdrawals for some accounts can only be made once per month"""


class InsufficientFunds(BaseBankAccountException):
    """Must have more funds than requested withdraw amount"""


class AccountHistoryData(BaseModel):
    recordGuid: str
    time: datetime
    transaction_type: str
    amount: float
    balance_after: float


class AccountHistory:
    def __init__(self) -> None:
        self._history = []

    @property
    def history(self):
        return self._history

    def add_record(
        self, amount: float, transaction_type: str, balance_after: float
    ) -> None:
        record_guid = str(uuid4())
        time_now = datetime.now(timezone.utc)
        record = AccountHistoryData(
            recordGuid=record_guid,
            time=time_now,
            transaction_type=transaction_type,
            amount=amount,
            balance_after=balance_after,
        )
        self._history.append(record)
        logger.info(f"GUID: {record_guid}")

    def get_records(self) -> List:
        return self._history


class BankAccount:
    def __init__(self) -> None:
        self._balance: float = 0
        self._account_history = AccountHistory()

    @property
    def balance(self) -> float:
        return self._balance

    @property
    def account_history(self) -> AccountHistory:
        return self._account_history

    def deposit(self, money: float) -> None:
        if money <= 0:
            raise DepositNotPositive(
                f"{money} was attempted to be deposited but deposit must be a positive value"
            )
        self._balance += money
        self._account_history.add_record(
            amount=money, transaction_type="deposit", balance_after=self._balance
        )

    def withdraw(self, money: float) -> None:
        if money <= 0:
            raise WithdrawalNotPositive(
                f"{money} was attempted to be withdrawn but withdrawal must be a positive value"
            )
        elif money > self._balance:
            raise (
                InsufficientFunds(
                    f"{money} was attempted to be withdrawn but you don't have enough funds"
                )
            )
        self._balance -= money
        self._account_history.add_record(
            amount=money, transaction_type="withdrawal", balance_after=self._balance
        )


class SavingsAccount(BankAccount):
    def __init__(self) -> None:
        super().__init__()
        self.withdrawn_this_month = False
        # Initialize as an empty tuple
        self.month_year_withdrawn: Tuple[int, int] = ()

    def withdraw(self, money: float) -> None:
        current_date = datetime.now(timezone.utc).date()
        current_month = current_date.month
        current_year = current_date.year

        # Check if a withdrawal has already been made this month
        if self.withdrawn_this_month and self.month_year_withdrawn == (
            current_month,
            current_year,
        ):
            self._account_history.add_record(
                amount=0, transaction_type="withdrawal", balance_after=self._balance
            )
            raise WithdrawalAlreadyMadeThisMonth(
                "Another withdrawal cannot be made until the next month."
            )

        if money <= 0:
            self._account_history.add_record(
                amount=0, transaction_type="withdrawal", balance_after=self._balance
            )
            raise WithdrawalNotPositive(
                f"{money} was attempted to be withdrawn but withdrawal must be a positive value"
            )
        elif money > self._balance:
            self._account_history.add_record(
                amount=0, transaction_type="withdrawal", balance_after=self._balance
            )
            raise InsufficientFunds(
                f"{money} was attempted to be withdrawn but you don't have enough funds"
            )

        self._balance -= money
        self._account_history.add_record(
            amount=money, transaction_type="withdrawal", balance_after=self._balance
        )

        # Update the withdrawal status and store the month and year
        self.withdrawn_this_month = True
        self.month_year_withdrawn = (current_month, current_year)


class CheckingAccount(BankAccount):
    def __init__(self) -> None:
        super().__init__()

    def withdraw(self, money: float) -> None:
        return super().withdraw(money)


if __name__ == "__main__":
    s = SavingsAccount()
    s.deposit(1000)
    s.withdraw(200)
    logger.debug(s.balance)
    logger.debug(s.account_history.get_records())
    s.withdraw(200)  # This will raise WithdrawalAlreadyMadeThisMonth error

    c = CheckingAccount()
    c.deposit(2)
    c.deposit(4)
    c.withdraw(1)
    c.withdraw(2)
    c.withdraw(3)
