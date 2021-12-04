GET_REGISTRATION_TOKENS_BY_ISSUER = """
SELECT r.token, r.issuer
FROM registration_tokens r
INNER JOIN members m on r.issuer = m.id
WHERE issuer = :issuer
"""

GET_REGISTRATION_TOKEN = """
SELECT r.token, r.issuer
FROM registration_tokens r
WHERE r.token = :token
"""

INSERT_REGISTRATION_TOKEN = """
INSERT INTO registration_tokens (token, issuer)
SELECT :token, m.id
FROM members m
WHERE m.username = :username
"""

DELETE_TOKEN = """
DELETE FROM registration_tokens
WHERE token = :token
"""
