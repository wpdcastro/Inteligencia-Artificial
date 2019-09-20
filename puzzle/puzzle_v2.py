import os

def achar_vazio(puzzle) :
	
	for celula in puzzle :
		if (puzzle[celula] == 0) :
			celula = celula.split("_")
			return celula

def down(puzzle):
	posicao_vazia = achar_vazio(puzzle)

	letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	
	letras_enumeradas = enumerate(letras)

	for letra in letras_enumeradas :
		if (letra[1] == posicao_vazia[0]) :
			posicao_nova_letra = letra[0] - 1

	local_puzzle = str(letras[posicao_nova_letra]) + "_" + str(posicao_vazia[1])
	novo_local   = str(posicao_vazia[0]) + "_" + str(posicao_vazia[1])

	puzzle[novo_local] = puzzle[local_puzzle]
	puzzle[local_puzzle] = 0

	return puzzle

def printa_puzzle(puzzle) :

	print("+----+----+----+")
	print("| %d   | %d   | %d  |" % (puzzle["a_1"], puzzle["a_2"], puzzle["a_3"]))
	print("+----+----+----+")
	print("| %d   | %d   | %d  |" % (puzzle["b_1"], puzzle["b_2"], puzzle["b_3"]))
	print("+----+----+----+")
	print("| %d   | %d   | %d  |" % (puzzle["c_1"], puzzle["c_2"], puzzle["c_3"]))
	print("+----+----+----+")
	print("| %d  | %d  | %d |" % (puzzle["d_1"], puzzle["d_2"], puzzle["d_3"]))
	print("+----+----+----+")

puzzle = {
	"a_1": 1, "a_2": 2, "a_3": 3,
	"b_1": 4, "b_2": 5, "b_3": 6,
	"c_1": 7, "c_2": 8, "c_3": 10,
	"d_1": 11, "d_2": 12, "d_3": 0,
}

printa_puzzle(puzzle)
puzzle = down(puzzle)
printa_puzzle(puzzle)