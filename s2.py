# Local
from bank import Bank
from user import User
from vendor import Vendor
from utils import Hash

# Standard
from datetime import datetime


## SCENARIO 2
# Persons
bank = Bank()
vendor = Vendor()
user = User("1", 10)

# Story
"""
	User after registration wants to perform 5 payments to vendor, each with 3$ value.
	Vendor is checking if User hasn't reached the daily limit of transactions.  
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

	user.request_transaction_with(vendor, 3)
	user.request_transaction_with(vendor, 3)
	user.request_transaction_with(vendor, 3)
	user.request_transaction_with(vendor, 3)
	user.request_transaction_with(vendor, 3)



