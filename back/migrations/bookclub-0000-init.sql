--
-- file: back/migrations/bookclub-0000-init.sql
--

create table if not exists members (
    id serial primary key,
    username varchar(63) unique not null,
    first_name varchar(63),
    last_name varchar(127),
    password varchar(255) not null,
    email varchar(255),
    created_on timestamp default now(),
    last_login timestamp
);

create table if not exist genres (
    id serial primary key,
    name varchar(63) unique not null
)

create table if not exists books (
    id serial primary key,
    title varchar(127),
    author varchar(127),
    genre_id int not null,
    foreign key (genre_id) references genre (id)
)

create table if not exists completions (
    id serial primary key,
    member_id int not null,
    book_id int not null,
    score numeric not null,
    completed_on timestamp default now(),
    foreign key (member_id) references members (id),
    foreign key (book_id) references books (id),
    check (score between 0 and 10)
)
