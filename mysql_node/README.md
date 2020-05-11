# Usage MySQL with Node.js/ (Local)

__Node.js__ 開発における __MySQL__ の基本操作を、`MySQL Client`により実行します。

- 参考

  - [MySQL Driver (npm)](https://www.npmjs.com/package/mysql)

- 前提

  - MySQLデータベースおよびテーブルは、SQLで作成済み。（内容後述：サンプルデータベース）

## 実行環境・バージョン

  ```
  $ mysql --version
  mysql  Ver 14.14 Distrib 5.7.29, for osx10.14 (x86_64) using  EditLine wrapper

  $ node --version
  v12.16.1

  $ npm --version
  6.14.4
  ```

## 実行準備

```
$ mkdir mysql_node && cd mysql_node

$ npm install mysql

$ code app.js
```

## 実行

```
$ node app.js
```

- 主ファイル `app.js` で基本的なCRUD操作を確認。

  - `.query()` によりsql文を記述し実行

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
