-- create Table command
CREATE TABLE posts (
  id       serial PRIMARY KEY,
  title    varchar(255) NOT NULL,
  body     text CHECK(length(body) > 2),
  is_draft boolean DEFAULT true,
  posted   timestamp DEFAULT statement_timestamp()
);

/* Results

psql_blogapp=# \d posts
                                       Table "public.posts"
  Column  |            Type             | Collation | Nullable |              Default              
----------+-----------------------------+-----------+----------+-----------------------------------
 id       | integer                     |           | not null | nextval('posts_id_seq'::regclass)
 title    | character varying(255)      |           | not null | 
 body     | text                        |           |          | 
 is_draft | boolean                     |           |          | true
 posted   | timestamp without time zone |           |          | statement_timestamp()
Indexes:
    "posts_pkey" PRIMARY KEY, btree (id)
Check constraints:
    "posts_body_check" CHECK (length(body) > 2)
*/
