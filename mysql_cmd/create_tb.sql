-- create Table command
CREATE TABLE posts (
  id       serial PRIMARY KEY,
  title    varchar(255) NOT NULL,
  body     text CHECK(length(body) >= 2),
  author   varchar(255) DEFAULT "im",
  is_draft boolean DEFAULT true
);