# Usage MySQL with Python/SQLAlchemhy (Local)

- Env & Version

  ```
  $ mysql --version
  mysql  Ver 14.14 Distrib 5.7.29, for osx10.14 (x86_64) 

  $ python --version
  Python 3.7.7

  $ poetry --version
  Poetry version 1.0.5
  ```

  - [SQLAlchemy](https://www.sqlalchemy.org/)

## Initial setup

```
$ poetry new mysql_sqlalchemy

$ cd mysql_sqlalchemy

$ poetry add sqlalchemy

$ code app.py
```

## Execute

```
$ poetry shell

$ python app.py
```
