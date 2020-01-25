from cryptography.fernet import Fernet
from user import User
import jsonpickle as json 

key = Fernet.generate_key()
f = Fernet(key)

dict = {
		"User": User()
	}

message = json.encode(dict)

encrypted = f.encrypt(message.encode('utf-8'))
decrypted = f.decrypt(encrypted)

print(message)
print(encrypted)
print(decrypted.decode('utf-8'))
