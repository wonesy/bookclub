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
