# !/usr/bin/env python3
# -*- coding: utf-8 -*-
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
	for i in range(len(resultado)):
		title = resultado[i][0]
		views = resultado[i][0]
		print("%s--%d" % (titulo,views))

	database.close()

def autores_populares(query2):
	database = connect()
	cursor = database.cursor()
	cursor.execute(query2)
	resultado = cursor.fetchall()
	for i in range(len(results)):
		name=resultado[i][0]
		views=resultado[i][1]
		print("%s--%d" % (name,views))

	database.close()

def porcentagem_erro(query3):
	database = connect()
	cursor = database.cursor()
	cursor.execute(query3)
	resultado = cursor.fetchall()
	
	for i in range(len(results)):
		date=resultado[i][0]
		err_prc=resultado[i][1]
		print("%s--%.1f %%" %(date,err_prc))

    database.close()

def main():
	database = connect()

	print(artigos_populares(query1))
	print(autores_populares(query2))
	print(porcentagem_erro(query3))

	database.close()

if __name__ == "__main__":
	main()
