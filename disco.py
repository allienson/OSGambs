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

        print(self.tamanho, self.seg_ocup)

    def add_arquivo(self, linha):
        linha = linha.replace(" ", "").replace("\n", "")
        char_list = linha.split(',')
        self.arquivos.append(char_list)
        #print(self.arquivos)

    def add_operacao(self, linha):
        linha = linha.replace(" ", "").replace("\n", "")
        char_list = linha.split(',')
        self.operacoes.append(char_list)
        #print(self.operacoes)

    def prepara_disco(self):
        for arq in self.arquivos:
            self.insere_arquivo(arq)

    def insere_arquivo(self, arq):
        nome = arq[0]
        inicial = int(arq[1])
        quant_blocos = int(arq[2])

        for i in range(0, quant_blocos):
            self.blocos[i+inicial] = nome
