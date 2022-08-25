bloco = str(input("DIGITE O CENTRO, DEPARTAMENTO OU NOME DO SERVIDOR DESEJADO: ")).upper()

with open(file="./servidores-2020-ufpe.csv", mode="r", encoding="utf8") as arquivo:
    linha = arquivo.readline()
    if len(bloco.split(" ")) == 1:
        while linha:
            if linha.find(bloco) != -1:
                string = linha.split(",")
                print(f"NOME COMPLETO: {string[0]}")
                print(f"CPF: {string[1]}")
                print(f"CARGO: {string[2]}")
                print(f"BLOCO, CENTRO OU DEPARTAMENTO: {string[4]}")
                print(f"INSTITUIÇÃO: {string[6]}")
                print(f"STATUS DO VÍNCULO: {string[7]}")
                print(f"DATA De VÍNCULO: {string[-1]}")
                print("=================================")
            linha = arquivo.readline()
    else:
        blocos = bloco.split(" ")
        while linha:
            aux = 0
            for i in blocos:
                if linha.find(i) != -1:
                    #print(i, end='\t')
                    aux += 1
            if aux == len(blocos):
                string = linha.split(",")
                print(f"NOME COMPLETO: {string[0]}")
                print(f"CPF: {string[1]}")
                print(f"CARGO: {string[2]}")
                print(f"BLOCO, CENTRO OU DEPARTAMENTO: {string[4]}")
                print(f"INSTITUIÇÃO: {string[6]}")
                print(f"STATUS DO VÍNCULO: {string[7]}")
                print(f"DATA DE VÍNCULO: {string[-1]}")
                print("=================================")
                #print(type(linha))
                #print(linha)
            linha = arquivo.readline()
