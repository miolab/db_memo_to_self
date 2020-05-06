# asdf による PostgreSQL セットアップ

- `asdf` バージョン

  ```
  $ asdf --version
  v0.7.8- ...
  ```

- GitHub : [asdf PostgreSQL](https://github.com/smashedtoatoms/asdf-postgres)

---

## Setup

```
$ asdf plugin-add postgres

$ asdf list all postgres

$ asdf install postgres x.x

$ asdf global postgres x.x
```

- uninstall

  `$ asdf plugin-remove postgres`

### Confirmation (version check)

```
$ psql --version
psql (PostgreSQL) 12.2
```

---

# Usage

## Server start & stop

- サーバー起動

  ```
  $ pg_ctl start
  ```

  - サーバー停止

    ```
    $ pg_ctl stop
    ```

- サーバー起動状態を確認

  ```
  $ pg_ctl status
  pg_ctl: server is running (PID: 38403)
  /Users/im/.asdf/installs/postgres/12.2/bin/postgres
  ```

  - stop時の結果： `pg_ctl: no server running`

---

## Basic Usage

- __DB 一覧__

  ```
  $ psql -l
                                      List of databases
          Name         |  Owner   | Encoding |   Collate   |    Ctype    | Access privileges 
  ----------------------+----------+----------+-------------+-------------+-------------------
  demo_dev             | postgres | UTF8     | ja_JP.UTF-8 | ja_JP.UTF-8 | 
  init_db_psql         | im       | UTF8     | ja_JP.UTF-8 | ja_JP.UTF-8 | 
  postgres             | im       | UTF8     | ja_JP.UTF-8 | ja_JP.UTF-8 | 
  template0            | im       | UTF8     | ja_JP.UTF-8 | ja_JP.UTF-8 | =c/im            +
                        |          |          |             |             | im=CTc/im
  template1            | im       | UTF8     | ja_JP.UTF-8 | ja_JP.UTF-8 | =c/im            +
                        |          |          |             |             | im=CTc/im
  (5 rows)
  ```

- __DB 新規作成__

  ```
  $ createdb xxxxxxxx
  ```

  - __DB 削除__

    ```
    $ dropdb xxxxxxxx
    ```

- __DB に接続__ `(psql)`

  例： `$ createdb psql_blogapp`

  ```
  $ psql psql_blogapp
  psql (12.2)
  Type "help" for help.

  psql_blogapp=#
  ```

  - __DB 切断__ `(\q)` or `(exit)`

    ```
    psql_blogapp=# \q
    ```

    - `# exit` でも可

  - DB 一覧表示 `(\l)`

    ```
    psql_blogapp=# \l
                                        List of databases
            Name         |  Owner   | Encoding |   Collate   |    Ctype    | Access privileges 
    ----------------------+----------+----------+-------------+-------------+-------------------
    demo_dev             | postgres | UTF8     | ja_JP.UTF-8 | ja_JP.UTF-8 | 
    init_db_psql         | im       | UTF8     | ja_JP.UTF-8 | ja_JP.UTF-8 | 
    postgres             | im       | UTF8     | ja_JP.UTF-8 | ja_JP.UTF-8 | 
    psql_blogapp         | im       | UTF8     | ja_JP.UTF-8 | ja_JP.UTF-8 | 
    template0            | im       | UTF8     | ja_JP.UTF-8 | ja_JP.UTF-8 | =c/im            +
                          |          |          |             |             | im=CTc/im
    template1            | im       | UTF8     | ja_JP.UTF-8 | ja_JP.UTF-8 | =c/im            +
                          |          |          |             |             | im=CTc/im
    (6 rows)
    ```

---

## Table

- __Table 作成__

  ```
  psql_blogapp=# create table posts (
  psql_blogapp(# title varchar(255),
  psql_blogapp(# body text);
  CREATE TABLE
  ```

    - __Table 削除__

      ```
      psql_blogapp=# drop table myposts;
      DROP TABLE
      ```

- __Table 一覧__ `(\dt)`

  ```
  psql_blogapp=# \dt
        List of relations
  Schema | Name  | Type  | Owner 
  --------+-------+-------+-------
  public | posts | table | im
  (1 row)
  ```

- __Table 情報（columnの型など）__ 確認 `(\d)`

  ```
  psql_blogapp-# \d posts
                        Table "public.posts"
  Column |          Type          | Collation | Nullable | Default 
  --------+------------------------+-----------+----------+---------
  title  | character varying(255) |           |          | 
  body   | text                   |           |          | 
  ```

- __Table 名を変更__

  ```
  psql_blogapp=# alter table posts rename to myposts;
  ALTER TABLE
  ```
