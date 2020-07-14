'''

class Point:
    def __init__(self, x , y):
        self.x = x
        self.y = y
    def move(self):
        print('move')

    def draw(self):
        print('draw')


point1 = Point()
point1.draw()

'''
class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f'hi, i am {self.name}')


omkar = Person("omkar shirodkar")

omkar.talk()
bob = Person("bob")
bob.talk()
