#######################
# Modulo de Processos #
#######################

# Class principal de definicao dos processos
class Processo:
	
	tempo_decorrido = 0
	arq_criados = []


	def __init__(self, pid, tempo_init, prioridade, tempo_cpu, quant_mem, impressora, scanner, modem, sata):
		self.pid     	= pid 
		self.tempo_init = tempo_init
		self.prioridade = prioridade
		self.tempo_cpu  = tempo_cpu
		self.quant_mem  = quant_mem
		self.impressora = impressora
		self.scanner    = scanner
		self.modem      = modem
		self.sata      	= sata
		self.inicio_memoria = 0

	def final_memoria(self):
		return self.inicio_memoria + self.quant_mem 


