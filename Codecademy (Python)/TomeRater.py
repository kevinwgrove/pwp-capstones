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
        existing_user = email
        try:
            self.users[existing_user]
            return "This user already exists."
        except KeyError:
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

    def unique_isbn(self):
        isbns = []
        for book in self.books.keys():
            isbn = book.isbn
            if isbn not in isbns:
                isbns.append(isbn)
            else:
                return print("That ISBN number is already assigned.")

    def most_read_book(self):
        most_read_book = {}
        for book, value in self.books.items():
            if value == max(self.books.values()):
                most_read_book.update({book: value}) 

    def highest_rated_book(self):
        highest_rated_book = []
        max_value = 0
        for book in self.books.keys():
            if max_value < book.get_average_rating():
                max_value = book.get_average_rating()
                highest_rated_book = [book]
            elif max_value == book.get_average_rating():
                highest_rated_book.append(book)
        return highest_rated_book            

    def most_positive_user(self):
        highest_rated_user = []
        max_value = 0
        for user in self.users.values():
            if max_value < user.get_average_rating():
                max_value = user.get_average_rating()
                highest_rated_user = [user]
            elif max_value == user.get_average_rating():
                highest_rated_user.append(user)
        return highest_rated_user
    

class User():
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.get_email()

    def change_email(self, new_email):
        self.new_email = new_email
        return print(self.name + "'s email has been updated.")

    def valid_email(self):
        check_for = [".com", ".edu", ".org"]
        if '@' not in self.email:
            return False
        for l in check_for:
            if l in self.email:
                return True
        return False

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
