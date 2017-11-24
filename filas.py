#######################
#   Modulo de Filas   #
#######################

# Class principal de definicao das filas
class Filas:
    # Fila de processos de tempo real
    processos_real = []
    # Fila de processos de usuario
    processos_usuario1 = []
    processos_usuario2 = []
    processos_usuario3 = []

    def __init__(self):
        self

    def adicionar_processo_na_fila(processo):
        if (processo.prioridade == 0):
            processos_real.append(proc)
        elif (processo.prioridade == 1):
            processos_usuario1.append(proc)
        elif (processo.prioridade == 2):
            processos_usuario2.append(proc)
        elif (processo.prioridade == 3):
            processos_usuario3.append(proc)
        else:
            print("Prioridade invalida")
            exit(0)
