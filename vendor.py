from transaction import Transaction

class Vendor:

	def __init__(self):
		self.__users = []
		self.__transactions = []

	def receivePayment(self, user, value):
		if not self.__hasRegistered(user):
			self.__register(user)
		self.__startTransactionWith(user, value)

# TRANSACTION SPECIFIC METHODS

	def __startTransactionWith(self, user, value):
		transaction = Transaction(user, self, value)
		self.__transactions.append(transaction)

# USER SPECIFIC METHODS

	def __hasRegistered(self, user):
		if user in self.__users:
			return True
		else:
			return False

	def __register(self, user):
		self.__users.append(user)

	def __unregister(self, user):
		try:
			self.__users.remove(user)
		except ValueError:
			print('Vendor have not registered this user')