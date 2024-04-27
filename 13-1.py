class User:
    login = 'Guest'

    def greet(self):
        print(f'Hi, my login is {self.login}')

class AuthenticatedUser(User):
    password = 'password'

    def authenticate(self,user_password):
        return True if user_password == self.password else False

class AccessObject:
    content = ''
    name = ''
    owner = AuthenticatedUser()

    def change_owner(self, old_owner_password:str, new_owner:AuthenticatedUser):
        if old_owner_password == self.owner.password and new_owner != self.owner :
            self.owner = new_owner
            print(f'The ownership changing of {self.name} was successful! New owner is {self.owner.login}')
        else: print(f'Unauthorised attempt of {self.name} owner changing detected!')


alice = AuthenticatedUser()
alice.login = "Alice"
bob = AuthenticatedUser()
bob.login = "Bob"
bob.password = "uNc1e"

log = AccessObject()
log.owner = alice
log.name = "Computer logs"
log.content = "There is no entries yet"

security_policy = AccessObject()
security_policy.owner = bob
security_policy.name = "Enterprise security policy"
security_policy.content = "Only authorized users may access objects"

log.change_owner(bob.password, bob)
security_policy.change_owner(bob.password, alice)

