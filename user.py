from utils import RSA

class User:

  def __init__(self):
    self.vendors = []
    self.expiration_date = 180
    self.coins = 0
    self.session_key = b''
    self.f = 0

  def send_session_key_to(self, instance, message):
    print('\n++++++ SESSION ACKNOWLEDGE START ++++++++')
    print('[USER] Sending RSA encrypted session_key:', message)
    instance.receive_session_key(message)

  def send_message_to(self, instance, message):
    # print('[USER] Sending message:', message)
    return instance.receive_message(message)

  def finalize_coins(self, coins, f):
    print('[USER] Gained %d coins' % coins)
    self.coins = coins
    self.f = f

  def set_session_key(self, session_key):
    print('[USER] Created new session_key:', session_key)
    self.session_key = session_key

  def set_vendor_session_key(self, session_key):
    print('[USER] Created new session_key:', session_key)
    self.vendor_session_key = session_key

  def has_first_payment_with(self, vendor):
    if vendor in self.vendors:
      return True
    return False
