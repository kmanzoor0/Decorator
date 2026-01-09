# class Student:
#      def __init__(self,name,marks):
#          self.name = name
#          self.marks = marks
# a = Student('kashif',54)
# print(a.name)
# print(a.marks)
#
# class BankAccount:
#     def __init__(self,balance):
#         self.balance = balance
#     def  deposit(self,amount):
#         if amount > 0:
#             self.balance += amount
#             print(self.balance)
#     def withdraw(self,amount):
#         if amount < self.balance:
#             self.balance -= amount
#             print(self.balance)
#         else:
#             print('Balance is not enogh')
#     def show_balance(self):
#         print(self.balance)
#
# a = BankAccount(50)
# a.deposit(20)
# a.withdraw(30)
# a.show_balance()
def decorator(func):
    def inner():
        print('Decorator is running')
        func()
        print('Decorator is finished')

    return inner
@decorator
def greet():
    print('Hello Python')

greet()