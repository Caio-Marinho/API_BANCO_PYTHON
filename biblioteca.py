import requests

def via_cep(cep):
    lista= []
    if len(cep) == 8:
        link = f"https://viacep.com.br/ws/{cep}/json/"
        requisicao = requests.get(link)
        dic_requisicao = requisicao.json()
        uf = dic_requisicao['uf']
        cidade = dic_requisicao['localidade']
        bairro = dic_requisicao['bairro']
        print(dic_requisicao)
        for i in dic_requisicao:
            lista.append(dic_requisicao[i])
        print(lista)
    else:
        return "CEP Inválido"