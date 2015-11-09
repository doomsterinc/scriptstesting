# -*- coding: latin1 -*-

class Clientes:
    """ Exemplo de classe """

    #Atributos da classe
    nome = ""
    idade = 0

    def __init__(self, nome, idade):
        """Construtor da classe"""
        self.nome = nome
        self.idade = idade

    def __repr__(self):
        return "O cliente %s tem %i anos" % (self.nome, self.idade)

    #Método da classe
    def exibeCliente(self):
        """Método da classe """
        print("O cliente %s tem %i anos" % (self.nome, self.idade))

def apagarCliente(self):
    """Apaga os dados do cliente"""
    self.nome = ""
    self.idade = 0

print("Classe original:", dir(Clientes))

#O novo método é inserido na classe
Clientes.apagarCliente = apagarCliente

print("Classe modificada:", dir(Clientes))

c = Clientes("Carlos Silva", 39)

#Usando o nome método
c.apagarCliente()
print(c)


def infoClass(cls):
    """
    Função decoradora de classes
    """
    #Classe que irá envolver a outra classe
    class Infos(cls):
        """
        Classe derivada que mostra os parâmetros de inicialização
        """

        def __init__(self, *args, **kargs):
            print ('Classe:', repr(cls))
            print ('args:', args)
            print ('kargs:', kargs)

            # Executa a inicialização da classe original
            cls.__init__(self, *args, **kargs)


    # Retorna a nova classe
    return Infos