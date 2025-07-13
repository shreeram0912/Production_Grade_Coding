# AES Advance Encryption Standard (Convert Plain text into Cipher text), AES-128, 192, 256 (16, 24, 32) encryption.
# For encryption need encryption key, which set on operating system level. (1 byte = 8 bit) 
# CBC Cipher Block Chain

import base64 # Encoding
import os, sys # Operating system, System
from loguru import logger
from Cryptodome.Cipher import AES 
from Cryptodome.Protocol.KDF import PBKDF2 # Password Based Key Derivation Function

try:
    encryption_key = "key1" # For encryption & decryption
    initialization_vector = "my_username_pass"
    salt = "salt" # Second layer of protection

    if not (encryption_key and initialization_vector and salt):
        raise Exception(F"Error while fetching details for encryption_key/initialization_vector/salt")
except Exception as e:
    logger.error("Error occurred. Details: %s", e)
    sys.exit(0)

BS = 16
pad = lambda s: bytes(s + (BS - len(s) % BS) * chr(BS - len(s) % BS), 'utf-8')
unpad = lambda s: s[0:-ord(s[-1:])]

def get_private_key():
    Salt = salt.encode('utf-8')
    # Take encryption_key & salt iterate 1000 time & Return 64 byte long character.
    kdf = PBKDF2(encryption_key, salt, 64, 1000) 
    key32 = kdf[:32] # From 64 byte long character take only 32 byte character
    return key32 # Return private_key on basis of encryption_key & salt after 1000 iteration

# Padding add remaining byte in character or raw
def encrypt(raw):
    raw = pad(raw)
    # IV initialization vector used for add randomness in password
    cipher = AES.new(get_private_key(), AES.MODE_CBC, initialization_vector.encode('utf-8'))
    return base64.b64encode(cipher.encrypt(raw))

def decrypt(enc):
    cipher = AES.new(get_private_key(), AES.MODE_CBC, initialization_vector.encode('utf-8'))
    return unpad(cipher.decrypt(base64.b64decode(enc))).decode('utf-8')

# print(encrypt("1234"))
# print(decrypt("B0yrRpe8EWVzg0ZPiBss1g=="))

# Setting the encryption_key, iv on operating system level
# Linux = export key_name value_name
# Windows = set key_name=value_name
# Access the key using print(os.environ.get("key")) or echo %key%