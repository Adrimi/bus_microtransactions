from utils import Transaction, RSA
from cryptography.fernet import Fernet
from cryptography.fernet import InvalidToken
import jsonpickle


class Vendor:

  class User_Info:
    def __init__(self, key):
      self.session_key = key

  def __init__(self):
    self.__users = []
    self.__transactions = []
    self.__private_key = RSA.generate_private_key()
    self.public_key = RSA.public_key(self.__private_key)

  def receive_session_key(self, message):
    print('[VENDOR] Received RSA encrypted session_key. Decoding...')
    session_key = RSA.decrypt(self.__private_key, message)
    print('[VENDOR] Session key decoded:', session_key)
    self.__users.append(Vendor.User_Info(session_key))
    print('++++++ SESSION ACKNOWLEDGE END ++++++++\n')

  def send_session_key_to(self, instance):
    print('\n++++++ SESSION ACKNOWLEDGE START ++++++++')
    self.session_key = Fernet.generate_key()
    encrypted_session_key = RSA.encrypt(instance.public_key, self.session_key)
    print('[VENDOR] Sending RSA encrypted session_key:', encrypted_session_key)
    instance.reveive_session_key_from_vendor(encrypted_session_key)

  def send_message_to(self, instance, message):
    print('[VENDOR] Sending message:', message)
    return instance.receive_message(message)

  def send_message_to_bank(self, instance, message):
    print('[VENDOR] Sending message:', message)
    return instance.receive_message_vendor(message)

  def receive_message(self, message):
    for user in self.__users:
      f = Fernet(user.session_key)
      try:
        decrypted_message = f.decrypt(message)
      except InvalidToken as e:
        continue
      else:
        json = jsonpickle.decode(decrypted_message)
        print('[VENDOR] Message decrypted')
        response = f.encrypt(self.handle(json))
        print('[VENDOR] Send response:', response)
        return response


  def handle(self, json):
    payment_value = json['Payment']
    f = json['F']
    if payment_value * f <= 1:
      print('[VENDOR] Accepted payment')
      return 'success'
    else:
      print('[VENDOR] Rejected payment')
      return 'failure'

  # USER SPECIFIC METHODS

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
