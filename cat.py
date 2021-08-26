class Cat:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def getName(self):# нужны ли нам эти функции?!
        return self.name

    def getGender(self):
        return self.gender

    def getAge(self):
        return self.age

def pet_info(self):# не понимаю почему ругается?!
    print(f'Имя питомца: {self.getName()}, Пол питомца: {self.getGender()}, Возраст: {self.getAge()}')

fedor = Cat("Федор", "мальчик", 5) # тоже не понимаю почему ругается?!
pet_info(fedor)

