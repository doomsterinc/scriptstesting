# -*- coding: latin1 -*-

import testemod
import os.path
import glob
import time
import traceback


lista = []

def quadrado1 (elemento):
	lista.append(elemento)
	print(elemento)
	return elemento ** 2

print (quadrado1(4))
print(lista)

resultado = 2 * quadrado1(9)
print (resultado)
print (lista)

lista = [10,20,30,40,50,60]

print (testemod.media(lista))

print (testemod.soma(lista))

print(testemod.__doc__)

#criando um objeto do tipo file
temp = open("temp.txt", "w")

#escrevendo no arquivo
for i in range(100):
	temp.write('%i dolares valem %f reais\n' % (i, i * 1.70))

#fechando o arquivo
temp.close()

temp = open("temp.txt","r")

for linhas in temp:
	print (linhas)

temp.close()

#mostra uma lista de nomes de arquivos 
# e seus respectivos tamanhos

for arq in sorted(glob.glob("*.py")):
	print (arq, os.path.getsize(arq))


# localtime() retorna a data e hora local no formato struct_time
print (time.localtime())

#asctime() retorna a data e hora como uma string
print (time.asctime())

#time() retorna o tempo do sistema em segundos
ts1 = time.time()

# gmtime() converte segundos para struct_time
tt1 = time.gmtime(ts1)
print (ts1, "->", tt1)

# somando uma hora
tt2 = time.gmtime(ts1 + 3600.)

# mktime() converte struct_time para segundos
ts2 = time.mktime(tt2)
print (ts2, "->", tt2)

#clock() retirna o tempo desde quando o programa
#iniciou, em segundos
print("O progrma levou", time.clock(), "segundos ate agora...")


#contando os segundos ...
for i in range(5):
	#sleep() espera durante o numero de segundos
	# especificados como parametros
	time.sleep(1)
	print (i + 1, "segundo(s)...")


##### erro

try:
	print(1/0)
except ZeroDivisionError, e:
	print ("erro ao tentar dividir por zero")

list = []

for i in range(3):
	while 1:
		try:
			list.append(int(input("digite um valor: ")))
			break;
		except:
			print("digite apensa numeros")
print (list)

## erro com traceback
list = []
for i in range(3):
	while 1:
		try:
			list.append(int(input("digite um numero: ")))
			break;
		except:
			trace = traceback.format_exc()

			print ("Ocorreu o erro: ", trace)

			#cria um arquivo de log de erro
			open("trace.log","a").write(trace)

print (list)


def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print ("Divisao por zero!")
    else:
        print ("Resultado", result)
    finally:
        print ("Executando a causa finally")


#colhendo algumas informacoes
#dos objetos globais no programa
from types import ModuleType

def info(n_obj):
	#cria uma referencia ao obj
	obj = globals()[n_obj]

	#mostra informacoes do objeto
	print("nome do objeto: ", n_obj)
	print("identificador: ", id(obj))
	print("Tipo: ", type(obj))
	print("Representacao", repr(obj))
	# se for um modulo
	if isinstance(obj, ModuleType):
		print("itens: ")
		for item in dir(obj):
			print (item)
	#mostrando as informacoes 
for n_obj in dir():
	info(n_obj)

# -*- coding: latin1 -*-

# Amplitude de um vetor 3D
amp = lambda x, y, z: (x ** 2 + y ** 2 + z ** 2) ** .5

print(amp(1, 1, 1))
print(amp(3, 4, 5))

#orientacao a objetos

class Clientes:
	"""Exemplo de classe """

	#atributos de classe
	nome = ""
	idade = 0

	def __init__(self,nome,idade):
		#construtor da classe
		self.nome = nome
		self.idade = idade

	#metodo de classe
	def exibeCliente(self):
		"""Metodo da classe"""
		print ("O cliente %s tem %i anos" % (self.nome, self.idade))

c = Clientes("jose", 34)
print (c)

c.exibeCliente()

class Projetil():
	"""classe projetil """
	def __init__ (self,alcance, tempo):
		"""contrutctor"""
		self.alcance = alcance
		self.tempo = tempo

		@property
		def velocidade(self):
		    return self.alcance/self.tempo

pro = Projetil(1000, 45)
print (pro.velocidade)
