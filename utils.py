from datetime import datetime
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding, rsa


class Certificate:

  def __init__(self, bank, user, user_public_key, expiration_date, f):
    self.bank = bank
    self.user = user
    self.user_public_key = user_public_key 
    self.expiration_date = expiration_date
    self.f = f


class Transaction: 

  def __init__(self, user, vendor, value):
    self.user = user
    self.vendor = vendor
    self.timestamp = datetime.now()
    self.value = value


class RSA:

	@staticmethod
	def generate_private_key():
		return rsa.generate_private_key(
      public_exponent = 35,
      key_size = 512,
      backend = default_backend()
    ).private_bytes(
    	encoding = serialization.Encoding.PEM,
    	format = serialization.PrivateFormat.PKCS8,
    	encryption_algorithm = serialization.NoEncryption()
    )

	@staticmethod
	def public_key(private_key):
		return serialization.load_pem_private_key(
			private_key,
		  password = None,
		  backend = default_backend()
		  ).public_key().public_bytes(
		  encoding = serialization.Encoding.PEM,
		  format = serialization.PublicFormat.SubjectPublicKeyInfo)

	@staticmethod
	def encrypt(public_key, data):
		return serialization.load_pem_public_key(
			public_key,
			backend = default_backend()
			).encrypt(
			data,
			padding.OAEP(
				mgf = padding.MGF1(algorithm = hashes.SHA256()),
				algorithm = hashes.SHA256(),
				label = None
			)
		)

	@staticmethod
	def decrypt(private_key, data):
		return serialization.load_pem_private_key(
			private_key,
		  password = None,
		  backend = default_backend()
		  ).decrypt(
			data,
			padding.OAEP(
				mgf = padding.MGF1(algorithm = hashes.SHA256()),
				algorithm = hashes.SHA256(),
				label = None
			)
		)