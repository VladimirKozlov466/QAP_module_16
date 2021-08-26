class Cat:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def getName(self):
        return self.name

    def getGender(self):
        return self.gender

    def getAge(self):
        return self.age

    def pet_info(self):
        return f'Имя питомца: {self.getName()}, Пол питомца: {self.getGender()}, Возраст: {self.getAge()}'

fedor = Cat(name="Федор", gender="мальчик", age=5) # тоже не понимаю почему ругается?!
print(fedor.pet_info())

