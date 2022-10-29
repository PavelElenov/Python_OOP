from project.user import User


class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {}
        self.rented_books = {}

    def get_book(self, author, book_name, days_to_return, user: User):
        if author in self.books_available and book_name in self.books_available[author]:
            self.books_available[author].remove(book_name)
            user.books.append(book_name)
            # if user.username not in self.rented_books:
            #     self.rented_books[user.username] = {}
            self.rented_books[user.username] = {book_name: days_to_return}
            return f"{book_name} successfully rented for the next {days_to_return} days!"
        for username in self.rented_books.values():
            if book_name in username:
                return f'The book "{book_name}" is already rented and will be available in ' \
                           f'{username[book_name]} days!'

    def return_book(self, author, book_name, user: User):
        if book_name in user.books:
            user.books.remove(book_name)
            self.books_available[author].append(book_name)
            self.rented_books[user.username].pop(book_name)
        else:
            return f"{user.username} doesn't have this book in his/her records!"
