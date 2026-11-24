n = 14
min = 3
max = 28


def vetor():
    vetor = list()
    input(f"Introduza {n} valores entre {min} e {max} para formar a matriz: ")
    for i in range(n):
        while True:
            texto = input(f"  Valor {i + 1}/{n}: ").strip()
            try:
                valor = int(texto)
            except ValueError:
                print("  Entrada inválida: introduza um número inteiro.")
                continue
            if valor < min or valor > max:
                print(f"Valor fora do intervalo [{min}, {max}].")
                continue
            vetor.append(valor)
            break
    return vetor
 

vetor()