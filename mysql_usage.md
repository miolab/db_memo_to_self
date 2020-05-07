# MySQL Usage

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

- サーバー起動状態を確認

  ```
  $ mysql.server status
   SUCCESS! MySQL running (29727)
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

- __DB 一覧__

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

- __Table 一覧__

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
  mysql> show processlist;
  +----+------+-----------+-----------+---------+------+----------+------------------+
  | Id | User | Host      | db        | Command | Time | State    | Info             |
  +----+------+-----------+-----------+---------+------+----------+------------------+
  |  4 | root | localhost | mydb_test | Query   |    0 | starting | show processlist |
  +----+------+-----------+-----------+---------+------+----------+------------------+
  1 row in set (0.00 sec)
  ```
---

## CRUD commands

- `DB 作成`

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

- __テーブル削除__ （兼、テーブル作成前の事前準備） `DROP TABLE`

  ```
  mysql> drop table if exists menu;
  Query OK, 0 rows affected, 1 warning (0.01 sec)
  ```

- __テーブル作成__ (`Field` 作成)

  ```
  mysql> create table menu (
      -> id integer primary key auto_increment,
      -> name text,
      -> score real,
      -> stars integer);
  Query OK, 0 rows affected (0.01 sec)
  ```

- __テーブル構造を確認__

  ```
  mysql> desc menu;
  +-------+---------+------+-----+---------+----------------+
  | Field | Type    | Null | Key | Default | Extra          |
  +-------+---------+------+-----+---------+----------------+
  | id    | int(11) | NO   | PRI | NULL    | auto_increment |
  | name  | text    | YES  |     | NULL    |                |
  | score | double  | YES  |     | NULL    |                |
  | stars | int(11) | YES  |     | NULL    |                |
  +-------+---------+------+-----+---------+----------------+
  4 rows in set (0.00 sec)
  ```

  以下コマンドでも同様に可；

  - `describe table_name`

  - `show columns from table_name`

  - `show fields from table_name`

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
  mysql> update menu set score = 120.2
      -> where name = "math";
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


  // 数値加算をする例
  mysql> update menu set score = score + 10
      -> where stars = 8;
  Query OK, 2 rows affected (0.00 sec)
  Rows matched: 2  Changed: 2  Warnings: 0

  mysql> select * from menu;
  +----+---------+-------+-------+
  | id | name    | score | stars |
  +----+---------+-------+-------+
  |  1 | math    | 120.2 |    10 |
  |  2 | english |  98.1 |     8 |
  |  3 | physics | 100.5 |     8 |
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

- `ORDER BY` (昇順 `ASC` / 降順 `DESC`)

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


  // 昇順と降順を組み合わせ（例：starsグループを昇順にしつつ、scoreは降順にして抽出）
  mysql> select * from menu
      -> order by stars, score desc;
  +----+---------+-------+-------+
  | id | name    | score | stars |
  +----+---------+-------+-------+
  |  3 | physics |  90.5 |     8 |
  |  2 | english |  88.1 |     8 |
  |  1 | math    | 120.2 |    10 |
  +----+---------+-------+-------+
  3 rows in set (0.00 sec)


  // 先頭から2件抽出（limit）
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


  // 上記例で、OFFSET を使う例
  mysql> select * from menu
    -> order by score desc
    -> limit 2 offset 1;
  +----+---------+-------+-------+
  | id | name    | score | stars |
  +----+---------+-------+-------+
  |  3 | physics |  90.5 |     8 |
  |  2 | english |  88.1 |     8 |
  +----+---------+-------+-------+
  2 rows in set (0.00 sec)
  ```

- `LIKE`

  - `_` 任意の1文字を代替

    ```
    mysql> select * from menu
        -> where name like 'ma_h';
    +----+------+-------+-------+
    | id | name | score | stars |
    +----+------+-------+-------+
    |  1 | math | 120.2 |    10 |
    +----+------+-------+-------+
    1 row in set (0.00 sec)
    ```

  - `%` 任意の複数文字（1文字以上）を代替

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

- フィールドの文字数カウント `(LENGTH)`

  ```
  mysql> select name, length(name)
      -> from menu;
  +---------+--------------+
  | name    | length(name) |
  +---------+--------------+
  | math    |            4 |
  | english |            7 |
  | physics |            7 |
  +---------+--------------+
  3 rows in set (0.00 sec)
  ```

- フィールドの任意の文字数だけを抽出 `(SUBSTRING)`

  ○文字目から○文字目までを指定して表示

  ```
  mysql> select substring(name, 1, 3) 
      -> from menu;
  +-----------------------+
  | substring(name, 1, 3) |
  +-----------------------+
  | mat                   |
  | eng                   |
  | phy                   |
  +-----------------------+
  3 rows in set (0.00 sec)
  ```

- 複数フィールド名を __連結__ して表示 `(CONCAT)`

  ```
  mysql> select concat(name, '(', stars, ')') from menu;
  +-------------------------------+
  | concat(name, '(', stars, ')') |
  +-------------------------------+
  | math(10)                      |
  | english(8)                    |
  | physics(8)                    |
  +-------------------------------+
  3 rows in set (0.00 sec)
  ```

  - ラベル名を任意の名前にしたい場合は、`AS`を使用

    ```
    mysql> select concat(name, '(', stars, ')')
        -> as name_and_stars
        -> from menu;
    +----------------+
    | name_and_stars |
    +----------------+
    | math(10)       |
    | english(8)     |
    | physics(8)     |
    +----------------+
    3 rows in set (0.00 sec)
    ```

- __重複データを除外して抽出__ 表示 `(SELECT DISTINCT)`

  ```
  mysql> select stars from menu;
  +-------+
  | stars |
  +-------+
  |    10 |
  |     8 |
  |     8 |
  +-------+
  3 rows in set (0.00 sec)

  // DISTINCT で重複値を除外
  mysql> select distinct stars from menu;
  +-------+
  | stars |
  +-------+
  |    10 |
  |     8 |
  +-------+
  2 rows in set (0.00 sec)
  ```

---

## Change fields (ALTER TABLE)

- フィールド名の __変更__

  ```
  mysql> alter table menu
      -> change column score points real;
  Query OK, 0 rows affected (0.02 sec)
  Records: 0  Duplicates: 0  Warnings: 0

  mysql> select * from menu;
  +----+---------+--------+-------+
  | id | name    | points | stars |
  +----+---------+--------+-------+
  |  1 | math    |  120.2 |    10 |
  |  2 | english |   88.1 |     8 |
  |  3 | physics |   90.5 |     8 |
  +----+---------+--------+-------+
  3 rows in set (0.00 sec)
  ```

  - column名だけの変更であっても、型指定は要。

- フィールドを __追加__

  ```
  mysql> alter table menu
      -> add type text after name;
  Query OK, 0 rows affected (0.12 sec)
  Records: 0  Duplicates: 0  Warnings: 0

  mysql> select * from menu;
  +----+---------+------+--------+-------+
  | id | name    | type | points | stars |
  +----+---------+------+--------+-------+
  |  1 | math    | NULL |  120.2 |    10 |
  |  2 | english | NULL |   88.1 |     8 |
  |  3 | physics | NULL |   90.5 |     8 |
  +----+---------+------+--------+-------+
  3 rows in set (0.00 sec)
  ```

  - `AFTER ...` は省略可（末尾へ追加される）

    ```
    mysql> alter table menu
        -> add priority int;
    Query OK, 0 rows affected (0.11 sec)
    Records: 0  Duplicates: 0  Warnings: 0

    mysql> select * from menu;
    +----+---------+------+--------+-------+----------+
    | id | name    | type | points | stars | priority |
    +----+---------+------+--------+-------+----------+
    |  1 | math    | NULL |  120.2 |    10 |     NULL |
    |  2 | english | NULL |   88.1 |     8 |     NULL |
    |  3 | physics | NULL |   90.5 |     8 |     NULL |
    +----+---------+------+--------+-------+----------+
    3 rows in set (0.00 sec)
    ```

- フィールドを __削除__

  ```
  mysql> alter table menu
      -> drop column type,
      -> drop column priority;
  Query OK, 0 rows affected (0.12 sec)
  Records: 0  Duplicates: 0  Warnings: 0

  mysql> select * from menu;
  +----+---------+--------+-------+
  | id | name    | points | stars |
  +----+---------+--------+-------+
  |  1 | math    |  120.2 |    10 |
  |  2 | english |   88.1 |     8 |
  |  3 | physics |   90.5 |     8 |
  +----+---------+--------+-------+
  3 rows in set (0.00 sec)
  ```

- フィールドの __型を変更__

  例："score"フィールドを、`double`型から`float`型へ変更

  ```
  mysql> alter table menu
      -> modify score float;
  ```

  例："name"フィールドを、`varchar`型(15)へ変更

  ```
  mysql> alter table menu
      -> modify name varchar(15);
  ```

---

## Index

- `INDEX` を __追加__

  ```
  mysql> alter table menu add index stars_index(stars);
  Query OK, 0 rows affected (0.03 sec)
  Records: 0  Duplicates: 0  Warnings: 0
  ```

- `INDEX` を __確認__

  （`Key_name`）

  ```
  mysql> show index from menu;
  +-------+------------+-------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
  | Table | Non_unique | Key_name    | Seq_in_index | Column_name | Collation | Cardinality | Sub_part | Packed | Null | Index_type | Comment | Index_comment |
  +-------+------------+-------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
  | menu  |          0 | PRIMARY     |            1 | id          | A         |           3 |     NULL | NULL   |      | BTREE      |         |               |
  | menu  |          1 | stars_index |            1 | stars       | A         |           2 |     NULL | NULL   | YES  | BTREE      |         |               |
  +-------+------------+-------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
  2 rows in set (0.00 sec)
  ```

  - 検証 `(EXPLAIN)`

    ```
    mysql> explain select * from menu where name = 'score';
    +----+-------------+-------+------------+------+---------------+------+---------+------+------+----------+-------------+
    | id | select_type | table | partitions | type | possible_keys | key  | key_len | ref  | rows | filtered | Extra       |
    +----+-------------+-------+------------+------+---------------+------+---------+------+------+----------+-------------+
    |  1 | SIMPLE      | menu  | NULL       | ALL  | NULL          | NULL | NULL    | NULL |    3 |    33.33 | Using where |
    +----+-------------+-------+------------+------+---------------+------+---------+------+------+----------+-------------+
    1 row in set, 1 warning (0.00 sec)
    ```

- `INDEX` を __削除__

  ```
  mysql> alter table menu drop index stars_index;
  Query OK, 0 rows affected (0.01 sec)
  Records: 0  Duplicates: 0  Warnings: 0
  ```

- INDEX のメリット・デメリット

  - 抽出が早くなる

  - レコード新規作成や更新が遅くなる（つどつどIndex を貼るため）

---

## Aggregate commands

- レコードの __件数をカウント__

  ```
  mysql> select count(*) from menu;
  +----------+
  | count(*) |
  +----------+
  |        3 |
  +----------+
  1 row in set (0.01 sec)
  ```

- フィールドの __データ種別の件数__ を集計 `(DISTINCT)`

  ```
  mysql> select distinct stars from menu;
  +-------+
  | stars |
  +-------+
  |    10 |
  |     8 |
  +-------+
  2 rows in set (0.00 sec)
  ```

- フィールドの 合計`(SUM)` / 最大値`(MAX)` / 最小値`(MIN)` / 平均値`(AVG)`

  ```
  mysql> select sum(score) from menu;
  +------------+
  | sum(score) |
  +------------+
  |      298.8 |
  +------------+
  1 row in set (0.01 sec)


  mysql> select max(score) from menu;
  +------------+
  | max(score) |
  +------------+
  |      120.2 |
  +------------+
  1 row in set (0.00 sec)


  mysql> select min(score) from menu;
  +------------+
  | min(score) |
  +------------+
  |       88.1 |
  +------------+
  1 row in set (0.00 sec)


  mysql> select avg(score) from menu;
  +-------------------+
  | avg(score)        |
  +-------------------+
  | 99.60000000000001 |
  +-------------------+
  1 row in set (0.00 sec)
  ```

- フィールドの __データ種別ごと__ の合計値などを集計 `(GROUP BY / HAVING)`

  ```
  mysql> select stars, sum(score)
      -> from menu
      -> group by stars;
  +-------+------------+
  | stars | sum(score) |
  +-------+------------+
  |     8 |      178.6 |
  |    10 |      120.2 |
  +-------+------------+
  2 rows in set (0.00 sec)


  mysql> select stars, sum(score)
      -> from menu
      -> group by stars
      -> having sum(score) > 150;
  +-------+------------+
  | stars | sum(score) |
  +-------+------------+
  |     8 |      178.6 |
  +-------+------------+
  1 row in set (0.00 sec)
  ```

---

## Random generator / selector

- `RAND()`

  `0.0 ~ 1.0` までの乱数を生成する

  ```
  mysql> select rand();
  +---------------------+
  | rand()              |
  +---------------------+
  | 0.47782104320621216 |
  +---------------------+
  1 row in set (0.00 sec)
  ```

- __整数値のランダムデータ__ 生成 （例； `1 ~ 10`）

  ```
  mysql> select ceil( rand() * 10 );
  +---------------------+
  | ceil( rand() * 10 ) |
  +---------------------+
  |                   7 |
  +---------------------+
  1 row in set (0.00 sec)

  mysql> select ceil( rand() * 10 );
  +---------------------+
  | ceil( rand() * 10 ) |
  +---------------------+
  |                  10 |
  +---------------------+
  1 row in set (0.00 sec)
  ```

  - `CEIL` : 小数値の切り上げ

- レコードから無作為に抽出する例

  ```
  // 1件をランダムに抽出 (LIMIT 1)
  mysql> select * from menu order by rand() limit 1;
  +----+---------+-------+-------+
  | id | name    | score | stars |
  +----+---------+-------+-------+
  |  2 | english |  88.1 |     8 |
  +----+---------+-------+-------+
  1 row in set (0.00 sec)

  mysql> select * from menu order by rand() limit 1;
  +----+---------+-------+-------+
  | id | name    | score | stars |
  +----+---------+-------+-------+
  |  3 | physics |  90.5 |     8 |
  +----+---------+-------+-------+
  1 row in set (0.00 sec)


  // 2件をランダム抽出 (LIMIT 2)
  mysql> select * from menu order by rand() limit 2;
  +----+---------+-------+-------+
  | id | name    | score | stars |
  +----+---------+-------+-------+
  |  3 | physics |  90.5 |     8 |
  |  2 | english |  88.1 |     8 |
  +----+---------+-------+-------+
  2 rows in set (0.00 sec)
  ```

---

## Handling multiple Tables

- 複数テーブルの取り扱い

  - (準備)

  ```
  mysql> create database double_table_db;
  Query OK, 1 row affected (0.00 sec)

  mysql> use double_table_db;
  Database changed


  mysql> create table movies (
      -> id integer primary key auto_increment,
      -> title text,
      -> director text,
      -> year integer);
  Query OK, 0 rows affected (0.03 sec)

  mysql> create table boxoffice (
      -> movie_id integer primary key,
      -> length_minutes real,
      -> domestic_sales integer,
      -> international_sales integer);
  Query OK, 0 rows affected (0.02 sec)


  mysql> insert into movies values
    -> (null, "Eva Jo", "Anno", 2007)
    -> (null, "Eva Ha", "Anno", 2009),
    -> (null, "Eva Q", "Anno", 2012),
    -> (null, "Frozen", "Chris", 2013),
    -> (null, "Frozen 2", "Chris", 2019),
    -> (null, "Toy story", "Lasseter", 1995);

  mysql> insert into boxoffice values 
      -> (1, 120.5, 555566666, 777788888),
      -> (2, 130.5, 333344444, 888899999),
      -> (3, 90.1, 123456789, 234567898),
      -> (4, 150.6, 456456456, 789789789),
      -> (5, 99.6, 456456456, 489789789);


  mysql> select * from movies;
  +----+-----------+----------+------+
  | id | title     | director | year |
  +----+-----------+----------+------+
  |  1 | Eva Jo    | Anno     | 2007 |
  |  2 | Eva Ha    | Anno     | 2009 |
  |  3 | Eva Q     | Anno     | 2012 |
  |  4 | Frozen    | Chris    | 2013 |
  |  5 | Frozen 2  | Chris    | 2019 |
  |  6 | Toy story | Lasseter | 1995 |
  +----+-----------+----------+------+
  6 rows in set (0.00 sec)

  mysql> select * from boxoffice;
  +----------+----------------+----------------+---------------------+
  | movie_id | length_minutes | domestic_sales | international_sales |
  +----------+----------------+----------------+---------------------+
  |        1 |          120.5 |      555566666 |           777788888 |
  |        2 |          130.5 |      333344444 |           888899999 |
  |        3 |           90.1 |      123456789 |           234567898 |
  |        4 |          150.6 |      456456456 |           789789789 |
  |        5 |           99.6 |      456456456 |           489789789 |
  +----------+----------------+----------------+---------------------+
  5 rows in set (0.00 sec)
  ```

- 基本

  ```
  mysql> select m.title, b.domestic_sales
      -> from movies m, boxoffice b
      -> where m.id = b.movie_id;
  +----------+----------------+
  | title    | domestic_sales |
  +----------+----------------+
  | Eva Jo   |      555566666 |
  | Eva Ha   |      333344444 |
  | Eva Q    |      123456789 |
  | Frozen   |      456456456 |
  | Frozen 2 |      456456456 |
  +----------+----------------+
  5 rows in set (0.00 sec)


  // AND 等の条件も組み合わせ付与可能
  mysql> select m.title, b.domestic_sales
      -> from movies m, boxoffice b
      -> where m.id = b.movie_id and m.director = "Anno";
  +--------+----------------+
  | title  | domestic_sales |
  +--------+----------------+
  | Eva Jo |      555566666 |
  | Eva Ha |      333344444 |
  | Eva Q  |      123456789 |
  +--------+----------------+
  3 rows in set (0.01 sec)
  ```

- __内部結合__ `(INNER JOIN)`

  ベース側テーブルのうち、条件マッチしていないレコードは除外される。

  ```
  mysql> select * from movies
      -> inner join boxoffice
      -> on id = movie_id;
  +----+----------+----------+------+----------+----------------+----------------+---------------------+
  | id | title    | director | year | movie_id | length_minutes | domestic_sales | international_sales |
  +----+----------+----------+------+----------+----------------+----------------+---------------------+
  |  1 | Eva Jo   | Anno     | 2007 |        1 |          120.5 |      555566666 |           777788888 |
  |  2 | Eva Ha   | Anno     | 2009 |        2 |          130.5 |      333344444 |           888899999 |
  |  3 | Eva Q    | Anno     | 2012 |        3 |           90.1 |      123456789 |           234567898 |
  |  4 | Frozen   | Chris    | 2013 |        4 |          150.6 |      456456456 |           789789789 |
  |  5 | Frozen 2 | Chris    | 2019 |        5 |           99.6 |      456456456 |           489789789 |
  +----+----------+----------+------+----------+----------------+----------------+---------------------+
  5 rows in set (0.00 sec)
  ```

  - カラム指定や、条件式など組み合わせる例

  ```
  mysql> select title, year, domestic_sales
    -> from movies
    -> inner join boxoffice
    -> on id = movie_id;
  +----------+------+----------------+
  | title    | year | domestic_sales |
  +----------+------+----------------+
  | Eva Jo   | 2007 |      555566666 |
  | Eva Ha   | 2009 |      333344444 |
  | Eva Q    | 2012 |      123456789 |
  | Frozen   | 2013 |      456456456 |
  | Frozen 2 | 2019 |      456456456 |
  +----------+------+----------------+
  5 rows in set (0.00 sec)


  mysql> select title, year, domestic_sales
      -> from movies
      -> inner join boxoffice
      -> on id = movie_id
      -> where length_minutes > 120;
  +--------+------+----------------+
  | title  | year | domestic_sales |
  +--------+------+----------------+
  | Eva Jo | 2007 |      555566666 |
  | Eva Ha | 2009 |      333344444 |
  | Frozen | 2013 |      456456456 |
  +--------+------+----------------+
  3 rows in set (0.00 sec)
  ```

- __外部結合__ `(OUTER JOIN)`

  どちらかのテーブルにしか存在しないレコードも取得する。

  ```
  mysql> select * from movies
      -> left outer join boxoffice
      -> on id = movie_id;
  +----+-----------+----------+------+----------+----------------+----------------+---------------------+
  | id | title     | director | year | movie_id | length_minutes | domestic_sales | international_sales |
  +----+-----------+----------+------+----------+----------------+----------------+---------------------+
  |  1 | Eva Jo    | Anno     | 2007 |        1 |          120.5 |      555566666 |           777788888 |
  |  2 | Eva Ha    | Anno     | 2009 |        2 |          130.5 |      333344444 |           888899999 |
  |  3 | Eva Q     | Anno     | 2012 |        3 |           90.1 |      123456789 |           234567898 |
  |  4 | Frozen    | Chris    | 2013 |        4 |          150.6 |      456456456 |           789789789 |
  |  5 | Frozen 2  | Chris    | 2019 |        5 |           99.6 |      456456456 |           489789789 |
  |  6 | Toy story | Lasseter | 1995 |     NULL |           NULL |           NULL |                NULL |
  +----+-----------+----------+------+----------+----------------+----------------+---------------------+
  6 rows in set (0.00 sec)
  ```

---

## Transaction

  _複数の処理をまとめて行う_ ための仕組み

- `BEGIN` / `COMMIT`

  ```
  mysql> begin;
  Query OK, 0 rows affected (0.00 sec)

  mysql> update menu
      -> set score = score + 100
      -> where name = "english";
  Query OK, 1 row affected (0.00 sec)
  Rows matched: 1  Changed: 1  Warnings: 0

  mysql> update menu
      -> set score = score - 100
      -> where name = "math";
  Query OK, 1 row affected (0.00 sec)
  Rows matched: 1  Changed: 1  Warnings: 0

  mysql> commit;
  Query OK, 0 rows affected (0.00 sec)


  mysql> select * from menu;
  +----+---------+-------+-------+
  | id | name    | score | stars |
  +----+---------+-------+-------+
  |  1 | math    |  20.2 |    10 |
  |  2 | english | 188.1 |     8 |
  |  3 | physics |  90.5 |     8 |
  +----+---------+-------+-------+
  3 rows in set (0.00 sec)
  ```

  - `BEGIN` の代わりに `START TRANSACTION` でもOK

    ```
    mysql> start transaction;
    Query OK, 0 rows affected (0.00 sec)

    mysql> update menu set score = score - 100 where name = "english";
    Query OK, 1 row affected (0.00 sec)
    Rows matched: 1  Changed: 1  Warnings: 0

    mysql> update menu set score = score + 100 where name = "math";
    Query OK, 1 row affected (0.00 sec)
    Rows matched: 1  Changed: 1  Warnings: 0

    mysql> commit;
    Query OK, 0 rows affected (0.00 sec)

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

  - COMMIT せずに `ROLLBACK` すると、BEGIN 以降の変更を __取り消し__ できる。

    ```
    mysql> begin;
    Query OK, 0 rows affected (0.00 sec)

    mysql> update menu
        -> set score = score + 100
        -> where name = "english";
    Query OK, 1 row affected (0.00 sec)
    Rows matched: 1  Changed: 1  Warnings: 0

    mysql> update menu set score = score - 100 where name = "math";
    Query OK, 1 row affected (0.01 sec)
    Rows matched: 1  Changed: 1  Warnings: 0

    mysql> select * from menu;
    +----+---------+-------+-------+
    | id | name    | score | stars |
    +----+---------+-------+-------+
    |  1 | math    |  20.2 |    10 |
    |  2 | english | 188.1 |     8 |
    |  3 | physics |  90.5 |     8 |
    +----+---------+-------+-------+
    3 rows in set (0.00 sec)

    mysql> rollback;
    Query OK, 0 rows affected (0.01 sec)

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

## External SQL file execution

- `source xxxx.sql`

  ( `source dir_hoge/xxxx.sql` )

  ```
  mysql> source mysql_cmd/create_tb.sql;
  Query OK, 0 rows affected (0.03 sec)


  mysql> desc posts;
  +----------+---------------------+------+-----+---------+----------------+
  | Field    | Type                | Null | Key | Default | Extra          |
  +----------+---------------------+------+-----+---------+----------------+
  | id       | bigint(20) unsigned | NO   | PRI | NULL    | auto_increment |
  | title    | varchar(255)        | NO   |     | NULL    |                |
  | body     | text                | YES  |     | NULL    |                |
  | author   | varchar(255)        | YES  |     | im      |                |
  | is_draft | tinyint(1)          | YES  |     | 1       |                |
  +----------+---------------------+------+-----+---------+----------------+
  5 rows in set (0.01 sec)
  ```
