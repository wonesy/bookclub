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
WHERE id = :club_id
"""

INSERT_CLUB = """
INSERT INTO clubs (name, slug)
VALUES (:name, :slug)
"""

GET_CLUBS_BY_USERNAME = """
SELECT c.id, c.name, c.slug
FROM clubs c
INNER JOIN club_members cm on cm.club_id=c.id
INNER JOIN members m on m.id=cm.member_id
WHERE m.username = :username
"""


GET_CLUB_MEMBERS_BY_CLUB_ID = """
select m.username, m.first_name, m.last_name
from members m
inner join club_members c on m.id=c.member_id
where c.club_id = :club_id
"""
