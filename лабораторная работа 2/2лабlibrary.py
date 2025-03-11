class Book:
    def __init__(self, id_: int, name: str, pages: int):
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        return f'Книга "{self.name}" (id={self.id})'

    def __repr__(self) -> str:
        return f"Book(id_={self.id}, name='{self.name}', pages={self.pages})"


class Library:
    def __init__(self, books: list[Book] | None = None):
        self.books: list[Book] = books if books is not None else []

    def get_next_book_id(self) -> int:
        """Возвращает ID для следующей книги."""
        return 1 if not self.books else self.books[-1].id + 1

    def get_index_by_book_id(self, book_id: int) -> int:
        """Возвращает индекс книги по её ID."""
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    # Тестирование
    book1 = Book(id_=1, name="Книга 1", pages=200)
    book2 = Book(id_=2, name="Книга 2", pages=300)
    
    library = Library(books=[book1, book2])
    empty_library = Library()

    print(f"Следующий ID: {library.get_next_book_id()}")  # 3
    print(f"Индекс книги 2: {library.get_index_by_book_id(2)}")  # 1

    try:
        library.get_index_by_book_id(99)  # Вызовет ошибку
    except ValueError as e:
        print(e)  # "Книги с запрашиваемым id не существует"

    print(f"ID для пустой библиотеки: {empty_library.get_next_book_id()}")  # 1