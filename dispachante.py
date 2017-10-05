# Class principal de definicao dos processos
class Processo:
	
	def __init__(self, pid, tempo_init, prioridade, tempo_cpu, quant_mem, impressora, scanner, modem, disco):
		self.pid     	= pid 
		self.tempo_init = tempo_init
		self.prioridade = prioridade
		self.tempo_cpu  = tempo_cpu
		# self.offset     = offset # esse valor a gente vai ter que calcular a partir do gerenciador de arquivos eu acho
		self.quant_mem  = quant_mem
		self.impressora = impressora
		self.scanner    = scanner
		self.modem      = modem
		self.disco      = disco


def dispachante_init(caminho_proc, caminho_arq):

	# Lista representacao de processos no formato da entrada
	strings_proc = []
	# Lista de processos
	processos = []

	le_arquivo(caminho_proc, strings_proc)
	prepara_procs(strings_proc, processos)
	imprime_processos(processos)

def le_arquivo(caminho, strings_proc):
	
	try:
		fp = open(caminho, 'r')
		
		for line in fp:
			linha = line.replace('\n', '')
			strings_proc.append(linha)

		fp.close()
	except FileNotFoundError:
		print("!! Arquivo nao encontrado !!")

def prepara_procs(strings_proc, processos):
	# Lista de interios convertidos a partir das strings
	int_list = []
	# Contador de IDs dos processos
	pid = 1

	for string in strings_proc:
		int_list = list(map(int, string.split(',')))
		tempo_init = int(int_list[0])
		prioridade = int(int_list[1])
		tempo_cpu  = int(int_list[2])
		quant_mem  = int(int_list[3])
		impressora = int(int_list[4])
		scanner    = int(int_list[5])
		modem      = int(int_list[6])
		disco      = int(int_list[7])
		proc = Processo(pid, tempo_init, prioridade, tempo_cpu, quant_mem, impressora, scanner, modem, disco)
		processos.append(proc)
		pid += 1

def imprime_processos(processos):

	for proc in processos:
		print("\n")
		print("PID:        " + str(proc.pid))
		print("prioridade: " + str(proc.prioridade))
		# print("offset:   " + str(proc.offset))
		print("blocos:     " + str(proc.quant_mem))
		print("impressora: " + str(proc.impressora))
		print("scanner:    " + str(proc.scanner))
		print("modem:      " + str(proc.modem))
		print("disco:      " + str(proc.disco))
