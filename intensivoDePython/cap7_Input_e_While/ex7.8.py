sanduiches_pedidos = ['misto quente', 'x-burguer', 'x-salada', 'x-frango', 'x-tudo', 'pastrami']
sanduiches_prontos = []
ativado = True

for lanche in sanduiches_pedidos:
        pedido = sanduiches_pedidos.pop()
        print(f"Próximo pedido: {pedido.title()}")
        sanduiches_prontos.append(pedido)
    
for sanduiche in sanduiches_prontos:
        print(f"Seu pedido {sanduiche} está pronto")
    