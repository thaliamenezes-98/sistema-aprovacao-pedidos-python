# Recebe a entrada do usuário (valor e prioridade)
entrada = input().strip()

valor_str, prioridade = entrada.split()

valor = int(valor_str)

# Verifica se o pedido pode ser aprovado
if valor <= 1000 and (prioridade == "alta" or prioridade == "media"):
    print("aprovado")

# Verifica se o pedido deve ir para revisão
elif valor > 1000 and prioridade == "alta":
    print("revisao")

# Todos os demais casos são rejeitados
else:
    print("rejeitado")