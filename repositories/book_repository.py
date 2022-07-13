from db.run_sql import run_sql

from models.author import Author
from models.book import Book
import repositories.author_repository as author_repository

def save(book):
    sql = "INSERT INTO books (title, total_pages, author_id) VALUES (%s, %s, %s) RETURNING *"
    values = [book.title, book.total_pages, book.author.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    book.id = id
    return book

def select_all():
    books = []
    sql = "SELECT * FROM books"
    results = run_sql(sql)
    for row in results:
        author = author_repository.select(row['author_id'])
        book = Book(row['title'], row['total_pages'], author, row['id'])
        books.append(book)
    return books

def select(id):
    book = None
    sql = "SELECT * FROM books WHERE id = %s"
    values = id
    result = run_sql(sql, values)[0]
    
    if result is not None:
        author = author_repository.select(result['author_id'])
        book = Book(result['title'], author, result['total_pages'], result['id'])
    
    return book
    

def delete(id):
    sql = "DELETE  FROM books WHERE id = %s"
    values = [id]
    run_sql(sql, values)
    
    # UPDATE