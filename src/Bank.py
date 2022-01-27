import Customer as cu

class Bank:
    def __init__(self):
        self.customer_list = []

    def _load(self):
        """
            Loads Customer and Accounts from a mockdata.txt file
        """
        fw = open("mockdata.txt", "rt")
        new_line = fw.readline()
        temp_list = []
        while(new_line):
            new_line = new_line.replace("\n","")
            new_line = new_line.replace("#",":")
            temp_list = new_line.split(":")
            self.customer_list.append(cu.Customer(int(temp_list[0]), temp_list[1], temp_list[2]))
            temp_list = temp_list[3:]
            index = 0
            while(index < len(temp_list)):
                self.customer_list[len(self.customer_list)-1].add_account_with_id(int(temp_list[index]))
                #print(temp_list[index +1])
                self.customer_list[len(self.customer_list)-1].deposit(int(temp_list[index]), float(temp_list[index +2]))
                index += 3
            new_line = fw.readline()

    def get_customers(self):
        """
            returns a list of all customers name and pnr
            @returns: a list with fromat [{name, pnr}, {name, pnr}]
        """
        temp_list = []
        for customer in self.customer_list:
            temp_list.append({"name": customer.get_name(),"pnr":customer.get_pnr()})
        return temp_list

    def add_customer(self, name, pnr):
        """
            Adds a new customer to the bank
            @param name: the name of the customer
            @param pnr: the personnummer of the customer
            @returns: True if successful else False
        """
        for i in range(len(self.customer_list)):
            if(self.customer_list[i].get_pnr() == pnr):
                return False
        self.customer_list.append(cu.Customer(self.generate_customer_id(), name, pnr))
        return True
        
    def generate_customer_id(self):
        """
            Generates a new unique customer id
            @returns: new customer id
        """
        new_id = 111111
        id_found = False
        while(not id_found):
            id_found = True
            for customer in self.customer_list:
                if(customer.get_id() == new_id):
                    id_found = False
                    new_id += 1
                    break
        return new_id

    def get_customer(self, pnr):
        """
            returns information about a customer such as id, name, pnr, and account information
            @param pnr: personnummer to search for
            @returns: list of format [id, name, account info]
        """
        c_list = []
        for customer in self.customer_list:
            if(customer.get_pnr() == pnr):
                c_list.append(customer.get_id())
                c_list.append(customer.get_name())
                c_list.append(customer.get_all_accounts_info())
        return c_list

    def change_customer_name(self, name, pnr):
        """
            Change the name of a customer
            @param name: new name
            @param pnr: identifier personnummer
            @returns: True if successful else False
        """
        for i in range(len(self.customer_list)):
            if(self.customer_list[i].get_pnr() == pnr):
                self.customer_list[i].set_name(name)
                return True
        return False

    def remove_customer(self, pnr):
        """
            Removes a customer from the bank and withdraws all the money in all of the customers accounts.
            @param pnr: identifier personnummer
            @returns: empty dict if no customer found else removed account info
        """
        for i in range(len(self.customer_list)):
            if(self.customer_list[i].get_pnr() == pnr):
                temp_info = self.customer_list[i].close_all_accounts()
                del self.customer_list[i]
                return temp_info
        return {}

    def add_account(self, pnr):
        """
            Adds a new account
            @param pnr: identifier personnummer
            @returns: account id if successful and -1 if not
        """
        new_id = self.generate_new_account_id()
        for i in range(len(self.customer_list)):
            if(self.customer_list[i].get_pnr() == pnr):
                self.customer_list[i].add_account_with_id(new_id)
                return new_id
        return -1

    def generate_new_account_id(self):
        """
            Generates new account id
            @returns: new account id
        """
        new_id = 1000
        found_id = False
        while(found_id == False):
            new_id += 1
            found_id = True
            for c in self.customer_list:
                for a in c.get_all_account_id():
                    if(int(a) == new_id):
                        found_id = False
        return new_id

    def get_account(self, pnr, account_id):
        """
            Returns info about a account
            @param pnr: identifier personnummer
            @param account_id: account id
            @returns: info about account if exists else returns false
        """
        for i in range(len(self.customer_list)):
            if(self.customer_list[i].get_pnr() == pnr):
                return self.customer_list[i].get_account_info(account_id)
        return False

    def deposit(self, pnr, account_id, amount):
        """
            Add money to an account
            @param pnr: identifier personnummer
            @param account_id: account id
            @param amount: amount
            @returns: True if successful False if not
        """
        for i in range(len(self.customer_list)):
            if(self.customer_list[i].get_pnr() == pnr):
                return self.customer_list[i].deposit(account_id, amount)
        return False

    def withdraw(self, pnr, account_id, amount):
        """
            Widthdraw money from account
            @param pnr: identifier personnummer
            @param account_id: account id
            @param amount: amount
            @returns: True if successful False if not
        """
        for i in range(len(self.customer_list)):
            if(self.customer_list[i].get_pnr() == pnr):
                return self.customer_list[i].withdraw(account_id, amount)
        return False

    def close_account(self, pnr, account_id):
        """
            Remove an account from a customer
            @param pnr:
            @param account_id: account id
            @returns: info about closed account if successful else returns False
        """
        for i in range(len(self.customer_list)):
            if(self.customer_list[i].get_pnr() == pnr):
                temp_dict = self.customer_list[i].close_account(account_id)
                return f'Account with account number: {temp_dict["account_nr"]} of type: {temp_dict["account_type"]} has been closed! \n${temp_dict["amount"]} widthdrawn.'
        return False



if __name__ == '__main__':
    print("Bank is run from cmd")
    b = Bank()
    b._load()
    b.add_customer("steve2", "123456")
    print(b.add_account("123456"))
    print(b.deposit( "123456", 1001, 200))
    print(b.deposit( "123456", 1001, 2330))
    print(b.get_account("123456", 1001))
    print(b.withdraw( "123456", 1001, 150))
    print(b.get_account("123456", 1001))
    print(b.withdraw( "123456", 1001, 3000))
    print(b.get_account("123456", 1001))
    print(b.withdraw( "123456", 1009, 3000))
    print(b.get_account("123456", 1001))
    print(b.close_account( "123456", 1001))
    print(b.get_account("123456", 1001))