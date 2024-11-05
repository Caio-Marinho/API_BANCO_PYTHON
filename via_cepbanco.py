import mysql.connector
import requests
lista = []
chaves = []
banco = mysql.connector.connect(
    host="0.tcp.sa.ngrok.io",
    port = 17698,
    user="root",
    password="teste",
    database= "cdd40"
)
cep = '50810020'#input("Digite o cep: ")
if len(cep) == 8:
    link = f"https://viacep.com.br/ws/{cep}/json/"
    requisicao = requests.get(link)
    dic_requisicao = requisicao.json()
    print(dic_requisicao)
    for i in dic_requisicao:
        chaves.append(i)
        lista.append(dic_requisicao[i])
    espaco = ', '.join(["%s"]*len(dic_requisicao))
    titulo = ', '.join(chaves)
    meucursor = banco.cursor()
    sql = (f"INSERT INTO endereco ({titulo})"
           f"VALUES ({espaco});")
    lista[0] = lista[0][:5]+lista[0][6:]
    dados = tuple(lista)
    meucursor.execute(sql,dados)
    banco.commit()
    meucursor.close()
    banco.close()
else:
    print("CEP Inválido")



