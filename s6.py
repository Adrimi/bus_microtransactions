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
user.session_key = symmetric_key
user.send_session_key_to(bank, RSA.encrypt(bank.public_key, symmetric_key))

coins = 7
user_credits_message = jsonpickle.encode({
	'Coins' : coins
	}).encode('utf-8')

user_encrypted_message = Fernet(user.session_key).encrypt(user_credits_message)
response = user.send_message_to(bank, user_encrypted_message)

print('[MAIN] Response:', response)

if isinstance(response, float):
	user.finalize_coins(coins, response)

# if user.certificate.f is not new_certificate.f:
# 	user.coins = coins
# 	user.certificate = new_certificate
# 	print('User bought %d coins' % coins)

# ===

# if not user.has_first_payment_with(vendor):

# 	register_message = {
# 		"certificate": user.certificate,
# 		"vendor": vendor,
# 		"time": datetime.now(),
# 		"payment": 0.05
# 	}

# 	user.send_message_to(vendor, register_message)

# 	if vendor.has_registered(user):
# 		ack = vendor.send_message_to(bank, register_message)

# 		if ack == 200:
# 			flag = False
# 			loop_counter = 0

# 			while not flag:
# 				loop_counter += 1

# 				register_message["payment"] = choice([0.01, 0.03, 0.05])
# 				user.send_message_to(vendor, register_message)

# 				probability = register_message["payment"] * user.certificate.f
				
# 				print('[%d] prob: %f' % (loop_counter, probability))

# 				if random() < probability:
# 					response = bank.receive_warning_from(vendor, register_message)

# 					if response == 400:
# 						print('Bank has flag the User for suspicious activity')
# 						flag = True





