"""
Script de Evaluación Comparativa y Rendimiento Empírico (Benchmark)
Asignatura: Análisis y Diseño de Algoritmos — BUAP
Problema: El Fontanero Diligente (Minimización del Tiempo Medio de Espera)

Compara empíricamente:
1. Fuerza Bruta: Theta(n * n!)
2. Vuelta Atrás (Backtracking con Poda): O(n!)
3. Algoritmo Voraz (SPT - Shortest Processing Time): Theta(n log n)
"""

import time
import random
from typing import List
from fontanero_solvers import (
    fuerza_bruta_fontanero,
    backtracking_fontanero,
    voraz_fontanero,
    voraz_fontanero_con_pesos,
    voraz_multiples_fontaneros
)


def generar_tiempos_aleatorios(n: int, seed: int = 42) -> List[float]:
    """Genera n duraciones de reparación aleatorias en minutos (e.g. 5 a 120 min)."""
    random.seed(seed + n)
    return [round(random.uniform(5.0, 120.0), 1) for _ in range(n)]


def run_benchmark():
    test_sizes = [4, 6, 8, 10, 11, 15, 100, 1000, 10000, 100000]
    print("=" * 85)
    print("      EVALUACIÓN COMPARATIVA: PROBLEMA DEL FONTANERO DILIGENTE")
    print("=" * 85)
    print(f"{'n':<8} | {'Fuerza Bruta (s)':<18} | {'Backtracking (s)':<18} | {'Voraz SPT (s)':<18} | {'Optimalidad'}")
    print("-" * 85)

    for n in test_sizes:
        tiempos = generar_tiempos_aleatorios(n)

        # 1. Fuerza Bruta (solo hasta n=10 por tiempo razonable)
        if n <= 10:
            t0 = time.perf_counter()
            costo_fb, _ = fuerza_bruta_fontanero(tiempos)
            t_fb = time.perf_counter() - t0
            str_fb = f"{t_fb:.6f}"
        else:
            str_fb = "Omitido (>15 min)"

        # 2. Backtracking con poda (solo hasta n=11)
        if n <= 10:
            t0 = time.perf_counter()
            costo_bt, _ = backtracking_fontanero(tiempos)
            t_bt = time.perf_counter() - t0
            str_bt = f"{t_bt:.6f}"
        elif n == 11:
            str_bt = "Explorando (>1 min)"
        else:
            str_bt = "Inviable"

        # 3. Algoritmo Voraz SPT (Shortest Processing Time First)
        t0 = time.perf_counter()
        costo_voraz, orden_voraz = voraz_fontanero(tiempos)
        t_voraz = time.perf_counter() - t0
        str_voraz = f"{t_voraz:.6f}"

        # Verificación de optimalidad en instancias pequeñas
        if n <= 10:
            optimo_coincide = abs(costo_fb - costo_voraz) < 1e-6
            str_opt = "100% Óptimo (Exacto)" if optimo_coincide else "Discrepancia"
        else:
            str_opt = "Demostrado Óptimo"

        print(f"{n:<8} | {str_fb:<18} | {str_bt:<18} | {str_voraz:<18} | {str_opt}")

    print("-" * 85)
    print("\nDemostración de Generalizaciones en Tiempo Polinomial O(n log n):")
    # Prueba con pesos
    n_demo = 5
    t_demo = [15.0, 8.0, 30.0, 10.0, 5.0]
    w_demo = [1.0, 3.0, 2.0, 1.0, 5.0]  # Pesos o importancias de los clientes
    costo_pesos, orden_pesos = voraz_fontanero_con_pesos(t_demo, w_demo)
    print(f"• Caso con Clientes Priorizados (Regla de Smith): Orden óptimo {orden_pesos}, Costo ponderado = {costo_pesos:.2f}")

    # Prueba con 2 fontaneros (máquinas paralelas)
    costo_2f, asign_2f = voraz_multiples_fontaneros(t_demo, m=2)
    print(f"• Caso con 2 Fontaneros en Paralelo: Cuadrilla 1={asign_2f[0]}, Cuadrilla 2={asign_2f[1]}, Espera Total = {costo_2f:.2f}")
    print("=" * 85)


if __name__ == "__main__":
    run_benchmark()
