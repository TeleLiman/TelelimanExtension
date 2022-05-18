<?php
namespace App\Controllers;

class HomeController
{	
	public function index(){
		return view('index');
	}
	function conf(){
		$rootpassword = extensionDb('rootpassword');;
		$servername = server()->name;
		$serverip = server()->ip_address;
		$telegram_token = extensionDb('telegram_token');;
		$user_id = extensionDb('chat_id');
		
		$json = array('serverip' => $serverip, 'serverport' => 22, 'telegramtoken' => $telegram_token, 'userid' => $user_id, 'servername' => $servername, 'sshusername' => 'root', 'sshpassword' => $rootpassword);
		$json = json_encode($json);
		
		$file = fopen('/liman/extensions/teleliman/scripts/settings.json', 'w');
		fwrite($file, $json);
		fclose($file);
		return '<meta http-equiv="refresh" content="0;URL=/">';
	}
}
