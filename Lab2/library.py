BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book
class Book:
    def __init__(self, id_: int, name: str, pages: int):
        """
        Инициализация объекта книги.

        :param id_: Идентификатор книги
        :param name: Название книги
        :param pages: Количество страниц в книге
        """
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        """
        Возвращает строку формата: Книга "название_книги".

        :return: Описание книги в виде строки
        """
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        """
        Возвращает валидную строку Python для инициализации экземпляра.

        :return: Строка для инициализации экземпляра
        """
        return f'Book(id_={self.id}, name={repr(self.name)}, pages={self.pages})'


# TODO написать класс Library
class Library:
    def __init__(self, books=[]):
        """
        Создание объекта Библиотека

        :param books: Список книг (по умолчанию пустой список)
        """
        self.books = books

    def get_next_book_id(self) -> int:
        """
        Возврат идентификатора для добавления новой книги в библиотеку.

        :return: Идентификатор для новой книги
        """
        if not self.books:
            return 1
        return self.books[-1].id + 1

    def get_index_by_book_id(self, book_id: int) -> int:
        """
        Возврат индекса книги в списке по её идентификатору.

        :param book_id: Идентификатор книги
        :return: Индекс книги в списке
        :raise ValueError: Если книги с указанным id не существует
        """
        for idx, book in enumerate(self.books):
            if book.id == book_id:
                return idx
        raise ValueError(f"Книги с запрашиваемым id = {book_id} не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
