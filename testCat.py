from cat import Cat
from cat import pet_info # почему не дает импортировать все функции и классы через "import cat"??

Baron = Cat("Барон", "мальчик", 2)
Sam = Cat("Сэм", "мальчик", 2)

# --------- Вывод из этого файла

print(f'Имя питомца: {Baron.getName()}, Пол питомца: {Baron.getGender()}, Возраст: {Baron.getAge()} года')
print(f'Имя питомца: {Sam.getName()}, Пол питомца: {Sam.getGender()}, Возраст: {Sam.getAge()} года')
print("xxxxxxxxxxxxxxxxx----------xxxxxxxxxxxxxxxxxx")

# ---------- Вывод без функций getName, getGender, getAge!!!!
# не понял до конца зачем они нужны?

print(f'Имя питомца: {Baron.name}, Пол питомца: {Baron.gender}, Возраст: {Baron.age} года')
print("-----------------------------------------------")

# ---------- Вывод через функцию из оригинального файла (надо ли?!)
# выводит в дополнение вымышленного питомца "Федора" из оригинального файла (на первом месте)!!!!

pet_info(Baron)
pet_info(Sam)