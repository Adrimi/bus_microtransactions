# Local
from bank import Bank
from user import User
from vendor import Vendor
from utils import RSA
from cryptography.fernet import Fernet

# Standard
from datetime import datetime
import jsonpickle
from secrets import choice
from random import random


## SCENARIO 4
# Players
bank = Bank()
vendor = Vendor()
user = User()

symmetric_key = Fernet.generate_key()
user.set_session_key(symmetric_key)
user.send_session_key_to(bank, RSA.encrypt(bank.public_key, symmetric_key))

coins = 7
user_credits_message = jsonpickle.encode({
	'Coins' : coins
	}).encode('utf-8')

user_encrypted_message = Fernet(user.session_key).encrypt(user_credits_message)
response = user.send_message_to(bank, user_encrypted_message)

print('[MAIN] Response:', response)

response = Fernet(user.session_key).decrypt(response)
response = response.decode('utf-8')

if 'success' in response:
	user.finalize_coins(coins, float(response.split(': ')[1]))
elif 'failure' in response:
	print('[MAIN] Failure response from bank')

# ===

if not user.has_first_payment_with(vendor):

	# Create new session key for new connection (this time with Vendor) and send it to him
	symmetric_key = Fernet.generate_key()
	user.set_vendor_session_key(symmetric_key)
	user.send_session_key_to(vendor, RSA.encrypt(vendor.public_key, symmetric_key))

	# Also create new session key Bank - Vendor
	vendor.send_session_key_to(bank)	
	# ack = vendor.send_message_to(bank, user_encrypted_payment_message)

	flag = False
	loop_counter = 0

	while not flag:
		loop_counter += 1

		random_payment = choice([0.01, 0.03, 0.05])
		user_payment_message = jsonpickle.encode({
			"Time": datetime.now(),
			"F": user.f,
			"Payment": random_payment
		}).encode('utf-8')

		user_encrypted_payment_message = Fernet(user.session_key).encrypt(user_payment_message)
		response = user.send_message_to(vendor, user_encrypted_payment_message)			
		probability = random_payment * user.f
		# print('[%d] prob: %f' % (loop_counter, probability))

		if random() < probability:
			print('\n\n\n *** WARNING ***')
			user_warning_message = jsonpickle.encode({
				'SessionKey': user.session_key
				}).encode('utf8')
			user_encrypted_warning_message = Fernet(vendor.session_key).encrypt(user_warning_message)

			warning_response = vendor.send_message_to_bank(bank, user_encrypted_warning_message)

			decrypted_response = Fernet(vendor.session_key).decrypt(warning_response).decode('utf-8')
			response = float(decrypted_response)
			print(response)

			if response == 400:
				print('[MAIN] Bank has flag the User for suspicious activity')
				print('[MAIN] Mark at:', loop_counter)
				flag = True
