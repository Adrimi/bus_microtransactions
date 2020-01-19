from utils import Certificate


class User:

  def __init__(self, address, max_single_transaction_price):
    self.address = address
    self.public_key = "this_is_an_user_private_key"
    self.expiration_date = 180
    self.max_single_transaction_price = max_single_transaction_price

    self.vendors = []

  def create_certificate(self, bank):
    self.certificate = Certificate(
      bank,
      self,
      self.address,
      self.public_key,
      self.expiration_date,
      self.max_single_transaction_price
    )

  # VENDOR SPECIFIC METHODS

  def send_registration_to(self, vendor, message):
    vendor.receive_payment_from(self, message)

  def has_first_payment_with(self, vendor):
    if not vendor in self.vendors:
      return True
    return False
