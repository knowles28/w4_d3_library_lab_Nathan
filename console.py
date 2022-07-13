import pdb
from models.author import Author
from models.book import Book

import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

author1 = Author("Bill", "Shakespeare")
author_repository.save(author1)

author2 = Author("JK", "Rowling")
author_repository.save(author2)

book1 = Book("Hamlet", "150", author1)
book_repository.save(book1)

book2 = Book("Harry Potter 1", "300", author2)
book_repository.save(book2)

# author_repository.select_all()

# book_repository.select_all()

pdb.set_trace()