####################
# Modulo de Leitor #
####################

from processo import Processo
from disco import Disco

# Popula a fila geral de processos com objetos do classe
# Processo atraves dos dados lidos do arquivo txt
def preparar_processos(caminho):
    fh = open(caminho, 'r')
    # Contador de IDs dos processos
    pid = 0
    processos = list()

    for linha in fh:
        linha = linha.replace(" ","").replace("\n", "")
        int_list = linha.split(',')

        tempo_init = int(int_list[0])
        prioridade = int(int_list[1])
        tempo_cpu = int(int_list[2])
        quant_mem = int(int_list[3])
        impressora = int(int_list[4])
        scanner = int(int_list[5])
        modem = int(int_list[6])
        sata = int(int_list[7])

        proc = Processo(pid, tempo_init, prioridade, tempo_cpu, quant_mem, impressora, scanner, modem, sata)
        pid += 1
        processos.append(proc)

    processos.sort(key=lambda x: x.tempo_init)
    return processos


def preparar_disco(caminho):
    disco = Disco()
    fh = open(caminho, 'r')

    tamanho = int(fh.readline())
    seg_ocup = int(fh.readline())
    disco.inicializa_disco(tamanho, seg_ocup)

    for i in range(2, seg_ocup + 2):
        linha = fh.readline()
        disco.add_arquivo(linha)

    for linha in fh:
        disco.add_operacao(linha)

    return disco
