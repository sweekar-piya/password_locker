#!/Users/sweekar.piya/Documents/python_learning/automate_boring_stuff_with_python/password_locker/.venv/bin/python

# pass.py: Vulnerable password locker program
import os, sys
import pickle
import pyperclip
from pathlib import Path
from src.utils.const import PROJECT_ROOT
from src.utils.crypto import encrypt, decrypt


def encrypt_passwords(data_path):
    from data.creds import CREDENTIALS
    
    encrypted_creds = {}
    
    for k, v in CREDENTIALS.items():
        encrypted_creds.setdefault(k, "")
        encrypted_creds[k] = encrypt(v)
        
    with open(data_path / "encrypted_creds.pkl", 'wb') as file:
        pickle.dump(encrypted_creds, file)
    
def decrypt_passwords(data_path, key):
    try:
        with open(data_path / "encrypted_creds.pkl", 'rb') as file:
            credential = decrypt(pickle.load(file)[key])
        return credential.decode("utf-8")    
    except KeyError:
        raise KeyError(f"The account named {key} is not found.")    
    

if __name__ == "__main__":
    
    data_path = Path(PROJECT_ROOT) / "data"

    if not os.path.exists(data_path/"encrypted_creds.pkl"): 
        print("No encryptions found, encrypting passwords!")
        encrypt_passwords(data_path)  
        sys.exit()
        
    if len(sys.argv) < 2:
        print('Provide account to copy account from the terminal.')
        sys.exit()
        
    account = sys.argv[1]
    pyperclip.copy(decrypt_passwords(data_path, account))