# Usage

## Server start & login

- サーバー起動

  ```
  $ mysql.server start
  ```

  - サーバー停止

    ```
    $ mysql.server stop

    // 強制停止
    $ mysql.server stop -f
    ```

- ログイン

  ```
  mysql -uroot
  ```

  - ログアウト

    ```
    mysql> exit
    ```

---

## Basic Usage

- ログインユーザー情報

  ```
  mysql> select user();
  +----------------+
  | user()         |
  +----------------+
  | root@localhost |
  +----------------+
  1 row in set (0.00 sec)
  ```

- ユーザーの __一覧情報__

  ```
  mysql> select user, host from mysql.user;
  +---------------+-----------+
  | user          | host      |
  +---------------+-----------+
  | mysql.session | localhost |
  | mysql.sys     | localhost |
  | root          | localhost |
  +---------------+-----------+
  3 rows in set (0.00 sec)
  ```

- DB 一覧

  ```
  mysql> show databases;
  +--------------------+
  | Database           |
  +--------------------+
  | information_schema |
  | mydb_test          |
  | mysql              |
  | performance_schema |
  | sys                |
  +--------------------+
  5 rows in set (0.01 sec)
  ```

- Table 一覧

  ```
  mysql> show tables from mydb_test;
  +---------------------+
  | Tables_in_mydb_test |
  +---------------------+
  | menu                |
  +---------------------+
  1 row in set (0.00 sec)
  ```

- __いま使用中のDB__ を確認

  ```
  mysql> select database();
  +------------+
  | database() |
  +------------+
  | mydb_test  |
  +------------+
  1 row in set (0.00 sec)
  ```

- 接続しているユーザー・DB等もろもろを確認（起動中のスレッド情報表示）

  ```
  mysql> mysql> show processlist;
  +----+------+-----------+-----------+---------+------+----------+------------------+
  | Id | User | Host      | db        | Command | Time | State    | Info             |
  +----+------+-----------+-----------+---------+------+----------+------------------+
  |  4 | root | localhost | mydb_test | Query   |    0 | starting | show processlist |
  +----+------+-----------+-----------+---------+------+----------+------------------+
  1 row in set (0.00 sec)
  ```
---

## CRUD commands

- DB 作成

  ```
  mysql> create database mydb_test;
  Query OK, 1 row affected (0.00 sec)
  ```

  - DB 削除

    `mysql> drop database if exists mock_db;`

    - 存在確定 DB を削除するなら

      `mysql> drop database mock_db;` でも可

- 使用する `DB` を選択/切り替え

  ```
  mysql> use mydb_test
  Database changed
  ```

- `table`作成 & `Column`作成

  ```
  mysql> drop table if exists menu;
  Query OK, 0 rows affected, 1 warning (0.01 sec)

  mysql> create table menu (
      -> id integer primary key auto_increment,
      -> name text,
      -> score real,
      -> stars integer);
  Query OK, 0 rows affected (0.01 sec)
  ```

---

### Create

- `row`を追加

  ```
  mysql> insert into menu values (null, "math", 85.5, 10);
  Query OK, 1 row affected (0.00 sec)

  mysql> insert into menu values (null, "english", 88.1, 8);
  Query OK, 1 row affected (0.00 sec)

  mysql> insert into menu values (null, "physics", 90.5, 8);
  Query OK, 1 row affected (0.00 sec)

  mysql> select * from menu
      -> ;
  +----+---------+-------+-------+
  | id | name    | score | stars |
  +----+---------+-------+-------+
  |  1 | math    |  85.5 |    10 |
  |  2 | english |  88.1 |     8 |
  |  3 | physics |  90.5 |     8 |
  +----+---------+-------+-------+
  3 rows in set (0.00 sec)

  ```

---

### Update

- `row`のデータ更新

  ```
  mysql> update menu set score=120.2 where name="math";
  Query OK, 1 row affected (0.00 sec)
  Rows matched: 1  Changed: 1  Warnings: 0

  mysql> select * from menu;
  +----+---------+-------+-------+
  | id | name    | score | stars |
  +----+---------+-------+-------+
  |  1 | math    | 120.2 |    10 |
  |  2 | english |  88.1 |     8 |
  |  3 | physics |  90.5 |     8 |
  +----+---------+-------+-------+
  3 rows in set (0.00 sec)
  ```

---
### Delete

- `row`のデータ削除

  ```
  // preparing
  mysql> insert into menu values (null, "japanese", 77.7, 5);
  Query OK, 1 row affected (0.00 sec)

  mysql> select * from menu;
  +----+----------+-------+-------+
  | id | name     | score | stars |
  +----+----------+-------+-------+
  |  1 | math     | 120.2 |    10 |
  |  2 | english  |  88.1 |     8 |
  |  3 | physics  |  90.5 |     8 |
  |  4 | japanese |  77.7 |     5 |
  +----+----------+-------+-------+
  4 rows in set (0.00 sec)


  // DELETE
  mysql> delete from menu where name="japanese";
  Query OK, 1 row affected (0.00 sec)

  mysql> select * from menu;
  +----+---------+-------+-------+
  | id | name    | score | stars |
  +----+---------+-------+-------+
  |  1 | math    | 120.2 |    10 |
  |  2 | english |  88.1 |     8 |
  |  3 | physics |  90.5 |     8 |
  +----+---------+-------+-------+
  3 rows in set (0.00 sec)


  // preparing
  mysql> insert into menu values (null, "japanese", 77.7, 5);
  Query OK, 1 row affected (0.00 sec)

  mysql> select * from menu;
  +----+----------+-------+-------+
  | id | name     | score | stars |
  +----+----------+-------+-------+
  |  1 | math     | 120.2 |    10 |
  |  2 | english  |  88.1 |     8 |
  |  3 | physics  |  90.5 |     8 |
  |  5 | japanese |  77.7 |     5 |
  +----+----------+-------+-------+
  4 rows in set (0.00 sec)


  // DELETE
  mysql> delete from menu where stars=5;
  Query OK, 1 row affected (0.00 sec)

  mysql> select * from menu;
  +----+---------+-------+-------+
  | id | name    | score | stars |
  +----+---------+-------+-------+
  |  1 | math    | 120.2 |    10 |
  |  2 | english |  88.1 |     8 |
  |  3 | physics |  90.5 |     8 |
  +----+---------+-------+-------+
  3 rows in set (0.00 sec)
  ```

---

### Read

### データ抽出いろいろ

- column指定

  ```
  mysql> select * from menu;
  +----+---------+-------+-------+
  | id | name    | score | stars |
  +----+---------+-------+-------+
  |  1 | math    | 120.2 |    10 |
  |  2 | english |  88.1 |     8 |
  |  3 | physics |  90.5 |     8 |
  +----+---------+-------+-------+
  3 rows in set (0.00 sec)


  mysql> select id, name
      -> from menu;
  +----+---------+
  | id | name    |
  +----+---------+
  |  1 | math    |
  |  2 | english |
  |  3 | physics |
  +----+---------+
  3 rows in set (0.00 sec)

  ```

- `AND`, `OR`, `NOT` 検索

  - AND

    ```
    mysql> select * from menu
        -> where id >= 2 and score < 90.5;
    +----+---------+-------+-------+
    | id | name    | score | stars |
    +----+---------+-------+-------+
    |  2 | english |  88.1 |     8 |
    +----+---------+-------+-------+
    1 row in set (0.04 sec)
    ```

  - OR

    ```
    mysql> select * from menu
        -> where id >= 2 or score < 95;
    +----+---------+-------+-------+
    | id | name    | score | stars |
    +----+---------+-------+-------+
    |  2 | english |  88.1 |     8 |
    |  3 | physics |  90.5 |     8 |
    +----+---------+-------+-------+
    2 rows in set (0.00 sec)
    ```

  - NOT

    ```
    mysql> select * from menu
        -> where not id = 3;
    +----+---------+-------+-------+
    | id | name    | score | stars |
    +----+---------+-------+-------+
    |  1 | math    | 120.2 |    10 |
    |  2 | english |  88.1 |     8 |
    +----+---------+-------+-------+
    2 rows in set (0.01 sec)


    mysql> select * from menu
        -> where id <> 3;
    +----+---------+-------+-------+
    | id | name    | score | stars |
    +----+---------+-------+-------+
    |  1 | math    | 120.2 |    10 |
    |  2 | english |  88.1 |     8 |
    +----+---------+-------+-------+
    2 rows in set (0.00 sec)


    mysql> select * from menu
        -> where id != 3;
    +----+---------+-------+-------+
    | id | name    | score | stars |
    +----+---------+-------+-------+
    |  1 | math    | 120.2 |    10 |
    |  2 | english |  88.1 |     8 |
    +----+---------+-------+-------+
    2 rows in set (0.00 sec)
    ```

- `BETWEEN` （○以上○以下）

  ```
  mysql> select * from menu
      -> where stars between 5 and 8;
  +----+---------+-------+-------+
  | id | name    | score | stars |
  +----+---------+-------+-------+
  |  2 | english |  88.1 |     8 |
  |  3 | physics |  90.5 |     8 |
  +----+---------+-------+-------+
  2 rows in set (0.00 sec)
  ```

- `IN` / `NOT IN`

  ```
  // IN
  mysql> select * from menu 
    -> where stars in(9, 10, 11);
  +----+------+-------+-------+
  | id | name | score | stars |
  +----+------+-------+-------+
  |  1 | math | 120.2 |    10 |
  +----+------+-------+-------+
  1 row in set (0.00 sec)


  // NOT IN
  mysql> mysql> select * from menu
      -> where stars not in(9, 10, 11);
  +----+---------+-------+-------+
  | id | name    | score | stars |
  +----+---------+-------+-------+
  |  2 | english |  88.1 |     8 |
  |  3 | physics |  90.5 |     8 |
  +----+---------+-------+-------+
  2 rows in set (0.00 sec)
  ```

- `IS NULL` / `ISNULL`

  ```
  // preparing
  mysql> insert into menu values(
      -> null,
      -> "some subject",
      -> 99.9,
      -> null);
  Query OK, 1 row affected (0.00 sec)

  mysql> select * from menu;
  +----+--------------+-------+-------+
  | id | name         | score | stars |
  +----+--------------+-------+-------+
  |  1 | math         | 120.2 |    10 |
  |  2 | english      |  88.1 |     8 |
  |  3 | physics      |  90.5 |     8 |
  |  6 | some subject |  99.9 |  NULL |
  +----+--------------+-------+-------+
  4 rows in set (0.01 sec)


  // IS NULL / ISNULL
  mysql>  select * from menu
      -> where stars is null;
  +----+--------------+-------+-------+
  | id | name         | score | stars |
  +----+--------------+-------+-------+
  |  6 | some subject |  99.9 |  NULL |
  +----+--------------+-------+-------+
  1 row in set (0.00 sec)

  mysql> select * from menu
      -> where isnull(stars);
  +----+--------------+-------+-------+
  | id | name         | score | stars |
  +----+--------------+-------+-------+
  |  6 | some subject |  99.9 |  NULL |
  +----+--------------+-------+-------+
  1 row in set (0.01 sec)


  // IS NOT NULL / NOT ISNULL
  mysql> select * from menu
      -> where stars is not null;
  +----+---------+-------+-------+
  | id | name    | score | stars |
  +----+---------+-------+-------+
  |  1 | math    | 120.2 |    10 |
  |  2 | english |  88.1 |     8 |
  |  3 | physics |  90.5 |     8 |
  +----+---------+-------+-------+
  3 rows in set (0.00 sec)

  mysql> select * from menu
      -> where not isnull(stars);
  +----+---------+-------+-------+
  | id | name    | score | stars |
  +----+---------+-------+-------+
  |  1 | math    | 120.2 |    10 |
  |  2 | english |  88.1 |     8 |
  |  3 | physics |  90.5 |     8 |
  +----+---------+-------+-------+
  3 rows in set (0.00 sec)


  // delete
  mysql> delete from menu where stars is null;
  Query OK, 1 row affected (0.00 sec)

  mysql> select * from menu;
  +----+---------+-------+-------+
  | id | name    | score | stars |
  +----+---------+-------+-------+
  |  1 | math    | 120.2 |    10 |
  |  2 | english |  88.1 |     8 |
  |  3 | physics |  90.5 |     8 |
  +----+---------+-------+-------+
  3 rows in set (0.00 sec)
  ```

- `ORDER BY` (`ASC` / `DESC`)

  ```
  // 昇順 (デフォルト or ASC)
  mysql> select * from menu
      -> order by score;
  +----+---------+-------+-------+
  | id | name    | score | stars |
  +----+---------+-------+-------+
  |  2 | english |  88.1 |     8 |
  |  3 | physics |  90.5 |     8 |
  |  1 | math    | 120.2 |    10 |
  +----+---------+-------+-------+
  3 rows in set (0.00 sec)

  mysql> select * from menu
      -> order by score asc;
  +----+---------+-------+-------+
  | id | name    | score | stars |
  +----+---------+-------+-------+
  |  2 | english |  88.1 |     8 |
  |  3 | physics |  90.5 |     8 |
  |  1 | math    | 120.2 |    10 |
  +----+---------+-------+-------+
  3 rows in set (0.00 sec)


  // 降順 (DESC)
  mysql> select * from menu
      -> order by score desc;
  +----+---------+-------+-------+
  | id | name    | score | stars |
  +----+---------+-------+-------+
  |  1 | math    | 120.2 |    10 |
  |  3 | physics |  90.5 |     8 |
  |  2 | english |  88.1 |     8 |
  +----+---------+-------+-------+
  3 rows in set (0.00 sec)


  // 先頭から2件抽出
  mysql> select * from menu
      -> order by score desc
      -> limit 2;
  +----+---------+-------+-------+
  | id | name    | score | stars |
  +----+---------+-------+-------+
  |  1 | math    | 120.2 |    10 |
  |  3 | physics |  90.5 |     8 |
  +----+---------+-------+-------+
  2 rows in set (0.00 sec)


  // 2件目(=1)から2件抽出
  mysql> select * from menu
      -> order by score desc
      -> limit 1,2;
  +----+---------+-------+-------+
  | id | name    | score | stars |
  +----+---------+-------+-------+
  |  3 | physics |  90.5 |     8 |
  |  2 | english |  88.1 |     8 |
  +----+---------+-------+-------+
  2 rows in set (0.00 sec)
  ```

- `LIKE`

  ```
  mysql> select * from menu
      -> where name like "ma%";
  +----+------+-------+-------+
  | id | name | score | stars |
  +----+------+-------+-------+
  |  1 | math | 120.2 |    10 |
  +----+------+-------+-------+
  1 row in set (0.00 sec)


  mysql> select * from menu
      -> where name like "%i%";
  +----+---------+-------+-------+
  | id | name    | score | stars |
  +----+---------+-------+-------+
  |  2 | english |  88.1 |     8 |
  |  3 | physics |  90.5 |     8 |
  +----+---------+-------+-------+
  2 rows in set (0.00 sec)
  ```

---

## Other commands

- レコード件数をカウント

  ```
  mysql> select count(*) from menu;
  +----------+
  | count(*) |
  +----------+
  |        3 |
  +----------+
  1 row in set (0.01 sec)
  ```

---

## Join

