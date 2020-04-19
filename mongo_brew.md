# Homebrew による MongoDB セットアップ

- `Homebrew` バージョン

  ```
  $ brew --version
  Homebrew 2.2.13
  ```

- GitHub : [MongoDB](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-os-x/)

---

## Setup

```
$ brew tap mongodb/brew

$ brew install mongodb-community
```

## Usage

```
# run DB server

$ brew services start mongodb-community

==> Tapping homebrew/services
Cloning into '/usr/local/Homebrew/Library/Taps/homebrew/homebrew-services'...
remote: Enumerating objects: 7, done.
remote: Counting objects: 100% (7/7), done.
remote: Compressing objects: 100% (7/7), done.
remote: Total 698 (delta 0), reused 3 (delta 0), pack-reused 691
Receiving objects: 100% (698/698), 193.18 KiB | 280.00 KiB/s, done.
Resolving deltas: 100% (272/272), done.
Tapped 1 command (40 files, 267KB).
==> Successfully started `mongodb-community` (label: homebrew.mxcl.mongodb-community)
```

```
# confirm about version (to check about server running)

$ mongo --version
MongoDB shell version v4.2.5
git version: 2261279b51ea13df08ae708ff278f0679c59dc32
allocator: system
modules: none
build environment:
    distarch: x86_64
    target_arch: x86_64
```

```
# connect DB

$ mongo
MongoDB shell version v4.2.5
connecting to: mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb
.
.
.

>

```

```
# disconnect DB

> exit
bye

```

---

## Test 1

```
# List DB

> show dbs
admin   0.000GB
config  0.000GB
local   0.000GB


# Create DB (if NOT exist) or Read DB (if exist)

> use db_test
switched to db db_test


> show dbs
admin   0.000GB
config  0.000GB
local   0.000GB


# Confirm running DB

> db
db_test


# Add Collection

> db.createCollection("users")
{ "ok" : 1 }
> show dbs
admin    0.000GB
config   0.000GB
db_test  0.000GB
local    0.000GB

```

```
# Delete DB

> db.dropDatabase();
{ "dropped" : "db_test", "ok" : 1 }


> show dbs
admin   0.000GB
config  0.000GB
local   0.000GB

```

---

Create & Delete Document

```
> show dbs
admin   0.000GB
config  0.000GB
local   0.000GB

> use db_test
switched to db db_test

> db
db_test


# Create Document

> db.users.insertOne({name:"im", movie:"eva"})
{
        "acknowledged" : true,
        "insertedId" : ObjectId("5e9c3f0f3b3fd6b8e4c7fa7c")
}


# Show Document(s)

> db.users.find()
{ "_id" : ObjectId("5e9c3f0f3b3fd6b8e4c7fa7c"), "name" : "im", "movie" : "eva" }


# Show Document(s) pretty

> db.users.find().pretty()
{
        "_id" : ObjectId("5e9c3f0f3b3fd6b8e4c7fa7c"),
        "name" : "im",
        "movie" : "eva"
}


# Create Document (add)

> db.users.insertOne({name:"im2", movie:"attack on titan"}
... )
{
        "acknowledged" : true,
        "insertedId" : ObjectId("5e9c40a43b3fd6b8e4c7fa7d")
}


> db.users.find().pretty()
{
        "_id" : ObjectId("5e9c3f0f3b3fd6b8e4c7fa7c"),
        "name" : "im",
        "movie" : "eva"
}
{
        "_id" : ObjectId("5e9c40a43b3fd6b8e4c7fa7d"),
        "name" : "im2",
        "movie" : "attack on titan"
}


> db.users.insertOne({name:"im3", movie:"fullmetal alchemist", music:"edm"} )
{
        "acknowledged" : true,
        "insertedId" : ObjectId("5e9c41253b3fd6b8e4c7fa7e")
}


> db.users.find().pretty()
{
        "_id" : ObjectId("5e9c3f0f3b3fd6b8e4c7fa7c"),
        "name" : "im",
        "movie" : "eva"
}
{
        "_id" : ObjectId("5e9c40a43b3fd6b8e4c7fa7d"),
        "name" : "im2",
        "movie" : "attack on titan"
}
{
        "_id" : ObjectId("5e9c41253b3fd6b8e4c7fa7e"),
        "name" : "im3",
        "movie" : "fullmetal alchemist",
        "music" : "edm"
}


# find the Document

> db.users.find({"name": "im2"}).pretty()
{
        "_id" : ObjectId("5e9c40a43b3fd6b8e4c7fa7d"),
        "name" : "im2",
        "movie" : "attack on titan"
}
```

```
# Delete Document

> db.users.deleteOne({"name":"im2"})
{ "acknowledged" : true, "deletedCount" : 1 }


> db.users.find()
{ "_id" : ObjectId("5e9c3f0f3b3fd6b8e4c7fa7c"), "name" : "im", "movie" : "eva" }
{ "_id" : ObjectId("5e9c41253b3fd6b8e4c7fa7e"), "name" : "im3", "movie" : "fullmetal alchemist", "music" : "edm" }


> db.users.find().pretty()
{
        "_id" : ObjectId("5e9c3f0f3b3fd6b8e4c7fa7c"),
        "name" : "im",
        "movie" : "eva"
}
{
        "_id" : ObjectId("5e9c41253b3fd6b8e4c7fa7e"),
        "name" : "im3",
        "movie" : "fullmetal alchemist",
        "music" : "edm"
}

```
