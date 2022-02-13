# -*- coding: utf-8-*-

# Copyright 2018 Felix
__author__ = 'felix'
__version__ = "0.0.1"


arquivo = 'SentiLex-lem-PT01.txt'


def acessoarq():
    global pol
    listapalavras = {}
    with open(arquivo, 'r') as fh:
        for line in fh.readlines():
            print(line)
            buscapol = line.find('POL=')
            buscaponto = line.find('.')
            chave = line[:buscaponto]
            pol = line[(buscapol + 4):(buscapol + 6)].split(';')
            """
            if "-1" in line:
                pol = line[(buscapol+4):(buscapol+6)]

            elif "1" or "0" in line:
                pol = line[(buscapol + 4):(buscapol + 5)]
            """
            palavra = chave
            a = input()
            print(palavra, chave)
            listapalavras[palavra] = pol

    return listapalavras


def getfrase():
    print('Como você esta? \n')
    frase = input().lower().split()
    return frase


def comparacao(frase, listapalavras):
    contador = 0
    print(listapalavras)
    for palavra in frase:
        print(palavra)
        """for key, value in listapalavras.items():
            if palavra == key:
                contador += value"""

        contador += int(listapalavras.get(palavra.lower(), 0))

    return contador



#getfrase()
#acessoarq()
#print(comparacao(getfrase(), acessoarq()))


if __name__ == '__main__':
    with open('lex.txt', 'r') as lexfile:
        loadedlex = lexfile.readlines()

    for line in loadedlex:
        print(line)
        a = input()
