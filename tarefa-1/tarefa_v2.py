# Rodrigo Fuelber Franke

import random as rand
import math
import time

import sys
sys.setrecursionlimit(2000) # Set a new limit, e.g., 2000

RANDOM_QUANT = 1_000
RANDOM_RANGE = 0, 1_500

def generate_array(random_num) -> list[int]:
    return [rand.randint(RANDOM_RANGE[0], RANDOM_RANGE[1]) for _ in range (random_num)]

def quicksort(array_original: list[int]) -> list[int]:
    
    if not array_original:
        return array_original
    
    array_ordenado = []
    
    menor, igual, maior = [], [], []
    
    pivot = array_original[len(array_original)-1]
    
    for num in array_original:
        if num < pivot:
            menor.append(num)
            
        elif num == pivot:
            igual.append(num)
            
        else:
            maior.append(num)
            
    array_ordenado = quicksort(menor) + igual + quicksort(maior)
    
    return array_ordenado


def is_prime(number: int) -> bool:
    if number <= 1:
        return False
    
    if number == 2:
        return True
    
    if number % 2 == 0:
        return False
    
    for num in range(3, int(math.sqrt(number))+1, 2):
        if number % num == 0:
            return False
        
    return True

def find_primes(array: list[int]) -> list[int]:
        return list(filter(is_prime, array))



tamanhos_tempos = {}
option = 1_000
options = [1_000, 1_000, 5_000, 5_000, 10_000, 10_000, 50_000, 50_000, 100_000, 100_000]

def estatistica():
    resultados = {}

    for idx, valor in enumerate(options):
        chave = f"C{idx+1}"
        cenarios = []
        for _ in range(1, 11):
            dicionario = {}
            if idx % 2 == 0:  
                inicio_geral = time.perf_counter()
                array_desordenado = generate_array(valor)

                # TOrdenar Quicksort
                start_time = time.perf_counter()
                array_ordenado = quicksort(array_desordenado)
                end_time = time.perf_counter()
                dicionario["TOrdenar"] = f"Tempo: {(end_time - start_time) * 1000:.3f} ms"

                # TPrimos
                start_time = time.perf_counter()
                primes = find_primes(array_desordenado)
                end_time = time.perf_counter()
                dicionario["TPrimos"] = f"Tempo: {(end_time - start_time) * 1000:.3f} ms"

                # TTotal
                final_geral = time.perf_counter()
                dicionario["Tempo Total"] = f"Tempo: {(final_geral - inicio_geral) * 1000:.3f} ms"

            else:  
                inicio_gerar = time.perf_counter()
                array_desordenado = generate_array(valor)
                final_gerar = time.perf_counter()
                tempo_gerar = (final_gerar - inicio_gerar) * 1000  # ms

                array_ordenado = quicksort(array_desordenado)

                inicio_geral = time.perf_counter()

                # TOrdenar Quicksort
                start_time = time.perf_counter()
                array_ordenado = quicksort(array_ordenado)
                end_time = time.perf_counter()
                dicionario["TOrdenar"] = f"Tempo: {(end_time - start_time) * 1000:.3f} ms"

                # TPrimos
                start_time = time.perf_counter()
                primes = find_primes(array_desordenado)
                end_time = time.perf_counter()
                dicionario["TPrimos"] = f"Tempo: {(end_time - start_time) * 1000:.3f} ms"

                # TTotal
                final_geral = time.perf_counter()
                elapsed_time = (final_geral - inicio_geral) * 1000 + tempo_gerar
                dicionario["Tempo Total"] = f"Tempo: {elapsed_time:.3f} ms"

            cenarios.append(dicionario)
        resultados[chave] = cenarios

    return resultados

def opcoes():
    #for option in options:
        for i in range(10):
            temp = {}
            inicio_geral = time.perf_counter()

            # Gerar Array
            start_time = time.perf_counter()
            arr = generate_array(option)
            end_time = time.perf_counter()
            elapsed_time = (end_time - start_time) * 1000  # ms
            string = f"Tempo: {elapsed_time:.3f} ms"
            temp["Gerar Array"] = string

            # Quicksort
            start_time = time.perf_counter()
            sorted_arr = quicksort(arr)
            end_time = time.perf_counter()
            elapsed_time = (end_time - start_time) * 1000  # ms
            string = f"Tempo: {elapsed_time:.3f} ms"
            temp["Quicksort desordenado"] = string

            # Checar Primos não ordenado
            start_time = time.perf_counter()
            primes = find_primes(sorted_arr)
            end_time = time.perf_counter()
            elapsed_time = (end_time - start_time) * 1000  # ms
            string = f"Tempo: {elapsed_time:.3f} ms"
            temp["Checar Primos desordenado"] = string

            # Tempo Total
            final_geral = time.perf_counter()
            elapsed_time = (final_geral - inicio_geral) * 1000  # ms
            string = f"Tempo: {elapsed_time:.3f} ms"
            temp["Tempo Total p1"] = string


            inicio_ordenados = time.perf_counter()
            # Quicksort já ordenado
            start_time = time.perf_counter()
            sorted_arr = quicksort(sorted_arr)
            end_time = time.perf_counter()
            elapsed_time = (end_time - start_time) * 1000  # ms
            string = f"Tempo: {elapsed_time:.3f} ms"
            temp["Quicksort ordenado"] = string

            # Checar Primos já ordenados
            start_time = time.perf_counter()
            primes = find_primes(sorted_arr)
            end_time = time.perf_counter()
            elapsed_time = (end_time - start_time) * 1000  # ms
            string = f"Tempo: {elapsed_time:.3f} ms"
            temp["Checar Primos ordenado"] = string
            #tamanhos_tempos[f"{option}"] = temp


            # Tempo Total
            final_ordenados = time.perf_counter()
            elapsed_time = (final_ordenados - inicio_ordenados) * 1000  # ms
            string = f"Tempo: {elapsed_time:.3f} ms"
            temp["Tempo Total p2"] = string

            temp["Quantidade de Primos"] = len(primes)
            tamanhos_tempos[f"{option}_{i}"] = temp

        return tamanhos_tempos

    
import json
if __name__ == "__main__":
    filename = "estatisticas.json"
    valores = estatistica()
    with open(filename, 'w') as f:
        json.dump(valores, f, indent=4) # indent=4 for pretty-printing with 4 spaces

    resultados_json = {}
    for cenario, resultados in valores.items():
        soma_tordenar = 0.0
        soma_tprimos = 0.0
        soma_ttotal = 0.0
        for res in resultados:
            tordenar = float(res["TOrdenar"].split(":")[1].replace("ms", "").strip())
            tprimos = float(res["TPrimos"].split(":")[1].replace("ms", "").strip())
            ttotal = float(res["Tempo Total"].split(":")[1].replace("ms", "").strip())
            soma_tordenar += tordenar
            soma_tprimos += tprimos
            soma_ttotal += ttotal
        tordenar_media = soma_tordenar / 10
        tprimos_media = soma_tprimos / 10
        ttotal_media = soma_ttotal / 10
        pct_tordenar = (tordenar_media / ttotal_media) * 100
        pct_tprimos = (tprimos_media / ttotal_media) * 100
        resultados_json[cenario] = {
            "%TOrdenar": round(pct_tordenar, 2),
            "%TPrimos": round(pct_tprimos, 2),
            "TMedia": round(ttotal_media, 2)
        }
    with open("resultados.json", "w") as f:
        json.dump(resultados_json, f, indent=4)