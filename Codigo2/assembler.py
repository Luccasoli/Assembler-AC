# lib para trabalhar com argumentos
import sys

def verificador(argumento):
	try:
		file_name = argumento[1]
	except IndexError:
		print("Não foi passado nenhum arquivo")
		sys.exit(0)

	if(not file_name.endswith(".s")):
		print("O arquivo informado não é válido! (!= .s)")
		sys.exit(0)
	try:
			# Acessa um arquivo para leitura
			arq = open(file_name, 'r')
			arq.close()
	except FileNotFoundError as e:
			print("O arquivo informado não existe!") 
			sys.exit(0)
	return argumento[1]

def main():
	
	file_name = verificador(sys.argv)
	
	nomeArqFinal = file_name
	nomeArqFinal.replace('.s', '.m')

	arq = open(file_name, 'r')
	codigoCompleto = arq.readlines()

	codigoCompleto.remove('\n')

	print(codigoCompleto)

if __name__ == "__main__":
	main()