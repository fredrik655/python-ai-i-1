import Bank as bk



def main():
    #init bank class
    bank = bk.Bank()
    # load and create customers and accounts from mockdata.txt
    bank._load()

    #print all the customers that was loaded
    customer_list = bank.get_customers()
    #print_all_customer(customer_list)

    #add a new customer with unique pnr
    print(f"customer added: {bank.add_customer('Rafael', '19911112')}")

    # print all the customer again
    customer_list = bank.get_customers()
    #print_all_customer(customer_list)

    # change the name of a customer
    bank.change_customer_name("dude",'19911112' )

    # print all the customer again
    customer_list = bank.get_customers()
    #print_all_customer(customer_list)

    # remove a customer
    """remove_statment = bank.remove_customer("19911111")
    print(f'removed accounts: {remove_statment["removed_accounts"]}')
    print(f'returned amount: {remove_statment["amount"]}')"""

    # print all the customer again
    customer_list = bank.get_customers()
    #print_all_customer(customer_list)

    # remove account by account id
    print(bank.close_account("19911213", 1007))

    print("here")
    print(bank.get_customer("19860107"))
    # add new account 
    bank.add_account("19860107")
    bank.add_account("19860107")
    bank.add_account("19860107")
    bank.add_account("19860107")

    # get info about a customer
    print(bank.get_customer("19860107"))

    # deposit money to a customers account
    print(bank.deposit("19860107", 1003, 123))
    print(bank.get_customer("19860107"))

    # widthdraw money from a customers account
    print(bank.withdraw("19860107", 1003, 100))
    print(bank.get_customer("19860107"))


def print_all_customer(customer_list):
    """
        prints all customers names and pnr
        @param customer_list: a list of objects customer
    """
    for customer in customer_list:
        print("new customer ==============")
        print("name:" + customer["name"])
        print("pnr:" + customer["pnr"])




if __name__ == "__main__":
    main()