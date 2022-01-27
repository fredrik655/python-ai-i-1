

import Account as ac


class Customer:
    
    def __init__(self, id, name, pnr):
        self.id = id
        self.customer_name = name
        self.pnr = pnr
        self.customer_accounts = []


    def get_id(self):
        """
            Get customer id
            @returns: customer id
        """
        return self.id

    def get_name(self):
        """
            Get customer name
            @returns: customer name
        """
        return self.customer_name

    def set_name(self, name):
        """
            sets name of customer
            @param name: sets name
        """
        self.customer_name = name

    def get_pnr(self):
        """
            get personnummer of customer
            @returns: personnummer
        """
        return self.pnr

    def add_account_with_id(self, account_id):
        """
            Add account with account id
            @param account_id: account id
            @returns: True if successful else False
        """
        for account in self.customer_accounts:
            if(account.get_account_number() == account_id):
                return False
        self.customer_accounts.append(ac.Account(account_id))
        return True

    def get_account(self, account_id):
        """
            Get customer account
            @param account_id: account id
            @returns: account if successful else null
        """
        for account in self.customer_accounts:
            if(account.get_account_number() == account_id):
                return account
        return null

    def get_account_info(self, account_id):
        """
            Get info about an account
            @param account_id: account id
            @returns: account info as a dict or if no account was found returns empty string
        """
        for account in self.customer_accounts:
            if(account.get_account_number() == account_id):
                return account.get_account_info()
        return ""

    def close_account(self, account_id):
        """
            Close a customer account
            @param account_id: account id
            @returns: info about closed account if successful else empty string
        """
        for i in range(len(self.customer_accounts)):
            if(int(self.customer_accounts[i].get_account_number()) == account_id):
                pop_item = self.customer_accounts[i].get_account_info()
                del self.customer_accounts[i]
                return pop_item
        return ""

    def close_all_accounts(self):
        """
            Close all customer accounts
            @returns: info about all closed accounts and the amount of money in all closed accounts
        """
        total_return_amount = 0
        removed_accounts = []
        for account in self.customer_accounts:
            total_return_amount += account.get_amount()
            removed_accounts.append(account.get_account_number())
        return {"amount": total_return_amount, "removed_accounts": removed_accounts}

    def get_all_accounts_info(self):
        """
            Get information about all accounts
            @returns: list of all customer accounts info
        """
        accounts = []
        for account in self.customer_accounts:
            accounts.append(account.get_account_info())
        return accounts

    def get_all_account_id(self):
        """
            Get all account ids
            @returns: list of account ids
        """
        ids = []
        for ac in self.customer_accounts:
            ids.append(ac.get_account_number())
        return ids

    def deposit(self, account_id, amount):
        """
            Deposit money into a customer account
            @param account_id: account id
            @param amount: amount to deposit
            @returns: True if successful else False
        """
        for i in range(len(self.customer_accounts)):
            if(int(self.customer_accounts[i].get_account_number()) == account_id):
                self.customer_accounts[i].deposit(amount)
                return True
        return False

    def withdraw(self, account_id, amount):
        """
            Widthdraw money from a customer account
            @param account_id: account id
            @param amount: amount to widthdraw
            @returns: True if successful else False
        """
        for i in range(len(self.customer_accounts)):
            if(int(self.customer_accounts[i].get_account_number()) == account_id):
                return self.customer_accounts[i].withdraw(amount)
        return False



if __name__ == '__main__':
    print("Customer is called from cmd")
    c1 = Customer(0, "steve", "123123")
    c1.add_account_with_id(1002)
    print(c1.get_account(1002).get_account_info())
