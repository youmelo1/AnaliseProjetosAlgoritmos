import random as rand
import math

RANDOM_QUANT = 1_000
RANDOM_RANGE = 0, 1_500

def generate_array() -> list[int]:
    return [rand.randint(RANDOM_RANGE[0], RANDOM_RANGE[1]) for _ in range (RANDOM_QUANT)]

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


def opcoes():
    print('Gerando array com números aleatórios...')
    arr = generate_array()
    print(f'Primeiros 5 números do array: {arr[:5]}')
    print('Ordenando array com quicksort...')
    sorted_arr = quicksort(arr)
    print(f'Primeiros 5 números do array ordenado: {sorted_arr[:5]}')

    print('Buscando números primos no array ordenado...')
    primes = find_primes(sorted_arr)
    print(f'Primeiros 5 números primos encontrados: {primes[:5]}')

    print("\nOpções:")
    print("1 - Ver todo o array aleatório")
    print("2 - Ver todo o array ordenado")
    print("3 - Ver todos os números primos encontrados")
    escolha = input("Escolha uma opção (1/2/3): ")

    while True:
        if escolha == "1":
            print("Array aleatório completo:")
            print(arr)
        elif escolha == "2":
            print("Array ordenado completo:")
            print(sorted_arr)
        elif escolha == "3":
            print("Todos os números primos encontrados:")
            print(primes)
        elif escolha == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")
        print("\nOpções:")
        print("1 - Ver todo o array aleatório")
        print("2 - Ver todo o array ordenado")
        print("3 - Ver todos os números primos encontrados")
        print("0 - Sair")
        escolha = input("Escolha uma opção (1/2/3/0): ")
 
       
if __name__ == "__main__":
    opcoes()
    