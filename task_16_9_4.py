class VolunteerList:
    def __init__(self, status="membership"):
        self.status = status

class GuestList(VolunteerList):
    def __init__(self, name, surname, residence, status):
        super().__init__(status)
        self.name = name
        self.surname = surname
        self.address = residence
    def guest_to_be_on_party(self):
        return '"{0} {1}, г.{2}, статус "{3}"'.format(self.name, self.surname,
                                                    self.address, self.status)

membership_1 = GuestList("Андрей", "Иванов", "Москва", "Гуру")
membership_2 = GuestList("Сергей", "Косякин", "Архангельск", "Падаван")
membership_3 = GuestList("Ольга", "Разгуляева", "Челябинск", "Колеблющийся")
membership_4 = GuestList("Наталья", "Суворова", "Геленджик", "Гуру")
membership_5 = GuestList("Илья", "Сахно", "Биробиджан", "Падаван")
membership_6 = GuestList("Мария", "Стрельцова", "Новосибирск", "Мастер")

print(membership_1.guest_to_be_on_party())
print(membership_2.guest_to_be_on_party())
print(membership_3.guest_to_be_on_party())
print(membership_4.guest_to_be_on_party())
print(membership_5.guest_to_be_on_party())
print(membership_6.guest_to_be_on_party())
