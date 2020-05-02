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

- DB 一覧

  ```
  mysql> show databases;
  +--------------------+
  | Database           |
  +--------------------+
  | information_schema |
  | mysql              |
  | performance_schema |
  | sys                |
  +--------------------+
  4 rows in set (0.01 sec)
  ```

## CRUD commands

- DB 作成

  ```
  mysql> create database mydb_test;
  Query OK, 1 row affected (0.00 sec)
  ```

- 使用する `DB` を選択/切り替え

  ```
  mysql> use mydb_test
  Database changed
  ```

- `table`作成 & `row`を追加

  ```
  mysql> drop table if exists menu;
  Query OK, 0 rows affected, 1 warning (0.01 sec)

  mysql> create table menu (
      -> id integer primary key auto_increment,
      -> name text,
      -> score real,
      -> stars integer);
  Query OK, 0 rows affected (0.01 sec)

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