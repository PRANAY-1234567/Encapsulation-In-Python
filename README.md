📘 Python Program: Encapsulation Example (Bank Class)


📌 Overview

This Python program demonstrates Encapsulation, a key concept of Object-Oriented Programming (OOP).

Encapsulation means hiding internal data and allowing access only through specific methods.
In this example, the bank balance is kept private and accessed using a method.

⚙️ Source Code
class Bank:
    def __init__(self):
        self.__balance = 1000

    def show_balance(self):
        print("Balance is", self.__balance)

b = Bank()
b.show_balance()
🧠 How It Works
1️⃣ Create a Class
class Bank:
Defines a class named Bank.
Represents a simple bank system.
2️⃣ Constructor Method
def __init__(self):
Automatically runs when an object is created.
Initializes the class variables.
3️⃣ Private Variable
self.__balance = 1000
__balance is a private variable.
Double underscore (__) makes it inaccessible directly from outside the class.
This is called data hiding (encapsulation).
4️⃣ Public Method
def show_balance(self):
A method used to access the private data.
It prints the balance.
5️⃣ Create Object
b = Bank()
Creates an object b of the Bank class.
6️⃣ Access Data via Method
b.show_balance()
Calls the method to safely access the private balance.
▶️ Output
Balance is 1000
🔑 Key Concepts Demonstrated
Classes and Objects
Encapsulation
Private Variables (__balance)
Data Hiding
Public Methods
🔒 Why Use Encapsulation?

Encapsulation helps to:

Protect sensitive data
Prevent direct modification
Improve code security
Maintain better control over data
⚠️ Important Note

Trying to access the private variable directly will cause an error:

print(b.__balance)   # ❌ Not allowed
🚀 Improved Version (With Deposit Method)
class Bank:
    def __init__(self):
        self.__balance = 1000

    def deposit(self, amount):
        self.__balance += amount

    def show_balance(self):
        print("Balance is", self.__balance)

b = Bank()
b.deposit(500)
b.show_balance()

Output:

Balance is 1500
📚 Learning Outcome

After understanding this program, you will learn:

What encapsulation is
How to use private variables
How to control access to data using methods
Why data hiding is important in real-world applications

<img width="598" height="697" alt="image" src="https://github.com/user-attachments/assets/8d1a4df4-381f-4ac1-82cd-b2842d16d07f" />
