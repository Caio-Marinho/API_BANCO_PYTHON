import mysql.connector
banco = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database= "turmaa"
)
meucursor = banco.cursor()
pesquisa = 'select * from alunos;'
meucursor.execute(pesquisa)
resultado= meucursor.fetchall()
for x in resultado:
    print(x)
nome = input("Diga seu nome: ")
telefone = input("Diga seu telefone: ")
sql = "INSERT INTO alunos(nome,telefone) VALUES (%s,%s);"
data = (nome,telefone)
meucursor.execute(sql,data)
banco.commit()
meucursor.close()
banco.close()