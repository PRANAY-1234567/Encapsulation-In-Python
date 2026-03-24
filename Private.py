class Bank:
    def __init__(self):
        self.__balance = 1000

    def show_balance(self):
        print("Balance is", self.__balance)

b = Bank()
b.show_balance()