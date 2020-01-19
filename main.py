# Local
from bank import Bank
from user import User
from vendor import Vendor
from utils import Hash

# Standard
from datetime import datetime


bank = Bank()
vendor = Vendor()
user = User("1", 10)

# SCENARIO 1
user.create_certificate(bank)

if user.has_first_payment_with(vendor) :

	random_hashed_number = Hash().get_hashed_number()
	register_message = {
		"certiicate": user.certificate,
		"vendor": vendor,
		"time": datetime.now(),
		"payment": (1, random_hashed_number)
	}

	user.send_registration_to(vendor, register_message)



