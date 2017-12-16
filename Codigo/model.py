"""
		Aqui vai ser a classe que vai conter os registradores e as instruções(o mips...)
"""

class MIPS: 

	## REGISTRADORES

	# Os registradores são case insensitive, então lembrar de quando sempre que ler um reg usar .lowercase ou .uppercase
	regs_by_name = ['$zero', '$at', '$v0', '$v1', '$a0', '$a1', '$a2', '$a3', '$t0', '$t1', '$t2', '$t3', '$t4', '$t5', '$t6', '$t7', '$s0', '$s1', '$s2', '$s3', '$s4', '$s5', '$s6', '$s7', '$t8', '$t9', '$k0', '$k1', '$gp', '$sp', '$fp', '$ra']

	regs_by_num = ['$0', '$1', '$2', '$3', '$4', '$5', '$6', '$7', '$8', '$9', '$10', '$11', '$12', '$13', '$14', '$15', '$16', '$17', '$18', '$19', '$20', '$21', '$22', '$23', '$24', '$25', '$26', '$27', '$28', '$29', '$30', '$31']
	"""
		$at/$1 = assembler temporary
		$v0/$2 ~ $v1/$3 = values for function returns and expression evaluation
		$a0/$4 ~ $a3/$7 = function arguments
		$t0/$8 ~ $t7/$15 = temporaries (caller-saved)
		$s0/$16 ~ $s7/$23 = saved temporaries (callee-saved)
		$t8/$24 ~ $t9/$25 = temporaries (caller-saved)
		$k0/$26 = reserved for OS kernel
		$gp/$28 = global pointer
		$sp/$29 = stack pointer
		$fp/$30 = frame pointer
		$ra/$31 = return address
	"""

# ************************************************************************************************

	## INSTRUÇÕES

	# Instruções em excesso, tem que filtrar dps
	# olhar opcode no arquivo pra fazer o map(acho que vai precisar msm)
	instructions_r = ['add', 'addu', 'sub', 'subu', 'mult', 'multu', 'div', 'divu', 'mfhi', 'mflo', 'and', 'or', 'xor', 'nor', 'slt', 'sltu', 'sll', 'sllv', 'srl', 'srlv', 'sra', 'srav', 'jr', 'jalr', 'syscall']

	instructions_i = ['addi', 'addiu', 'lw', 'lh', 'lhu', 'lb', 'lbu', 'sw', 'sh', 'sb', 'lui', 'ori', 'andi', 'xori', 'slti', 'sltiu', 'beq', 'bne']

	instructions_j = ['j', 'jal']


	## DIRECTIVES

	# Faltam várias eu acho, até pq n tem a .word por exemplo, que é uma das principais
	directives = ['.text', '.data', '.long', '.byte', '.short', '.space', '.ascii']
	"""
		.long val
		.byte val
		.short val
		.space size
		.ascii string
	"""

# ************************************************************************************************

	## criar map e métodos

	mapReg = {'$zero': '$zero', '$0': '$zero', 
	'$at': '$at', '$1': '$at',
	'$v0': '$v0', '$$2': '$v0',
	'$v1': '$v1', '$3': '$v1',
	'$a0': '$a0', '$4': '$a0',
	'$a1': '$a1', '$5': '$a1',
	'$a2': '$a2', '$6': '$a2',
	'$a3': '$a3', '$7': '$a3',
	'$t0': '$t0', '$8': '$t0',
	'$t1': '$t1', '$9': '$t1',
	'$t2': '$t2', '$10': '$t2',
	'$t3': '$t3', '$11': '$t3',
	'$t4': '$t4', '$12': '$t4',
	'$t5': '$t5', '$13': '$t5',
	'$t6': '$t6', '$14': '$t6',
	'$t7': '$t7', '$15': '$t7',
	'$s0': '$s0', '$16': '$s0',
	'$s1': '$s1', '$17': '$s1',
	'$s2': '$s2', '$18': '$s2',
	'$s3': '$s3', '$19': '$s3',
	'$s4': '$s4', '$20': '$s4',
	'$s5': '$s5', '$21': '$s5',
	'$s6': '$s6', '$22': '$s6',
	'$s7': '$s7', '$23': '$s7',
	'$t8': '$t8', '$24': '$t8',
	'$t9': '$t9', '$25': '$t9',
	'$k0': '$k0', '$26': '$k0',
	'$k1': '$k1', '$27': '$k1',
	'$gp': '$gp', '$28': '$gp',
	'$sp': '$sp', '$29': '$sp',
	'$fp': '$fp', '$30': '$fp',
	'$ra': '$ra', '$31': '$ra',
	}