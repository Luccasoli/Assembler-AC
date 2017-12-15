# lib para trabalhar com argumentos
import sys

while True:
	
	# String de paramentro na chamada no terminal
	try:
		file_name = sys.argv[1]
	except IndexError:
		print("Não foi passado nenhum arquivo")
		break

	if(file_name.endswith(".asm")):	# Verfica se o arquivo informado tem a extensão correta (ACHAR UM FORMA DE INTERROMPER O PROGRAMA)
		try:
			# Acessa um arquivo para leitura
			arq = open(file_name, 'r')

			#Lê cada linha do arquivo e transforma em uma lista de strings
			codigoCompleto = arq.readlines()
			#codigoCompleto.remove('')

			# Lista de linhas de cada espaço
			linhasData = []
			linhasText = []
			estouEmData = False
			estouEmText = False

			# Lê o código uma vez
			for linha in codigoCompleto:
				if(linha.find('.text') != -1):
					estouEmText = True
					estouEmData = False
					
				elif(estouEmText):
					linhasText.append(linha)

				elif(linha.find('.data') != -1):
					estouEmText = False
					estouEmData = True
					
				elif(estouEmData):
					linhasData.append(linha)

			print(".data:")
			for aux in linhasData:
				print(aux)
			print(".text:")
			for aux in linhasText:
				print(aux)
			#for l in lista:
			#	print(l[:-1])
			#print(codigoCompleto)
			break

		except FileNotFoundError as e:
			print("O arquivo informado não existe!") 
			break

	else:	# Finaliza o programa caso a extensão seja incorreta
		print("O arquivo informado não é válido! (!= .asm)")
		break

