from bank import Bank
from user import User
from vendor import Vendor


bank = Bank()
vendor = Vendor()

user = User("1", 10)
user.createCertificate(bank)

