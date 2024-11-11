# Dicionário com taxas de câmbio predefinidas
taxas_cambio = {
    ("USD", "EUR"): 0.85,   # Exemplo: 1 USD = 0.85 EUR
    ("EUR", "USD"): 1.18,   # Exemplo: 1 EUR = 1.18 USD
    ("USD", "BRL"): 5.25,   # Exemplo: 1 USD = 5.25 BRL
    ("BRL", "USD"): 0.19,   # Exemplo: 1 BRL = 0.19 USD
    ("EUR", "BRL"): 6.20,   # Exemplo: 1 EUR = 6.20 BRL
    ("BRL", "EUR"): 0.16,   # Exemplo: 1 BRL = 0.16 EUR
}

# Função pura para validar se o valor é um número positivo
def validar_valor(valor):
    try:
        valor = float(valor)
        return valor > 0
    except ValueError:
        return False

# Função pura para aplicar a taxa de câmbio
def converter_moeda(valor, taxa_cambio):
    return valor * taxa_cambio

# Função que gera as opções de moedas disponíveis
def listar_moedas():
    return {
        "USD": "Dólar Americano",
        "EUR": "Euro",
        "BRL": "Real Brasileiro",
    }

# Interface do usuário simulada para seleção de moeda e valor
def interface_usuario():
    # Listando as moedas disponíveis
    moedas = listar_moedas()
    print("Moedas disponíveis:")
    for codigo, nome in moedas.items():
        print(f"{codigo}: {nome}")
    
    # Seleção de moeda inicial e final
    moeda_origem = input("Digite o código da moeda de origem: ").upper()
    moeda_destino = input("Digite o código da moeda de destino: ").upper()
    
    # Verificar se a taxa de câmbio existe no dicionário
    if (moeda_origem, moeda_destino) not in taxas_cambio:
        print("Taxa de câmbio não disponível para essas moedas.")
        return
    
    # Valor para converter
    valor_str = input("Digite o valor a ser convertido: ")
    
    # Validação de entrada
    if not validar_valor(valor_str):
        print("Valor inválido! Por favor, insira um número positivo.")
        return
    
    valor = float(valor_str)
    taxa_cambio = taxas_cambio[(moeda_origem, moeda_destino)]
    
    # Conversão e exibição do resultado
    valor_convertido = converter_moeda(valor, taxa_cambio)
    print(f"Taxa de câmbio usada: {taxa_cambio}")
    print(f"Valor convertido: {valor_convertido:.2f} {moeda_destino}")

    print("\nDesenvolvido por: Nicolas MArquez Dalfovo")

# Executando a interface do usuário
interface_usuario()
