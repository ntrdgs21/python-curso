current_users = ["nathan", "ariadne", "júnior", "joão", "marjorie"]
new_users = ["nathan", "ariadne", "maria", "isiah", "aisha"]
users_upper = [user.upper() for user in current_users]


for user in new_users:
    if user in current_users and user in users_upper:
        print(f"{user}: esse nome de usuário já está sendo usado, escolha um novo nome")
    else:
        print(f"O nome de usuário {user} está disponível")
