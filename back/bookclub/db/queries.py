GET_ALL_MEMBERS = """
SELECT username, first_name, last_name, password, email, created_on, last_login
FROM members
"""

GET_MEMBER_BY_USERNAME = f"""
{GET_ALL_MEMBERS}
WHERE username = :username
"""
