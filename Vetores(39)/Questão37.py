def ordenar_vetor_especial(vetor):
 
    parte_crescente = vetor[:6]
    parte_decrescente = vetor[6:]

    parte_decrescente.reverse()

    vetor_ordenado = sorted(parte_crescente + parte_decrescente)

    return vetor_ordenado

vetor = [1, 2, 3, 4, 5, 6, 11, 10, 9, 8, 7] 

vetor_ordenado = ordenar_vetor_especial(vetor)

print("Vetor ordenado:", vetor_ordenado)
