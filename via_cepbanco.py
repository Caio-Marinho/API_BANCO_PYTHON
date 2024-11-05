import mysql.connector
import requests
lista = []
banco = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database= "turmaa"
)
cep = input("Digite o cep: ")
if len(cep) == 8:
    link = f"https://viacep.com.br/ws/{cep}/json/"
    requisicao = requests.get(link)
    dic_requisicao = requisicao.json()
    print(dic_requisicao)
    for i in dic_requisicao:
        lista.append(dic_requisicao[i])
    meucursor = banco.cursor()
    sql = ("INSERT INTO endereco (cep,lougradouro,complemento,unidade,bairro,localidade,uf,estado,regiao,ibge,gia,ddd,siafi)"
           "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);")
    dados = tuple(lista)
    meucursor.execute(sql,dados)
    banco.commit()
    meucursor.close()
    banco.close()
else:
    print("CEP Inválido")



