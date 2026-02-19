class IndustrialFurnace:
    def __init__(self, power, temperature):
        # Приватные атрибуты
        self.__power = power
        self.__temperature = temperature
        self.__brand = "ПромПечь"

    @property
    def power(self):
        return self.__power

    @power.setter
    def power(self, value):
        if value <= 0:
            raise ValueError("Мощность должна быть больше 0!")
        self.__power = value

    @property
    def temperature(self):
        return self.__temperature

    @temperature.setter
    def temperature(self, value):
        if not (0 <= value <= 2000):
            raise ValueError("Температура вне диапазона (0-2000)!")
        self.__temperature = value

    @property
    def brand(self):
        return self.__brand


    @property
    def energy_consumption(self):
        return self.__power * 1


furnace = IndustrialFurnace(10, 500)
print(f"Мощность: {furnace.power}, Потребление: {furnace.energy_consumption} Название:{"Промпечь"}")

try:
    furnace.power = -10
except ValueError as e:
    print(f"Ошибка: {e}")

try:
    furnace.temperature = 5000
except ValueError as e:
    print(f"Ошибка: {e}")
