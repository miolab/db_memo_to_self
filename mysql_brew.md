# MySQL を Homebrew でインストールしてセットアップ

## Setup

- `MySQL`の brew パッケージ確認

  ```
  $ brew search mysql
  ==> Formulae
  automysqlbackup            mysql-client@5.7           mysql-search-replace
  mysql                      mysql-connector-c++        mysql@5.6
  mysql++                    mysql-connector-c++@1.1    mysql@5.7
  mysql-client               mysql-sandbox              mysqltuner
  ==> Casks
  mysql-connector-python     mysql-utilities            navicat-for-mysql
  mysql-shell                mysqlworkbench             sqlpro-for-mysql
  ```

- インストール（例：`5.7系`バージョン指定）

  ```
  $ brew install mysql@5.7
  .
  .
  .
  ==> Caveats
  We've installed your MySQL database without a root password. To secure it run:
      mysql_secure_installation

  MySQL is configured to only allow connections from localhost by default

  To connect run:
      mysql -uroot

  mysql@5.7 is keg-only, which means it was not symlinked into /usr/local,
  because this is an alternate version of another formula.

  If you need to have mysql@5.7 first in your PATH run:
    echo 'export PATH="/usr/local/opt/mysql@5.7/bin:$PATH"' >> ~/.bash_profile

  For compilers to find mysql@5.7 you may need to set:
    export LDFLAGS="-L/usr/local/opt/mysql@5.7/lib"
    export CPPFLAGS="-I/usr/local/opt/mysql@5.7/include"

  To have launchd start mysql@5.7 now and restart at login:
  brew services start mysql@5.7
  Or, if you don't want/need a background service you can just run:
  /usr/local/opt/mysql@5.7/bin/mysql.server start
  ==> Summary
  🍺  /usr/local/Cellar/mysql@5.7/5.7.29: 319 files, 232MB
  ```

- **PATH** を通す

  ```
  $ echo 'export PATH="/usr/local/opt/mysql@5.7/bin/:$PATH"' >> ~/.bash_profile

  $ source ~/.bash_profile
  ```

- インストール確認（MySQL バージョン確認）

  ```
  $ mysql --version
  mysql  Ver 14.14 Distrib 5.7.29, for osx10.14 (x86_64) using  EditLine wrapper
  ```

- 文字コード`utf8`設定

  ```
  $ vim /usr/local/etc/my.cnf

  # Default Homebrew MySQL server config
  [mysqld]
  character-set-server=utf8    -> この1行を追記
  # Only allow connections from localhost
  bind-address = 127.0.0.1
  ~
  ```

---

## Usage

- **サーバー起動**

  ```
  $ brew services start mysql@5.7
  ==> Successfully started `mysql@5.7` (label: homebrew.mxcl.mysql@5.7)
  ```

  - 再起動

    ```
    $ brew services restart mysql@5.7
    Stopping `mysql@5.7`... (might take a while)
    ==> Successfully stopped `mysql@5.7` (label: homebrew.mxcl.mysql@5.7)
    ==> Successfully started `mysql@5.7` (label: homebrew.mxcl.mysql@5.7)
    ```

  - 停止

    ```
    $ brew services stop mysql@5.7
    Stopping `mysql@5.7`... (might take a while)
    ==> Successfully stopped `mysql@5.7` (label: homebrew.mxcl.mysql@5.7)
    ```
