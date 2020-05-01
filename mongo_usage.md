# MongoDB Usage

- 動作環境 / 構築環境

  - macOS Mojave (10.14.6)

  - その他バージョン

    ```
    $ mongo --version
    MongoDB shell version v4.2.5
    ```

## Start/Stop MongoDB (mongodb-community) Server

```
$ brew services start mongodb-community

$ brew services stop mongodb-community
```

## Basic Usage

```
> // List DB
> show dbs
admin   0.000GB
config  0.000GB
local   0.000GB


> // Create DB(if NOT exist) or Read DB(if exist)
> use db_test
switched to db db_test

> show dbs
admin   0.000GB
config  0.000GB
local   0.000GB


> // Confirm connecting DB temporally
> db
db_test


> // Confirm connecting DB info
> db.stats()
{
	"db" : "db_test",
	"collections" : 1,
	"views" : 0,
	"objects" : 2,
	"avgObjSize" : 70.5,
	"dataSize" : 141,
	"storageSize" : 36864,
	"numExtents" : 0,
	"indexes" : 1,
	"indexSize" : 36864,
	"scaleFactor" : 1,
	"fsUsedSize" : 73430564864,
	"fsTotalSize" : 121018208256,
	"ok" : 1
}
```

## Collection

```
> // Create Collection
> db.createCollection("users")
{ "ok" : 1 }

> show dbs
admin    0.000GB
config   0.000GB
db_test  0.000GB
local    0.000GB


> // Confirm Collections
> show collections
users


> // Rename Collection
> db.users.renameCollection("players")
{ "ok" : 1 }

> show collections
players


> //  Drop Collection
> db.players.drop()
true

> show collections
>

```

## Delete DB

```
> show dbs
admin    0.000GB
config   0.000GB
db_test  0.000GB
local    0.000GB

> db.dropDatabase();
{ "dropped" : "db_test", "ok" : 1 }

> show dbs
admin   0.000GB
config  0.000GB
local   0.000GB

```

---

## Document (Create & Delete)

```
> // (Preparing)
> show dbs
admin   0.000GB
config  0.000GB
local   0.000GB

> use db_test
switched to db db_test

> db
db_test


> // Create Document
> db.users.insertOne({name:"im", movie:"eva"})
{
        "acknowledged" : true,
        "insertedId" : ObjectId("5e9c3f0f3b3fd6b8e4c7fa7c")
}


> // Show Document(s)
> db.users.find()
{ "_id" : ObjectId("5e9c3f0f3b3fd6b8e4c7fa7c"), "name" : "im", "movie" : "eva" }


> // Show Document(s) pretty
> db.users.find().pretty()
{
        "_id" : ObjectId("5e9c3f0f3b3fd6b8e4c7fa7c"),
        "name" : "im",
        "movie" : "eva"
}


> // Create Document (add)
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

> // スキーマが異なっても追加可能
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


> // Find the Document
> db.users.find({"name": "im2"}).pretty()
{
        "_id" : ObjectId("5e9c40a43b3fd6b8e4c7fa7d"),
        "name" : "im2",
        "movie" : "attack on titan"
}


> // Delete Document
> db.users.deleteOne({"name":"im2"})
{ "acknowledged" : true, "deletedCount" : 1 }

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

- _note :_ (\$gte)

  `mongo`中で **`JavaScript`構文を使う** ことも可能。

  ```
  > use mydb
  switched to db mydb

  > db
  mydb

  > for (let i=0; i<10; i++){
  ... db.users.insert({
  ... score: Math.random()
  ... });
  ... }
  WriteResult({ "nInserted" : 1 })

  > db.users.count()
  10

  > db.users.find().pretty()
  {
          "_id" : ObjectId("5ea269d5300a3db730b7d9c6"),
          "score" : 0.3424395295988656
  }
  {
          "_id" : ObjectId("5ea269d5300a3db730b7d9c7"),
          "score" : 0.24752730877269857
  }
  {
          "_id" : ObjectId("5ea269d5300a3db730b7d9c8"),
          "score" : 0.9113878946219832
  }
  {
          "_id" : ObjectId("5ea269d5300a3db730b7d9c9"),
          "score" : 0.10169106071842116
  }
  {
          "_id" : ObjectId("5ea269d5300a3db730b7d9ca"),
          "score" : 0.9701633185848546
  }
  {
          "_id" : ObjectId("5ea269d5300a3db730b7d9cb"),
          "score" : 0.35060178300607925
  }
  {
          "_id" : ObjectId("5ea269d5300a3db730b7d9cc"),
          "score" : 0.15544475238848432
  }
  {
          "_id" : ObjectId("5ea269d5300a3db730b7d9cd"),
          "score" : 0.20395166378332164
  }
  {
          "_id" : ObjectId("5ea269d5300a3db730b7d9ce"),
          "score" : 0.1400865230286369
  }
  {
          "_id" : ObjectId("5ea269d5300a3db730b7d9cf"),
          "score" : 0.6242031598658185
  }

  > db.users.remove({})
  WriteResult({ "nRemoved" : 10 })

  > db.users.find()
  >
  ```

---

## Document (Update)

```
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


> // Update Document
> db.users.update({"name": "im"}, {$set: {"movie": "cowboy bebop"}})
WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })

> db.users.find().pretty()
{
        "_id" : ObjectId("5e9c3f0f3b3fd6b8e4c7fa7c"),
        "name" : "im",
        "movie" : "cowboy bebop"
}
{
        "_id" : ObjectId("5e9c41253b3fd6b8e4c7fa7e"),
        "name" : "im3",
        "movie" : "fullmetal alchemist",
        "music" : "edm"
}
>

```

---

## Extract Field

```
> db.users.find()
{ "_id" : ObjectId("5ea2835a5cc6fafc5bc910ef"), "name" : "math", "score" : 90 }
{ "_id" : ObjectId("5ea283885cc6fafc5bc910f0"), "name" : "science", "score" : 80 }
{ "_id" : ObjectId("5ea284985cc6fafc5bc910f1"), "name" : "geography", "score" : 65 }


> // 通常検索
> db.users.find({name: "math"})
{ "_id" : ObjectId("5ea2835a5cc6fafc5bc910ef"), "name" : "math", "score" : 90 }


> // 〜以上 ($gte)
> db.users.find({score: {$gte: 80}})
{ "_id" : ObjectId("5ea2835a5cc6fafc5bc910ef"), "name" : "math", "score" : 90 }
{ "_id" : ObjectId("5ea283885cc6fafc5bc910f0"), "name" : "science", "score" : 80 }


> // 〜を上回る ($gt)
> db.users.find({score: {$gt: 80}})
{ "_id" : ObjectId("5ea2835a5cc6fafc5bc910ef"), "name" : "math", "score" : 90 }


> // 〜以下 ($lte)
> db.users.find({score: {$lte: 80}})
{ "_id" : ObjectId("5ea283885cc6fafc5bc910f0"), "name" : "science", "score" : 80 }
{ "_id" : ObjectId("5ea284985cc6fafc5bc910f1"), "name" : "geography", "score" : 65 }


> // 〜を下回る ($gt)
> db.users.find({score: {$lt: 80}})
{ "_id" : ObjectId("5ea284985cc6fafc5bc910f1"), "name" : "geography", "score" : 65 }


> // Equal ($eq)
> db.users.find({score: {$eq: 80}})
{ "_id" : ObjectId("5ea283885cc6fafc5bc910f0"), "name" : "science", "score" : 80 }


> // NOT Equal ($ne)
> db.users.find({score: {$ne: 80}})
{ "_id" : ObjectId("5ea2835a5cc6fafc5bc910ef"), "name" : "math", "score" : 90 }
{ "_id" : ObjectId("5ea284985cc6fafc5bc910f1"), "name" : "geography", "score" : 65 }
```

- _note :_

  - `JavaScript の正規表現`を抽出条件として使う。（例）

    ```
    > db.users.find({name: /ma/})
    { "_id" : ObjectId("5ea2835a5cc6fafc5bc910ef"), "name" : "math", "score" : 90 }

    > db.users.find({name: /h/})
    { "_id" : ObjectId("5ea2835a5cc6fafc5bc910ef"), "name" : "math", "score" : 90 }
    { "_id" : ObjectId("5ea284985cc6fafc5bc910f1"), "name" : "geography", "score" : 6
    5 }

    > db.users.find({name: /^s/})
    { "_id" : ObjectId("5ea283885cc6fafc5bc910f0"), "name" : "science", "score" : 80
    }
    ```

  - フィールドの値に何が入っているかを調べる

    ```
    > db.users.distinct("name")
    [ "geography", "math", "science" ]
    ```

  - その他、抽出コマンド

    #### AND 抽出

    ```
    > db.users.find({name: /e/, score: {$gt: 77}})
    { "_id" : ObjectId("5ea283885cc6fafc5bc910f0"), "name" : "science", "score" : 80 }
    ```

    #### OR 抽出

    ```
    > // OR 抽出 ($or ...通常)
    > db.users.find({$or: [{name: /e/}, {score: {$gt: 77}}]})
    { "_id" : ObjectId("5ea2835a5cc6fafc5bc910ef"), "name" : "math", "score" : 90 }
    { "_id" : ObjectId("5ea283885cc6fafc5bc910f0"), "name" : "science", "score" : 80 }
    { "_id" : ObjectId("5ea284985cc6fafc5bc910f1"), "name" : "geography", "score" : 65 }

    > // OR 抽出 ($in ...同一field内)
    > db.users.find({score: {$in: [90, 65]}})
    { "_id" : ObjectId("5ea2835a5cc6fafc5bc910ef"), "name" : "math", "score" : 90 }
    { "_id" : ObjectId("5ea284985cc6fafc5bc910f1"), "name" : "geography", "score" : 65 }
    ```

    #### exists 抽出

    ```
    > // (preparing)
    > db.users.insert({name: "history", score: 72, type: "jp"})
    > WriteResult({ "nInserted" : 1 })

    > // $exists
    > db.users.find({type: {\$exists: true}})
    > { "\_id" : ObjectId("5ea293d0975efb40f5beb893"), "name" : "history", "score" : 72, "type" : "jp" }

    > // 「true」の代わりに「1」でも可
    > db.users.find({type: {\$exists: 1}})
    > { "\_id" : ObjectId("5ea293d0975efb40f5beb893"), "name" : "history", "score" : 72, "type" : "jp" }

    > db.users.find({type: {\$exists: false}})
    > { "\_id" : ObjectId("5ea2835a5cc6fafc5bc910ef"), "name" : "math", "score" : 90 }
    > { "\_id" : ObjectId("5ea283885cc6fafc5bc910f0"), "name" : "science", "score" : 80 }
    > { "\_id" : ObjectId("5ea284985cc6fafc5bc910f1"), "name" : "geography", "score" : 65 }
    ```

---

## 表示する`field`を指定

```
> // true(または 1) か false(または 0) を指定
> db.users.find({}, {name: true, score: 1})
> { "\_id" : ObjectId("5ea2835a5cc6fafc5bc910ef"), "name" : "math", "score" : 90 }
> { "\_id" : ObjectId("5ea283885cc6fafc5bc910f0"), "name" : "science", "score" : 80 }
> { "\_id" : ObjectId("5ea284985cc6fafc5bc910f1"), "name" : "geography", "score" : 65 }
> { "\_id" : ObjectId("5ea293d0975efb40f5beb893"), "name" : "history", "score" : 72 }

> // false(=0)で、表示除外
> db.users.find({}, {score: 0})
> { "\_id" : ObjectId("5ea2835a5cc6fafc5bc910ef"), "name" : "math" }
> { "\_id" : ObjectId("5ea283885cc6fafc5bc910f0"), "name" : "science" }
> { "\_id" : ObjectId("5ea284985cc6fafc5bc910f1"), "name" : "geography" }
> { "\_id" : ObjectId("5ea293d0975efb40f5beb893"), "name" : "history", "type" : "jp" }


> // Error になるパターン（1,0 が混在しているため）
> db.users.find({}, {name: 1, score: 0})
> Error: error: {

        "ok" : 0,
        "errmsg" : "Projection cannot have a mix of inclusion and exclusion.",
        "code" : 2,
        "codeName" : "BadValue"

}

> // ただし、_id だけは例外で扱える
> db.users.find({}, {\_id: 0, score: 1})
> { "score" : 90 }
> { "score" : 80 }
> { "score" : 65 }
> { "score" : 72 }
```

- _note :_

  - その他： `findOne()`（1 件だけ抽出）

  ```
  > db.users.findOne({}, {\_id: 0})
  > { "name" : "math", "score" : 90 }
  ```

  - `find()` と組み合わせて使うその他コマンド

    #### skip()

    ```
    > db.users.find({}, {\_id: 0})
    > { "name" : "math", "score" : 90 }
    > { "name" : "science", "score" : 80 }
    > { "name" : "geography", "score" : 65 }
    > { "name" : "history", "score" : 72, "type" : "jp" }

    > db.users.find({}, {\_id: 0}).skip(2);
    > { "name" : "geography", "score" : 65 }
    > { "name" : "history", "score" : 72, "type" : "jp" }
    ```

    #### sort()

    ```
    > // 昇順 (: 1)
    > db.users.find({}, {\_id: 0}).sort({score: 1})
    > { "name" : "geography", "score" : 65 }
    > { "name" : "history", "score" : 72, "type" : "jp" }
    > { "name" : "science", "score" : 80 }
    > { "name" : "math", "score" : 90 }

    > // 降順 (: -1)
    > db.users.find({}, {\_id: 0}).sort({score: -1})
    > { "name" : "math", "score" : 90 }
    > { "name" : "science", "score" : 80 }
    > { "name" : "history", "score" : 72, "type" : "jp" }
    > { "name" : "geography", "score" : 65 }
    ```

    #### limit()

    ```
    > db.users.find({}, {\_id: 0}).limit(3)
    > { "name" : "math", "score" : 90 }
    > { "name" : "science", "score" : 80 }
    > { "name" : "geography", "score" : 65 }

    > db.users.find({}, {\_id: 0}).sort({score: -1}).limit(3)
    > { "name" : "math", "score" : 90 }
    > { "name" : "science", "score" : 80 }
    > { "name" : "history", "score" : 72, "type" : "jp" }
    ```

---

## Document (Update: _other command_)

```
> db.users.find({name: "math"}, {\_id: 0})
> { "name" : "math", "score" : 90 }


> // 加算（$inc）
> db.users.update({name: "math"}, {$inc: {score: 10}})
> WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })

> db.users.find({name: "math"}, {\_id: 0})
> { "name" : "math", "score" : 100 }

> db.users.update({name: "math"}, {\$inc: {score: -5}})
> WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })

> db.users.find({name: "math"}, {\_id: 0})
> { "name" : "math", "score" : 95 }


> // 乗算 ($mul)
> db.users.update({name: "math"}, {$mul: {score: 2}})
> WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
> db.users.find({name: "math"}, {\_id: 0})
> { "name" : "math", "score" : 190 }


> // fieldのリネーム ($rename)
> db.users.update({name: "math"}, {\$rename: {score: "point"}})
> WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
> db.users.find({name: "math"}, {\_id: 0})
> { "name" : "math", "point" : 190 }


> // fieldを追加 ($set)
> db.users.update({name: "math"}, {$set: {type: "subject"}})
> WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
> db.users.find({name: "math"}, {\_id: 0})
> { "name" : "math", "point" : 190, "type" : "subject" }


> // field 削除 ($unset)
> db.users.update({name: "math"}, {$unset: {type: "", point: ""}})
> WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
> db.users.find({name: "math"}, {\_id: 0})
> { "name" : "math", "score" : 190 }
```

### upsert

```
> // データが存在していたら更新し、存在してなかったら新規作成（upsert）
> db.users.update({name: "english"}, {name: "english", score: 85}, {upsert: true}
> )
> WriteResult({

        "nMatched" : 0,
        "nUpserted" : 1,
        "nModified" : 0,
        "_id" : ObjectId("5ea626b7384e74b99c3abfbf")

})

> db.users.find()
> { "\_id" : ObjectId("5ea2835a5cc6fafc5bc910ef"), "name" : "math", "score" : 190 }
> { "\_id" : ObjectId("5ea283885cc6fafc5bc910f0"), "name" : "science", "score" : 80 }
> { "\_id" : ObjectId("5ea284985cc6fafc5bc910f1"), "name" : "geography", "score" : 65 }
> { "\_id" : ObjectId("5ea293d0975efb40f5beb893"), "name" : "history", "score" : 72, "type" : "jp" }
> { "\_id" : ObjectId("5ea626b7384e74b99c3abfbf"), "name" : "english", "score" : 85 }

> db.users.update({name: "english"}, {name: "english", score: 160}, {upsert: true
> })
> WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })

> db.users.find()
> { "\_id" : ObjectId("5ea2835a5cc6fafc5bc910ef"), "name" : "math", "score" : 190 }
> { "\_id" : ObjectId("5ea283885cc6fafc5bc910f0"), "name" : "science", "score" : 80
> }
> { "\_id" : ObjectId("5ea284985cc6fafc5bc910f1"), "name" : "geography", "score" : 6
> 5 }
> { "\_id" : ObjectId("5ea293d0975efb40f5beb893"), "name" : "history", "score" : 72,
> "type" : "jp" }
> { "\_id" : ObjectId("5ea626b7384e74b99c3abfbf"), "name" : "english", "score" : 160
> }
```

### remove()

```
> db.users.remove({name: "english"})
> WriteResult({ "nRemoved" : 1 })

> db.users.find()
> { "\_id" : ObjectId("5ea2835a5cc6fafc5bc910ef"), "name" : "math", "score" : 190 }
> { "\_id" : ObjectId("5ea283885cc6fafc5bc910f0"), "name" : "science", "score" : 80 }
> { "\_id" : ObjectId("5ea284985cc6fafc5bc910f1"), "name" : "geography", "score" : 65 }
> { "\_id" : ObjectId("5ea293d0975efb40f5beb893"), "name" : "history", "score" : 72, "type" : "jp" }
```

---

## index

```
> db.users.getIndexes()
> [

        {
                "v" : 2,
                "key" : {
                        "_id" : 1
                },
                "name" : "_id_",
                "ns" : "mydb.users"
        }

]


> // 降順で index をつくる
> db.users.createIndex({score: -1})
> {

        "createdCollectionAutomatically" : false,
        "numIndexesBefore" : 1,
        "numIndexesAfter" : 2,
        "ok" : 1

}

> db.users.getIndexes()
> [

        {
                "v" : 2,
                "key" : {
                        "_id" : 1
                },
                "name" : "_id_",
                "ns" : "mydb.users"
        },
        {
                "v" : 2,
                "key" : {
                        "score" : -1
                },
                "name" : "score_-1",
                "ns" : "mydb.users"
        }

]


> // index を削除
> db.users.dropIndex("score\_-1")
> { "nIndexesWas" : 2, "ok" : 1 }

> db.users.getIndexes()
> [

        {
                "v" : 2,
                "key" : {
                        "_id" : 1
                },
                "name" : "_id_",
                "ns" : "mydb.users"
        }

]


> // unique なインデックスを作る
> db.users.createIndex({name: 1}, {unique: true})
> {

        "createdCollectionAutomatically" : false,
        "numIndexesBefore" : 1,
        "numIndexesAfter" : 2,
        "ok" : 1

}

> db.users.getIndexes()
> [

        {
                "v" : 2,
                "key" : {
                        "_id" : 1
                },
                "name" : "_id_",
                "ns" : "mydb.users"
        },
        {
                "v" : 2,
                "unique" : true,
                "key" : {
                        "name" : 1
                },
                "name" : "name_1",
                "ns" : "mydb.users"
        }

]

> db.users.insert({name: "math"})
> WriteResult({

        "nInserted" : 0,
        "writeError" : {
                "code" : 11000,
                "errmsg" : "E11000 duplicate key error collection: mydb.users index: name_1 dup key: { name: \"math\" }"
        }

})
```

---

## DB のバックアップと復元

```
$ mongodump -d mydb  // バックアップ作成
.
.

$ mongo mydb

> db
> mydb
> db.users.remove({name: "math"})
> WriteResult({ "nRemoved" : 1 })
> db.users.find()
> { "\_id" : ObjectId("5ea283885cc6fafc5bc910f0"), "name" : "science", "score" : 80 }
> { "\_id" : ObjectId("5ea284985cc6fafc5bc910f1"), "name" : "geography", "score" : 65 }
> { "\_id" : ObjectId("5ea293d0975efb40f5beb893"), "name" : "history", "score" : 72, "type" : "jp" }
> exit
> bye


$ mongorestore --drop  // 復元。--drop は「上書き」
.
.

$ mongo mydb

> db.users.find()
> { "\_id" : ObjectId("5ea2835a5cc6fafc5bc910ef"), "name" : "math", "score" : 190 }
> { "\_id" : ObjectId("5ea283885cc6fafc5bc910f0"), "name" : "science", "score" : 80 }
> { "\_id" : ObjectId("5ea284985cc6fafc5bc910f1"), "name" : "geography", "score" : 65 }
> { "\_id" : ObjectId("5ea293d0975efb40f5beb893"), "name" : "history", "score" : 72, "type" : "jp" }

```

その他の使用方法は、`--help`で確認

- \$ mongodump --help
- \$ mongorestore --help
