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

    // Connect DB
    $db = "mydb_test";
    $user = "root";
    $password = "";
    $charset = "utf8mb4";
    $dsn = "mysql:dbname={$db};host=127.0.0.1;charset={$charset}";

    $dbh = new PDO($dsn, $user, $password);

    // Handling DB
    $sql = "select * from menu";
    $stmt = $dbh->prepare($sql);
    $stmt->execute();

    // foreach($records as $row){
    while ($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
      // $records = $stmt->fetch(PDO::FETCH_ASSOC);
      echo "<tr>\n";
      echo "\t<td>{$row['name']}</td>\n";
      echo "\t<td>{$row['score']}</td>\n";
      echo "\t<td>{$row['stars']}</td>\n";
      echo "</tr>\n";
    }

    // Disconnect DB
    $dbh = null;
    ?>

  </table>
</body>

</html>