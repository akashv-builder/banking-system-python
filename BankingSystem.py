#defining a bank class
class Bank(object):
    #class variable
    IfSC_code=999999

    #constructor of Bank class
    def __init__(self,bankname,branchname,loc):
        self.ifsc=Bank.IfSC_code+1
        self.bankname=bankname
        self.branchname=branchname
        self.loc=loc

    #making method in bank class
    def bank_info(self):

        print(" IFSC code: {0}\n Bank name:{1}\n Branch Name:{2}\n loc:{3}".format(self.ifsc,self.bankname,self.branchname,self.loc))

#defining a customer class
class Customer():
    #class variable
    CustomerID=10001

    #constructor of customer class
    def __init__(self,custname,address,number,email):
        self.customer_ID=Customer.CustomerID+1
        self.custname=custname
        self.address=address
        self.Phone_number=number
        self.email=email

    #defining method in customer class
    def customer_details(self):

        print("\n Customer name: {1}\n customer id:{0}\n address:{2}\n Phone Number:{3}\n email:{4}".format(self.customer_ID,self.custname,self.address,self.Phone_number,self.email))



#making account class
class Account(Bank,Customer):
    #class variable
    Accound_id=10001

    #constructor of account class
    def __init__(self,loc,bankname,branchname,cust,balance):
        super(Account,self).__init__(bankname,branchname,loc)
        self.account_id=Account.Accound_id+1
        self.Cust=cust
        self.balance=balance

    #defining account info method
    def account_info(self):
        print("\n Account information for {}".format(self.Cust.custname))
        print(" Account id:{0}\n Balance in account:{1}".format(self.account_id,self.balance))


    #defining deposite method
    def deposit(self,PanCard,amount):

        #using conditional statements
        if PanCard==1:
            self.balance=int(self.balance)+int(amount)

        else:
            print " Please Provide Pancard and Aadhar Card"
        print " Account balance is:"+str(self.balance)
        return self.balance


    #defining withdraw method
    def widthraw(self,amount_debit,sbin):
        original=int(self.balance)-amount_debit
        #conditional statements to check the  for debit process
        if original > sbin:
            print " Your Account Debited with {}".format(amount_debit)
            self.balance=original
            return self.balance
        else:
            print (" You dont have not enough cash.")

    #method that returns balance
    def get_balance(self,z):

        return z

#defining saving class
class Saving(Account):
    #constructor of saving class
    def __init__(self,bankname,branchname,loc,cust, balance):
        super(Saving,self).__init__(loc,bankname,branchname,cust, balance)

    #function to get saving account information
    def getSavingAccountInfo(self):
        super(Saving,self).account_info()


    def getSminBalance(self,smin):
        return smin

    #function to open an account of a specific type
    def selection(self):
        n=int(raw_input("\n Enter type of account you want to create (Savings=1/Current=2): "))
        if (n == 1 or n == 2):
            if n == 1:
                return 3000
            else:
                return 5000

        else:
            print("Please Enter correct option")


#defining main function
def main():
    print("\n\t\t\t*****WELCOME TO THE BANK*****")


    print " "
    #Bank class info
    print("Enter your details\n")
    bankname=raw_input(" Please enter the name of the bank: ")
    branchname=raw_input(" Please enter the branch name: ")
    loc=raw_input(" Please enter the LOC: ")

    # b.bank_info()
    b=Bank(bankname,branchname,loc)

    # Customer class info
    print("\n*****Enter the customer Details*****\n")

    #taking the customer name
    Customername=raw_input("Enter the name of the customer:")

    #taking the customer address
    address=raw_input("Enter the address:")

    #taking phone number of user
    phonenumber=int(raw_input("Enter the phone number:"))

    #taking email id of user
    email=raw_input("Enter the email-id:")

    # Making Customer class object
    c=Customer(Customername,address,phonenumber,email)



    print("\n*****Please enter the amount you want to deposit*****")

    #taking balance as input from user
    balance = int(raw_input("\n Enter the amount: "))

    # Making Account class object
    a=Account(loc,bankname,branchname,c,balance)
    print("\n*****Account Information*****\n")

    #calling the different functions through the objects created
    b.bank_info()
    c.customer_details()
    a.account_info()
    s = Saving(bankname, branchname, loc, c, balance)
    y=s.selection()

    #taking the operation type input
    n=int(raw_input(" Enter the operation you want to perform (Deposit=1/Withdrawl=2): "))
    z=0
    if (n ==1 or n==2):
        if n==1:
            #taking the amount from user
            amount = int(raw_input("\n Enter the amount: "))
            pan = int(raw_input(" Do you have pan card True=1/False=2:"))
            z=a.deposit(pan,amount)

        else:
            #taking the amount to withdraw
            withdraw = int(raw_input("\n Enter the amount to withdraw: "))
            z=a.widthraw(withdraw,y)

    else:
        print("Please enter correct option")

    s.getSavingAccountInfo()
    print " New balance:"+str(z)
    print " Minimum balance required for this type of account is: "+str(s.getSminBalance(y))

    print("\nCongratulations your Account has been created ")

#calling the main function
main()