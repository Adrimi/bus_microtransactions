from transaction import Transaction

class Vendor:

	def __init__(self):
		self.users = []
		self.transactions = []

	def receivePayment(self, user, value):
		if !self.hasRegistered(user):
			self.register(user)
		self.startTransactionWith(user, value)

# TRANSACTION SPECIFIC METHODS

	def startTransactionWith(self, user, value):
		transaction = Transaction(user, self, value)
		self.transactions.append(transaction)

# USER SPECIFIC METHODS

	def hasRegistered(self, user):
		if user in self.users:
			return True
		else:
			return False

	def register(self, user):
		self.users.append(user)

	def unregister(self, user):
		try:
			self.users.remove(user)
		except ValueError:
			print('Vendor have not registered this user')