class Disco:
    blocos = []
    arquivos = []
    operacoes = []

    tamanho = 0
    seg_ocup = 0

    def inicializa_disco(tamanho, seg_ocup):
        for i in range(0, tamanho):
            blocos.append("0")

        self.tamanho = tamanho
        self.seg_ocup = seg_ocup

        print(self.tamanho, self.seg_ocup)

    def add_arquivo(linha):
        linha = linha.replace(" ", "").replace("\n", "")
        char_list = linha.split(',')
        arquivos.append(char_list)
        print(arquivos)
