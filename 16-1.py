import json
with open('config.json','r') as cfg:
    data = json.loads(cfg.read())
data_attempts = data["attempts"]
db_users = {}
for i in range(len(data["users"])):
    db_users.update({data["users"][i]["password"]:\
                     data["users"][i]["login"]})

def check_password():
    i = data_attempts - 1
    while i:
        try:
            passwd = input('Enter your password, please: ')
            return db_users[passwd]
            break
        except KeyError:
            print(f'Sorry, password is invalid. Try again!\
                  \n{i} attempt(s) left')
            i -= 1
    else:
        try:
            passwd = input('Enter your password, please: ')
            return db_users[passwd]
        except KeyError:
            return 'Intruder'
       
user = check_password()
if user != 'Intruder':
    print (f'Welcome, {user} It\'s nice to see you again')
else:
    print('Sorry, I don\'t know you')