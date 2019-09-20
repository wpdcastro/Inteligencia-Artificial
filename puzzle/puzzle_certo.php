<?php 

class No {

	public $estado;
	public $pai;
	public $acao;
	public $custo;
	public $profundidade;
}

class Agente {

	public function getVazio($no_base) {

	}
	
	public function up($no_base) {

	}

	public function down($no_base) {

	}

	public function right($no_base) {

	}

	public function left($no_base) {

	}

	public function sucessor($no_base) {
		$lista = [];

		$lista["up"]    = $this->up($no_base);
		$lista["down"]  = $this->down($no_base);
		$lista["left"]  = $this->rigth($no_base);
		$lista["right"] = $this->left($no_base);

		return $lista;
	}
}
	$matriz = [
				[1,2,3],
				[4,5,6],
				[7,8,9],
			  ];

	$agente = new Agente();
	$no = new No();

	$sucessor = $agente->sucessor($matriz);

	print_r($sucessor);