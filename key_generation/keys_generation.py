from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes

def async_keys_generation(size=1024):
    keys = RSA.generate(size)
    key_private = keys.export_key()
    key_public = keys.public_key().export_key()
    with open('logs/private.pem', 'wb') as file_keys_private:
        file_keys_private.write(key_private)
    with open('logs/public.pem', 'wb') as file_key_puvlic:
        file_key_puvlic.write(key_public)