<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>Document</title>
  </head>
  <body>
    <form action="" method="GET">
      <input type="number" name="var1" placeholder="Enter The First Number: ">
      <input type="number" name="var2" placeholder="Enter The Second Number: ">
      <input type="submit" value="Calculate">
    </form>
  </body>

  <?php
    try {
      $var1 = $_GET["var1"];
      $var2 = $_GET["var2"];
      echo $var1 + $var2;
    } catch (Exception $e) {

    }
   ?>
</html>
