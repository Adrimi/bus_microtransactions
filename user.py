from certificate import Certificate

class User:

	def __init__(self, address, maxSingleTransactionPrice):
		self.address = address
		self.publicKey = 'this_is_an_user_private_key'
		self.expirationDate = 180
		self.maxSingleTransactionPrice = maxSingleTransactionPrice


	def createCertificate(self, bank):
		self.certificate = Certificate(bank, self, self.address, self.publicKey, self.expirationDate, self.maxSingleTransactionPrice)