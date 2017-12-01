#########################
# Modulo de Despachante #
#########################

from processo import Processo
import time
from memoria import Memoria
from entrada_saida import Entrada_Saida
from fila import Fila
from disco import Disco
from leitor import preparar_processos
from leitor import preparar_disco


# Fila geral de processos
processos = list()

memoria = Memoria()
recurso = Entrada_Saida()
disco   = Disco()
fila    = Fila()

tempo = 0

# Inicializa a execucao do SO
def despachante_init(caminho_proc, caminho_arq):
    global processos
    global disco

    processos = preparar_processos(caminho_proc)
    executar_processos()

    disco = preparar_disco(caminho_arq)
    disco.prepara_disco()
    disco.executa_operacoes(fila.todos_processos)
    disco.imprime_disco()

def executar_processos():
    while (fila.existe_processos_para_executar() or existe_processo_para_entrar_em_execucao()):
        adicionar_processos_nas_filas_de_execucao(tempo)
        escalonar()

def existe_processo_para_entrar_em_execucao():
    return len(processos) > 0

def adicionar_processos_nas_filas_de_execucao(tempo_atual):
    if ((len(processos) > 0)):
        while ((processos[0].tempo_init <= tempo_atual)):
            fila.adiciona_em_fila(processos.pop(0))
            if (len(processos) == 0): break

def escalonar():
    global tempo

    #testa fila real
    for i in range(0,len(fila.processos_real)):
        if(fila.processos_real[i].tempo_decorrido == 0):
            if(memoria.memoria_disponivel(fila.processos_real[i])):
                executa_real(fila.processos_real.pop(i))
                return
        else:
            executa_real(fila.processos_real.pop(i))
            return

    #testa a fila de prioridade 1
    for i in range(0,len(fila.processos_usuario1)):
        if(fila.processos_usuario1[i].tempo_decorrido == 0):
            if(memoria.memoria_disponivel(fila.processos_usuario1[i])):
                executa_usuario(fila.processos_usuario1[i],fila.processos_usuario1,i)
                return
        else:
            executa_usuario(fila.processos_usuario1[i],fila.processos_usuario1,i)
            return

    #testa a fila de prioridade 2
    for i in range(0,len(fila.processos_usuario2)):
        if(fila.processos_usuario2[i].tempo_decorrido == 0):
            if(memoria.memoria_disponivel(fila.processos_usuario2[i])):
                executa_usuario(fila.processos_usuario2[i],fila.processos_usuario2,i)
                return
        else:
            executa_usuario(fila.processos_usuario2[i],fila.processos_usuario2,i)
            return

    #testa a fila de prioridade 3
    for i in range(0,len(fila.processos_usuario3)):
        if(fila.processos_usuario3[i].tempo_decorrido == 0):
            if(memoria.memoria_disponivel(fila.processos_usuario3[i])):
                executa_usuario(fila.processos_usuario3[i],fila.processos_usuario3,i)
                return
        else:
            executa_usuario(fila.processos_usuario3[i],fila.processos_usuario3,i)
            return
    tempo += 1


def executa_real(proc):
    global tempo
    for i in range(0, proc.tempo_cpu):
        print("    P" + str(proc.pid) + " instrucao " + str(i + 1))
        #time.sleep(1)
    memoria.libera_memoria_real(proc)
    tempo += proc.tempo_cpu

def executa_usuario(proc, fila,pos):
    global tempo
    tempo += 1
    proc.tempo_decorrido += 1

    print("    P" + str(proc.pid) + " instrucao " + str(proc.tempo_decorrido))
    #time.sleep(1)

    if (proc.tempo_cpu == proc.tempo_decorrido):
        memoria.libera_memoria_usuario(proc)
        fila.pop(pos)
        
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
