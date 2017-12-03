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
tempo_aging = 0
last_pid = -1

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
    tempo_aging = 0
    while (fila.existe_processos_para_executar() or existe_processo_para_entrar_em_execucao()):
        adicionar_processos_nas_filas_de_execucao(tempo)
        escalonar()
        tempo_aging += 1
        if(tempo_aging == 20):
            tempo_aging = 0
            fila.aging()

def existe_processo_para_entrar_em_execucao():
    return len(processos) > 0

def adicionar_processos_nas_filas_de_execucao(tempo_atual):
    if ((len(processos) > 0)):
        while ((processos[0].tempo_init <= tempo_atual)):
            proc = processos.pop(0)
            if memoria.processo_cabe_na_memoria(proc):
                fila.adiciona_em_fila(proc)
            else:
                print("\nProcesso " + str(proc.pid) + "=> NOT STARTED")
                print("    O processo exige mais memoria do que o sistema possui.\n")
            if (len(processos) == 0): break

def escalonar():
    global tempo

    if(tenta_escalonar_processo_real()):
        return True
    elif(tenta_escalonar_processo_usuario()):
        return True
    else:
        tempo += 1

def tenta_escalonar_processo_real():
    #testa fila real
    for i in range(0,len(fila.processos_real)):
        if(fila.processos_real[i].tempo_decorrido == 0):
            if(memoria.memoria_disponivel(fila.processos_real[i])):
                executa_real(fila.processos_real.pop(i))
                return True
        else:
            executa_real(fila.processos_real.pop(i))
            return True
        return False

def tenta_escalonar_processo_usuario():
    #testa a fila de prioridade 1
    for i in range(0,len(fila.processos_usuario1)):
        if(fila.processos_usuario1[i].tempo_decorrido == 0):
            if (recurso.recursos_estao_disponiveis(fila.processos_usuario1[i])):
                if(memoria.memoria_disponivel(fila.processos_usuario1[i])):
                    recurso.alocar_recurso(fila.processos_usuario1[i])
                    executa_usuario(fila.processos_usuario1[i],fila.processos_usuario1,i)
                    return True
        else:
            executa_usuario(fila.processos_usuario1[i],fila.processos_usuario1,i)
            return True

    #testa a fila de prioridade 2
    for i in range(0,len(fila.processos_usuario2)):
        if(fila.processos_usuario2[i].tempo_decorrido == 0):
            if (recurso.recursos_estao_disponiveis(fila.processos_usuario2[i])):
                if(memoria.memoria_disponivel(fila.processos_usuario2[i])):

                    recurso.alocar_recurso(fila.processos_usuario2[i])
                    executa_usuario(fila.processos_usuario2[i],fila.processos_usuario2,i)
                    return True
        else:
            executa_usuario(fila.processos_usuario2[i],fila.processos_usuario2,i)
            return True

    #testa a fila de prioridade 3
    for i in range(0,len(fila.processos_usuario3)):
        if(fila.processos_usuario3[i].tempo_decorrido == 0):
            if (recurso.recursos_estao_disponiveis(fila.processos_usuario3[i])):
                if(memoria.memoria_disponivel(fila.processos_usuario3[i])):
                    recurso.alocar_recurso(fila.processos_usuario3[i])
                    executa_usuario(fila.processos_usuario3[i],fila.processos_usuario3,i)
                    return True
        else:
            executa_usuario(fila.processos_usuario3[i],fila.processos_usuario3,i)
            return True


def executa_real(proc):
    global tempo
    
    imprime_processo_info(proc)
    print("Process " + str(proc.pid) + "=> STARTED")

    for i in range(0, proc.tempo_cpu):
        print("    P" + str(proc.pid) + " instrucao " + str(i + 1))
    print("\tP" + str(proc.pid) + " return SIGINT")

    memoria.libera_memoria_real(proc)
    tempo += proc.tempo_cpu

def executa_usuario(proc, fila, pos):
    global tempo
    global last_pid
    
    if(proc.tempo_decorrido == 0):        
        imprime_processo_info(proc)

    tempo += 1
    proc.tempo_decorrido += 1

    if(last_pid == proc.pid):
        print("\tP" + str(proc.pid) + " instruction " + str(proc.tempo_decorrido))
    else:
        print("\nProcess " + str(proc.pid) + " =>")
        print("\tP" + str(proc.pid) + " instruction " + str(proc.tempo_decorrido))

    last_pid = proc.pid

    if (proc.tempo_cpu == proc.tempo_decorrido):
        print("\tP" + str(proc.pid) + " return SIGINT")
        recurso.liberar_recurso(proc)
        memoria.libera_memoria_usuario(proc)
        fila.pop(pos)
        return

    fila.append(fila.pop(pos))
        
# Imprime os dados de cada processo executado pelo dispachante
def imprime_processo_info(proc):
    print('')
    print("Process " + str(proc.pid) + "=> STARTED")   
    print("    PID:        " + str(proc.pid))
    print("    prioridade: " + str(proc.prioridade))
    if(proc.prioridade != 0):
        print("    offset:     " + str(proc.inicio_memoria + 64))
    else:
        print("    offset:     " + str(proc.inicio_memoria))
    print("    blocos:     " + str(proc.quant_mem))
    print("    impressora: " + str(proc.impressora))
    print("    scanner:    " + str(proc.scanner))
    print("    modem:      " + str(proc.modem))
    print("    sata:       " + str(proc.sata))