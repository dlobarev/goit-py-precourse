usrs = {'Alice':'C00peR','Bob':'uNc1e','Carl':'ClariNet'}
passwd = input('Enter your password, please: ')
def get_key(val): 
    for key, value in usrs.items():
        if val == value:
            print (f'Welcome, {key}! It\'s nice to see you again')
if passwd in usrs.values():
    get_key(passwd)
else:
    print('Sorry, I don\'t know you')
