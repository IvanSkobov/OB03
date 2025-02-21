class Author():
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality

class Book():
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_info_book(self):
        print(f"Название книги: {self.title}, автор: {self.author.name}")

author = Author("Лев Толстой", "Русский")
book = Book("Война и мир", author)


book.get_info_book()

        