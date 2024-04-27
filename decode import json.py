import json
from cryptography.fernet import Fernet
key = b'5tlOpu2Bvib0m_yllgmzfhYVmonJNUR7bKCcdNh827Y='
cipher = Fernet(key)

with open("protected_config.json", "r") as protected_config_json:
    protected_config = protected_config_json.read()

parsed_protected_config = json.loads(protected_config)

encrypted_session_key = cipher.decrypt(parsed_protected_config["session_key"].encode())
parsed_protected_config["session_key"] = encrypted_session_key.decode()

for i in range(len(parsed_protected_config["admins"])):
    encrypted_admin_login = cipher.decrypt(parsed_protected_config["admins"][i]["login"].encode())
    parsed_protected_config["admins"][i]["login"] = encrypted_admin_login.decode()

    encrypted_admin_password = cipher.decrypt(parsed_protected_config["admins"][i]["password"].encode())
    parsed_protected_config["admins"][i]["password"] = encrypted_admin_password.decode()

decrypted_config = json.dumps(parsed_protected_config, indent=2)

with open("decrypted_config.json", "w") as protected_config_json:
    protected_config_json.write(decrypted_config)
