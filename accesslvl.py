class User:
    def __init__(self, user_name):
        self.name = user_name

    def find_myself_in_list(self, user_list):
        return user_list.count(self) != 0

class AccessControlList:
    def __init__(self, denied_users, allowed_users):
        self.denied = denied_users
        self.allowed = allowed_users

    def request_access(self, user):
        if user.find_myself_in_list(self.denied):
            print("Access denied!")
            return False
        elif user.find_myself_in_list(self.allowed):
            print("Access granted")
            return True
        else:
            print("Access denied!")
            return False

class AccessLevel:
    def __init__(self, level):
        self.levels = {"unclassified", "secret", "top secret"}
        if self.verify(level):
            self.level = level

    def verify(self, level):
        return level in self.levels

if __name__ == '__main__':
    alice = User("Alice")
    bob = User("Bob")
    carl = User("Carl")
    david = User("David")
    denied_user_list = [bob, carl, bob]
    allowed_user_list = [alice, bob, carl]
    acl = AccessControlList(denied_user_list, allowed_user_list)
    print(acl.request_access(alice))  # True
    print(acl.request_access(bob))  # False
    print(acl.request_access(david))  # False
