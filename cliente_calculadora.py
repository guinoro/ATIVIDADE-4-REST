# importa lib requests / faz requisições HTTP
import requests

# define a url base
BASE_URL = "https://calculadora-fxpc.onrender.com"

# consulta a rota GET /operations para listar as operações
def listar_operacoes():
    # requisição GET para /operations, pedindo resposta no formato JSON
    resp = requests.get(f"{BASE_URL}/operations", headers={"Accept": "application/json"})
    
    # se a requisição falhar, levanta uma exceção para sabermos
    resp.raise_for_status()
    
    # converte JSON em lista python e retorna
    return resp.json()

# realiza uma operação matemática
def calcular(op, a, b):
    # define a URL da operação (ex: /operations/soma)
    url = f"{BASE_URL}/operation/{op}/{a}/{b}"
    
    # define o corpo da requisição POST em JSON, com os dois parâmetros numéricos
    data = {"param1": a, "param2": b}
    
    # requisição POST para a URL da operação, com o corpo JSON e cabeçalho
    resp = requests.post(url, json=data, headers={"Accept": "application/json"})
    
    # se der erro na requisição, levanta exceção
    resp.raise_for_status()
    
    # retorna apenas o resultado numérico da operação
    return resp.json()["result"]

# se o script for executado diretamente (não importado como módulo), executa este bloco
if __name__ == "__main__":
    # imprime a lista de operações disponíveis na API
    print("Operações disponíveis:", listar_operacoes())
    
    # exemplo de soma: 3 + 2 → imprime resultado
    print("3 + 2 =", calcular("soma", 3, 2))

    # exemplo de subtração: 30 - 25 → imprime resultado
    print("30 - 25 =", calcular("subtracao", 30, 25))
    
    # exemplo de divisão: 10 ÷ 4 → imprime resultado
    print("10 / 4 =", calcular("divisao", 10, 4))

    # exemplo de multiplicação: 5 x 12 → imprime resultado
    print("5 x 12 =", calcular("multiplicacao", 5, 12))