from utils import Transaction
from bank import Bank


class Vendor:

  def __init__(self):
    self.__users = []
    self.__transactions = []

  def receive_registration_from(self, user, message):
    if self.__is_user_verified(user, message):
      print('user is verified')
      if not self.has_registered(user):
        self.__register(user)
        print('user registered in vendor\'s database')
      else:
        print('user has already been registered in this vendor')

  def receive_payment_from(self, user, value):
    if user.certificate.max_total_vendor_transaction_value >= self.current_sum_of_transactions_from(user) + value:
      print('vendor can accept payment from user!')
      self.__start_transaction_with(user, value)
    else:
      print('user had reach limit of total allowed sum of transactions with this vendor')

  # TRANSACTION SPECIFIC METHODS

  def __start_transaction_with(self, user, value):
    transaction = Transaction(user, self, value)
    self.__transactions.append(transaction)

  def current_sum_of_transactions_from(self, user):
    sum = 0
    for transaciton in self.__transactions:
      if transaciton.user == user:
        sum = sum + transaciton.value
    return sum

  # USER SPECIFIC METHODS

  def has_registered(self, user):
    if user in self.__users:
      return True
    return False

  def __is_user_verified(self, user, message):
    user_certificate = message["certiicate"]
    if user_certificate.bank.public_key == Bank.PUBLIC_KEY:
      if user_certificate.user_public_key == user.public_key:
        return True
    return False

  def __register(self, user):
    self.__users.append(user)

  def __unregister(self, user):
    try:
      self.__users.remove(user)
    except ValueError:
      print('Vendor have not registered this user')
