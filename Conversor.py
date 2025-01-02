import requests

print("""Seja bem-vindo ao conversor de moedas!
      [1] Dólar Americano
      [2] Real Brasileiro
      [3] Euro
      [4] Libra
      [5] Franco Suíço
      [6] Peso Argentino""")

# Mapeia as opções para os códigos de moeda
moedas = {
    1: "USD",
    2: "BRL",
    3: "EUR",
    4: "GBP",
    5: "CHF",
    6: "ARS"
}

# Escolha da moeda de origem
while True:
    try:
        moeda1 = int(input('Qual sua moeda de origem? '))
        if moeda1 in moedas:
            moeda1 = moedas[moeda1]
            break
        else:
            print("Opção inválida, tente novamente.")
    except ValueError:
        print("Entrada inválida, digite um número.")

# Escolha da moeda de destino
while True:
    try:
        moeda2 = int(input('Para qual moeda deseja converter? '))
        if moeda2 in moedas:
            moeda2 = moedas[moeda2]
            break
        else:
            print("Opção inválida, tente novamente.")
    except ValueError:
        print("Entrada inválida, digite um número.")

# Construção da URL com as moedas escolhidas
url = f'https://v6.exchangerate-api.com/v6/d8af87726095b44fcd330b67/pair/{moeda1}/{moeda2}'

# Faz a requisição
resposta = requests.get(url)
if resposta.status_code == 200:
    conversao = resposta.json()
    taxa = conversao.get("conversion_rate")
    valor = float(input("Digite o valor que deseja converter: "))
    valor_convertido = valor * taxa
    print(f"A taxa de conversão de {moeda1} para {moeda2} é: {taxa}")
    print(f"O valor convertido é: {valor_convertido:.2f} {moeda2}")
else:
    print("Erro ao acessar a API. Verifique sua conexão ou chave de API.")
