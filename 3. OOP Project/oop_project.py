from bank_accounts import *

Dave = BankAccount(1000, "Dave")
Sara = BankAccount(2000, "Sara")

print('\n')

Dave.getBalance()
Sara.getBalance()

Dave.deposit(100)
Sara.deposit(150)

Dave.withdraw(10000)
Sara.withdraw(100)

Dave.transfer(10, Sara)
Sara.transfer(20000, Dave)

################################################################
# Creating new instances to check InterestRewardsAcct class
Jim = InterestRewardsAcct(initialAmount=1000, acctName='Jim')
# Depositing $100 into Jim's InterestRewardsAcct account
Jim.deposit(100)
# Jim transfers amount to Dave
Jim.transfer(100, Dave)

################################################################
# Creating new instances to check SavingsAcct class
Blaze = SavingsAcct(1000, "Blaze")
Blaze.getBalance()
Blaze.deposit(100)
Blaze.transfer(1000, Sara)
