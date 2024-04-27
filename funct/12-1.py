#Password authentication function, 3 attempts, returns users 'Name' or 'Intruder'
def check_password():
    i = 2
    while i:
        try:
            passwd = input('Enter your password, please: ')
            return db_users[passwd]
            break
        except KeyError:
            print('Sorry, password is invalid. Try again!')
            print(f'{i} attempt(s) left')
            i -= 1
    else:
        try:
            passwd = input('Enter your password, please: ')
            return db_users[passwd]
        except KeyError:
            return 'Intruder'
#--------------------------------------------------------------------------------------------
            
#Second factor auth function, argument = expected_auth_code, returns True or False
def check_auth_code(expected_auth_code):
    second_factor = input('Enter authentication code, please: ')
    return True if second_factor == expected_auth_code else False
#--------------------------------------------------------------------------------------------           

db_users = {'C00peR':'Alice', 'uNc1e':'Bob', 'ClariNet':'Carl'}
factor = False
user = check_password()
if user != 'Intruder': factor = check_auth_code('1111')
print (f'Welcome, {user} It\'s nice to see you again') if factor else print('Sorry, I don\'t know you')