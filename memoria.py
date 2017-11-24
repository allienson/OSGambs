class Memoria:

	def  __init__(self):
		self.memoria_real =[]
		self.memoria_usuario = []
		self.inicializa_memoria()

	def inicializa_memoria(self):
		for i in range(0,64):
			self.memoria_real.append(0)

		for i in range(0,960):
			self.memoria_usuario.append(0)

	def memoria_disponivel(self,processo):
	    if(processo.prioridade == 0):
	    	return self.busca_memoria_real(processo)
	    else:
	    	return self.busca_memoria_usuario(processo)

	def busca_memoria_real(self,processo):
			count = 0
			for i in range(0,64):
				if self.memoria_real[i] == 0 :
					count +=1
				else:
					count = 0
				if (count == processo.quant_mem):
					processo.inicio_memoria = i - processo.quant_mem + 1
					for j in range(processo.inicio_memoria ,i+1):
						self.memoria_real[j] = 1
					return True
			print("Nao exite espaco suficiente na memoria de tempo real")
			return False

	def busca_memoria_usuario(self,processo):
			count = 0
			for i in range(0,960):
				if self.memoria_usuario[i] == 0 :
					count +=1
				else:
					count = 0
				if (count == processo.quant_mem):
					processo.inicio_memoria = i - processo.quant_mem + 1
					for j in range(processo.inicio_memoria ,i+1):
						self.memoria_usuario[j] = 1
					return True
			print("Nao exite espaco suficiente na memoria de usuario")
			return False

	def libera_memoria(self, processo):
		if(processo.prioridade == 0):
			return self.libera_memoria_real(processo)
		else:
			return self.libera_memoria_usuario(processo)

	def libera_memoria_real(self, processo):
		for i in range(processo.inicio_memoria, processo.final_memoria()):
			self.memoria_real[i] = 0

	def libera_memoria_usuario(self, processo):
		for i in range(processo.inicio_memoria, processo.final_memoria()):
			self.memoria_usuario[i] = 0