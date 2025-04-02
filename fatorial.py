def fatorial(n):
    if n == 0 or n == 1:
        return 1
    return n * fatorial(n - 1)

while True:
    entrada = input("Digite um número para calcular o fatorial (ou 'sair' para encerrar): ")
    
    if entrada.lower() == "sair":
        print("Encerrando o programa...")
        break  # Sai do loop

    if not entrada.isdigit():
        print("Entrada inválida! Digite um número válido ou 'sair'.")
        continue  # Volta ao início do loop

    num = int(entrada)
    print(f"O fatorial de {num} é {fatorial(num)}")

