from project.user import User

dict = {}
user = User(1, 'Pavel', )
book_name = 'hello'
dict[user.username] = {book_name: 17}
print(dict)