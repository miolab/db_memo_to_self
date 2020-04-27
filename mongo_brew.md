# Homebrew による MongoDB セットアップ

- 動作環境 / 構築環境

  - macOS Mojave (10.14.6)

  - その他バージョン

    ```
    $ brew --version
    Homebrew 2.2.13

    $ mongo --version
    MongoDB shell version v4.2.5
    ```

- 参考

  (GitHub) [MongoDB](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-os-x/)

---

## セットアップ

```
$ brew tap mongodb/brew

$ brew install mongodb-community
```

## 確認

- run DB server

  ```
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

- confirm about version (to check about server running)

  ```
  $ mongo --version

  MongoDB shell version v4.2.5
  git version: 2261279b51ea13df08ae708ff278f0679c59dc32
  allocator: system
  modules: none
  build environment:
  distarch: x86_64
  target_arch: x86_64
  ```

- connect DB

  ```
  $ mongo

  MongoDB shell version v4.2.5
  connecting to: mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb
  .
  .
  .

  >
  ```

- disconnect DB

  ```
  > exit
  bye
  ```
