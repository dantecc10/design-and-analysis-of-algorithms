"""
Módulo de Solución del Problema del Agente Viajero (TSP)
Asignatura: Análisis y Diseño de Algoritmos
Profesora: Mtra. Irene Olaya Ayaquica Martínez

Implementación de paradigmas algorítmicos:
1. Fuerza Bruta (Enumeración exhaustiva) - O(n!)
2. Programación Dinámica (Algoritmo de Held-Karp) - O(n^2 * 2^n)
3. Ramificación y Poda (Branch and Bound con cotas de costo mínimo)
4. Algoritmo Voraz (Heurística del Vecino más Cercano) - O(n^2)
5. Búsqueda Local (Heurística 2-Opt) - O(k * n^2)
"""

import itertools
import math
import heapq
from typing import List, Tuple, Dict


def brute_force_tsp(dist_matrix: List[List[float]]) -> Tuple[float, List[int]]:
    """
    Resuelve el TSP simétrico o asimétrico mediante Fuerza Bruta.
    Explora todas las permutaciones de los nodos {1, 2, ..., n-1} fijando el nodo 0.
    Complejidad Temporal: Theta((n-1)! * n) = Theta(n!)
    Complejidad Espacial: O(n)
    """
    n = len(dist_matrix)
    if n <= 1:
        return 0.0, [0]
    
    cities = list(range(1, n))
    min_cost = float('inf')
    best_tour = []

    for perm in itertools.permutations(cities):
        current_tour = [0] + list(perm) + [0]
        current_cost = 0.0
        for i in range(n):
            current_cost += dist_matrix[current_tour[i]][current_tour[i + 1]]
        
        if current_cost < min_cost:
            min_cost = current_cost
            best_tour = current_tour[:-1]

    return min_cost, best_tour


def held_karp_tsp(dist_matrix: List[List[float]]) -> Tuple[float, List[int]]:
    """
    Resuelve el TSP usando Programación Dinámica (Algoritmo de Bellman-Held-Karp).
    Representa subconjuntos de ciudades como máscaras de bits.
    Subproblema: C(mask, j) = costo mínimo de visitar las ciudades en 'mask',
    terminando en la ciudad 'j', habiendo iniciado en 0.
    
    Complejidad Temporal: Theta(n^2 * 2^n)
    Complejidad Espacial: Theta(n * 2^n)
    """
    n = len(dist_matrix)
    if n <= 1:
        return 0.0, [0]

    # memo[(mask, j)] = (costo_minimo, predecesor)
    # mask: entero donde el bit k está activo si la ciudad k ha sido visitada.
    memo: Dict[Tuple[int, int], Tuple[float, int]] = {}

    # Caso base: máscara sólo con la ciudad origen (0), terminando en 0 con costo 0
    memo[(1, 0)] = (0.0, -1)

    # Iterar sobre tamaños de subconjuntos de 2 a n
    for size in range(2, n + 1):
        for subset in itertools.combinations(range(1, n), size - 1):
            mask = 1  # Incluye siempre la ciudad 0
            for city in subset:
                mask |= (1 << city)
            
            for j in subset:
                prev_mask = mask ^ (1 << j)
                best_cost = float('inf')
                best_prev = -1
                
                # Probar todos los posibles predecesores 'i' en prev_mask
                if prev_mask == 1:
                    # El único predecesor es la ciudad 0
                    cost = memo[(1, 0)][0] + dist_matrix[0][j]
                    best_cost = cost
                    best_prev = 0
                else:
                    for i in subset:
                        if i != j and (prev_mask & (1 << i)):
                            if (prev_mask, i) in memo:
                                cost = memo[(prev_mask, i)][0] + dist_matrix[i][j]
                                if cost < best_cost:
                                    best_cost = cost
                                    best_prev = i

                memo[(mask, j)] = (best_cost, best_prev)

    # Cerrar el ciclo regresando a la ciudad 0
    full_mask = (1 << n) - 1
    min_total_cost = float('inf')
    last_city = -1

    for j in range(1, n):
        if (full_mask, j) in memo:
            total_cost = memo[(full_mask, j)][0] + dist_matrix[j][0]
            if total_cost < min_total_cost:
                min_total_cost = total_cost
                last_city = j

    # Reconstrucción del tour óptimo
    tour = []
    curr_city = last_city
    curr_mask = full_mask

    while curr_city != -1:
        tour.append(curr_city)
        _, prev_city = memo[(curr_mask, curr_city)]
        curr_mask ^= (1 << curr_city)
        curr_city = prev_city

    tour.reverse()
    return min_total_cost, tour


def branch_and_bound_tsp(dist_matrix: List[List[float]]) -> Tuple[float, List[int]]:
    """
    Resuelve el TSP usando Ramificación y Poda (Branch and Bound).
    Estrategia Best-First Search con cola de prioridad y cota inferior basada
    en los dos arcos de menor costo incidentes en cada vértice no visitado.
    
    Complejidad Temporal: O(n!) en el peor caso, pero típicamente podando
    el 80-95% del espacio de búsqueda.
    """
    n = len(dist_matrix)
    if n <= 1:
        return 0.0, [0]

    # Precalcular las dos aristas salientes mínimas de cada nodo para la cota inferior
    min_edges = []
    for i in range(n):
        edges = sorted([dist_matrix[i][j] for j in range(n) if i != j])
        first_min = edges[0] if len(edges) > 0 else 0.0
        second_min = edges[1] if len(edges) > 1 else first_min
        min_edges.append((first_min, second_min))

    # Cota inferior inicial: 0.5 * sum(first_min + second_min)
    initial_lower_bound = sum(e[0] + e[1] for e in min_edges) / 2.0

    # Priority Queue almacena tuplas: (cota_inferior, costo_acumulado, camino_actual, visitados_set)
    pq = []
    heapq.heappush(pq, (initial_lower_bound, 0.0, [0], {0}))

    best_cost = float('inf')
    best_tour = []

    while pq:
        lb, current_cost, path, visited = heapq.heappop(pq)

        # Si la cota inferior del nodo ya supera la mejor solución encontrada, podar
        if lb >= best_cost:
            continue

        u = path[-1]

        # Si hemos visitado todas las ciudades, cerrar el ciclo volviendo al origen 0
        if len(path) == n:
            total_cost = current_cost + dist_matrix[u][0]
            if total_cost < best_cost:
                best_cost = total_cost
                best_tour = list(path)
            continue

        # Ramificación: expandir a todas las ciudades no visitadas
        for v in range(n):
            if v not in visited:
                new_cost = current_cost + dist_matrix[u][v]
                # Estimación de nueva cota inferior
                new_visited = visited | {v}
                new_lb = new_cost
                for k in range(n):
                    if k not in new_visited:
                        new_lb += min_edges[k][0]
                new_lb += min_edges[v][0] if v != 0 else 0.0

                if new_lb < best_cost:
                    heapq.heappush(pq, (new_lb, new_cost, path + [v], new_visited))

    return best_cost, best_tour


def nearest_neighbor_tsp(dist_matrix: List[List[float]]) -> Tuple[float, List[int]]:
    """
    Heurística voraz (Greedy) del Vecino más Cercano.
    Construye una solución voraz seleccionando en cada paso la ciudad no visitada más próxima.
    Complejidad Temporal: Theta(n^2)
    Complejidad Espacial: Theta(n)
    """
    n = len(dist_matrix)
    if n <= 1:
        return 0.0, [0]

    unvisited = set(range(1, n))
    current_city = 0
    tour = [current_city]
    total_cost = 0.0

    while unvisited:
        next_city = min(unvisited, key=lambda city: dist_matrix[current_city][city])
        total_cost += dist_matrix[current_city][next_city]
        current_city = next_city
        tour.append(current_city)
        unvisited.remove(current_city)

    # Retorno al origen
    total_cost += dist_matrix[current_city][0]
    return total_cost, tour


def two_opt_improvement(dist_matrix: List[List[float]], initial_tour: List[int]) -> Tuple[float, List[int]]:
    """
    Heurística de mejora local 2-Opt.
    Elimina dos aristas que se cruzan y reconecta los subcaminos de manera invertida.
    """
    n = len(initial_tour)
    tour = list(initial_tour)
    improved = True

    def calculate_tour_cost(t: List[int]) -> float:
        cost = 0.0
        for i in range(len(t)):
            cost += dist_matrix[t[i]][t[(i + 1) % len(t)]]
        return cost

    best_cost = calculate_tour_cost(tour)

    while improved:
        improved = False
        for i in range(1, n - 1):
            for k in range(i + 1, n):
                # Calcular el cambio en la distancia al revertir el tramo de i a k
                a, b = tour[i - 1], tour[i]
                c, d = tour[k], tour[(k + 1) % n]
                
                cost_before = dist_matrix[a][b] + dist_matrix[c][d]
                cost_after = dist_matrix[a][c] + dist_matrix[b][d]

                if cost_after < cost_before - 1e-9:
                    # Invertir el segmento [i, k]
                    tour[i:k + 1] = reversed(tour[i:k + 1])
                    best_cost = calculate_tour_cost(tour)
                    improved = True
                    break
            if improved:
                break

    return best_cost, tour
