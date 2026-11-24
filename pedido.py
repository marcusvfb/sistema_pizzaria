 # pedido.py - calcula o total do pedido
def calcular_total(precos):
    return sum(precos)

total = calcular_total([42, 45, 48])
print(f"Total do pedido: R$ {total},00")