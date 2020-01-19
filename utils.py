from datetime import datetime
from random import randint


class Certificate:

  def __init__(self, bank, user, user_adderss, user_public_key, expiration_date, max_total_vendor_transaction_value):
    self.bank = bank
    self.user = user
    self.user_address = user_adderss
    self.user_public_key = user_public_key
    self.expiration_date = expiration_date
    self.max_total_vendor_transaction_value = max_total_vendor_transaction_value


class Transaction:

  def __init__(self, user, vendor, value):
    self.user = user
    self.vendor = vendor
    self.timestamp = datetime.now()
    self.value = value


class Hash:

	def __init__(self):
		self.random_number = randint(1, 1000000000000000000000000000000000)

	def get_hashed_number(self):
		for n in range(10):
			self.random_number = hash(self.random_number)
		return self.random_number

