GET_ALL_MEMBERS = """
SELECT username, first_name, last_name, password, email, created_on, last_login
FROM members
"""

GET_MEMBER_BY_USERNAME = f"""
{GET_ALL_MEMBERS}
WHERE username = :username
"""

INSERT_MEMBER = f"""
INSERT INTO members (username, password, first_name, last_name, email, last_login)
VALUES (:username, :password, :first_name, :last_name, :email, now())
RETURNING *
"""

UPDATE_MEMBER = f"""
UPDATE members
SET username = :new_username,
    first_name = :first_name,
    last_name = :last_name,
    email = :email
WHERE username = :old_username
RETURNING *
"""

#############################################
#                                           #
#                  GENRES                   #
#                                           #
#############################################

GET_ALL_GENRES = """
SELECT name
FROM genres
"""

INSERT_GENRE = """
INSERT INTO genres (name) VALUES (:name)
"""

#############################################
#                                           #
#                  BOOKS                    #
#                                           #
#############################################

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

#############################################
#                                           #
#                  CLUBS                    #
#                                           #
#############################################

GET_ALL_CLUBS = """
SELECT id, name, slug
FROM clubs
"""

GET_CLUB_BY_SLUG = """
SELECT id, name, slug
FROM clubs
WHERE slug = :slug
"""

GET_CLUB_BY_ID = """
SELECT id, name, slug
FROM clubs
WHERE id = :id
"""

INSERT_CLUB = """
INSERT INTO clubs (name, slug)
VALUES (:name, :slug)
"""
