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
