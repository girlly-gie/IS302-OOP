# Fernandez,Girlly
class Books:

    def __init__(self, title, author, year):
        self.title_gmf = title
        self.author_gmf = author
        self.year_gmf = year

    def display_book(self):
        print("Title:", self.title_gmf)
        print("Author:", self.author_gmf)
        print("Year:", self.year_gmf)

book1 = Books("Python Programming", "John Smith", "2022")
book1.display_book()