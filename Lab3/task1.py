class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """Класс с информацией о бумажной книге". """
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self._pages = pages

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if value <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = value

    def __str__(self) -> str:
        return f"{super().__str__()} Количество страниц: {self.pages}"


class AudioBook(Book):
    """Класс с информацией об аудиокниге"""
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._duration = duration

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, value: float) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError("Продолжительность должна быть числом!")
        if value <= 0:
            raise ValueError("Продолжительность должна быть положительным числом!")
        self._duration = value

    def __str__(self) -> str:
        return f"{super().__str__()} Продолжительность: {self.duration} часов"


if __name__ == "__main__":
    book1 = Book(name="Python Programming", author="E G Krylova")
    print(book1)

    paper_book1 = PaperBook(name="Physics", author="A E VASILYEV", pages=150)
    print(paper_book1)

    # Попытка изменить атрибуты name
    # paper_book.name = "New Book"  # Вызовет AttributeError
    paper_book1.pages = 500

    audio_book1 = AudioBook(name="Polyrama podcast", author="D M ANTONYAN", duration=2.5)
    print(audio_book1)
    audio_book1.duration = 10
