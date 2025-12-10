class MergeSorter:
    """
    Clase que contiene la lógica de ordenamiento Merge Sort.
    """

    # =======================================================
    # MÉTODO MERGE 
    # =======================================================

    SwapCount = 0       
    ComparisonCount = 0 
    def merge(self, my_list, left, right):
        """
        Mezcla dos listas ordenadas ('izquierda' y 'derecha') guardando
        el resultado en 'lista_destino' usando el índice 'k'.
        """
        i, j, k = 0, 0, 0  # Índices para izquierda, derecha y destino

        # 1. Comparar y mover el menor a la lista destino
        while i < len(left) and j < len(right): 
            self.ComparisonCount += 1  # Contar comparación
            if left[i] < right[j]: # Si el de la izquierda es menor
                my_list[k] = left[i] # Sobrescribimos usando k
                self.SwapCount +=1
                i += 1
            else:
                my_list[k] = right[j]
                self.SwapCount +=1   # Sobrescribimos usando k
                j += 1
            k += 1 # Avanzamos una casilla en el destino

        # 2. Si sobraron elementos en la izquierda, los copiamos
        while i < len(left): # Mientras i sea menor al tamaño de la izquierda
            my_list[k] = left[i]
            self.SwapCount +=1
            i += 1
            k += 1

        # 3. Si sobraron elementos en la derecha, los copiamos
        while j < len(right):
            my_list[k] = right[j]
            self.SwapCount +=1
            j += 1
            k += 1
            
        print(my_list)
  

    # =======================================================
    # OPCIÓN 1: MERGE SORT RECURSIVO (Divide y Vencerás)
    # =======================================================
    def sort_direct(self, my_list):

        print(my_list)
        # 1. Caso Base: Una lista de 0 o 1 elemento ya está ordenada
        if len(my_list) <= 1:
            return

        # 2. Dividir: Crear copias de las mitades
        mid = len(my_list) // 2
        left = my_list[:mid]
        right = my_list[mid:]

        # 3. Vencerás: Ordenar recursivamente cada mitad
        self.sort_direct(left)  # Ordena la mitad izquierda
        self.sort_direct(right) # Ordena la mitad derecha

        # 4. Combinar: Usar los 3 índices para unir todo en my_list
        # Nota: 'my_list' ya tiene el tamaño correcto, así que 'k' funciona perfecto.
        self.merge(my_list, left, right)


    # =======================================================
    # OPCIÓN 2: MERGE SORT NATURAL (Por Secuencias)
    # =======================================================
    def sort_natural(self, my_list):
        # Bucle principal del Merge Sort Natural
        ordenado = False  # Bucle hasta que la lista esté ordenada
        
        while not ordenado: # Repetir hasta ordenar
            # 1. Buscar secuencias que ya vienen ordenadas (runs)
            runs = self.get_natural_runs(my_list)
            
            # Si solo hay 1 secuencia, terminamos
            if len(runs) <= 1:
                ordenado = True
                return

            nuevas_secuencias = [] # Lista para las nuevas secuencias fusionadas
            
            # 2. Mezclar parejas de secuencias
            while len(runs) > 1:
                seq1 = runs.pop(0) # Extraemos la primera secuencia
                print(seq1)
                seq2 = runs.pop(0) # Extraemos la segunda secuencia
                print(seq2)
                
                # Creamos una lista vacía pero con "espacios reservados" (ceros)
                # del tamaño exacto para que el índice 'k' pueda escribir en ella.
                tamano_total = len(seq1) + len(seq2)
                mezclar = [0] * tamano_total         
                
                # Ahora sí podemos usar el método merge con i, j, k
                self.merge(mezclar, seq1, seq2)
                
                # Agregamos la secuencia fusionada a la lista de nuevas secuencias
                nuevas_secuencias.append(mezclar)
                        
            if runs: # Si hay una secuencia restante
                nuevas_secuencias.append(runs[0]) # Agregarla tal cual
                print(nuevas_secuencias)
            
            # 3. Reconstruir la lista original con las secuencias fusionadas
            my_list.clear() # Vaciamos la lista original
            for seq in nuevas_secuencias: # Agregamos cada secuencia fusionada
                my_list.extend(seq) # Reconstruimos la lista original
               

    def get_natural_runs(self, my_list):
        """Detecta partes de la lista que ya están ordenadas."""
        if not my_list: return [] # Lista vacía
        
        runs = [] # Lista de secuencias ordenadas
        actual = [my_list[0]] # Lista para la secuencia actual
        
        for i in range(1, len(my_list)): # Empezamos desde el segundo elemento
            self.ComparisonCount += 1  # Contar comparación
            if my_list[i] >= my_list[i-1]: #mientras i sea mayor o igual a i-1
                actual.append(my_list[i]) # Agregamos a la secuencia actual
                
            else: # Si i es menor que i-1
                runs.append(actual)  # Guardamos la secuencia actual             
                actual = [my_list[i]] # Empezamos una nueva secuencia

        runs.append(actual)
        return runs