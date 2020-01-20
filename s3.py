from utils import AES
from os import urandom

string = "digitaledigitale"
public_key = urandom(32) + b'_' + urandom(16)

encrypted_string = AES(public_key).encrypt(string)
print(encrypted_string)

decrypted_string = AES(public_key).decrypt(encrypted_string)
print(decrypted_string)