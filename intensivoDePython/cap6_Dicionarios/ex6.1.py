import json
pessoa = {
    'primeiro_nome': 'nathan', 
    'sobrenome': 'rodrigues', 
    'idade': '23', 
    'cidade': 'rio de janeiro'}

# print(f"Informações sobre o cliente: \n{pessoa['primeiro_nome']} \n{pessoa['sobrenome']} \n{pessoa['idade']} \n{pessoa['cidade']}")

# print("Informações sobre o cliente:")
# for chave, valor in pessoa.items():
#     print(f"{chave.replace('_', ' ').title()}: {valor}")

print("Informações sobre o cliente:")
print(json.dumps(pessoa, indent=4, ensure_ascii=False))