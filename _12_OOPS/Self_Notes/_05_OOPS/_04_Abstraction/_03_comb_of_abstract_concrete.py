'''
Let’s try a larger application like fund transfer before moving on to our application. So, in fund transfer there are
three types NEFT/IMPS/PTGS.

We can create an abstract class FundTransfer and extend it in the child classes. Create an abstract method transfer and
implement in all the child classes.

Create an abstract class FundTransfer with following attributes,
accountNumber:
int, balance : float and following methods,
validate(amount) : to check if the accountNumber is 10 digits,transfer the amount in non-negative and less than balance,
and return true, if not false
transfer (amount) : abstract method with no definition

Create a class NEFTTransfer which extends FundTransfer and implements transfer method,
transfer(amount) : Check if transfer amount + 5% of transfer amount is less than balance, then subtract transfer amount
and 5% service charge from balance and return true, if not return false

Create a class IMPSTransfer which extends FundTransfer and implements transfer method,
transfer(amount) : Check if the transfer amount + 2% of transfer amount is less than balance, then subtract transfer
amount and 2% service charge from balance and return true, if not return false

Create a class RTGSTransfer which extends FundTransfer and implements Trandfer method,
transfer(amount) : Check if transfer amount is greater than Rs.10000, then subtract the transfer amount from balance and
return true, if not return false

Add appropriate getters/setters, constructors with super() to create objects

Note: Print “Account number or transfer amount seems to be wrong”
if validate function returns false.
Print “Transfer could not be made” if transfer function returns
false.
Sample Input/Output:
Enter your account number: 1234567890
Enter the balance of the amount: 10000
Enter the type of transfer to be made:
1. NEFT
2. IMPS
3. RTGS
1
Enter the amount to be transferred : 2000
Transfer occurred successfully remaining balance is 7900.0
'''

from abc import ABC, abstractmethod

global ref


class FundTransfer(ABC):
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    @property
    def account_number(self):
        return self.__account_number

    @account_number.setter
    def account_number(self, account_number):
        if len(str(account_number)) == 10:
            self.__account_number = account_number

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, balance):
        if balance > 0:
            self.__balance = balance

    def validate(self, amount):
        return len(str(self.account_number)) == 10 \
               and self.balance > amount > 0

    @abstractmethod
    def transfer(self, amount):
        pass


class NEFTTransfer(FundTransfer):

    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)

    def transfer(self, amount):
        sc = amount * 0.05
        if (amount + sc) < self.balance:
            self.balance = self.balance - (amount + sc)
            return True
        return False


class IMPSTransfer(FundTransfer):

    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)

    def transfer(self, amount):
        sc = amount * 0.02
        if (amount + sc) < self.balance:
            self.balance = self.balance - (amount + sc)
            return True
        return False


class RTGSTransfer(FundTransfer):

    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)

    def transfer(self, amount):
        if self.balance > amount >= 10000:
            self.balance = self.balance - amount
            return True
        return False


def main():
    global ref
    an = int(input('Enter your account number: '))
    bal = int(input('Enter your account balance: '))

    print('Enter your choice')
    print('1. NEFT\n2. IMPS\n3. RTGS\n')
    choice = int(input())

    if choice == 1:
        ref = NEFTTransfer(an, bal)
    elif choice == 2:
        ref = IMPSTransfer(an, bal)
    elif choice == 3:
        ref = RTGSTransfer(an, bal)
    else:
        print('INVALID CHOICE')

    amt = int(input('Enter the amount to be transfered: '))

    if ref.validate(amt):
        if ref.transfer(amt):
            print('Transfer was successful')
            print(f'Remaining balance is {ref.balance}')
        else:
            print('Transfer could not be made')
    else:
        print('Account number or transfer amount seems to be wrong')


if __name__ == '__main__':
    main()
