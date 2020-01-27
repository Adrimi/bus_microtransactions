from copy import copy
from utils import RSA, MQTT
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
			self.client = MQTT('BANK')

	def __init__(self):
		self.__private_key = RSA.generate_private_key()
		self.public_key = RSA.public_key(self.__private_key)
		self.users_info = []

		self.c = 3 # 2 to 10
		self.M = 16 # 5 to 30  

	def receive_message_from(self, vendor, message):
		user_index = self.__get_user_index_with(message["certificate"])
		if user_index == -1:
			print('Bank don\'t know this user')
		else:
			user_info = self.users_info[user_index]

			user_info.vendors.append(vendor)
			if user_info.polling_counter < self.M:
				return 200
			else:
				return 400

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
		session_key = RSA.decrypt(self.__private_key, message)
		self.users_info.append(Bank.User_Info(session_key))


	def receive_message(self, message):
		for user in self.users_info:
			f = Fernet(user.session_key)
			try:
				encrypted_message = f.decrypt(message)
			except InvalidToken as e:
				continue
			else:
				json = jsonpickle.decode(encrypted_message)
				print('[BANK] Message decrypted')
				return self.handle(json, user.max_credit)

	# === HELPER METHODS === 

	def handle(self, json, max_credit):
		if 'Coins' in json:
			coins = json['Coins'] 
			if coins > max_credit:
				print('[BANK] User cannot buy such many credits!')
				return 'failure'
			else:
				print('[BANK] User bought %d credits' % coins)
				f = self.c / coins
				return f


	# def __get_user_index_with(self, certificate):
	# 	for index, user in enumerate(self.users):
	# 		if user.certificate is certificate:
	# 			return index
	# 	return -1

