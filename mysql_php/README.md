# Usage MySQL with PHP (Local)

__PHP__ 開発による __MySQL__ の基本操作を実装し、動作を確認・検証します。

## 実行環境・バージョン

動作確認はすべて、macOS（10.14.6）上で行っています。

バージョンは次のとおりです。

```
$ mysql --version
mysql  Ver 14.14 Distribv 5.7.29, for osx10.14 (x86_64)

$ php --version
PHP 7.3.17
```

- 前提

  - データベースおよびテーブルは、MySQL側で直接作成済み。（内容後述：サンプルデータベース）

## 実行

```
$ cd mysql_php

$ php -S localhost:8000
```

- `http://localhost:8000/` で結果確認。

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
