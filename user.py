from utils import Certificate


class User:

  def __init__(self, key):
    self.public_key = key

    self.vendors = []
    self.address = "address"
    self.expiration_date = 180
    self.coins = 0

  def create_certificate(self, bank):
    self.certificate = Certificate(
      bank,
      self,
      self.address,
      self.public_key,
      self.expiration_date,
      10
    )

  # VENDOR SPECIFIC METHODS

  # def request_transaction_with(self, vendor, value):
    # vendor.receive_payment_from(self, value)

  def send_message_to(self, vendor, message):
    vendor.receive_message_from(self, message)

  def has_first_payment_with(self, vendor):
    if vendor in self.vendors:
      return True
    return False
