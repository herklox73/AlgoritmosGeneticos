import numpy as np
import pygad
beneficios = np.array([2, 2.5])
consumo_materiales = np.array([2, 3])
material_maximo = 500

def funcion_fitness_restricciones(ga_instance, solucion, idx):
    # Añadir offset para cumplir restricción de mínimo 10 unidades
    solucion_ajustada = solucion + 50
    
    # Calcular beneficio total
    beneficio_total = np.sum(solucion_ajustada * beneficios)
    
    # Calcular consumo de materiales
    consumo_total = np.sum(solucion_ajustada * consumo_materiales)
    
    # Penalización si se excede el límite de materiales
    if consumo_total > material_maximo:
        return 0
    else:
        return beneficio_total

# Configuración del AG
ga_optimizacion = pygad.GA(
    num_generations=1000,
    num_parents_mating=2,
    sol_per_pop=10,
    num_genes=2,
    fitness_func=funcion_fitness_restricciones,
    mutation_type='random',
    mutation_probability=0.6
)

# Ejecutar
print("=== Optimización con Restricciones ===\n")
ga_optimizacion.run()

# Resultados
mejor_solucion, mejor_fitness, _ = ga_optimizacion.best_solution()
solucion_final = mejor_solucion + 50

print(f"\nMejor solución de producción:")
print(f"Producto 1: {int(solucion_final[0])} unidades")
print(f"Producto 2: {int(solucion_final[1])} unidades")
print(f"Beneficio total: ${mejor_fitness:.2f}")

# Verificar restricciones
consumo = 2*solucion_final[0] + 3*solucion_final[1]
print(f"Consumo de materiales: {consumo:.0f}/{material_maximo}")

# Visualizar evolución
ga_optimizacion.plot_fitness()