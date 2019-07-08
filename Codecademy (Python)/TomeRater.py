class TomeRater():
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        return Book()

    def create_novel(self, title, author, isbn):
        return Fiction()

    def create_non_fiction(self, title, subject, level, isbn):
        return Non_Fiction()

    def add_book_to_user(self, book, email, rating=None):
        if email not in self.users:
            return "No user with email " + email + " !"
        else:
            user = self.users[email]
            user.read_book(book, rating)
            book.add.rating(rating)
            if book not in self.books:
                self.books[book] = 1
            else:
                self.books[book] += 1

    def add_user(self, name, email, user_books=None):
        new_user = User(name, email)
        if user_books != None:
            for book in user_books:
                add_book_to_user(book, email)

    def print_catalog(self):
        for book in self.books.keys():
            print(book)

    def print_users(self):
        for users in self.users.values():
            print(users)

    def most_read_book(self):
        most_read_book = {}
        for book, value in self.books.items():
            if len(value) == max(self.books.values()):
                most_read_book.update({book: len(value)}) 


    def highest_rated_book(self):
        highest_rated_book = []
        for book, value in self.books.keys():
            if value == max(book.get_average_rating()):
                highest_rated_book += book
        return highest_rated_book            

    def most_positive_user(self):
        most_positive_user = []
        for user in self.users.values():
            if user == max(user.get_average_rating()):
                most_positive_user += user
        return most_positive_user


class User():
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.get_email()

    def change_email(self, address):
        pass

    def __repr__(self):
        return "Username:  " + self.name + ", email:  " + self.email + ", books read:  " + str(len(self.books))

    def __eq__(self, user):
        if self.name == user.name and self.email == user.email:
            return True
        else:
            return False

    def read_book(self, book, rating=None):
        self.books[book] = rating

    def get_average_rating(self):
        total_ratings = 0
        for rating in self.books.values():
            total_ratings += rating
        return total_ratings / len(self.books)


class Book():
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, isbn):
        self.isbn = isbn
        return print(book.title + " ISBN number has been updated to " + str(book.isbn))

    def add_rating(self, rating):
        if rating >= 0 and rating <= 4:
            return self.ratings.append(rating)
        else:
            return "Invalid Rating"

    def __eq__(self, book):
        if self.title == book.title and self.isbn == book.isbn:
            return True
        else:
            return False
        
    def get_average_rating(self):
        total_ratings = 0
        for rating in self.ratings:
            total_ratings += rating
        return "The average rating of " + self.title + " is:  " + str(total_ratings / len(self.ratings))

    def __hash__(self):
        return hash((self.title, self.isbn))

class Fiction(Book):
    def __init__(self, title, isbn, author):
        self.title = title
        self.isbn = isbn
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return self.title + " by " + self.author

class Non_Fiction(Book):
    def __init__(self, title, isbn, subject, level):
        self.title = title
        self.isbn = isbn
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return self.title + ", a " + self.level + " manual on " + self.subject

    

kgrove = User("kgrove", "kwg@gmail.com")
book = Book("The Jackal", 69)
book1 = Book("A", 9)
kgrove.read_book(book, 3)
kgrove.read_book(book1, 2)

print(kgrove.get_average_rating())

book.add_rating(3)
book.add_rating(2)
book.add_rating(3)

print(book.get_average_rating())

print(kgrove.books)

# alice = Fiction("Alice in Wonderland", 0,"Lewis Carroll")
# print(alice)



#book.get_title()
#print(book.title, book.isbn)

