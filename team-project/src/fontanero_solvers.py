"""
Módulo de Solución del Problema del Fontanero Diligente
Asignatura: Análisis y Diseño de Algoritmos — BUAP
Profesora: Mtra. Irene Olaya Ayaquica Martínez

Problema:
Un fontanero tiene n reparaciones pendientes con tiempos {t_1, t_2, ..., t_n}.
Se busca el orden de atención pi que minimice el tiempo total (o medio) de espera:
    W(pi) = sum_{k=1}^n (sum_{j=1}^k t_{pi_j}) = sum_{i=1}^n (n - i + 1) * t_{pi_i}

Técnicas implementadas:
1. Fuerza Bruta: O(n * n!)
2. Algoritmo Voraz (SPT - Shortest Processing Time): Theta(n log n)
3. Vuelta Atrás (Backtracking con poda por cota inferior): O(n!) peor caso
4. Generalización con Prioridades/Pesos (Regla de Smith): Theta(n log n)
5. Generalización con Múltiples Fontaneros (m máquinas paralelas): Theta(n log n)
"""

import itertools
import time
from typing import List, Tuple, Dict


def calcular_tiempo_espera_total(orden: List[int], tiempos: List[float]) -> float:
    """
    Calcula el tiempo de espera acumulado total de todos los clientes.
    W(pi) = sum_{i=1}^n (n - i + 1) * tiempos[pi[i-1]]
    """
    n = len(orden)
    w_total = 0.0
    for i, idx in enumerate(orden):
        peso = n - i
        w_total += peso * tiempos[idx]
    return w_total


def fuerza_bruta_fontanero(tiempos: List[float]) -> Tuple[float, List[int]]:
    """
    Explora todas las n! permutaciones posibles de las tareas.
    Complejidad Temporal: Theta(n * n!)
    Complejidad Espacial: Theta(n)
    """
    n = len(tiempos)
    if n == 0:
        return 0.0, []
    
    indices = list(range(n))
    mejor_espera = float('inf')
    mejor_orden = []

    for perm in itertools.permutations(indices):
        espera = calcular_tiempo_espera_total(list(perm), tiempos)
        if espera < mejor_espera:
            mejor_espera = espera
            mejor_orden = list(perm)

    return mejor_espera, mejor_orden


def voraz_fontanero(tiempos: List[float]) -> Tuple[float, List[int]]:
    """
    Algoritmo Voraz: Regla SPT (Shortest Processing Time First).
    Ordena las tareas de menor a mayor tiempo de duración.
    Garantiza la solución óptima exacta.
    Complejidad Temporal: Theta(n log n)
    Complejidad Espacial: Theta(n)
    """
    n = len(tiempos)
    if n == 0:
        return 0.0, []

    # Crear lista de tuplas (tiempo, indice_original) y ordenar en orden no decreciente
    ordenado = sorted(enumerate(tiempos), key=lambda x: x[1])
    mejor_orden = [idx for idx, _ in ordenado]
    mejor_espera = calcular_tiempo_espera_total(mejor_orden, tiempos)
    return mejor_espera, mejor_orden


def backtracking_fontanero(tiempos: List[float]) -> Tuple[float, List[int]]:
    """
    Vuelta Atrás (Backtracking) con Poda por Cota Inferior.
    Complejidad Temporal: O(n!) peor caso, pero poda ramas subóptimas.
    """
    n = len(tiempos)
    if n == 0:
        return 0.0, []

    # Solución inicial voraz para fijar la mejor cota superior inicial
    mejor_espera, mejor_orden = voraz_fontanero(tiempos)

    # Tiempos ordenados para calcular cotas inferiores rápidas
    tiempos_restantes_ordenados = sorted(tiempos)

    def cota_inferior_parcial(ruta_parcial: List[int], visitados: set) -> float:
        """Calcula una cota inferior del tiempo total alcanzable desde la ruta parcial."""
        k = len(ruta_parcial)
        # Costo exacto ya comprometido por los elementos elegidos
        costo_fijado = 0.0
        for i, idx in enumerate(ruta_parcial):
            costo_fijado += (n - i) * tiempos[idx]
        
        # Para los no visitados, el mejor escenario teórico es emparejarlos en orden SPT
        no_visitados = [tiempos[i] for i in range(n) if i not in visitados]
        no_visitados.sort()
        for j, t in enumerate(no_visitados):
            costo_fijado += (n - (k + j)) * t
        return costo_fijado

    mejor_espera_global = [mejor_espera]
    mejor_orden_global = [list(mejor_orden)]

    def backtrack(etapa: int, ruta_actual: List[int], visitados: set):
        if etapa == n:
            costo = calcular_tiempo_espera_total(ruta_actual, tiempos)
            if costo < mejor_espera_global[0]:
                mejor_espera_global[0] = costo
                mejor_orden_global[0] = list(ruta_actual)
            return

        # Cota inferior
        lb = cota_inferior_parcial(ruta_actual, visitados)
        if lb >= mejor_espera_global[0]:
            return  # Poda

        for cand in range(n):
            if cand not in visitados:
                visitados.add(cand)
                backtrack(etapa + 1, ruta_actual + [cand], visitados)
                visitados.remove(cand)

    # Iniciar búsqueda con el mejor valor conocido
    backtrack(0, [], set())
    return mejor_espera_global[0], mejor_orden_global[0]


def voraz_fontanero_con_pesos(tiempos: List[float], pesos: List[float]) -> Tuple[float, List[int]]:
    """
    Generalización con clientes de diferente importancia/prioridad (w_i).
    Regla de Smith: Ordenar por cociente (t_i / w_i) de menor a mayor.
    Minimiza sum_{i=1}^n w_i * E_i en tiempo Theta(n log n).
    """
    n = len(tiempos)
    # Ordenar por t_i / w_i ascendente
    ordenado = sorted(range(n), key=lambda i: tiempos[i] / pesos[i])
    
    # Calcular costo ponderado total
    tiempo_acumulado = 0.0
    costo_ponderado_total = 0.0
    for idx in ordenado:
        tiempo_acumulado += tiempos[idx]
        costo_ponderado_total += pesos[idx] * tiempo_acumulado

    return costo_ponderado_total, ordenado


def voraz_multiples_fontaneros(tiempos: List[float], m: int) -> Tuple[float, Dict[int, List[int]]]:
    """
    Generalización con m fontaneros trabajando en paralelo (P || sum C_j).
    Regla voraz: Ordenar tiempos de menor a mayor y repartir en round-robin a las cuadrillas.
    Garantiza solución óptima en Theta(n log n).
    """
    ordenados = sorted(enumerate(tiempos), key=lambda x: x[1])
    asignaciones = {k: [] for k in range(m)}
    
    for i, (idx, t) in enumerate(ordenados):
        fontanero_id = i % m
        asignaciones[fontanero_id].append(idx)

    # Calcular tiempo acumulado total de espera
    espera_total = 0.0
    for f_id, tareas in asignaciones.items():
        k = len(tareas)
        for j, t_idx in enumerate(tareas):
            espera_total += (k - j) * tiempos[t_idx]

    return espera_total, asignaciones
