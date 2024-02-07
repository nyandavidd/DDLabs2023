# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class Animal:
    def __init__(self, name: str, height: float, weight: float):
        """
        Создание объекта Животное

        :param name: Имя
        :param height: Рост животного
        :param weight: Вес животного

        Примеры:
        >>> pet = Animal('Vinnie the Pooh', 103, 180.5)
        """
        if type(name) != str:
            raise TypeError('Name of animal must be a str')
        self.name = name

        if type(height) not in (int, float):
            raise TypeError('Height of animal must be a number')
        if height <= 0:
            raise ValueError('Height must be positive number')
        self.height = height

        if type(weight) not in (int, float):
            raise TypeError('Weight of animal must be a number')
        if weight <= 0:
            raise ValueError('Weight must be positive number')
        self.weight = weight

    def eat(self, food: str) -> str:
        """
        Функция для представления приема пищи

        :param food: Пища, которую ест животное

        :return: Сообщение о приеме пищи

        Примеры:
        >>> pet = Animal('Sharik', 70.5, 70.4 )
        >>> pet.eat('Fish')
        """
        ...

    def sleep(self, hours: int) -> str:
        """
        Функция для представления сна

        :param hours: Количество часов сна

        :return: Сообщение о сне

        Примеры:
        >>> pet = Animal('Gav', 50, 15.8)
        >>> pet.sleep(6)
        """
        ...


class TV:
    def __init__(self, brand: str, screen_size: float, is_smart: bool):
        """
        Создание объекта Телевизор

        :param brand: Марка телевизора
        :param screen_size: Размер экрана в дюймах
        :param is_smart: Флаг, указывающий, является ли телевизор умным

        Примеры:
        >>> tv = TV('Samsung', 24, True)
        """
        if not isinstance(brand, str):
            raise TypeError('Марка телевизора должна быть строкой')
        self.brand = brand

        if not isinstance(screen_size, (int, float)):
            raise TypeError('Размер экрана должен быть числом')
        if screen_size <= 0:
            raise ValueError('Размер экрана должен быть положительным числом')
        self.screen_size = screen_size

        if not isinstance(is_smart, bool):
            raise TypeError('Флаг "is_smart" должен быть типа bool')
        self.is_smart = is_smart

    def turn(self, turn_to: str) -> str:
        """
        Включение или выключение телевизора.

        :param turn_to: выбор включения или выключения телевизора.

        :return: Сообщение о включении

        Примеры:
        >>> tv = TV("LG", 42, True)
        >>> tv.turn('on')
        """
        if turn_to not in ('on', 'off'):
            raise TypeError('Turn position can be on or off')
        ...

    def change_channel(self, channel: int) -> None:
        """
        Смена канала на телевизоре.

        :param channel: Номер канала

        Примеры:
        >>> tv = TV("Panasonic", 49, False)
        >>> tv.change_channel(7)
        """
        ...


class Car:
    def __init__(self, model: str, year: int, num: str, fuelcap: float):
        """
        Создание объекта Автомобиль

        :param model: Модель автомобиля
        :param year: Год выпуска автомобиля
        :param num: Номер автомобиля
        :param fuelcap: Запас топлива в автомобиле

        Примеры:
        >>> car1 = Car('Bugatti Solaris', 1964, 'а124аа39', 40.5)
        """
        if type(model) != str:
            raise TypeError('Model of car must be a str')
        self.model = model

        if type(year) != int:
            raise TypeError('Year of car must be an int')
        self.year = year

        if type(num) != str:
            raise TypeError('Num of car must be str')
        self.num = num

        if type(fuelcap) not in (int, float):
            raise TypeError('Fuelcap must be a number')
        if fuelcap < 0:
            raise ValueError('Fuelcap must be positive number')
        self.fuelcap = float(fuelcap)

    def beep(self) -> str:
        """
        Звуковой сигнал машины.

        :return: Сообщение о звуковом сигнале машины

        Примеры:
        >>> car1 = Car('Bugatti Solaris', 1964, 'а124аа39', 40.5)
        >>> car1.beep()
        """
        ...

    def start(self) -> str:
        """
        Включение двигателя автомобиля.

        :return: Сообщение о включенном двигателе

        Примеры:
        >>> car1 = Car('Bugatti Solaris', 1964, 'а124аа39', 40.5)
        >>> car1.start()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
