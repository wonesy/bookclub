insert into members (id, username, first_name, last_name, password, email)
values (1, 'wonesy', 'Cameron', 'Jones', '$2b$12$hO62n6U146wVqOeb.0oRXum0NlJCkhCLaUkVhdsk9eGZEwNa6lZzS', 'camandrewjones@gmail.com');

insert into genres (id, name) values (1, 'fantasy');

insert into books (title, author, genre_id, slug)
values ('The Name of the Wind', 'Patrick Rothfuss', 1, '5091-patrick-rothfuss-the-name-of-the-wind');

insert into clubs (id, name, slug)
values (1, 'Citizens of Satan\''s Butthole', '0000-citizens-of-satans-butthole');

insert into club_members(club_id, member_id) values(1, 1);
