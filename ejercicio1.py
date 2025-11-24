import random
import numpy as np

# Función objetivo a maximizar: f(x) = -x^2 + 10x
def funcion_fitness(x):
    return -x**2 + 10*x

# Crear población inicial
def crear_poblacion(tamano, min_val, max_val):
    return [random.uniform(min_val, max_val) for _ in range(tamano)]

# Selección por torneo
def seleccion_torneo(poblacion, fitness, k=3):
    seleccionados = random.sample(list(zip(poblacion, fitness)), k)
    seleccionados.sort(key=lambda x: x[1], reverse=True)
    return seleccionados[0][0]

# Cruce de un punto (para valores reales, promedio)
def cruce(padre1, padre2):
    alpha = random.random()
    hijo1 = alpha * padre1 + (1 - alpha) * padre2
    hijo2 = alpha * padre2 + (1 - alpha) * padre1
    return hijo1, hijo2

# Mutación
def mutacion(individuo, tasa_mutacion, min_val, max_val):
    if random.random() < tasa_mutacion:
        return individuo + random.gauss(0, 1)
    return individuo

# Algoritmo Genético principal
def algoritmo_genetico(generaciones=50, tam_poblacion=20):
    # Parámetros
    min_val, max_val = -10, 20
    tasa_mutacion = 0.1
    
    # Inicialización
    poblacion = crear_poblacion(tam_poblacion, min_val, max_val)
    
    mejor_historico = None
    mejor_fitness_historico = float('-inf')
    
    for gen in range(generaciones):
        # Evaluación
        fitness = [funcion_fitness(ind) for ind in poblacion]
        
        # Mejor de la generación
        mejor_idx = fitness.index(max(fitness))
        if fitness[mejor_idx] > mejor_fitness_historico:
            mejor_historico = poblacion[mejor_idx]
            mejor_fitness_historico = fitness[mejor_idx]
        
        # Nueva población
        nueva_poblacion = []
        
        # Elitismo: mantener el mejor
        nueva_poblacion.append(poblacion[mejor_idx])
        
        # Generar nueva población
        while len(nueva_poblacion) < tam_poblacion:
            # Selección
            padre1 = seleccion_torneo(poblacion, fitness)
            padre2 = seleccion_torneo(poblacion, fitness)
            
            # Cruce
            hijo1, hijo2 = cruce(padre1, padre2)
            
            # Mutación
            hijo1 = mutacion(hijo1, tasa_mutacion, min_val, max_val)
            hijo2 = mutacion(hijo2, tasa_mutacion, min_val, max_val)
            
            nueva_poblacion.extend([hijo1, hijo2])
        
        poblacion = nueva_poblacion[:tam_poblacion]
        
        if gen % 10 == 0:
            print(f"Generación {gen}: Mejor fitness = {mejor_fitness_historico:.4f}, x = {mejor_historico:.4f}")
    
    return mejor_historico, mejor_fitness_historico

# Ejecutar el algoritmo
print("=== Optimización con Algoritmo Genético ===\n")
mejor_x, mejor_f = algoritmo_genetico(generaciones=50, tam_poblacion=20)
print(f"\nSolución óptima encontrada:")
print(f"x = {mejor_x:.4f}")
print(f"f(x) = {mejor_f:.4f}")
print(f"\nSolución teórica: x = 5, f(x) = 25")