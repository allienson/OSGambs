#########################
# Modulo de Despachante #
#########################

from processo import Processo
import time
from memoria import Memoria
from entrada_saida import Entrada_Saida
from fila import Fila
from disco import Disco


# Fila geral de processos
processos = []

memoria = Memoria()
recurso = Entrada_Saida()
disco   = Disco()
fila    = Fila()

tempo = 0


# Inicializa a execucao do SO
def despachante_init(caminho_proc, caminho_arq):
    # Lista representacao de processos no formato da entrada
    # strings_proc = []
    #preencher_processos(caminho_proc)
    #loop_controle()

    preencher_processos(caminho_proc)
    le_arqs(caminho_arq)
    loop_controle()
    executa_processos()

    disco.prepara_disco()
    disco.executa_operacoes(processos)
    disco.imprime_disco()

# Le um arquivo texto e salva em uma lista de strings
# onde cada string eh referente a uma linha do arquivo
def loop_controle():
    
    #for i in range(0,len(processos)):
    while (fila.existe_processos_para_executar()or len(processos) > 0):
        
        if((len(processos) > 0)):
            while ((processos[0].tempo_init <= tempo)):
                if(memoria.memoria_disponivel(processos[0])):
                    fila.adiciona_em_fila(processos.pop(0))
                else:
                    processos.pop(0)
                if(len(processos) == 0): break

        executa_processos()
    #print(memoria.memoria_real)


#def memoria_disponivel():
#    return True


# Popula a fila geral de processos com objetos do classe
# Processo atraves dos dados lidos do arquivo txt
def preencher_processos(caminho):

    fh = open(caminho, 'r')    
    # Contador de IDs dos processos
    pid = 0

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

def executa_processos():
    global tempo

    if (fila.existe_processo_real()):
        executa_real(fila.processos_real[0])
    elif (fila.existe_processo_1() and recurso.alocar_recurso(fila.processos_usuario1[0])):
        executa_usuario(fila.processos_usuario1[0], fila.processos_usuario1)
    elif (fila.existe_processo_2()):
        executa_usuario(fila.processos_usuario2[0], fila.processos_usuario2)
    elif (fila.existe_processo_3()):
        executa_usuario(fila.processos_usuario3[0], fila.processos_usuario3)
    else:
        tempo += 1

def executa_real(proc):
    global tempo
    for i in range(0, proc.tempo_cpu):
        print("    P" + str(proc.pid) + " instrucao " + str(i + 1))
        time.sleep(1)
    memoria.libera_memoria_real(proc)
    tempo += proc.tempo_cpu
    fila.processos_real.pop(0)

def executa_usuario(proc, fila):
    global tempo
    tempo += 1
    proc.tempo_cpu -= 1
    proc.tempo_decorrido += 1

    print("    P" + str(proc.pid) + " instrucao " + str(proc.tempo_decorrido))
    time.sleep(1)

    if (proc.tempo_cpu == 0):
        memoria.libera_memoria_usuario(proc)
        fila.pop(0)

def le_arqs(caminho):

    fh = open(caminho, 'r')    
    
    tamanho = int(fh.readline())
    seg_ocup = int(fh.readline())
    disco.inicializa_disco(tamanho, seg_ocup)    

    for i in range(2, seg_ocup+2):
        linha = fh.readline()
        disco.add_arquivo(linha)
    
    for linha in fh:
        disco.add_operacao(linha)


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
