# -*- coding: utf-8 -*-
#! /usr/bin/env

import psycopg2
import time

query1 = "select * from view_artigos_populares"
query2 = "select * from view_autores_populares"
query3 = "select * from view_porcentagem_erros"

def connect():
	return psycopg2.connect("dbname=news")

def artigos_populares(query1):
	database = connect()
	cursor = database.cursor()
	cursor.execute(query1)
	resultado = cursor.fetchall()

	texto = "Os três artigos mais populares: \n"
	for i in range(len(resultado)):
		texto += "%-35s -- %-10s visualizações\n" %(i[0], i[1])
	texto += "\n"
	return texto
	database.close()

def autores_populares(query2):
	database = connect()
	cursor = database.cursor()
	cursor.execute(query2)
	resultado = cursor.fetchall()

	texto = "Autores com maior popularidade:\n"
	for i in range(len(resultado)):
		texto += "%35s -- %-10s visualizações\n" %(i[0], i[1])
	texto += "\n"
	return texto
	database.close()

def porcentagem_erro(query3):
	database = connect()
	cursor = database.cursor()
	cursor.execute(query3)
	resultado = cursor.fetchall()
	
	texto = "Quais dias têm mais de 1% das requisições com erros:\n"
    for i in range(len(resultado)):
        texto += "%-35s -- %-10.4s%s erros\n" %(i[0], i[1], '%')
    texto += "\n"
    return texto
    database.close()

def main():
	database = connect()

	artigos_populares(query1)
	autores_populares(query2)
	porcentagem_erro(query3)

	database.close()

if __name__ == "__main__":
	main()