sanduiches_pedidos = ['misto quente', 'x-burguer', 'x-salada', 'x-frango', 'x-tudo']
sanduiches_prontos = []
i = 0

for i in range (3):
    sanduiches_pedidos.append('pastrami')
print(sanduiches_pedidos)

while 'pastrami' in sanduiches_pedidos:
     nao_tem = sanduiches_pedidos.remove('pastrami')
print("Não temos o sanduíche de pastrami em nosso restaurante")

for lanche in sanduiches_pedidos:
        pedido = sanduiches_pedidos.pop()
        print(f"Próximo pedido: {pedido.title()}")
        sanduiches_prontos.append(pedido)
    
for sanduiche in sanduiches_prontos:
        print(f"Seu pedido {sanduiche} está pronto")