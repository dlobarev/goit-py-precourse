class AccessLevel:
    def __init__(self, pname, plevel = 0):
        self.name = pname
        self.level = plevel

    def __eq__(self, other):
        return self.level == other.level
    
    def __lt__(self, other):
        return self.level <= other.level
    
    def __gt__(self, other):
        return self.level >= other.level

class AccessObject:
    def __init__(self, pname, pcontent, paccess_level):
        self.content = pcontent
        self.name = pname
        self.access_level = paccess_level

class User:
    login = "Guest"
    def __init__(self, pname, paccess_level):
        self.login = pname
        self.__mandatum = paccess_level
    
    def greet(self):
        print(f"Hi, my login is {self.login}")

    @property
    def mandatum(self):
        return self.__mandatum.level

    @mandatum.setter
    def mandatum(self, new_paccess_level):
        if (new_paccess_level.name != '') & (new_paccess_level.level >= 0):
            self.__mandatum = new_paccess_level
        else:
            print('Not a valid acсess level')

    def get_access(self, access_object):
        if access_object.access_level.level <= self.mandatum:
            print(f"Content for you {self.login}: {access_object.content}")
        else:  print(f"Access to {access_object.name} denied!")

unclassified = AccessLevel("Unclassified", 1)
secret = AccessLevel("Secret", 2)
top_secret = AccessLevel("Top Secret", 3)

alice = User("Alice", top_secret)
bob = User("Bob", unclassified)

password_database = AccessObject(
    "Password Database",
    "Alice - C00peR, Bob - uNc1e",
    secret
)

alice.greet()
alice.get_access(password_database)

bob.greet()
bob.get_access(password_database)
