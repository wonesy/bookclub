GET_ALL_GENRES = """
SELECT name
FROM genres
"""

INSERT_GENRE = """
INSERT INTO genres (name) VALUES (:name)
"""
