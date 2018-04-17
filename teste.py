import sys

quadro = {'length':0, 'checksum':0, 'id':0, 'flags':0, 'dados':'0b0'}

def getQuadroInfo(sequenciaBinaria):
	# sequenciaBinaria: string com todos os dados no formato de enquadramento por contagem
	# considera que os dados no formato:
	# 	SYNC | SYNC | length | chksum | ID | flags | dados
	
	sequenciaBinaria = sequenciaBinaria[2:] # remove o '0b' do inicio
	x = sequenciaBinaria[:16]
	x = int(x, 2) # converte de base 2 para 10
	# x = socket.ntohs(x) # converte de network-order para host-order
	quadro['length'] = x
	
	x = sequenciaBinaria[16:32]
	x = int(x, 2) # converte de base 2 para 10
	quadro['checksum'] = x
	# x = socket.ntohs(x)
	
	x = sequenciaBinaria[32:40]
	x = int(x, 2) # converte de base 2 para 10
	quadro['id'] = x
	# x = socket.ntohs(x)
	
	x = sequenciaBinaria[40:48]
	x = int(x, 2) # converte de base 2 para 10
	quadro['flags'] = x
	# x = socket.ntohs(x)
	
	tamDados = quadro['length']
	quadro['dados'] = sequenciaBinaria[48:(48 + 8*tamDados)]
	# x = socket.ntohs(x)
	

num = '0b00000000000000010000000000000000000000000000000011111111'

#seq = bin(num)
getQuadroInfo(num)
print(quadro)
