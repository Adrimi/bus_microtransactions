from datetime import datetime
from random import randint
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend


class Certificate:

  def __init__(self, bank, user, user_adderss, user_public_key, expiration_date, f):
    self.bank = bank
    self.user = user
    self.user_address = user_adderss
    self.user_public_key = user_public_key
    self.expiration_date = expiration_date
    self.f = f


class Transaction:

  def __init__(self, user, vendor, value):
    self.user = user
    self.vendor = vendor
    self.timestamp = datetime.now()
    self.value = value


class AES:

	def __init__(self, public_key):
		self.key, self.vi = public_key.split(b'_')

		self.cipher = Cipher(algorithms.AES(self.key), modes.CBC(self.vi), backend = default_backend())

	def encrypt(self, message):
		enc = self.cipher.encryptor()
		message = message.encode('latin-1', 'strict')
		return enc.update(message) + enc.finalize()

	def decrypt(self, message):
		dec = self.cipher.decryptor()

		message = dec.update(message) + dec.finalize()
		return message.decode('latin-1', 'strict')


class Hash:

	def __init__(self):
		self.random_number = randint(1, 1000000000000000000000000000000000)
		for n in range(10):
			self.random_number = hash(self.random_number)
