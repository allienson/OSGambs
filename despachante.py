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
processos_usuario1 = []
processos_usuario2 = []
processos_usuario3 = []

tempo = 0


# Inicializa a execucao do SO
def despachante_init(caminho_proc, caminho_arq):
    # Lista representacao de processos no formato da entrada
    strings_proc = []

    #le_arquivo(, strings_proc)
    prepara_filas_proc(caminho_proc)

    executa_processos()


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
def prepara_filas_proc(caminho):

    fh = open(caminho, 'r')    
    # Contador de IDs dos processos
    pid = 1

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
        disco = int(int_list[7])

        proc = Processo(pid, tempo_init, prioridade, tempo_cpu, quant_mem, impressora, scanner, modem, disco)
        pid += 1

        if (prioridade == 0):
            processos_real.append(proc)
        elif (prioridade == 1):
            processos_usuario1.append(proc)
        elif (prioridade == 2):
            processos_usuario2.append(proc)
        elif (prioridade == 3):
            processos_usuario3.append(proc)
        else:
            print("Prioridade inválida")
            exit(0)

    processos_real.sort(key=lambda x: x.tempo_init)  # Ordena os processos por ordem de chegada
    processos_usuario1.sort(key=lambda x: x.tempo_init)
    processos_usuario2.sort(key=lambda x: x.tempo_init)
    processos_usuario3.sort(key=lambda x: x.tempo_init)
    print(processos_real)

#def escalonador(proc):
    # if proc.prioridade == 0:
 #   imprime_processo(proc)
  #  executa_processo(proc)
    # else:

#    processos_real.pop()


def executa_processos():
    global tempo

    while ((len(processos_real) != 0) or (len(processos_usuario1) != 0) or (len(processos_usuario2) != 0) or (len(processos_usuario3) != 0)):
        print(tempo)

        if ((len(processos_real) != 0) and (processos_real[0].tempo_init <= tempo)):
            executa_real(processos_real[0])
        elif ((len(processos_usuario1) != 0) and (processos_usuario1[0].tempo_init <= tempo)):
            executa_usuario(processos_usuario1[0], processos_usuario1)
        elif ((len(processos_usuario2) != 0) and (processos_usuario2[0].tempo_init <= tempo)):
            executa_usuario(processos_usuario2[0], processos_usuario2)
        elif ((len(processos_usuario3) != 0) and (processos_usuario3[0].tempo_init <= tempo)):
            executa_usuario(processos_usuario3[0], processos_usuario3)
        else:
            tempo += 1


def executa_real(proc):
    global tempo
    for i in range(0, proc.tempo_cpu):
        print("    P" + str(proc.pid) + " instrucao " + str(i + 1))
        time.sleep(1)

    processos_real.pop(0)
    tempo += proc.tempo_cpu


def executa_usuario(proc, fila):
    global tempo
    tempo += 1
    proc.tempo_cpu -= 1
    proc.tempo_decorrido += 1

    print("    P" + str(proc.pid) + " instrucao " + str(proc.tempo_decorrido))
    time.sleep(1)

    if (proc.tempo_cpu == 0):
        fila.pop(0)


# Imprime os dados de cada processo executado pelo dispachante
# def imprime_processo(proc):
#     print("Dispachante =>")
#     print("    PID:        " + str(proc.pid))
#     print("    prioridade: " + str(proc.prioridade))
#     # print("    offset:   " + str(proc.offset))
#     print("    blocos:     " + str(proc.quant_mem))
#     print("    impressora: " + str(proc.impressora))
#     print("    scanner:    " + str(proc.scanner))
#     print("    modem:      " + str(proc.modem))
#     print("    disco:      " + str(proc.disco))
#     print("\n")
#  str(proc.quant_mem))
#     print("    impressora: " + str(proc.impressora))
#     print("    scanner:    " + str(proc.scanner))
#     print("    modem:      " + str(proc.modem))
#     print("    disco:      " + str(proc.disco))
#     print("\n")
