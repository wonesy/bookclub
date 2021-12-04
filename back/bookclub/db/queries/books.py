GET_ALL_BOOKS = """
SELECT b.title, b.author, b.slug, g.name as "genre"
FROM books b
INNER JOIN genres g on b.genre_id = g.id
"""

INSERT_BOOK = """
INSERT INTO books (title, author, slug, genre_id)
SELECT :title, :author, :slug, id FROM genres WHERE name = :genre
"""

GET_BOOK_BY_SLUG = """
SELECT b.title, b.author, b.slug, g.name as "genre"
FROM books b
INNER JOIN genres g on b.genre_id = g.id
WHERE b.slug = :slug
"""
