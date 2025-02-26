class Library:
    def __init__(self, books: list = None):
        self.books: list = books if books is not None else []

    def get_next_book_id(self) -> int:
        if not self.books:
            return 1
        else:
            return self.books[-1].id + 1

    def get_index_by_book_id(self, book_id: int) -> int:
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")

if __name__ == '__main__':
    class Book:
        def __init__(self, id_: int, name: str, pages: int):
            self.id = id_
            self.name = name
            self.pages = pages

        def __str__(self) -> str:
            return f'Книга "{self.name}" (id={self.id})'

        def __repr__(self) -> str:
            return f"Book(id_={self.id}, name='{self.name}', pages={self.pages})"

    book1 = Book(id_=1, name="Книга 1", pages=200)
    book2 = Book(id_=2, name="Книга 2", pages=300)
    library = Library(books=[book1, book2])

    next_id = library.get_next_book_id()
    print(f"Следующий ID книги: {next_id}")

    try:
        index = library.get_index_by_book_id(2)
        print(f"Индекс книги с id=2: {index}")
        index = library.get_index_by_book_id(3)
    except ValueError as e:
        print(e)

    empty_library = Library()
    next_id_empty = empty_library.get_next_book_id()
    print(f"Следующий ID книги в пустой библиотеке: {next_id_empty}")