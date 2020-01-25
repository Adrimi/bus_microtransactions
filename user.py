from utils import Certificate, RSA


class User:

  def __init__(self):
    self.__private_key = RSA.generate_private_key()
    self.public_key = RSA.public_key(self.__private_key)

    self.vendors = []
    self.expiration_date = 180
    self.coins = 0

  def create_certificate(self, bank):
    self.certificate = Certificate(
      bank,
      self.public_key,
      self.expiration_date,
      0
    )

  # VENDOR
  # BANK 

  def send_to(self, bank, message):
    print(message)
    bank.receive(message)

  # def request_transaction_with(self, vendor, value):
    # vendor.receive_payment_from(self, value)

  def send_message_to(self, vendor, message):
    vendor.receive_message_from(self, message)

  def has_first_payment_with(self, vendor):
    if vendor in self.vendors:
      return True
    return False
