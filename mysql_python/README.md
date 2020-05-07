# Usage MySQL with Python/MySQLClient (Local)

- Env & Version

  ```
  $ mysql --version
  mysql  Ver 14.14 Distrib 5.7.29, for osx10.14 (x86_64) 

  $ python --version
  Python 3.7.7

  $ poetry --version
  Poetry version 1.0.5
  ```

## Setup

```
$ poetry new mysql_python

$ cd mysql_python

$ poetry add mysqlclient

$ code app.py
```

## Execute

```
$ poetry shell

(in poetry venv)
$ python app.py

$ exit
```
