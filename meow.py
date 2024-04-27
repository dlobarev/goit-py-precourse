class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight


class Cat(Animal):
    def __init__(self, nickname, weight, breed):
        super().__init__(nickname, weight)
        self.breed = breed
        
    def say(self):
        return "Meow"


cat = Cat("Simon", 10, "british")
print(cat.nickname)  # Simon
print(cat.breed)  # british
print(cat.weight)  # 10
print(cat.say())