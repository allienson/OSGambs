#######################
# Modulo de Processos #
#######################

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
