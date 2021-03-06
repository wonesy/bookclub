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

GET_BOOK_CHOICES_BY_CLUB_ID = """
SELECT b.title, b.author, g.name as "genre", b.slug, m.username, bc.month, bc.year
FROM book_choices bc
INNER JOIN books b on b.id=bc.book_id
INNER JOIN members m on m.id=bc.member_id
INNER JOIN genres g on b.genre_id=g.id
WHERE bc.club_id = :club_id
ORDER BY bc.year DESC, bc.month DESC
"""
