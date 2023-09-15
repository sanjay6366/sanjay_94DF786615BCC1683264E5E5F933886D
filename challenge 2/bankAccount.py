'''implement a class bankAccount that representes a bank account. The class should have private variables.account number,account name,account balance.
Includes methods of:
deposit money,withdraw money,display account balance
cannot be accessed from outside the class.Write a program to create an instance for the class bankAccount and test deposit and withdraw functions.'''

class bankAccount:
  def __init__(self,account_number,account_name,initial_balance=0.0):
     self.__account_id=account_number
     self.__account_name=account_name
     self.__account_balance=initial_balance
    
 

  def deposit(self,amount):
    if amount>0:
      
      self.__account_balance+=amount
      print("deposited amount₹{}.accountBalance:₹{}".format(amount,self.__account_balance))
    else:
      print("entered a wrong number or insufficient balance")
  def withdraw(self,amount):
    if amount<self.__account_balance and amount>0:
      self.__account_balance-=amount
      print("withdrawn amount ₹{}.current account balance:₹{}".format(amount,self.__account_balance))
    else:
      print("insufficient balance or you have entered a invalid number")
   
  def display(self):
    
    print("accountNumber:{} holderName:{} accountBalance:₹{}".format(self.__account_id,self.__account_name,self.__account_balance)) 


#create a instance for the class bankAccount
account=bankAccount(account_number= "9789110100",account_name= "sanjay sivaraj",initial_balance= 3000.0)

account.display()
account.deposit(2000.00)
account.withdraw(500.00)
account.display()

    




