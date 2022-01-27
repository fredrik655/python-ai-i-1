
from re import S


class Account:
    """
        Account class 
        attributes:
        amount: int
        account_type: string
        account_nr: int
    """
    def __init__(self, account_nr):
        self.amount = 0
        self.account_type = "debit account"
        self.account_nr = account_nr

    def get_amount(self):
        """
            get amount of money in account
            @returns: amount
        """
        return self.amount

    
    def deposit(self, amount):
        """
        deposit is used to add money to the account
        @param amount: amount to deposit to the account
        """
        self.amount += amount

    def withdraw(self, amount):
        """
            withdraw removes money from the account.
            @param amount: amount to widthdraw
            @returns: True if successful else False if withdraw unsuccessful i.e. trying to widthdraw more money
            then is in the account 
        """
        new_amount = self.amount - amount
        if(new_amount >= 0):
            self.amount = new_amount
            return True
        else:
            return False

    def get_account_number(self):
        """
            Get account number
            @returns: account number
        """
        return self.account_nr


    def get_account_info(self):
        """
            returns a dict with all the info about the account
            @returns: dict in format {account_nr, account_typ, amount}
        """
        return {
            "account_nr": self.account_nr,
            "account_type": self.account_type,
            "amount": self.amount
        }

if __name__ == '__main__':
    print("Account is running from cmd")