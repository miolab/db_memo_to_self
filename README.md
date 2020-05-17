# Database & SQL memo

各種DBMSとSQLに関するいろいろチートシート。

## 各種 `RDBMS`, `NoSQL` のセットアップや文法メモ

| | 説明 | 補足（バージョン等） |
| :-- | :-- | :-- |
| [mysql_brew.md](https://github.com/miolab/db_memo_to_self/blob/master/mysql_brew.md) | **MySQL** を`Homebrew`でセットアップ | mysql@5.7 |
| [mysql_usage.md](https://github.com/miolab/db_memo_to_self/blob/master/mysql_usage.md) | **MySQL** コマンド確認用チートシート | mysql@5.7 |
| [psql_asdf.md](https://github.com/miolab/db_memo_to_self/blob/master/psql_asdf.md) | **PostgreSQL** を`asdf`でセットアップ | PostgreSQL 12.2 |
| [mongo_brew.md](https://github.com/miolab/db_memo_to_self/blob/master/mongo_brew.md) | **MongoDB** を`Homebrew`でセットアップ | MongoDB v4.2.5 (mongodb-community) |
| [mongo_usage.md](https://github.com/miolab/db_memo_to_self/blob/master/mongo_usage.md) | **MongoDB** コマンド確認用チートシート | MongoDB v4.2.5 (mongodb-community) |
| [path_windows.md](https://github.com/miolab/db_memo_to_self/blob/master/path_windows.md) | Windows 環境で各種 DB のパスを通す | Windows 10 |

---

## 各言語との連携メモ

| | 説明 | 補足（ライブラリ, ORM 等） |
| :-- | :-- | :-- |
| [mysql_python](https://github.com/miolab/db_memo_to_self/tree/master/mysql_python) | __Python__ + MySQL | MySQLClient / Poetry |
| [mysql_sqlalchemy](https://github.com/miolab/db_memo_to_self/tree/master/mysql_sqlalchemy) | __Python__ + MySQL | SQLAlchemy / Poetry |
| [mysql_php](https://github.com/miolab/db_memo_to_self/tree/master/mysql_php) | __PHP__ + MySQL | |
| [mysql_node](https://github.com/miolab/db_memo_to_self/tree/master/mysql_node) | __Node.js__ + MySQL | |
| [mysql_elixir](https://github.com/miolab/db_memo_to_self/tree/master/mysql_elixir) | __Elixir__ + MySQL | MyXQL _(on going)_ |

- note :

  `Elixir + PostgreSQL` の `Ecto` による連携を、別リポジトリ __[ecto_postgres](https://github.com/miolab/ecto_postgres)__ で実装。