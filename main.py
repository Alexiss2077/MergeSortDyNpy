import random
from merge_sort import MergeSorter

def main():
    sorter = MergeSorter()
    
    print("=== ORDENAMIENTO ===")
    
    # 1. Generar Lista
    try:
        n = int(input("¿Cuántos números deseas ordenar? "))
    except ValueError:
        n = 10
        
    my_list = [random.randint(1, 100) for _ in range(n)]
    print(f"\n[Original]: {my_list}")

    # 2. Menú
    print("\nElige el método:")
    print("1. Merge Sort Recursivo")
    print("2. Merge Sort Natural")
    opcion = input("Opción > ")

    # 3. Ordenar
    if opcion == "1":
        print("\n--> Ordenando recursivamente...")
        sorter.sort_direct(my_list)
    elif opcion == "2":
        print("\n--> Ordenando naturalmente...")
        sorter.sort_natural(my_list)
    else:
        print("Opción no válida.")

    
    if opcion == "1":
        # Reiniciar contadores
        sorter.SwapCount = 0
        sorter.ComparisonCount = 0
        
        sorter.sort_direct(my_list)
        
        print(f"Comparaciones: {sorter.ComparisonCount}")
        print(f"Movimientos: {sorter.SwapCount}")

    elif opcion == "2":
        # Reiniciar contadores
        sorter.SwapCount = 0
        sorter.ComparisonCount = 0
        
        sorter.sort_natural(my_list)
        
        print(f"Comparaciones: {sorter.ComparisonCount}")
        print(f"Movimientos: {sorter.SwapCount}")

    # 4. Resultado
    print(f"\n[Ordenada]: {my_list} ")

if __name__ == "__main__":
    main()