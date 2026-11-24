# Primeira função -> Calcular preço pizza.

def calcular_preco_pizza(tamanho):
    tabela = {
        "P": 25.0,
        "M": 35.0,
        "G": 45.0,
        }   
    "Para receber o 'value' do dicionário, é necessário acessa o 'key'"
    return tabela.get(tamanho,0)
    "Tabela.get() é uma forma segura de acessa valores no dict."
    ".get(tamanho,0) evitar retorno none se a chave não existir dentro do dict."

# Segunda função -> Calcular taxa de entrega. 

def calcular_taxa_de_entrega(distancia_km):
    if distancia_km <= 3:
       return 5.0
    elif distancia_km <= 7:
        return 10.0
    else:
        return 15.0

# Terceira função -> Aplicar desconto fidelidade.

def aplicar_desconto_fidelidade(subtotal, eh_cliente_fiel):
    if eh_cliente_fiel:
        return subtotal * 0.90
    else:
        return subtotal

# Quarta função -> Função 

def fechar_pedido(tamanho, distancia_km, eh_cliente_fiel):
    "Essa função reutiliza todas as funções anteriores."
    preco_pizza = calcular_preco_pizza(tamanho)
    taxa = calcular_taxa_de_entrega(distancia_km)
    subtotal = preco_pizza + taxa
    total = aplicar_desconto_fidelidade(subtotal, eh_cliente_fiel) 
    print(f"""
    =========================
    pizza({tamanho}): R$ {preco_pizza:.2f}
    taxa de entrega: R$ {taxa:.2f}
    total: R$ {total:.2f}
    =========================
    """)

fechar_pedido("M", 10, True)





    
    
    
    






