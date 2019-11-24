import os
import copy
import random

class No () :
	
	def __init__ (self, estado, pai = None, acao = "", profundidade = 0, h1 = "", h2 = "") :

		self.estado       = estado
		self.pai          = pai
		self.acao         = acao
		self.profundidade = profundidade
		self.h1           = h1
		self.h2           = h2

class Agente () :

	def __init__ (self, resultado) :
		self.objetivo = resultado

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

		no_up     = No(self.down(base_down)  , puzzle, "sobe" ,  profundidade)
		upH1      = self.heuristicaH1(no_up.estado)
		no_up.h1  = upH1
		upH2      = self.heuristicaH2(no_up.estado)
		no_up.h2  = upH2

		no_down    = No(self.up(base_up), puzzle, "desce"   ,  profundidade)
		downH1     = self.heuristicaH1(no_down.estado)
		no_down.h1 = downH1
		downH2     = self.heuristicaH2(no_down.estado)
		no_down.h2 = downH2

		no_right    = No(self.left(base_left)  , puzzle, "direita" ,  profundidade)
		rigthH1     = self.heuristicaH1(no_right.estado)
		no_right.h1 = rigthH1
		rigthH2     = self.heuristicaH2(no_right.estado)
		no_right.h2 = rigthH2

		no_left    = No(self.rigth(base_rigth), puzzle, "esquerda",  profundidade)
		leftH1     = self.heuristicaH1(no_left.estado)
		no_left.h1 = leftH1
		leftH2     = self.heuristicaH2(no_left.estado)
		no_left.h2 = leftH2

		lista.append(no_down)
		lista.append(no_up)
		lista.append(no_right)
		lista.append(no_left)

		return lista

	def achar_vazio(self,puzzle) :
			
		for celula in puzzle :
			if (puzzle[celula] == 0) :
				return celula

	def compara(self,original) :

		for chave in original :
		
			if original[chave] != self.objetivo[chave] :
				
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

	def heuristicaH1(self, original) :

		cont = 0; 

		for chave in original :
			if self.objetivo[chave] != 0 :
				if original[chave] != self.objetivo[chave] :
					cont = cont + 1
	
		return cont
	
	def heuristicaH2(self, original) :
		
		a = 1

		return a

	def gme (self, lista_nos, h) :
		print("GME")
		i = 0

		for no in lista_nos :
			print("atual: ", no.h1)
			print("----------------------")
			self.printa_puzzle(no.estado)
			
			if i == 2 :
				exit()

			i += 1

			if self.compara(no.estado) == True :
				print(no.acao)
				lista_acao = []
				pai = no.pai
				lista_acao.append(no.acao)
				print("final: ")
				print(lista_nos)
				while (pai != None) :
					pai_acao = pai.acao
					print(pai_acao)
					lista_acao.append(pai_acao)
					pai = pai.pai
				return lista_acao

			else :
				node = lista_nos.pop(0)
				lista_nos = self.sucessor(node, lista_nos)
				lista_nos_aux = copy.deepcopy(lista_nos)

				if h == 1 :
					print("validacao =====")
					lista_nos = self.sortAmigo(lista_nos)

	def sortAmigo(self, lista) :

		elementos = len(lista) - 1
		ordenado = False
		while not ordenado : 
			ordenado = True
			for i in range(elementos) :
				if lista[i].h1 > lista[i+1].h1 :
					lista[i], lista[i+1] = lista[i+1], lista[i]
					ordenado = False
		return lista

	def aEstrela(self, lista_nos) :

		print("estrela")
		
		for no in lista_nos :
			if self.compara(no.estado, self.objetivo) == True :
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
				node = lista_nos.pop(0)
				lista_nos = self.sucessor(node, lista_nos)

				if h == 1 :
					for idx, noh in enumerate(lista_nos) :
						for noh2 in lista_nos :
							if (idx + 1) < len(lista_nos) :
								if lista_nos[idx].h1 + lista_nos[idx].profundidade > lista_nos[int(idx) + 1].h1 + lista_nos[int(idx) + 1].profundidade : 
									menor_no = [lista_nos[idx]]

				lista_nos = menor_no 


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
		"b1": 4, "b2": 5, "b3": 6,
		"c1": 0, "c2": 7, "c3": 8,
	}

	objetivo = {
		"a1": 1, "a2": 2, "a3": 3,
		"b1": 4, "b2": 5, "b3": 6,
		"c1": 7, "c2": 8, "c3": 0,
	}
	
	lista_sucessores = []

	agente = Agente(objetivo)
	inicio = No(puzzle)

	print("ORIGINAL ------")
	agente.printa_puzzle(inicio.estado)
	print("------------")
	lista_sucessores.append(inicio)

	lista_acao = agente.gme(lista_sucessores, 1)
	print(lista_acao)
	#lista_acao = agente.aEstrela(lista_sucessores, 1)

	#lista_acao = agente.gme(lista_sucessores, 2)

	
if __name__ == "__main__":
	main()