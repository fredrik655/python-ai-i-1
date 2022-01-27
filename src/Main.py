import Bank as bk



def main():
    #init bank class
    bank = bk.Bank()
    # load and create customers and accounts from mockdata.txt
    bank._load()

    exit_loop = False

    while(exit_loop == False):
        print("===== enter a number ====")
        print("===== Bank options ====")
        print("===== 1: Display of all the customers in the bank ====")
        print("===== 2: Add a new customer ====")
        print("===== 3: Change a customers name ====")
        print("===== 4: Remove a customer from the bank ====")
        print("===== 5: Add a new Account ====")
        print("===== 6: Remove a specific account from a customer ====")
        print("===== Customer options ====")
        print("===== 7: Check information about a customer ====")
        print("===== 8: Deposit money to an account ====")
        print("===== 9: widthdraw some money ====")
        print("===== 10: Exit ====")
        user_input = 0
        try:
            user_input = int(input())
        except:
            print("input error exiting!!")
            exit_loop = True
        if(user_input == 1):
            #print all the customers that was loaded
            customer_list = bank.get_customers()
            print_all_customer(customer_list)
        elif(user_input == 2):
            #add a new customer with unique pnr
            print("Enter a name and pnr for new customer ex. steve 19911113")
            temp_name = ""
            temp_pnr = ""
            try:
                print("enter name")
                temp_name = input()
                print("enter pnr")
                temp_pnr = input()
            except:
                print("input error")
            if(bank.add_customer(temp_name, temp_pnr) == True):
                print("customer added")
            else:
                print("Error no customer added")
        elif(user_input == 3):
            # change the name of a customer
            print("Enter a new name for a customer")
            temp_name = ""
            temp_pnr = ""
            try:
                print("new name")
                temp_name = input()
                print("enter pnr")
                temp_pnr = input()
            except:
                print("input error")
            if(bank.change_customer_name(temp_name, temp_pnr) == True):
                print("customer added")
            else:
                print("Error name not changed")
        elif(user_input == 4):
            # remove a customer and print account info
            print("Enter a customer pnr to remove")
            temp_pnr = ""
            try:
                temp_pnr = input()
            except:
                print("input error")
            temp_return_data = bank.remove_customer(temp_pnr)
            if(temp_return_data != {}):
                print(f'${temp_return_data["amount"]} returned from accounts: {temp_return_data["removed_accounts"]}')
            else:
                print("Error removing customer")
        elif(user_input == 5):
            # add new account
            print("Enter a customer pnr to add new account")
            temp_pnr = ""
            try:
                temp_pnr = input()
            except:
                print("input error")
            temp_val = bank.add_account(temp_pnr)
            if( temp_val != -1):
                print(f"account added with id {temp_val}")
            else:
                print("Error adding account")
        elif(user_input == 6):
            #remove account from customer
            print("Enter a pnr and account id to remove")
            temp_id = 0
            temp_pnr = ""
            try:
                print("enter account id")
                temp_id = int(input())
                print("enter pnr")
                temp_pnr = input()
            except:
                print("input error")
            temp_return_data = bank.close_account(temp_pnr, temp_id)
            if(temp_return_data != False):
                print(temp_return_data)
            else:
                print("Error removing customer")
        elif(user_input == 7):
            # print info about a customer
            print("Enter a customer pnr to check info")
            temp_pnr = ""
            try:
                temp_pnr = input()
            except:
                print("input error")
            temp_return_data = bank.get_customer(temp_pnr)
            if(len(temp_return_data) != 0):
                print(f'customer id: {temp_return_data[0]}')
                print(f'customer name: {temp_return_data[1]}')
                print("customer accounts: ")
                for account in temp_return_data[2]:
                    print(f'account nr: {account["account_nr"]}, account type: {account["account_type"]}, account amount: {account["amount"]}')
            else:
                print("Error fetching customer info")
        elif(user_input == 8):
            #deposit money to and account
            print("Enter a pnr and account id amount to deposit")
            temp_id = 0
            temp_pnr = ""
            temp_amount = 0
            try:
                print("enter account id")
                temp_id = int(input())
                print("enter pnr")
                temp_pnr = input()
                print("enter amount")
                temp_amount = int(input())
            except:
                print("input error")
            temp_return_data = bank.deposit(temp_pnr, temp_id, temp_amount)
            if(temp_return_data != False):
                print("money deposited")
            else:
                print("Error depositing ")
        elif(user_input == 9):
            #widthdraw money from and account
            print("Enter a pnr and account id amount to widthdraw")
            temp_id = 0
            temp_pnr = ""
            temp_amount = 0
            try:
                print("enter account id")
                temp_id = int(input())
                print("enter pnr")
                temp_pnr = input()
                print("enter amount")
                temp_amount = int(input())
            except:
                print("input error")
            temp_return_data = bank.withdraw(temp_pnr, temp_id, temp_amount)
            if(temp_return_data != False):
                print("money widthdrawn")
            else:
                print("Error widthdrawning ")
        elif(user_input == 10):
            exit_loop = True
        else:
            print("input unknown exiting!!")
            exit_loop = True

def print_all_customer(customer_list):
    """
        prints all customers names and pnr
        @param customer_list: a list of objects customer
    """
    for customer in customer_list:
        print("=========================")
        print("name:" + customer["name"])
        print("pnr:" + customer["pnr"])


if __name__ == "__main__":
    main()