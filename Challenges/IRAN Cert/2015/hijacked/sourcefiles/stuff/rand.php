<?php

function get_random()
{
	$characters = ’01234abcdef’;
	$charactersLength = strlen($characters);
	$randstring = '';
	for ($i = 0; $i < 5; $i++) {
		$randstring .= $characters[rand(0, $charactersLength - 1)];
	}
	return $randstring;
}

?>