<?php
class Person {
  public $id;
  private $name;

  function __construct($name, $id) {
    $this->name = $name;
    $this->id = $id;
  }

  function getName() {
    return $this->name;
  }
}
$person = new Person("Tahsin", 12);
echo($person->getName());
echo($person->id);
 ?>
