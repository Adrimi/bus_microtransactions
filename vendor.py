from utils import Transaction
from bank import Bank


class Vendor:

  def __init__(self):
    self.__users = []
    self.__transactions = []


  def receive_message_from(self, user, message):
    if self.__is_user_verified(user, message):

      if message["payment"] * user.certificate.f <= 1:
        if not self.has_registered(user):
          self.__register(user)
          print('user registered in vendor\'s database')
        else:
          self.__start_transaction_with(user, message["payment"])

      else:
        print('Vendor rejected transaction')



  # TRANSACTION SPECIFIC METHODS

  def send_message_to(self, bank, message):
    self.bank = bank
    return bank.receive_message_from(self, message)


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
    user_certificate = message["certificate"]
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
