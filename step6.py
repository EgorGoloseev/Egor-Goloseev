class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display_info(self):
        print(f"Книга: {self.title}\nАвтор: {self.author}\nГод издания: {self.year}")

book1 = Book("Как не отчислится со 2 курса ", "Голосеев Егор", 2024)
book2 = Book("2024", "sharkys", 2024)

book1.display_info()
print()
book2.display_info()
