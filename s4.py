# Local
from bank import Bank
from user import User
from vendor import Vendor
from utils import Hash

# Standard
from datetime import datetime
from os import urandom
from secrets import choice
from random import random

user_public_key = urandom(32) + b'_' + urandom(16)

## SCENARIO 4
# Players
bank = Bank()
vendor = Vendor()
user = User(user_public_key)

# Story
"""
	An User sends his certificate to the Bank, with coins puchase request. 
	If Bank can sell the User this amount of coins, then creates new, modified certificate for the User. 
	User sends payment message to Vendor, then vendor is communicating with Bank and send back ACK. If 200, then Vendor accepts every payment from user with calculated probability.
"""
user.create_certificate(bank)

coins = 7
print(user.certificate.f)
new_certificate = bank.sell_credits(user, coins)

if user.certificate.f is not new_certificate.f:
	user.coins = coins
	user.certificate = new_certificate
	print('User bought %d coins' % coins)

# ===

if not user.has_first_payment_with(vendor):

	register_message = {
		"certificate": user.certificate,
		"vendor": vendor,
		"time": datetime.now(),
		"payment": 0.05
	}

	user.send_message_to(vendor, register_message)

	if vendor.has_registered(user):
		ack = vendor.send_message_to(bank, register_message)

		if ack == 200:
			flag = False
			loop_counter = 0

			while not flag:
				loop_counter += 1

				register_message["payment"] = choice([0.01, 0.03, 0.05])
				user.send_message_to(vendor, register_message)

				probability = register_message["payment"] * user.certificate.f
				
				print('[%d] prob: %f' % (loop_counter, probability))

				if random() < probability:
					response = bank.receive_warning_from(vendor, register_message)

					if response == 400:
						print('Bank has flag the User for suspicious activity')
						flag = True

















