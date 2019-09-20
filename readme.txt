## implementar ##
# busca em largura
# busca em profundidade --> bem melhor pra memoria
# busca em aprofundamento iterativo


Busca e largura : encontrar solução na menor profundidade possivel

Completa :  sim, se b é finito
	b --> fator de ramificação
Otima: sim, se o custo sempre aumenta com a profundidade
Complexidade
	tempo  : O(b^d+1)
		de acordo com os nós gerados, 
		no puzzle 
			O(b^m)
	espaço : O(b^d+1)
		todos os nós gerados precisam estar na memória (os que sao realmente necessários)
		no puzzle
		O(b*m)

# busca em aprofundamento iterativo
recebe um nó base
limite 0

faz busca profundidade limitada 
se n for objetivo a busca falha e l++
faz a busca de novo com o limite novo