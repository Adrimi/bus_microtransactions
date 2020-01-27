from utils import RSA, MQTT


class User:

  def __init__(self):
    self.vendors = []
    self.expiration_date = 180
    self.coins = 0
    self.session_key = b''
    self.f = 0
    self.client = MQTT('USER')

  # VENDOR
  # BANK 

  def send_session_key_to(self, bank, message):
    print(message)
    bank.receive_session_key(message)

  # def request_transaction_with(self, vendor, value):
    # vendor.receive_payment_from(self, value)

  def publish(self, topic, message):
    self.client.connect()
    self.client.publish(message)
    print('[USER] Message sent')
    rc = 0
    while rc == 0:
      rc = self.client.client.loop()
    print('[USER] Response on message')
    return rc


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
