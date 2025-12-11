class Bank():
    account_type = "Van Nam"
    locations = "Le"
    def __init__(self, name, number, balance):
        self.name = name
        self.number = number
        self.balance = balance
        self.account = Bank.account_type
        self.locations = Bank.locations
    
    def __repr__(self):
        print (" welcome to the sbi atm")
        print ("-----------------------")
        account_pin = int(input("please enter your number  "))

        if account_pin == 123:
            Account(self)
        else:
            print ("pin incorrect ")
            Error(self)
        return ' '.join([self.name,self.number])
    
def Error(self):
        account_pin = int (input(" please enter your pin number  "))
        if account_pin == 123:
            Account(self)
        else:
            print ("pin incorrect ")
            Error(self)
        return ' '.join([self.name,self.number])
    
def Account(self):
        print ("your card number is : XXXX XXXX 1337 ")
        print ("would you like to deposit  ")
        print ("""
               1) Balance
               2) Rut
               3) Gui
               4) Quit
               """)
        option = int(input("please enter choise : "))
        if option == 1:
            Balance(self)
        elif option == 2:
             Rut(self)
        elif option == 3:
             Gui(self)
        elif option == 4:
             exit()
def Balance(self):
        print ("Balance: ", self.balance)
        Account(self)
def Rut(self):
        w = int(input("please enter desired amount : "))
        if self.balance > 0 and self.balance >= w :
            self.balance = self.balance - w
            print ("your transaction is successfull ")
            print ("your balance : ", self.balance)
            print("")
        else:
            print ("your transaction is canlled due to ")
            print ("amount is not sufficient in your account ")
        Account(self)
def Gui(self):
        d = int(input("please enter desired amount : "))
        self.balance = self.balance + d
        print (" your transaction is successfull ")
        print ("Balane: ", self.balance)
        Account(self)
def Exit(self):
        print ("Exit")
t1 = Bank("Van Nam ", 1453210145, 1)

print (t1)
        
