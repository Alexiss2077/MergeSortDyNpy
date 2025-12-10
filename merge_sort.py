class MergeSorter:
    """
    Clase que contiene la lógica de ordenamiento Merge Sort.
    """
    def __init__(self):
        self.Mezclas    = 0
        self.Divisiones = 0

    # =======================================================
    # MÉTODO MERGE (Fusión de listas)
    # =======================================================
    def merge(self, my_list, left, right):
        """
        Mezcla dos listas ordenadas ('left' y 'right') guardando
        el resultado en 'my_list' (la lista destino).
        """
        i, j, k = 0, 0, 0  # Índices para izquierda, derecha y destino

        # 1. Comparar y mover el menor a la lista destino
        while i < len(left) and j < len(right): # Mientras haya elementos en ambas listas
            if left[i] < right[j]: # El de la izquierda es menor
                my_list[k] = left[i] # Copiar a la lista destino
                i += 1
            else: # El de la derecha es menor o igual
                my_list[k] = right[j] # Copiar a la lista destino
                j += 1
            k += 1

        # 2. Si sobraron elementos en la izquierda, los copiamos
        while i < len(left): # Mientras queden en la izquierda
            my_list[k] = left[i] # Copiar a la lista destino
            i += 1
            k += 1

        # 3. Si sobraron elementos en la derecha, los copiamos
        while j < len(right): # Mientras queden en la derecha
            my_list[k] = right[j] # Copiar a la lista destino
            j += 1
            k += 1
            

    # =======================================================
    # OPCIÓN 1: MERGE SORT RECURSIVO (Divide y Vencerás)
    # =======================================================
    def sort_direct(self, my_list):
        # 1. Caso Base: Una lista de 0 o 1 elemento ya esta ordenada
        if len(my_list) <= 1:
            return
        
        # 2. Dividir: Crear copias de las mitades
        mid = len(my_list) // 2 # Índice medio
        self.Divisiones += 1
        
        left = my_list[:mid] # Mitad izquierda
        right = my_list[mid:] # Mitad derecha

        print(f"Dividir: {my_list} -> {left} | {right}")

        # 3. Vencerás: Ordenar recursivamente cada mitad
        self.sort_direct(left)   # Ordena la mitad izquierda
        self.sort_direct(right)  # Ordena la mitad derecha

        # 4. Combinar: Usar el método merge
        self.Mezclas += 1
        self.merge(my_list, left, right) # Mezclar las dos mitades ordenadas

        print(f"Mezclar : {left} + {right} ---> Queda {my_list}")

    # =======================================================
    # OPCIÓN 2: MERGE SORT NATURAL (Por Secuencias)
    # =======================================================
    def sort_natural(self, my_list):
        
        while True:
            # 1. Buscar secuencias que ya vienen ordenadas (runs)
            runs = self.get_natural_runs(my_list) # Lista de secuencias ordenadas
            
            # Si solo hay 1 secuencia (o ninguna), terminamos
            if len(runs) <= 1:
                return

            self.Divisiones += 1
            nuevas_secuencias = [] # Para guardar las nuevas secuencias mezcladas
            
            # 2. Mezclar parejas de secuencias
            while len(runs) > 1:
                seq1 = runs.pop(0) # Primera secuencia
                seq2 = runs.pop(0) # Segunda secuencia
                print(f"Mezclando secuencias: {seq1} + {seq2}")
                
                # Crear espacio para la mezcla
                tamano_total = len(seq1) + len(seq2) # Tamaño combinado
                mezclar = [0] * tamano_total # Lista vacía para la mezcla        
                
                # Mezclamos
                self.Mezclas += 1
                self.merge(mezclar, seq1, seq2) # Mezclar las dos secuencias
                
                nuevas_secuencias.append(mezclar) # Guardar la secuencia mezclada
                        
            # Si quedó una secuencia huérfana (impar), la pasamos a la siguiente ronda
            if runs: 
                nuevas_secuencias.append(runs[0]) # Agregar la última secuencia sin mezclar
                print(f" Secuencia huérfana: {runs[0]}")
            
            # 3. Reconstruir la lista original completa para la siguiente iteración
            my_list.clear() # Vaciar la lista original
            for seq in nuevas_secuencias: # Agregar las nuevas secuencias mezcladas
                my_list.extend(seq) # Añadir los elementos de la secuencia
            
            # print(f"--- Fin de pasada: {my_list} ---")

    def get_natural_runs(self, my_list):
        """Detecta partes de la lista que ya están ordenadas."""
        if not my_list: return [] # Lista vacía
        
        runs = [] # Lista de secuencias ordenadas
        actual = [my_list[0]] # Iniciar la primera secuencia
        
        for i in range(1, len(my_list)): # Desde el segundo elemento
            if my_list[i] >= my_list[i-1]: # Si sigue en orden ascendente
                actual.append(my_list[i]) # Agregar a la secuencia actual
            else: # Si se rompe el orden
                runs.append(actual)   # Guardar la secuencia actual
                actual = [my_list[i]]  # Iniciar una nueva secuencia

        runs.append(actual) # Guardar la última secuencia
        return runs 