from utils import RSA


class User:

  def __init__(self):
    self.vendors = []
    self.expiration_date = 180
    self.coins = 0
    self.session_key = b''
    self.f = 0

  # VENDOR
  # BANK 

  def send_session_key_to(self, bank, message):
    print(message)
    bank.receive_session_key(message)

  # def request_transaction_with(self, vendor, value):
    # vendor.receive_payment_from(self, value)

  def send_message_to(self, bank, message):
    print(message)
    return bank.receive_message(message)

  def finalize_coins(self, coins, f):
    print('[USER] Gained %d coins' % coins)
    self.coins = coins
    self.f = f

  def has_first_payment_with(self, vendor):
    if vendor in self.vendors:
      return True
    return False
