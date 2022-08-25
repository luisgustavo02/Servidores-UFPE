bloco = str(input("DIGITE O CENTRO, DEPARTAMENTO OU NOME DO SERVIDOR DESEJADO: ")).upper()

with open(file="./servidores-2020-ufpe.csv", mode="r", encoding="utf8") as arquivo:
    linha = arquivo.readline()
    while linha:
        if linha.find(bloco) != -1:
            print(linha)
        linha = arquivo.readline()
