from cryptography.fernet import Fernet
from utils import Json

key = Fernet.generate_key()
f = Fernet(key)

dict = {
		"Imie": "Stara", 
		"Nazwisko" : "Bogacka",
		"Liczba_zebow": 2,
	}

message = Json(dict)

encrypted = f.encrypt(message.data)
decrypted = f.decrypt(encrypted)

print(message)
print(encrypted)
print(decrypted.decode('utf-8'))
