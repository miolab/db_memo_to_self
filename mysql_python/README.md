# Usage MySQL with Python/MySQLClient (Local)

__Python__ 開発による __MySQL__ の基本操作を、`MySQL Client`により実行します。

- 前提

  - データベースおよびテーブルは、MySQL側で直接作成済み。

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