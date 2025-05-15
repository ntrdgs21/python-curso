rios = {'Amazonas':'Brasil', 'senna':'frança ', 'Gandhi ': ' India'}
rios_corrigido = {rio.strip().lower(): pais.strip().lower() for rio, pais in rios.items()}
print(rios_corrigido)

for rio, pais in rios_corrigido.items():
    print(f"O pais do rio {rio} é {pais.title()}")
