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
 
def quatro_vetor(vetor):
    resultado = []
    for valor in range(len(vetor)):
        if valor %2 ==0:
            resultado.append(vetor[valor] * vetor[valor])
        else:
            resultado.append(vetor[valor])
    return resultado

def media(vetor):
    media = sum(vetor)/len(vetor)
    return media
 
def media_acima_da_media(vetor):
    m = media(vetor)
    acima =  sum(1 for x in vetor if x > m)
    return 100 * acima / len(vetor),m  

def ordenar_metade(vetor):
    n=len(vetor)
    meio = n // 2
    primeira_metade = sorted(vetor[:meio])
    segunda_metade = sorted(vetor[n-meio:], Reverse = True)
    if n % 2 == 1:
        centro = [vetor[meio]]
    else:
        centro = []

    return primeira_metade + centro + segunda_metade
