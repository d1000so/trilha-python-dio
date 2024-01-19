def tratar_endereco(string):
    # Dividir a string em partes usando vírgula como delimitador
    partes = string.split(',')

    # Aplicar strip() para remover espaços extras em cada parte
    partes_tratadas = [' '.join(palavra.strip() for palavra in parte.split()) for parte in partes]

    return partes_tratadas

endereco = input()
print(tratar_endereco(endereco))
