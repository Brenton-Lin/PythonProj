class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breath(self):
        print('inhale, exhale')


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breath(self):
        super().breath()
        print("underwater")

    def swim(self):
        print("just keep swimming")

fishy = Fish()

fishy.breath()
fishy.swim()
print(fishy.num_eyes)