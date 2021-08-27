class Client:
    def __init__(self, name, sum):
        self.name = name
        self.sum = sum
    def get_client_balance(self):
        return 'Клиент "{0}". Баланс: {1} руб.'.format(self.name, self.sum)

new_client_1 = Client("Иван Петров", 50)
new_client_2 = Client("Пётр Сидоров", 500)
new_client_3 = Client("Сидор Иванов", 5000)

print(new_client_1.get_client_balance())
print(new_client_2.get_client_balance())
print(new_client_3.get_client_balance())