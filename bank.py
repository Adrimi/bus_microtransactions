from copy import copy
from utils import RSA


class Bank:

	class User_Info:
		def __init__(self):
			self.max_credit = 10
			self.polling_counter = 0
			self.vendors = []

	def __init__(self):
		self.__private_key = RSA.generate_private_key()
		self.public_key = RSA.public_key(self.__private_key)

		# Bank Information about user activity
		self.users = []
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
	def receive(self, message):
		message = RSA.decrypt(self.__private_key, message)
		print(message)

		# if not user in self.users:
		# 	self.__register(user)

		# Create copy of certificate for further changes
		certificate = copy(user.certificate)
		user_index = self.users.index(user)

		if coins > self.users_info[user_index].max_credit + user.coins:
			print('User cannot buy such many credits!')
		else:
			f = self.c / coins
			certificate.f = f
		
		return certificate


	# USER SPECIFIC 

	def __get_user_index_with(self, certificate):
		for index, user in enumerate(self.users):
			if user.certificate is certificate:
				return index
		return -1

	def __register(self, user):
		self.users.append(user)
		self.users_info.append(Bank.User_Info())
