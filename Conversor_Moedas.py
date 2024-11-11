taxas_cambio = {
    ("USD", "EUR"): 0.85,   
    ("EUR", "USD"): 1.18,   
    ("USD", "BRL"): 5.25,   
    ("BRL", "USD"): 0.19,   
    ("EUR", "BRL"): 6.20,   
    ("BRL", "EUR"): 0.16,
}

def validar_valor(valor):
    try:
        valor = float(valor)
        return valor > 0
    except ValueError:
        return False

def converter_moeda(valor, taxa_cambio):
    return valor * taxa_cambio

def listar_moedas():
    return {
        "USD": "Dólar Americano",
        "EUR": "Euro",
        "BRL": "Real Brasileiro",
    }

def interface_usuario():
    moedas = listar_moedas()
    print("Moedas disponíveis:")
    for codigo, nome in moedas.items():
        print(f"{codigo}: {nome}")

    moeda_origem = input("Digite o código da moeda de origem: ").upper()
    moeda_destino = input("Digite o código da moeda de destino: ").upper()
    
    if (moeda_origem, moeda_destino) not in taxas_cambio:
        print("Taxa de câmbio não disponível para essas moedas.")
        return
    
    valor_str = input("Digite o valor a ser convertido: ")
    
    if not validar_valor(valor_str):
        print("Valor inválido! Por favor, insira um número positivo.")
        return
    
    valor = float(valor_str)
    taxa_cambio = taxas_cambio[(moeda_origem, moeda_destino)]
    
    valor_convertido = converter_moeda(valor, taxa_cambio)
    print(f"Taxa de câmbio usada: {taxa_cambio}")
    print(f"Valor convertido: {valor_convertido:.2f} {moeda_destino}")

interface_usuario()