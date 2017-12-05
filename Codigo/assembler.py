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

			# Lê cada linha do arquivo e transforma em uma lista de strings
			lista = arq.readlines()

			for l in lista:
				print(l[:-1])

		except FileNotFoundError as e:
			print("O arquivo informado não existe!") 
			break

	else:	# Finaliza o programa caso a extensão seja incorreta
		print("O arquivo informado não é válido! (!= .asm)")
		break

	print("n imprime")
