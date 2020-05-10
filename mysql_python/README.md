# Usage MySQL with Python/MySQLClient (Local)

__Python__ 開発による __MySQL__ の基本操作を、`MySQL Client`により実行します。

- 前提

  - データベースおよびテーブルは、MySQL側で直接作成済み。（内容後述：サンプルデータベース）

## 実行環境・バージョン

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
$ poetry new mysql_python

$ cd mysql_python

$ poetry add mysqlclient

$ code app.py
```

## 実行

```
$ poetry shell

(in poetry venv)$ python app.py
```

- 主ファイル `app.py` で基本的なCRUD操作を確認。

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
