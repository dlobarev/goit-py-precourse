import json
from cryptography.fernet import Fernet

def hide_config_data(key):
    with open('config.json','r') as cf:
        data = json.loads(cf.read())
    cipher = Fernet(key)
    for i in range(len(data["users"])):
        encrypted_login = cipher.encrypt(data["users"][i]["login"].encode())
        data["users"][i]["login"] = encrypted_login.decode()
        encrypted_password = cipher.encrypt(data["users"][i]["password"].encode())
        data["users"][i]["password"] = encrypted_password.decode()
    protected_config = json.dumps(data, indent=2)
    with open("protected_config.json", "w") as pcf:
        pcf.write(protected_config)

def show_config_data(key):
    with open('protected_config.json','r') as pcf:
        data = json.loads(pcf.read())
    cipher = Fernet(key)
    for i in range(len(data["users"])):
        decrypted_login = cipher.decrypt(data["users"][i]["login"].encode())
        data["users"][i]["login"] = decrypted_login.decode()
        decrypted_password = cipher.decrypt(data["users"][i]["password"].encode())
        data["users"][i]["password"] = decrypted_password.decode()
    unprotected_config = json.dumps(data, indent=2)
    with open("unprotected_config.json", "w") as ucf:
        ucf.write(unprotected_config)