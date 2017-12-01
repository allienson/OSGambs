class Entrada_Saida:
	def __init__(self):
		self.impressora1 = True
		self.impressora2 = True
		self.scanner = True
		self.modem = True
		self.sata1 = True
		self.sata2 = True

	def recursos_estao_disponiveis(self,processo):
		if(processo.scanner != 0 and self.scanner == False):
			return False
		if(processo.modem != 0 and self.modem == False):
			return False
		if(self.impressora_indisponivel(processo.impressora)):
			return False
		if(self.sata_indisponivel(processo.sata)):
			return False
		return True

	def impressora_indisponivel(self, cod_imp):
		if(cod_imp == 1 and self.impressora1 == False):
			return True
		if(cod_imp == 2 and self.impressora2 == False):
			return True
		return False

	def sata_indisponivel(self, cod_sata):
		if(cod_sata == 1 and self.sata1 == False):
			return True
		if(cod_sata == 2 and self.sata2 == False):
			return True
		return False

	def alocar_recurso(self,processo):
		if(processo.scanner == 1):
			self.scanner = False
		if(processo.modem == 1):
			self.modem = False
		self.alocar_sata(processo)
		self.alocar_impressora(processo)
		return True


	def alocar_sata(self,processo):
		if(processo.sata == 1):
			self.sata1 = False
		elif(processo.sata == 2):
			self.sata2 = False

	def alocar_impressora(self,processo):
		if(processo.impressora == 1):
			self.impressora1 = False
		elif(processo.impressora == 2):
			self.impressora2 = False






	def liberar_recurso(self,processo):
		if(processo.scanner == 1):
			self.scanner = True
		if(processo.modem == 1):
			self.modem = True
		self.liberar_sata(processo)
		self.liberar_impressora(processo)
		return True


	def liberar_sata(self,processo):
		if(processo.sata == 1):
			self.sata1 = True
		elif(processo.sata == 2):
			self.sata2 = True

	def liberar_impressora(self,processo):
		if(processo.impressora == 1):
			self.impressora1 = True
		elif(processo.impressora == 2):
			self.impressora2 = True

