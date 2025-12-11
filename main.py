import random
from merge_sort import MergeSorter  

def main():
    sorter = MergeSorter()
    
    while True:
        print("\n=== ORDENAMIENTO ===")
        
        # 1. Generar Lista Aleatoria
        try:
            entrada = input("¿Cuántos números deseas ordenar? (Enter para 10): ")
            
            if entrada.lower() == "s":
                print("Saliendo del programa")
                break
            n = int(entrada) if entrada else 10 # Valor por defecto
        except ValueError:
            n = 10
            
        my_list = [random.randint(1, 100) for _ in range(n)]
        print(f"\n[Original]: {my_list}")

        # 2. Menú
        print("\nElige el método:")
        print("1. Merge Sort Directo")
        print("2. Merge Sort Natural")
        opcion = input("Opción > ")

        # 3. Ordenar
        if opcion == "1": # Merge Sort Directo
            print("\n--> Ordenando recursivamente...")
            sorter.Mezclas    = 0
            sorter.Divisiones = 0
            sorter.sort_direct(my_list)
            
        

        elif opcion == "2":
            print("\n--> Ordenando naturalmente...")
            sorter.Mezclas    = 0
            sorter.Divisiones = 0
            sorter.sort_natural(my_list)
            
            
        else:
            print("Opción no válida.")
            return

        # 4. Resultado
        print(f"\n[Ordenada]: {my_list}")
        print(f"Estadísticas -> Divisiones: {sorter.Divisiones} | Mezclas: {sorter.Mezclas}")
        

if __name__ == "__main__":
    main()
