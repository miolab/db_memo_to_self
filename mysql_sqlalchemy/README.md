# Usage MySQL with Python/SQLAlchemhy (Local)

__Python__ の ORMライブラリ `SQLAlchemy` による __MySQL__ 基本操作を実装します。

- 参考

  - [SQLAlchemy](https://www.sqlalchemy.org/) （公式）

- 前提

  - データベースおよびテーブルは、MySQL側で直接作成済み。

## 実行環境・バージョン

- Mac OS (10.14.6)

  ```
  $ mysql --version
  mysql  Ver 14.14 Distrib 5.7.29, for osx10.14 (x86_64)

  $ python --version
  Python 3.7.7

  $ poetry --version
  Poetry version 1.0.5
  ```

## 実行準備

```
$ poetry new mysql_sqlalchemy

$ cd mysql_sqlalchemy

// add Driver
$ poetry add mysqlclient

// add ORM
$ poetry add sqlalchemy

$ code app.py
.
.
```

## 実行

```
$ poetry shell

(in poetry venv)$ python app.py
```

- メインファイル `app.py` で基本的なCRUD操作を確認。

- `$ exit` で実行環境を終了。

---

### サンプル データヘース

```
mysql> show processlist;
+----+------+-----------+-----------+---------+------+----------+------------------+
| Id | User | Host      | db        | Command | Time | State    | Info             |
+----+------+-----------+-----------+---------+------+----------+------------------+
| 35 | root | localhost | mydb_test | Query   |    0 | starting | show processlist |
+----+------+-----------+-----------+---------+------+----------+------------------+
1 row in set (0.01 sec)

mysql> select * from menu;
+----+---------+-------+-------+
| id | name    | score | stars |
+----+---------+-------+-------+
|  1 | math    | 120.2 |    10 |
|  2 | english |  88.1 |     8 |
|  3 | physics |  90.5 |     8 |
+----+---------+-------+-------+
3 rows in set (0.00 sec)

mysql> desc menu;
+-------+-------------+------+-----+---------+----------------+
| Field | Type        | Null | Key | Default | Extra          |
+-------+-------------+------+-----+---------+----------------+
| id    | int(11)     | NO   | PRI | NULL    | auto_increment |
| name  | varchar(15) | YES  |     | NULL    |                |
| score | float       | YES  |     | NULL    |                |
| stars | int(11)     | YES  |     | NULL    |                |
+-------+-------------+------+-----+---------+----------------+
4 rows in set (0.01 sec)
```
