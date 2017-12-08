"""
		Aqui é onde os arquivos .m(hexadecimais) serão gerados.
"""

file_name = input("Nome do arquivo a ser gerado: ")

file = open(file_name, 'w')
content = []

content.append("f0f0 f0f0 ")
#content.append(as conversões do .asm)
content.append(" f0f0 f0f0")

file.writelines(content)

file.close()