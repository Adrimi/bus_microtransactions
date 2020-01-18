from datetime import datetime


class Transaction:

	def __init__(self, user, vendor, value):
		self.user = user
		self.vendor = vendor
		self.timestamp = datetime.now()
		self.value = value