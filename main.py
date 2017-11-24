from despachante import despachante_init
import sys

# Le os argumentos em linha de comando, se tiverem sido utilizados.
# Se nao, pede ao usuario que insira os caminhos
if len(sys.argv) > 2:
	caminho_proc = sys.argv[1]
	caminho_arq = sys.argv[2]
else:
	#caminho_proc = input("Informe o caminho completo para o arquivo TXT de processos:")
	#caminho_arq = input("Informe o caminho completo para o arquivo TXT de arquivos:")

	caminho_proc = "txt/processos.txt"
	caminho_arq = "txt/arquivos.txt"

# Executa o modulo do Despachante
despachante_init(caminho_proc, caminho_arq)


