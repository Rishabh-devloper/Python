class Animal():
    def show(self):
        print("Hewy i am Animal here")
class Human(Animal):
    def show(self):
        print("heyyy I am human Hewre")
        
obj = Human()

obj.show()