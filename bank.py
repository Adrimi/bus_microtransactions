from utils import RSA
from cryptography.fernet import Fernet
from cryptography.fernet import InvalidToken
import jsonpickle


class Bank:

	class User_Info:
		def __init__(self, key):
			self.session_key = key
			self.max_credit = 10
			self.polling_counter = 0
			self.vendors = []

	def __init__(self):
		self.__private_key = RSA.generate_private_key()
		self.public_key = RSA.public_key(self.__private_key)
		self.users_info = []
		self.vendors_info = []

		self.c = 3 # 2 to 10
		self.M = 16 # 5 to 30  

	def receive_warning_from(self, vendor, message):
		user_index = self.__get_user_index_with(message["certificate"])
		user_info = self.users_info[user_index]

		user_info.polling_counter += 1
		print('Bank received warning\n')
		if user_info.polling_counter < self.M:
			return 200
		else:
			return 400

	# USER
	def receive_session_key(self, message):
		print('[BANK] Received RSA encrypted session_key. Decoding...')
		session_key = RSA.decrypt(self.__private_key, message)
		print('[BANK] Session key decoded:', session_key)
		self.users_info.append(Bank.User_Info(session_key))
		print('++++++ SESSION ACKNOWLEDGE END ++++++++\n')

	def reveive_session_key_from_vendor(self, message):
		print('[BANK] Received RSA encrypted session_key. Decoding...')
		session_key = RSA.decrypt(self.__private_key, message)
		print('[BANK] Session key decoded:', session_key)
		self.vendors_info.append(session_key)
		print('++++++ SESSION ACKNOWLEDGE END ++++++++\n')

	def receive_message(self, message):
		for user in self.users_info:
			f = Fernet(user.session_key)
			try:
				decrypted_message = f.decrypt(message)
			except InvalidToken as e:
				continue
			else:
				json = jsonpickle.decode(decrypted_message)
				print('[BANK] Message decrypted')
				response = f.encrypt(self.handle(json, user.max_credit).encode('utf-8'))
				print('[BANK] Sent response:', response)
				return response

	def receive_message_vendor(self, message):
		for vendor in self.vendors_info:
			f = Fernet(vendor)
			try:
				decrypted_message = f.decrypt(message)
			except InvalidToken as e:
				continue
			else:
				json = jsonpickle.decode(decrypted_message)
				print('[BANK] Message decrypted')
				response = f.encrypt(self.handle(json, vendor).encode('utf-8'))
				print('[BANK] Sent response:', response)
				return response

	# === HELPER METHODS === 

	# Extra info is user.max_credits (Coins) OR vendor (just his session_key)
	def handle(self, json, extra_info):
		if 'Coins' in json:
			coins = json['Coins'] 
			if coins > extra_info:
				print('[BANK] User cannot buy such many credits!')
				return 'failure'
			else:
				print('[BANK] User bought %d credits' % coins)
				f = self.c / coins
				return 'success: %f' % f

		if 'SessionKey' in json:
			user_session_key = json['SessionKey']
			for user in self.users_info:
				if user.session_key == user_session_key:
					user.vendors.append(extra_info)
					user.polling_counter += 1
					if user.polling_counter < self.M:
						return '200'
					else:
						return '400'
				return 'DUPA'
			print('[BANK] Got warning about unknown user')
