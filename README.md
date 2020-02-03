# db_memo_to_self

[Cheat sheet] Database &amp; SQL

---

## `PostgreSQL` のパスを通す（Windows 10）

### 手順

1. コントロールパネル >
1. システムとセキュリティ >
1. システム >
1. システムの詳細設定 >
1. （システムのプロパティ）詳細設定タブ > 環境変数 >
1. （システム環境変数内の __変数名__）`Path` > 編集 >
1. （環境変数の編集）新規 >
1. __変数値__ としてPostgreSQL下の `bin` までのパスを入力

    - 例
        ```
        C:\Program Files\PostgreSQL\12\bin
        ```
1. OK, OK.. でdone。

### パスが通ったか確認
```
$ psql --version

psql (PostgreSQL) 12.1
```


---

## `MySQL` のパスを通す（Windows）

### 手順

前述のPostgreSQLと基本的には同様。

  - MySQLパスの変数値（例）
    ```
    C:\Program Files\MySQL\MySQL Server 8.0\bin
    ```

### パスが通ったか確認
```
$ mysql --version

C:\Program Files\MySQL\MySQL Server 8.0\bin\mysql.exe  Ver 8.0.19 for Win64 on x86_64 (MySQL Community Server - GPL)
```


---




