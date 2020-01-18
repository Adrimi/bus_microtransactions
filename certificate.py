class Certificate:

	def __init__(self, bank, user, userAdderss, userPublicKey, expirationDate, maxSingleTransactionPrice):
		self.bank = bank
		self.user = user
		self.userAddress = userAdderss
		self.userPublicKey = userPublicKey
		self.expirationDate = expirationDate
		self.maxSingleTransactionPrice = maxSingleTransactionPrice