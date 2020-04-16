# asdf による PostgreSQL セットアップ

- `asdf` バージョン

  ```
  $ asdf --version
  v0.7.8- ...
  ```

- GitHub : [asdf PostgreSQL](https://github.com/smashedtoatoms/asdf-postgres)

---

## Setup

```
$ asdf plugin-add postgres

$ asdf install postgres x.x.x

$ asdf global postgres x.x.x

$ psql --version
# (e.g.)
# psql (PostgreSQL) 12.2

```

## Usage

```
$ pg_ctl start
# run server

$ createdb xxxxxxxx
# new create database

$ psql -l
# show list of all databases

$ psql -d xxxxxxxx
# connect to database named xxxxxxxx(opt. -d)
# more opt.
  -U:user(none=login user)
  -h:host(none=localhost)

$ pg_ctl stop
# stop server
```
