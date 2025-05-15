pizzas =["Calabresa", "Frango com Catupyri", "Marguerita", "Portuguesa", "Pepperoni", "Alho","Lombo", "4 Queijos", "Chocolate", "Banana"]

# print(f"Os três primeiros sabores do cardápio são: {pizzas[:3]}")
# numero_de_pizzas = len(pizzas)
# print(numero_de_pizzas)
# print(f"Os sabores do meio do cardápio: {pizzas[3:6]}")
# print(f"Os três últimos sabores do cardápio são: {pizzas[-3:]}")

noiva_pizzas = pizzas[:2]
minhas_pizzas = pizzas[:5]
noiva_pizzas.append("brigadeiro")

# print(f"No cardápio há esses sabores {pizzas}")
# print(f"Minha noiva prefere {noiva_pizzas[:2]} e pizza doce a de {noiva_pizzas[2:]}")

for pizza in minhas_pizzas:
    print(f"Eu prefiro esses sabores de pizza: {pizza}")
for sabores in noiva_pizzas[:2]:
    print(f"minha noiva prefere {sabores}")
    