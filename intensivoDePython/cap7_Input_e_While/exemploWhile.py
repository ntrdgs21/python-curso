# i = 1
# while i <= 5:
#     print(i)
#     i += 1

# prompt = "\nConte-me algo e eu repetirei para você: "
# prompt += "\n Digite 'sair' para encerrar o programa. "

# active = True
# while active:
#     mensagem = input(prompt)
#     if mensagem == 'sair':
#         active= False
#     else:
#         print(mensagem)

# prompt = "\nConte quais carros você tem na sua lista de compra: "
# prompt += "\n Digite 'sair' para encerrar o programa. "

# while True:
#     carro = input(prompt)
#     if carro == 'sair':
#         break
#     else:
#         print(carro)


i = 0
while i < 10:
    i +=1
    if i %2 ==0:
        continue

    print(i)