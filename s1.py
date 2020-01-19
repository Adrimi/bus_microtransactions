# Local
from bank import Bank
from user import User
from vendor import Vendor
from utils import Hash

# Standard
from datetime import datetime


## SCENARIO 1
# Persons
bank = Bank()
vendor = Vendor()
user = User("1", 0)

# Story
"""
	User is registering himself in vendor's database with register message. 
	Vendor is checking if user can be verified based on user certificate
	and user and the bank Public Key. 
"""
user.create_certificate(bank)

if not user.has_first_payment_with(vendor):

	random_hashed_number = Hash().get_hashed_number()
	register_message = {
		"certiicate": user.certificate,
		"vendor": vendor,
		"time": datetime.now(),
		"payment": (1, random_hashed_number)
	}

	user.send_registration_to(vendor, register_message)

	if vendor.has_registered(user):
		print('now user can start sending payment requests')

	# user.send_registration_to(vendor, register_message)
	# user.send_registration_to(vendor, register_message)
	# user.send_registration_to(vendor, register_message)
