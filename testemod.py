# -*- coding: latin1 -*-
# Arquivo listacalc.py
""" 
Modulo que contém duas funções
    Uma que calcula a média de uma lista
    E outra que calcula a soma de uma lista
"""

def media (lista):
	""" Calcula media dos itens de uma lista """
	return float (sum(lista)/ len(lista))

def soma(lista):
	"""Calcula a soma dos itens de uma lista"""
	return sum(lista)
