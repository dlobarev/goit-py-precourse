def get_fullname(first_name,last_name,middle_name=''):
   return (f'{first_name} {middle_name} {last_name}') if middle_name else (f'{first_name} {last_name}')
#return (f'{first_name} {last_name}')
print(get_fullname('Петро', 'Залізняк', 'Максимович'))