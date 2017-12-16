# lib para trabalhar com argumentos e outras mais (ignore)
import sys
import re
from Header import Header

# Extrai a quantidade de instruçoes, quantidade de identificadores, uma lista do conteudo DATA
# e outra lista com conteudo de TEXT e poe tudo no objeto !header!
def qntInstrucoes(header, codigoCompleto):
	estouEmText = False
	estouEmData = False
	listaData = []
	listaText = []
	contIdentificadores = 0

	for linha in codigoCompleto:
		if(linha.find('.text') != -1):
			estouEmText = True
			estouEmData = False
						
		elif(estouEmText):
			aux = re.sub('\s+',' ',linha).strip()
			listaText.append(aux)
			if(aux.endswith(':')):
				contIdentificadores += 1

		elif(linha.find('.data') != -1):
			estouEmText = False
			estouEmData = True
						
		elif(estouEmData):
			aux = re.sub('\s+',' ',linha).strip()
			linhasData.append(aux)
			if(aux.endswith(':')):
				contIdentificadores += 1

	
	header.qntIdentificadores = contIdentificadores
	header.listaData = listaData
	header.qntInstrucoes = ((len(listaText)+len(listaData))-contIdentificadores)
	
# Verifica a validade do argumento na chamada do programa
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

###############################################################

def main():
	
	file_name = verificador(sys.argv)
	
	nomeArqFinal = file_name
	nomeArqFinal.replace('.s', '.m')

	arq = open(file_name, 'r')
	codigoCompleto = arq.readlines()

	codigoCompleto.remove('\n')
	header = Header()
	qntInstrucoes(header, codigoCompleto)
	print(header.qntInstrucoes)

	content = []

	# HEADER

	content.append("f0f0 f0f0 ")
	content.append("0000 0000 ")
	content.append(hex(header.qntInstrucoes))
	content.append(" f0f0 f0f0")

	print(content)

if __name__ == "__main__":
	main()