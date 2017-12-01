###################
# Modulo de Filas #
###################

class Fila:
    # Tamanho da Fila
    TAMANHO_FILA = 1000
    # Processos executados
    todos_processos = list()
    # Fila de processos de tempo real
    processos_real = []
    # Fila de processos de usuario
    processos_usuario1 = []
    processos_usuario2 = []
    processos_usuario3 = []

    def adiciona_em_fila(self, proc):

        if (proc.prioridade == 0):
            if len(self.processos_real) < self.TAMANHO_FILA:
                self.processos_real.append(proc)
                self.todos_processos.append(proc)
        elif (proc.prioridade == 1):
            if len(self.processos_usuario1) < self.TAMANHO_FILA:
                self.processos_usuario1.append(proc)
                self.todos_processos.append(proc)
        elif (proc.prioridade == 2):
            if len(self.processos_usuario2) < self.TAMANHO_FILA:
                self.processos_usuario2.append(proc)
                self.todos_processos.append(proc)
        elif (proc.prioridade == 3):
            if len(self.processos_usuario3) < self.TAMANHO_FILA:
                self.processos_usuario3.append(proc)
                self.todos_processos.append(proc)
        else:
            print("Prioridade invalida")
            exit(0)

        self.processos_real.sort(key=lambda x: x.tempo_init)  # Ordena os processos por ordem de chegada
        self.processos_usuario1.sort(key=lambda x: x.tempo_init)
        self.processos_usuario2.sort(key=lambda x: x.tempo_init)
        self.processos_usuario3.sort(key=lambda x: x.tempo_init)

    def err_fila(self):
        print("Pilha cheia")

    def existe_processos_para_executar(self):
        return (len(self.processos_real) != 0) or (len(self.processos_usuario1) > 0) or (
            len(self.processos_usuario2) > 0) or (len(self.processos_usuario3) > 0)

    def existe_processo_real(self):
        return len(self.processos_real) != 0

    def existe_processo_1(self):
        return len(self.processos_usuario1) != 0

    def existe_processo_2(self):
        return len(self.processos_usuario2) != 0

    def existe_processo_3(self):
        return len(self.processos_usuario3) != 0

    def existe_processo_usuario(self):
        return (len(self.processos_usuario3) != 0) or (len(self.processos_usuario2) != 0) or (
        len(self.processos_usuario3))
