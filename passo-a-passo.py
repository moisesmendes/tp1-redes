# Ordem definida pelo professor:
# Lê arquivo de entrada -> Enquadra -> Codifica -> Transmite -> Recebe -> Decodifica - > Processa quadro -> Grava arquivo de saída
#------------------------------------------------

# Funcao que le texto de um arquivo de entrada lista.txt
def leitura_arquivo(filename='lista.txt'):
	arq = open(filename, 'r')
	texto = arq.read()
	print(texto)
	arq.close()
	return(texto)

# FUNCOES UTEIS:
	# ord('z') retorna valor ascii
	# chr(ord('z')) retorna char correspondente ao valor ascii
	# hex(10) retorna o valor inteiro passado como hexadecimal

# Funcao que converte cada caractere de uma string em seu valor ASCII hexadecimal
def str2hex(string):
	out = []
	for ch in string:
		out.append(hex(ord(ch)))
	return(out)
	
# Funcao que recebe uma lista de valores em hexadecimal e converte para base16
	# (basicamente remove os caracteres '0x' do inicio)
def encode16(hexlist):
	newlist = []
	for item in hexlist:
		
		item = item[2:]
		if(len(item)==1): # se o valor hexadecimal for tiver apenas 1 caractere
			item = ''.join(['0', item]) # acrescenta 0 antes (ex: 'a'->'0a')
			
		newlist.append(item)
	 
	result = ''.join(newlist)
	return(result)

# Funcao que recebe dados ja codificados em base16 e retorna o quadro no formato especificado
def enquadra(dados16):
	sync = 'dcc023c2'
	length = len(dados16) #TODO: usar network byte order
	# Cada hexadecimal representa 4 bits. Cada byte, 8 bits.
	# Entao nao eh necessario dividir por 2.
	length = round(length/2) #checar caso em que for impar
	
	length16 = hex(length)
	length16 = encode16([length16])
	
	checksum = 'zzzz'
	ID = '00'
	flags = '00'
	
	quadro = ''.join([sync, sync, length16, checksum, ID, flags, dados16])
	return(quadro)
	
	

text = leitura_arquivo()
hexa = str2hex(text)
print('hexa:\n', hexa)
print('tamanho: ', len(hexa))

r = encode16(hexa)
print('result:\n', r)
print('tamanho: ', len(r))

print('\n---------quadro final:--------\n', enquadra(r))





