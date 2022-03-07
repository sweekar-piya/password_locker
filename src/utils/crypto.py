import os
from dotenv import load_dotenv
from cryptography.fernet import Fernet

load_dotenv()

key = os.getenv("FERNET_KEY")

if key=="":
    key = Fernet.generate_key()
    print(f"Store this key under .env file: {key.decode('utf-8')}")
    
f = Fernet(key)

encrypt = lambda string: f.encrypt(string)
decrypt = lambda token: f.decrypt(token)
