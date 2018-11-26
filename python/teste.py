class Analise(object):

    def __init__(self, nome):
        self.nome = nome

    def acesso(self):
        dicionario = open(self.nome, 'r')
        conteudo = dicionario.read()
        return conteudo
    #    print(conteudo)

    def getfrase(self):
        frase = input('Como você esta?\n ')
        return frase

    def comparar(self, frase, conteudo):
        

analise = Analise('dicionario.txt')
analise.getfrase()
