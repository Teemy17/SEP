import ZODB, ZODB.config
path = "./config.xml"
db = ZODB.config.databaseFromURL(path)
connection = db.open()
root = connection.root

import ZODB, ZODB.config
import persistent
from abc import ABC, abstractmethod
import datetime

class Customer(persistent.Persistent):
    def __init__(self, name=""):
        self.name = name
        self.accounts = persistent.list.PersistentList()

    def __str__(self):
        return "Customer Name: " + self.name
    
    def addAccount(self, a):
        self.accounts.append(a)
        return a
    
    def getAccount(self, n):
        if 0 <= n < len(self.accounts):
            return self.accounts[n]
        return None

    def printStatus(self):
        print(self.__str__())
        for a in self.accounts:
            print("", end="    ")
            a.printStatus()

class Account(ABC):
    def __init__(self, balance = 0.0, owner = None):
        self.balance = balance
        self.owner = owner
        self.bankTransaction = []

    @abstractmethod
    def __str__(self):
        raise NotImplementedError('users must define __str__ to use this base class')

    def deposit(self, m):
        if m > 0:
            self.bankTransaction.append(BankTransaction(m, self.balance, self.balance + m, "Deposit"))
            self.balance += m

    @abstractmethod
    def withdraw(self, m):
        if m > 0 and self.balance >= m:
            self.bankTransaction.append(BankTransaction(m, self.balance, self.balance - m, "Withdraw"))
            self.balance -= m

    def transfer(self, m, o):
        if m > 0:
            self.bankTransaction.append(BankTransaction(m, self.balance, self.balance - m, f"Transfer to {o.owner}" ))
            self.balance -= m
            o.transferIn(m, self.owner) 

    def transferIn(self, m,o):
        if m > 0:
            self.bankTransaction.append(BankTransaction(m, self.balance, self.balance + m, f"Transfer from {o}" ))
            self.balance += m

    def accountDetail(self):
        return self.balance, self.owner

    def getBalance(self):
        return self.balance
    
    def printStatus(self):
        print("  ", self.__str__(), "Balance: ", self.balance)
    
    def printTransaction(self):
        for t in self.bankTransaction:
            t.printDetail()

class SavingAccount(Account, persistent.Persistent):
    def __init__(self, balance = 0.0, owner = None, interest = 1.00):
        Account.__init__(self, balance, owner)
        self.interest = interest

    def __str__(self):
        return "Saving Account"

    def printStatus(self):
        print("  ", self.__str__(), "Balance: ", self.balance, "Interest: ", self.interest)


class CurrentAccount(Account, persistent.Persistent):
    def __init__(self, balance = 0.0, owner = None, limit = -5000.0):
        Account.__init__(self, balance, owner)
        self.limit = limit

    def __str__(self):
        return "Current Account"

    def printStatus(self):
        print("  ", self.__str__(), "Balance: ", self.balance, "Limit: ", self.limit)

    def withdraw(self, m):
        if m > 0 and self.balance - m > self.limit:
            self.balance -= m

class BankTransaction(persistent.Persistent):
    def __init__(self,  amount = 0.0, old_balance = 0.0, new_balance = 0.0,ttype = ""):
        self.amount = amount
        self.old_balance = old_balance
        self.new_balance = new_balance
        self.timestamp = datetime.datetime.now()
        self.ttype = ttype

    def __str__(self):
        return "Transaction Type: " + self.ttype + "\n Amount: " + str(self.amount) + " \nOld Balance: " + str(self.old_balance) + " \nNew Balance: " + str(self.new_balance) + " \nTime Stamp: " + str(self.timestamp)

    def printDetail(self):
        print(self.__str__())
    