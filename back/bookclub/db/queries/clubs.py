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
