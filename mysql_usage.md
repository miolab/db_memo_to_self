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
