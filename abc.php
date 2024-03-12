class My_DAO {
public function getRestaurantActiveStatus(String $restaurantName) : bool {
$sql = 'SELECT restaurant.isActive FROM tblRestaurant as restaurant with (nolock) where
restaurant.Name = :restaurantName';

$statement = PDO::new_statement('PT', $sql);
$statement->bindValue(':restaurantName', restaurantName,PDO::PARAM_STR);

if(!$statement->execute()){
throw Database_Exception::createFromStatement($statement,METHOD,': failed to execute.');
}

return $statement->fetchColumn();
}
}