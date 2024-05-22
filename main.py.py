import random

class Rbi:
    def __init__(self):
        self.rbi_total_accounts = 0
        self.rbi_total_money = 4000

class TN(Rbi):
    def __init__(self):
        super().__init__()
        self.tn_total_accounts = 0
        self.tn_total_money = 2000


class Sbi(TN):
    def __init__(self):
        super().__init__()  
        self.account = {}
        self.balance = {}
        self.sbi_total_accounts = 0
        self.sbi_total_money = 10000
        self.a = 0

    def TotalMoney(self):
        totalamount = sum(self.balance.values()) + self.sbi_total_money
        print(totalamount, "is added to the Sbi Vault")

    def TotalAccounts(self):
        total_accou = self.sbi_total_accounts
        print("Total", total_accou, "Accounts has been created")

    def RbiTotalMoney(self):
        totalamount1 = sum(self.balance.values()) + self.rbi_total_money
        print(totalamount1, "is added to the Rbi Vault")

    def RbiTotalAccounts(self):
        total_accou1 = self.rbi_total_accounts
        print("Total", total_accou1, "Accounts has been created")

    def TNTotalMoney(self):
        totalamount2 = sum(self.balance.values()) + self.tn_total_money
        print(totalamount2, "is added to the TN Vault")

    def TNTotalAccounts(self):
        total_accou2 = self.tn_total_accounts
        print("Total", total_accou2, "Accounts has been created")

    def otp(self):
        num = random.randint(0, 2000)
        a = len(str(num))
        opt = int(a)
        print("Your OTP Is:", num)

        if a <= 3:
            print("You are Ready for a Transaction")
        else:
            print("You are not ready for Transaction")

    def accOpening(self):
        print("Welcome To State bank of India")
        x = str(input('Enter The Name: '))
        y = str(input('Enter the email id: '))
        self.a += 1
        z = [x, y]
        self.account[self.a] = z
        self.balance[self.a] = 0
        self.sbi_total_accounts += 1
        self.rbi_total_accounts += 1  
        self.tn_total_accounts += 1   
        print('Congrats', x, ', Your account number is ', self.a, '.')

    def close(self):
        x = int(input('Enter Account number To Close the Account: '))
        if x in self.account:
            self.account.pop(x)
            balance_to_remove = self.balance.pop(x)
            self.sbi_total_money -= balance_to_remove  
            self.sbi_total_accounts -= 1  
            self.rbi_total_accounts -= 1  
            self.tn_total_accounts -= 1   
            print("Action done, Your account ", x, ' has been closed')
        else:
            print("Account Number ", x, "  does not Exists")

    def deposit(self):
        x = int(input('Enter Account number: '))
        y = int(input('Enter Deposit amount: '))
        if x in self.balance:
            z = self.balance[x]
            newamount = z + y
            self.balance[x] = newamount
            self.sbi_total_money += y  
            self.rbi_total_money += y  
            self.tn_total_money += y   
            print('Your account is deposited with ', y, ' and Your current balance is ', newamount)
        else:
            print("Account number not found.")

    def withdraw(self):
        x = int(input('Enter Account number: '))
        y = int(input('Enter Withdrawal Amount: '))
        if x in self.balance:
            z = self.balance[x]
            if y <= z:
                newamount = z - y
                self.balance.update({x: newamount})
                self.sbi_total_money -= y
                self.rbi_total_money -= y  
                self.tn_total_money -= y   
            
                print(y, 'has been withdrawn and Your current balance is ', newamount)
            else:
                print("Sorry you have insufficient balance")
        else:
            print("Account number not found.")


b = Sbi()


sbi_account = open(r"C:\Users\lucif\OneDrive\Desktop\Ac_details.txt", 'r')
data = sbi_account.read()
sbi_account.close()
if len(data):
    b.account = eval(data)
    
balance = open(r"C:\Users\lucif\OneDrive\Desktop\Ac_Bal.txt", 'r')
bal = balance.read()
if len(bal):
    b.balance = eval(bal)
    
acc_no = open(r"C:\Users\lucif\OneDrive\Desktop\Ac_Num.txt", 'r')
num = acc_no.read()
if len(num):
    b.a = eval(num)
    
sbi_total_acc = open(r"C:\Users\lucif\OneDrive\Desktop\Sbi_accounts.txt", 'r')
data1 = sbi_total_acc.read()
if len(data1):
    b.sbi_total_accounts = eval(data1)
    
sbi_total_amount = open(r"C:\Users\lucif\OneDrive\Desktop\Sbi_Money.txt", 'r')
ba = sbi_total_amount.read()
if len(ba):
    b.sbi_total_money = eval(ba)
    
rbi_total_acc = open(r"C:\Users\lucif\OneDrive\Desktop\Rbi_Accounts.txt", 'r')
num1 = rbi_total_acc.read()
if len(num1):
    b.rbi_total_accounts = eval(num1)
    
rbi_total_amount = open(r"C:\Users\lucif\OneDrive\Desktop\Rbi_Money.txt", 'r')
data2 = rbi_total_amount.read()
rbi_total_amount.close()
if len(data2):
    b.rbi_total_money = eval(data2)
    
tn_acc = open(r"C:\Users\lucif\OneDrive\Desktop\TN_accounts.txt", 'r')
bal1 = tn_acc.read()
if len(bal1):
    b.tn_total_accounts = eval(bal1)
    
tn_money = open(r"C:\Users\lucif\OneDrive\Desktop\TN_Money.txt", 'r')
num2 = tn_money.read()
if len(num2):
    b.tn_total_money = eval(num2)
    
b.accOpening()
b.otp()
b.deposit()
b.accOpening()
b.otp()
b.deposit()
b.withdraw()
b.TotalMoney()
b.TotalAccounts()
b.RbiTotalMoney()
b.RbiTotalAccounts()
b.TNTotalMoney()
b.TNTotalAccounts()



file = open(r"C:\Users\lucif\OneDrive\Desktop\Ac_details.txt", 'w')
file.write(str(b.account))
file.close()

bal = open(r"C:\Users\lucif\OneDrive\Desktop\Ac_Bal.txt", 'w')
bal.write(str(b.balance))
bal.close()

acc_no = open(r"C:\Users\lucif\OneDrive\Desktop\Ac_Num.txt", 'w')
acc_no.write(str(b.a))
acc_no.close()

file1 = open(r"C:\Users\lucif\OneDrive\Desktop\Sbi_accounts.txt", 'w')
file1.write(str(b.sbi_total_accounts))
file1.close()

bal1 = open(r"C:\Users\lucif\OneDrive\Desktop\Sbi_Money.txt", 'w')
bal1.write(str(b.sbi_total_money))
bal1.close()

file2 = open(r"C:\Users\lucif\OneDrive\Desktop\Rbi_Accounts.txt", 'w')
file2.write(str(b.rbi_total_accounts))  
file2.close()

bal2 = open(r"C:\Users\lucif\OneDrive\Desktop\Rbi_Money.txt", 'w')
bal2.write(str(b.rbi_total_money))  
bal2.close()


file3 = open(r"C:\Users\lucif\OneDrive\Desktop\TN_accounts.txt", 'w')
file3.write(str(b.tn_total_accounts))  
file3.close()

bal3 = open(r"C:\Users\lucif\OneDrive\Desktop\TN_Money.txt", 'w')
bal3.write(str(b.tn_total_money))  
bal3.close()



