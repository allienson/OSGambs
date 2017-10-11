###################
# Modulo de Filas #
###################

from processo import Processo
import time

# Fila geral de processos
processos = []
# Fila de processos de tempo real
processos_real = []
# Fila de processos de usuario
processos_usuario = []

# Inicializa a execucao do SO
def despachante_init(caminho_proc, caminho_arq):

	# Lista representacao de processos no formato da entrada
	strings_proc = []

	le_arquivo(caminho_proc, strings_proc)
	prepara_proc_geral(strings_proc)
	
	for proc in processos:
		escalonador(proc)

# Le um arquivo texto e salva em uma lista de strings
# onde cada string eh referente a uma linha do arquivo
def le_arquivo(caminho, strings_proc):
	
	try:
		fp = open(caminho, 'r')
		
		for line in fp:
			linha = line.replace('\n', '')
			strings_proc.append(linha)

		fp.close()
	except FileNotFoundError:
		print("!! Arquivo nao encontrado !!")

# Popula a fila geral de processos com objetos do classe
# Processo atraves dos dados lidos do arquivo txt
def prepara_proc_geral(strings_proc):
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

	processos.sort(key=lambda x: x.tempo_init) # Ordena os processos por ordem de chegada


def escalonador(proc):
	if proc.prioridade == 0:
		imprime_processo(proc)
		executa_processo(proc)
	else:
		


def executa_processo(proc):

	print("Processo " + str(proc.pid) + "=>")
	print("    P" + str(proc.pid) + " STARTED")
	
	for i in range(0, proc.tempo_cpu):
		print("    P" + str(proc.pid) + " instrucao " + str(i+1))
		time.sleep(1)
	
	print("    P" + str(proc.pid) + " return SIGINT")
	time.sleep(1)
	print("\n")

# Imprime os dados de cada processo executado pelo dispachante
def imprime_processo(proc):

	print("Dispachante =>")
	print("    PID:        " + str(proc.pid))
	print("    prioridade: " + str(proc.prioridade))
	# print("    offset:   " + str(proc.offset))
	print("    blocos:     " + str(proc.quant_mem))
	print("    impressora: " + str(proc.impressora))
	print("    scanner:    " + str(proc.scanner))
	print("    modem:      " + str(proc.modem))
	print("    disco:      " + str(proc.disco))
	print("\n")
