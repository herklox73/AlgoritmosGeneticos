# Instalación: pip install pygad

import pygad
import numpy as np

# Función de fitness: maximizar f(x,y) = -(x-3)^2 - (y-2)^2
def funcion_fitness(ga_instance, solucion, idx_solucion):
    x, y = solucion
    fitness = -((x - 3)**2 + (y - 2)**2)
    return fitness

# Configurar parámetros del AG
parametros_ga = {
    'num_generations': 100,
    'num_parents_mating': 4,
    'sol_per_pop': 20,
    'num_genes': 2,
    'fitness_func': funcion_fitness,
    'gene_space': [{'low': -10, 'high': 10}, {'low': -10, 'high': 10}],
    'parent_selection_type': 'sss',
    'crossover_type': 'single_point',
    'mutation_type': 'random',
    'mutation_percent_genes': 20
}

# Crear instancia del AG
ga_instance = pygad.GA(**parametros_ga)

# Ejecutar el algoritmo
print("=== Optimización con PyGAD ===\n")
ga_instance.run()

# Obtener mejor solución
solucion, fitness_solucion, _ = ga_instance.best_solution()
print(f"\nMejor solución encontrada:")
print(f"x = {solucion[0]:.4f}, y = {solucion[1]:.4f}")
print(f"Fitness = {fitness_solucion:.4f}")
print(f"\nÓptimo teórico: x = 3, y = 2, fitness = 0")

# Visualizar evolución del fitness
ga_instance.plot_fitness()