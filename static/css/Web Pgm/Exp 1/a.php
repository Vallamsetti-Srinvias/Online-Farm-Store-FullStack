<?php
$keyword = $_GET['q'];
$data = ["apple", "banana", "carrot", "date", "fig"];
$result = [];

foreach ($data as $item) {
  if (stripos($item, $keyword) !== false) {
    $result[] = $item;
  }
}
echo implode("<br>", $result);
?>
