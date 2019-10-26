import os
import copy

# First Printar Estado Inicial
# Printar os Sucessores
#TO DO busca em largura
#    busca profundidade

class No () :
	
	def __init__ (self, estado, pai = None, acao = "", profundidade = 0, custo = "", h = "") :

		self.estado       = estado
		self.pai          = pai
		self.acao         = acao
		self.profundidade = profundidade
		self.custo        = custo
		self.h            = h

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
			
		base_up    = copy.deepcopy(puzzle.estado)
		base_down  = copy.deepcopy(puzzle.estado)
		base_left  = copy.deepcopy(puzzle.estado)
		base_rigth = copy.deepcopy(puzzle.estado)

		if puzzle.profundidade > 0 :
			profundidade = copy.deepcopy(puzzle.profundidade)
			profundidade = profundidade + 1
		else :
			profundidade = 0

		lista.append(No(self.up(base_up)      , puzzle, "down"   ,  profundidade, 1))
		lista.append(No(self.down(base_down)  , puzzle, "up" ,  profundidade, 1))
		lista.append(No(self.left(base_left)  , puzzle, "rigth" ,  profundidade, 1))
		lista.append(No(self.rigth(base_rigth), puzzle, "left",  profundidade, 1))

		return lista

	def achar_vazio(self,puzzle) :
			
		for celula in puzzle :
			if (puzzle[celula] == 0) :
				return celula

	def compara(self,original, objetivo) :

		for chave in original :
		
			if original[chave] != objetivo[chave] :
				
				return False

		return True

	def down(self,puzzle) :

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

	def up(self,puzzle):

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

	def rigth(self,puzzle) :

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

	def left(self,puzzle) :
		
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

	def custo_uniforme(self, lista_nos, objetivo, lista_ordenada) :
		print("Objetivo: ")
		self.printa_puzzle(objetivo)
		print("-----------------------")

		lista_ordenada = sorted (lista_nos, key = no.custo)
		for no in lista_ordenada :
			print("-----------------------")
			self.printa_puzzle(no.estado)
			print(no.acao)
			print("-----------------------")

			if self.compara(no.estado,objetivo) == True :
				print("Achou")
				print(no.acao)

				lista_acao = []
				pai = no.pai
				lista_acao.append(no.acao)

				while (pai != None) :
					pai_acao = pai.acao
					print(pai_acao)
					lista_acao.append(pai_acao)
					pai = pai.pai

				self.printa_puzzle(no.estado)
				break
			else :
				node = lista_nos.pop(0)
				lista_nos = self.sucessor(node, lista_nos)

	def busca_largura(self, lista_nos, objetivo) : 
		i = 0
		for no in lista_nos :
			print("ESTADO")
			self.printa_puzzle(no.estado)
			print("OBJETIVO")
			self.printa_puzzle(objetivo)
			print(len(lista_nos))
			if self.compara(no.estado, objetivo) == True :
				print("Achou")
				print(no.acao)
				lista_acao = []
				pai = no.pai
				lista_acao.append(no.acao)

				while (pai != None) :
					pai_acao = pai.acao
					print(pai_acao)
					lista_acao.append(pai_acao)
					pai = pai.pai
				return lista_acao

			else :
				
				print("AAAAAA NAO")
				self.printa_puzzle(no.estado)
				
		
				node = lista_nos.pop(0)
				lista_nos = self.sucessor(node, lista_nos)

	def h1(self, original, objetivo) :

		cont = 0; 

		for chave in original :
			if objetivo[chave] != 0 :
				if original[chave] != objetivo[chave] :
					cont = cont + 1
		

		return cont


	#def h2(self, original, objetivo) :
		#retorna a soma das distancias da peca para o lugar correto

	def busca_profundidade (self, lista_nos, objetivo, limite) :

		while len(lista_nos) > 0 :
			no = lista_nos.pop()
			if compara(no.estado, objetivo) == True : 
				print("Achou")
				self.printa_puzzle(no.estado)
				return no
			else : 
				self.sucessor(no, lista_nos)

		return None
		
	def busca_profundidade_limitada (self, lista_nos, objetivo, limite) :

		while len(lista_nos) > 0 :
			no = lista_nos.pop()
			if self.compara(no.estado, objetivo) == True : 
				print("Achou")
				self.printa_puzzle(no.estado)
				return no
			else : 
				if no.profundidade < limite :
					self.sucessor(no, lista_nos)
		return None

	def busca_profundidade_iterativa (self, lista_nos, objetivo) : 
		
		limite = 0
		
		while (r != None) :
			
			r = busca_profundidade_limitada()
				
			limite = limite + 1
		
		return r

def main() :

	puzzle = {
		"a1": 1, "a2": 2, "a3": 3,
		"b1": 0, "b2": 5, "b3": 6,
		"c1": 4, "c2": 7, "c3": 8,
	}

	objetivo = {
		"a1": 1, "a2": 2, "a3": 3,
		"b1": 4, "b2": 5, "b3": 6,
		"c1": 7, "c2": 8, "c3": 0,
	}
	
	lista_sucessores = []

	agente = Agente()
	inicio = No(puzzle)

	print("ORIGINAL ------")
	agente.printa_puzzle(inicio.estado)
	print("------------")
	lista_sucessores.append(inicio)

	lista_acao = agente.busca_largura(lista_sucessores, objetivo)

	#no = agente.busca_profundidade_limitada(lista_sucessores, objetivo, 3)
	#print(no.acao)

	#h1 = agente.h1(puzzle, objetivo)
	#print(h1)
	
if __name__ == "__main__":
	main()