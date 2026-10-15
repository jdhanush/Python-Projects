class BalanceException(Exception):
    pass



class BankAccount:
    
    def __init__(self, initialAmount, acctName):
        self.balance = initialAmount
        self.name = acctName
        print(f"\n{self.name}'s Account created \
              \nOpening balance = ${self.balance:.2f}")

        
    def getBalance(self):
        print(f"{self.name} Account's Current balance = ${self.balance:.2f}")

        
    def deposit(self, amount):
        self.balance += amount
        print(f"\n${amount} Deposited into {self.name}'s Account")
        self.getBalance()

        
    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"\nSorry {self.name}. Your account has only ${self.balance:.2f}")

            
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance -= amount
            print('\nWithdraw Complete')
            self.getBalance()
        
        except BalanceException as error:
            print(f"\nWitdraw Interrupted: {error}")
            
                        
    def transfer(self, amount, account):
        try:
            print("\n\n*****************\nBeginning Transfer ... 🚀" )
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print('\nTransfer Complete! ✅ \n*****************')
        
        except BalanceException as error:
            print(f"\nTransfer Interrupted ❌ {error}\n*****************")
            
        
            
        
# InterestRewardsAcct is the inherited class of BankAccount class.
# There will be no new properties for the child function, 
# hence we need need not create a new initializer i.e., __init__()          
class InterestRewardsAcct(BankAccount):
    def deposit(self, amount):
        self.balance += 1.05*amount
        print(f'Deposition with 5% Interest Rate on ${amount} amount is complete')
        self.getBalance()
    
    
    
class SavingsAcct(InterestRewardsAcct):
    
    def __init__(self, initialAmount, acctName):
        super().__init__(initialAmount, acctName)
        self.fee = 5
        
    def withdraw(self, amount):
         try:
             self.viableTransaction(amount + self.fee)
             self.balance -= (amount + self.fee)
             print('\nWithdraw Complete')
             self.getBalance()
         except BalanceException as error:
             print(f'\nWithdraw Interrupted: {error}')
