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

create table if not exists genres (
    id serial primary key,
    name varchar(63) unique not null
);

create table if not exists books (
    id serial primary key,
    title varchar(127) not null,
    author varchar(127) not null,
    genre_id int not null,
    slug varchar(255) unique not null,
    foreign key (genre_id) references genres (id)
);

create table if not exists completions (
    id serial primary key,
    member_id int not null,
    book_choice_id int not null,
    score numeric not null,
    comment varchar(128),
    completed_on timestamp default now(),
    foreign key (member_id) references members (id),
    foreign key (book_choice_id) references book_choices (id),
    check (score between 0 and 10)
);

create table if not exists clubs (
    id serial primary key,
    name varchar(63) unique not null,
    slug varchar(255) unique not null
);

create table if not exists club_members (
    id serial primary key,
    club_id int not null,
    member_id int not null,
    foreign key (club_id) references clubs (id),
    foreign key (member_id) references members (id),
    unique (club_id, member_id)
);

create table if not exists book_choices (
    id serial primary key,
    month int not null,
    year int not null,
    book_id int not null,
    member_id int not null,
    club_id int not null,
    foreign key (book_id) references books (id),
    foreign key (member_id) references members (id),
    foreign key (club_id) references clubs (id),
    unique (month, year, club_id),
    unique (club_id, book_id),
    check (month between 1 and 12),
    check (year between 2021 and 9999)
);

create table if not exists registration_tokens (
    id serial primary key,
    token varchar (256) unique not null,
    issuer int not null,
    club int not null,
    expires_on timestamp not null,
    foreign key (issuer) references members (id)
    foreign key (club) references clubs (id),
);
