from Crypto.Cipher import AES
from base64 import b64decode
from hashlib import sha256
from Crypto.Util.Padding import unpad

key_string = "vudzvuokmioomyialpkyydvgqdmdkdxy"  
key = sha256(key_string.encode()).digest()  
iv = b"tbbliftalildywic"  

if len(iv) != 16:
    raise ValueError("IV must be exactly 16 bytes long!")

base64_data = "ZzfccaKJB3CrDvOnj/6io5OR7jZGL0pr0sLO/ZcRNSa1JLrHA+k2RN1QkelHxKVvhrtiCDD14Aaxc266kJOzF59MfhoI5hJjc5hx7kvGAFw="
encrypted_data = b64decode(base64_data)
cipher = AES.new(key, AES.MODE_CBC, iv)
decrypted_data = cipher.decrypt(encrypted_data)
decrypted_data = decrypted_data.rstrip(b'\x00')

decrypted_text = decrypted_data.decode('utf-8')
print("Decrypted text :", decrypted_text)

