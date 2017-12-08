"""
		Aqui é onde os arquivos .m(hexadecimais) serão gerados.
"""

file_name = input("Nome do arquivo a ser gerado: ")

file = open(file_name, 'w')
content = []


# HEADER

content.append("f0f0 f0f0 ")
content.append("as conversões do .asm")
content.append(" f0f0 f0f0")
file.writelines(content)

## resto do arquivo


file.close()