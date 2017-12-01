class Disco:
    blocos = []
    arquivos = []
    operacoes = []

    tamanho = 0
    seg_ocup = 0

    def inicializa_disco(self, tamanho, seg_ocup):
        for i in range(0, tamanho):
            self.blocos.append("0")

        self.tamanho = tamanho
        self.seg_ocup = seg_ocup

    def add_arquivo(self, linha):
        linha = linha.replace(" ", "").replace("\n", "")
        char_list = linha.split(',')
        self.arquivos.append(char_list)

    def add_operacao(self, linha):
        linha = linha.replace(" ", "").replace("\n", "")
        char_list = linha.split(',')
        self.operacoes.append(char_list)
        
    def prepara_disco(self):
        for arq in self.arquivos:
            self.insere_arquivo(arq)

    def insere_arquivo(self, arq):
        nome = arq[0]
        inicial = int(arq[1])
        quant_blocos = int(arq[2])

        for i in range(0, quant_blocos):
            self.blocos[i+inicial] = nome

    def executa_operacoes(self, processos):
        op_id = 0

        for op in self.operacoes:
            op_id += 1
            pid = int(op[0])
            codigo = int(op[1])
            nome = op[2]
            if(codigo == 0):
                num_blocos = int(op[3])
            else:
                num_blocos = 0
            self.operacao(pid, codigo, nome, num_blocos, op_id, processos)
                
    def operacao(self, pid, codigo, nome, num_blocos, op_id, processos):
        count = 0
        pos = 0
        
        if(any(proc.pid == pid for proc in processos) == False):
            self.imprime_operacao(op_id, pid, codigo, nome, num_blocos, pos, sucesso=2)
        elif(codigo == 0):    
            for i in range(0, len(self.blocos)):
                if(self.blocos[i] == '0'):
                    if(count == 0):
                        pos = i
                    count += 1
                else:
                    count = 0
                if(num_blocos == count):
                    pos = i - num_blocos + 1
                    for j in range(pos, i+1):
                        self.blocos[j] = nome
                    self.imprime_operacao(op_id, pid, codigo, nome, num_blocos, pos, sucesso=1)
                    break
                
            self.imprime_operacao(op_id, pid, codigo, nome, num_blocos, pos, sucesso=0)
                   

        else:
            for i in range(0, len(self.blocos)):
                if(self.blocos[i] == nome):    
                    self.blocos[i] = '0'
            self.imprime_operacao(op_id, pid, codigo, nome, num_blocos, pos, sucesso=1)

    def imprime_operacao(self, op_id, pid, codigo, nome, num_blocos, pos, sucesso):
        if(sucesso == 0):
            print("Operacao " + str(op_id) + "=> Falha")
            print("O processo " + str(pid) + " nao pode criar o arquivo " + nome + " (falta de espcaco).\n")
        elif(sucesso == 1):
            print("Operacao " + str(op_id) + "=> Sucesso")
            if(codigo == 0):
                blocos_usados = []
                for i in range(0, num_blocos):
                    blocos_usados = pos+i
                print("O processo " + str(pid) + " criou o arquivo " + nome + ".\n")
            if(codigo == 1):
                print("O processo " + str(pid) + " deletou o arquivo " + nome + ".\n")   
        else:
            print("Operacao " + str(op_id) + "=> Falha")
            print("O processo " + str(pid) + " nao exite.\n")
        print('')
        print(self.blocos)
        print('')

    def imprime_disco(self):
        print(self.blocos)
        print('')
        for op in self.operacoes:
            print(op)