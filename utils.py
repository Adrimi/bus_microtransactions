from datetime import datetime
from random import randint
from cryptography.fernet import Fernet
import json


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


class Json:

	DEFAULT_ENCODING = 'utf-8'

	def __init__(self, data):
		self.data = json.dumps(data, sort_keys = True, indent = 2)
		self.encode()

	def __str__(self):
		if isinstance(self.data, bytes):
			return self.data.decode()
		return self.data

	def encoded(self):
		self.encode()
		return self

	def decoded(self):
		self.decode()
		return self

	def encode(self):
		self.data = self.data.encode(Json.DEFAULT_ENCODING)

	def decode(self):
		self.data = self.data.decode(Json.DEFAULT_ENCODING)
