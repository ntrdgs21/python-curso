pessoas = {'nathan':'22','ariadne':'16','marjorie':'5','aisha':'27','celio':'13'}

print("O número favorito de cada pessoa é:")
for chave, valor in pessoas.items(): 
     print(f"{chave.replace('_', ' ').title()}: {valor}")