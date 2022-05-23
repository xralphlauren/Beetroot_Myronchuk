class Author:
    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.book = []

    def __repr__(self):
        return f'Автор {self.name} из {self.country} {self.year} года рождения'


class Book:
    def __init__(self, name, year, author):
        self.name = name  # str
        self.year = year  # int
        self.author = author  # Объект! класса Author

    def __str__(self):
        return f'"{self.name}" автора {self.author.name} {self.year} года издания'

    def __repr__(self):
        return f'"{self.name}" автора {self.author.name} {self.year} года издания'


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []  # списки объектов Author
        self.authors = []  # списки объектов Book

    def __str__(self):
        s = self.name + ':\n'
        for b in self.books:
            s += f'{b},'
        return s

    def new_book(self, name, year, author):
        b = Book(name, year, author)
        self.books.append(b)
        return b

    def group_by_author(self, author):
        l = []
        for b in self.books:
            if b.author == author:
                l.append(b)
        return l

    def group_by_year(self, year):
        l = []
        for b in self.books:
            if b.year == year:
                l.append(b)
        return l

    def add_author(self, author):
        self.authors.append(author)

    def show_all_books(self):
        return self.books

    def show_all_authors(self):
        return self.authors

a = Author('Роулинг', 'UK', 1965)
b = Author('Кинг', 'USA', 1947)
l = Library('Библиотека Хогвартса')
print(l)
l.new_book('Оно', 2022, b)
print(l)
print(l.show_all_books())
print(l.show_all_books())