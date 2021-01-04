<?php
    
    class profile
    {
        public $username;
        private $password;
        
        public function __construct($username, $password)
        {
            $this->username=$username;
            $this->password=$password;
        }
    }
    
    
    $user = serialize(new profile('admin', 'admin'));
    
    $cookie_= "";
    for ($i=0; $i<strlen($user); $i++)
        $cookie_.=chr(ord($user[$i])^0x03);
    echo $cookie_;

?>