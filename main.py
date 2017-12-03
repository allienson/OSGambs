from despachante import despachante_init
import sys


def testa_caminho_arquivo(caminho):
    try:
      open(caminho, "r")
      return True
    except IOError:
      print("Error: Caminho incorreto.")
      exit(0)


# Le os argumentos em linha de comando, se tiverem sido utilizados.
# Se nao, pede ao usuario que insira os caminhos
if len(sys.argv) > 2:
	caminho_proc = sys.argv[1]
	caminho_arq = sys.argv[2]
	testa_caminho_arquivo(caminho_proc)
	testa_caminho_arquivo(caminho_arq)
else:
	caminho_proc = input("Informe o caminho completo para o arquivo TXT de processos:")
	testa_caminho_arquivo(caminho_proc)
	caminho_arq = input("Informe o caminho completo para o arquivo TXT de arquivos:")
	testa_caminho_arquivo(caminho_arq)

	#caminho_proc = "txt/processos.txt"
	#caminho_arq = "txt/arquivos.txt"

# Executa o modulo do Despachante
despachante_init(caminho_proc, caminho_arq)


