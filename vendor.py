from utils import Transaction
from bank import Bank


class Vendor:

  def __init__(self):
    self.__users = []
    self.__transactions = []

  def receive_payment_from(self, user, message):
    if not self.has_registered(user):
      self.__register(user)
    if self.__is_user_verified(user, message):
      print('user is verified')
      # self.__start

  # TRANSACTION SPECIFIC METHODS

  # def __start_transaction_with(self, user, value):
    #transaction will become on the end of checklist !!
    # transaction = Transaction(user, self, value)
    # self.__transactions.append(transaction)

  # USER SPECIFIC METHODS

  def __is_user_verified(self, user, message):
    user_certificate = message["certiicate"]
    if user_certificate.bank.public_key == Bank.PUBLIC_KEY:
      if user_certificate.user_public_key == user.public_key:
        return True
    return False

  def has_registered(self, user):
    if user in self.__users:
      return True
    return False

  def __register(self, user):
    self.__users.append(user)

  def __unregister(self, user):
    try:
      self.__users.remove(user)
    except ValueError:
      print('Vendor have not registered this user')
