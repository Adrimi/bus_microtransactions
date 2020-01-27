from datetime import datetime
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding, rsa

import paho.mqtt.client as mqtt
import os
from urllib.parse import urlparse

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
      public_exponent = 65537,
      key_size = 873,
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


class MQTT:

	LOGGER = ''

	def __init__(self, topic):
		self.client = mqtt.Client()
		self.client.on_message = MQTT.on_message
		self.client.on_connect = MQTT.on_connect
		self.client.on_publish = MQTT.on_publish
		self.client.on_subscribe = MQTT.on_subscribe
		self.client.on_log = MQTT.on_log

		url_str = os.environ.get('CLOUDMQTT_URL', 'mqtt://hairdresser.cloudmqtt.com:18137/%s' % topic)
		self.url = urlparse(url_str)
		self.topic = self.url.path[1:] or 'test'

	def connect(self):
		self.client.connect(self.url.hostname, self.url.port)

	def subscribe(self):
		self.client.subscribe(self.topic, 0)

	def publish(self, message):
		self.client.publish(self.topic, message)

	@staticmethod
	def on_connect(client, userdata, flags, rc):
	  print("Connect: " + str(rc))

	@staticmethod
	def on_message(client, obj, msg):
	  print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

	@staticmethod
	def on_publish(client, obj, mid):
	  print("Publish: " + str(mid))

	@staticmethod
	def on_subscribe(client, obj, mid, granted_qos):
	  print("Subscribed: " + str(mid) + " " + str(granted_qos))

	@staticmethod
	def on_log(client, obj, level, string):
	  print(string)
