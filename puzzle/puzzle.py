import os
import copy

# First Printar Estado Inicial
# Printar os Sucessores
#TO DO busca em largura
#    busca profundidade

class No () :
	
	def __init__ (self, estado, pai = "", acao = "", profundidade = "", custo = "") :

		self.estado       = estado
		self.pai          = pai
		self.acao         = acao
		self.profundidade = profundidade
		self.custo        = custo

#ver se ele esta ordenado, se sim retorna true
#busca em largura 

class Agente () :

	def printa_puzzle(self,puzzle) :

		print("+----+----+----+")
		print("| %d  | %d  | %d  |" % (puzzle["a1"], puzzle["a2"], puzzle["a3"]))
		print("+----+----+----+")
		print("| %d  | %d  | %d  |" % (puzzle["b1"], puzzle["b2"], puzzle["b3"]))
		print("+----+----+----+")
		print("| %d  | %d  | %d  |" % (puzzle["c1"], puzzle["c2"], puzzle["c3"]))
		print("+----+----+----+")

	def sucessor(self, puzzle, lista) :
			print("Raven Black")
			base_up    = copy.deepcopy(puzzle.estado)
			base_down  = copy.deepcopy(puzzle.estado)
			base_left  = copy.deepcopy(puzzle.estado)
			base_rigth = copy.deepcopy(puzzle.estado)

			lista.append(No(self.up(base_up)  , puzzle, "up",    0, 0))
			lista.append(No(self.down(base_down), puzzle, "down",    0, 0))
			lista.append(No(self.left(base_left), puzzle, "left",    0, 0))
			lista.append(No(self.rigth(base_rigth), puzzle, "rigth",    0, 0))

			return lista

	def achar_vazio(self,puzzle) :
			
		for celula in puzzle :
			if (puzzle[celula] == 0) :
				return celula

	def busca_profundidade(self, puzzle, lista) : 
		return True

	def busca_largura(self, puzzle) : 
		return True

	def busca_aprof_iterativa(self, puzzle) :
		limite = 0

		while (r == nulo) : 
			r = buscaProfLimitada(puzzle, l)
			limite = limite + 1
		
		return r

	def compara(self,puzzle1, puzzle2) :

		for chave in puzzle1 :		
			if (puzzle1[chave] != puzzle2[chave]) :
				return False
		
		return True

	def up(self,puzzle) :

			posicao_vazia = self.achar_vazio(puzzle)

			if (posicao_vazia == "a1") :
				puzzle["a1"] = puzzle["b1"]
				puzzle["b1"] = 0

			if (posicao_vazia == "a2") :
				puzzle["a2"] = puzzle["b2"]
				puzzle["b2"] = 0

			if (posicao_vazia == "a3") :
				puzzle["a3"] = puzzle["b3"]
				puzzle["b3"] = 0

			if (posicao_vazia == "b1") :
				puzzle["b1"] = puzzle["c1"]
				puzzle["c1"] = 0

			if (posicao_vazia == "b2") :
				puzzle["b2"] = puzzle["c2"]
				puzzle["c2"] = 0

			if (posicao_vazia == "b3") :
				puzzle["b3"] = puzzle["c3"]
				puzzle["c3"] = 0

			return puzzle

	def down(self,puzzle):

			posicao_vazia = self.achar_vazio(puzzle)

			if (posicao_vazia == "c1") :
				puzzle["c1"] = puzzle["b1"]
				puzzle["b1"] = 0

			if (posicao_vazia == "c2") :
				puzzle["c2"] = puzzle["b2"]
				puzzle["b2"] = 0

			if (posicao_vazia == "c3") :
				puzzle["c3"] = puzzle["b3"]
				puzzle["b3"] = 0

			if (posicao_vazia == "b1") :
				puzzle["b1"] = puzzle["a1"]
				puzzle["a1"] = 0

			if (posicao_vazia == "b2") :
				puzzle["b2"] = puzzle["a2"]
				puzzle["a2"] = 0

			if (posicao_vazia == "b3") :
				puzzle["b3"] = puzzle["a3"]
				puzzle["a3"] = 0

			return puzzle

	def left(self,puzzle) :

			posicao_vazia = self.achar_vazio(puzzle)

			if (posicao_vazia == "c1") :
				puzzle["c1"] = puzzle["c2"]
				puzzle["c2"] = 0

			if (posicao_vazia == "c2") :
				puzzle["c2"] = puzzle["c3"]
				puzzle["c3"] = 0

			if (posicao_vazia == "b1") :
				puzzle["b1"] = puzzle["b2"]
				puzzle["b2"] = 0

			if (posicao_vazia == "b2") :
				puzzle["b2"] = puzzle["b3"]
				puzzle["b3"] = 0

			if (posicao_vazia == "a1") :
				puzzle["a1"] = puzzle["a2"]
				puzzle["a2"] = 0

			if (posicao_vazia == "a2") :
				puzzle["a2"] = puzzle["a3"]
				puzzle["a3"] = 0

			return puzzle

	def rigth(self,puzzle) :
		
		posicao_vazia = self.achar_vazio(puzzle)

		if (posicao_vazia == "a2") :
			puzzle["a2"] = puzzle["c1"]
			puzzle["a1"] = 0

		if (posicao_vazia == "a3") :
			puzzle["a3"] = puzzle["a2"]
			puzzle["a2"] = 0

		if (posicao_vazia == "b2") :
			puzzle["b2"] = puzzle["b1"]
			puzzle["b1"] = 0

		if (posicao_vazia == "b3") :
			puzzle["b3"] = puzzle["b2"]
			puzzle["b2"] = 0
		
		if (posicao_vazia == "c2") :
			puzzle["c2"] = puzzle["c1"]
			puzzle["c1"] = 0

		if (posicao_vazia == "c3") :
			puzzle["c3"] = puzzle["c2"]
			puzzle["c2"] = 0

		return puzzle

	def buscaLargura(self, lista, no, objetivo) :
 		
 		while (self.compara(lista[0].estado, objetivo) != True) :
 			
 			lista = self.sucessor(lista[0],lista)
 			
 			print(len(lista))

 			lista.pop()

 			print(len(lista))
 		
     		#print(lista)
     	return lista
     	#print("este é o fera",lista[0].estado)


def main() :

	puzzle = {
		"a1": 1, "a2": 2, "a3": 3,
		"b1": 4, "b2": 5, "b3": 6,
		"c1": 7, "c2": 8, "c3": 0,
	}

	objetivo = {
		"a1": 1, "a2": 2, "a3": 3,
		"b1": 4, "b2": 0, "b3": 5,
		"c1": 7, "c2": 8, "c3": 6,
	}
	
	lista_sucessores = []

	agente = Agente()
	inicio = No(puzzle)

	print("ORIGINAL ------")
	agente.printa_puzzle(inicio.estado)
	print("------------")

	lista = agente.sucessor(inicio, lista_sucessores)
	#print(lista)
	agente.buscaLargura(lista, inicio, objetivo)

	# for l in lista :
	# #	agente.printa_puzzle(l.estado)
	# 	res = agente.compara(inicio.estado, l.estado)
	# 	if (res == True) :
	# 		res = "Igual"
	# 	else : 
	# 		res = "Nao igual"

	# 	print(l.acao , " : ", res)
	


if __name__ == "__main__":
	main()