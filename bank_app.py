import random
class Bank:
		customer={}
		def __init__(self):
			print()
			print("enter your choice:")
			print("1. create account")
			print("2. operate account")
			print("3. exit")
			print()
			self.i = int(input("Your choice:"))
			print()
		
		def create_account(self):
			self.name = input("enter your name:")
			print()
			self.balance = int(input("enter your balance:"))
			print()
			self.id = random.randint(10001,99999)
			Bank.customer[self.id] = [self.name,self.balance]
			print("your account is created")
			print("your account number is :",self.id)
			print()

		def operate_account(self):
			self.oname = input("enter your name:")
			self.no = int(input("enter your account number:"))
			print()
			if self.no not in Bank.customer:
				print("this account  is not present")
			else:
				print("1. view balance")
				print("2. withdraw")
				print("3. deposit")
				print("4. close account")
				print("5. previous menu")
				print()
				self.x = int(input("enter your choice:"))
				print()
				if self.x == 1:
					Bank.view_balance(self)
				if self.x == 2:
					Bank.withdraw(self)
				if self.x == 3:
					Bank.deposit(self)
				if self.x == 4:
					Bank.close_account(self)
				if self.x == 5:
					Bank.previous_menu(self)

		def view_balance(self):
			print("balance is:",Bank.customer.get(self.no)[1])

		def withdraw(self):
			self.w = int(input("enter amount to withdraw:"))
			print()
			if self.w >= Bank.customer[self.no][1]:
				print("entered amount is not correct")
			else:
				Bank.customer[self.no][1]=Bank.customer[self.no][1]-self.w
				print(self.w,"is withdrawn")

		def deposit(self):
			self.d = int(input("enter amount to be deposit:"))
			print()
			Bank.customer[self.no][1]=Bank.customer[self.no][1]+self.d
			print("your amount is deposited")

		def close_account(self):
			del Bank.customer[self.no]
			print("your account is closed")

		def previous_menu(self):
			Bank.__init__(self)


while True:
	b=Bank()
	if b.i == 1:
		b.create_account()
	elif b.i == 2:
		b.operate_account()
	elif b.i ==3:
		break
	else:
		print("wrong choice! Try again")	