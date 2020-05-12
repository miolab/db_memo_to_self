<!DOCTYPE html>
<html lang="ja">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>MySQL with PHP (READ)</title>
</head>

<body>
  <h1>MySQL with PHP (READ)</h1>
  <table>

    <?php

    use FFI\Exception;

    $db = "mydb_test";
    $user = "root";
    $password = "";
    $charset = "utf8mb4";
    $dsn = "mysql:dbname={$db};host=127.0.0.1;charset={$charset}";

    try {
      // Connect DB
      $dbh = new PDO($dsn, $user, $password);

      // Handling DB
      $sql = "select * from menu";
      $stmt = $dbh->prepare($sql);
      $stmt->execute();

      while ($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
        print "<tr>\n";
        print "\t<td>{$row['name']}</td>\n";
        print "\t<td>{$row['score']}</td>\n";
        print "\t<td>{$row['stars']}</td>\n";
        print "</tr>\n";
      }

      // Disconnect DB
      $dbh = null;
    } catch (Exception $e) {
      print "ただいま障害によりご迷惑をおかけしております";
    }
    ?>

  </table>
</body>

</html>