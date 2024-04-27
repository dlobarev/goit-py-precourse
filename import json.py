import json
from cryptography.fernet import Fernet
with open('config.json','r') as fh:
    jsd = fh.read()
    pjsd = json.loads(jsd)
    print(pjsd)
    key = b'5tlOpu2Bvib0m_yllgmzfhYVmonJNUR7bKCcdNh827Y='
    cipher = Fernet(key)
    print(pjsd['session_key'].encode())
    esk = cipher.encrypt(pjsd['session_key'].encode())
    pjsd['session_key'] = esk.decode()
    for i in range(len(pjsd["admins"])):
        encrypted_admin_login = cipher.encrypt(pjsd["admins"][i]["login"].encode())
        pjsd["admins"][i]["login"] = encrypted_admin_login.decode()
        encrypted_admin_password = cipher.encrypt(pjsd["admins"][i]["password"].encode())
        pjsd["admins"][i]["password"] = encrypted_admin_password.decode()
    protected_config = json.dumps(parsed_config, indent=2)
    
with open("protected_config.json", "w") as protected_config_json:
    protected_config_json.write(protected_config)



