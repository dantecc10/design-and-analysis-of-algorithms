# Especificación del Proyecto: Trabajo de Investigación y Exposición

> **Asignatura:** Análisis y Diseño de Algoritmos  
> **Docente:** Mtra. Irene Olaya Ayaquica Martínez  
> **Institución:** Benemérita Universidad Autónoma de Puebla (BUAP)  
> **Ponderación total:** 30% de la calificación final (*Trabajo de investigación: 20%* + *Exposición: 10%*)  
> **Modalidad:** Equipos de máximo 2 integrantes  

---

## 1. Objetivo General

Identificar, analizar y formalizar las **técnicas de diseño de algoritmos** aplicables a un problema clásico de optimización o decisión, así como clasificar rigurosamente dicho problema dentro de la **teoría de clases de complejidad computacional** ($P$, $NP$, $NP\text{-Completo}$, $NP\text{-Duro}$).

---

## 2. Actividades por Realizar

1. **Conformación de equipos:** Formar equipos de un máximo de **dos personas**.
2. **Selección del problema:** Elegir un único problema de la lista oficial de 15 problemas e investigar exhaustivamente las técnicas de diseño empleadas para resolverlo.
3. **Investigación de clases de complejidad:** Estudiar las clases $P$, $NP$, $NP\text{-Completo}$ y $NP\text{-Duro}$, determinando y demostrando formalmente a qué clase pertenece el problema seleccionado.
4. **Redacción del reporte formal:** Elaborar un documento de investigación con estructura académica y rigor matemático.
5. **Diseño de la presentación de diapositivas:** Crear el material visual de apoyo para la exposición oral del tema ante el grupo.

---

## 3. Catálogo de Problemas Disponibles

| # | Problema | Paradigmas Comunes Asociados | Clase Típica (Decisión / Optimización) |
|---|---|---|---|
| 1 | **Recorridos del caballo de ajedrez** (*Knight's Tour*) | Vuelta Atrás (*Backtracking*), Heurística de Warnsdorff | $NP\text{-Completo}$ (Camino Hamiltoniano) |
| 2 | **La división en párrafos** (*Text Justification*) | Programación Dinámica, Algoritmos Voraces (*Greedy*) | $P$ |
| 3 | **Caminos mínimos** (*Shortest Paths*) | Algoritmos Voraces (Dijkstra), Programación Dinámica (Bellman-Ford, Floyd-Warshall) | $P$ |
| 4 | **El agente viajero** (*Traveling Salesperson Problem - TSP*) | Fuerza Bruta, Vuelta Atrás, Ramificación y Poda, Programación Dinámica (Held-Karp), Heurísticas | $NP\text{-Completo}$ (Decisión) / $NP\text{-Duro}$ (Optimización) |
| 5 | **La mochila** (*Knapsack Problem*) | Algoritmos Voraces (Fraccionaria), Programación Dinámica (0/1), Ramificación y Poda | $NP\text{-Completo}$ (0/1) / Pseudo-polinomial |
| 6 | **El fontanero diligente** (*Pipe routing / Diligent Plumber*) | Algoritmos Voraces, Programación Dinámica | $P$ o $NP\text{-Duro}$ (según variante) |
| 7 | **La asignación de tareas** (*Assignment Problem*) | Método Húngaro, Ramificación y Poda | $P$ (Húngaro) / $NP\text{-Duro}$ (Generalizada) |
| 8 | **La multiplicación óptima de matrices** (*Matrix Chain Multiplication*) | Programación Dinámica, Memorización | $P$ |
| 9 | **Planificación** (*Interval / Job Scheduling*) | Algoritmos Voraces, Programación Dinámica, Ramificación y Poda | $P$ (Intervalos) / $NP\text{-Duro}$ (*Job-shop*) |
| 10 | **El torneo de tenis** (*Round-Robin Tournament*) | Divide y Vencerás (*Divide and Conquer*) | $P$ |
| 11 | **La función de Ackermann** | Recursión profunda, Computabilidad teórica | No recursiva primitiva |
| 12 | **Horarios de trenes** (*Train Timetabling Problem*) | Programación Entera Mixta, Heurísticas, Grafos | $NP\text{-Completo}$ |
| 13 | **Las n-reinas** (*N-Queens Problem*) | Vuelta Atrás (*Backtracking*), Ramificación y Poda | $NP\text{-Completo}$ (Generalizado) |
| 14 | **El laberinto** (*Maze Routing / Pathfinding*) | Búsqueda en Anchura (BFS), Búsqueda en Profundidad (DFS), Algoritmo $A^*$ | $P$ |
| 15 | **El coloreado de mapas** (*Map / Graph Coloring*) | Vuelta Atrás, Cadenas de Kempe, Heurística DSATUR | $P$ ($k=2$), $NP\text{-Completo}$ ($k \ge 3$) |

---

## 4. Estructura Obligatoria del Reporte (PDF)

El reporte de investigación debe seguir fielmente el orden y contenido estipulado:

### 4.1. Resumen (*Abstract*)
* Breve descripción del contenido global del documento (máximo 250-300 palabras).
* **Importante:** Debe sintetizar el documento en sí (objetivos, metodología analizada, resultados de complejidad y conclusiones), no ser una mera introducción histórica del tema.

### 4.2. Desarrollo del Tema Seleccionado
* **Descripción formal del problema:** Definición matemática precisa, variables de entrada, restricciones explícitas e implícitas, función objetivo o condición de aceptación.
* **Técnicas de diseño aplicables:**
  * Explicación teórica de cómo se implementa cada paradigma (por ejemplo: Fuerza Bruta, Vuelta Atrás, Ramificación y Poda, Programación Dinámica, Voraces/Heurísticas).
  * Pseudocódigo formal o formulación recursiva/recurrentes.
  * Análisis formal de complejidad temporal y espacial paso a paso (notaciones $O, \Omega, \Theta$).
* **Ejemplos de aplicación interdisciplinaria:**
  * Casos reales en ciencias de la computación, bioinformática, logística, ingeniería industrial, robótica, etc.
* **Clasificación en clases de complejidad:**
  * Definición teórica de las clases $P$, $NP$, $NP\text{-Completo}$ y $NP\text{-Duro}$.
  * Demostración o justificación rigurosa de a qué clase pertenece el problema (e.g. verificación de certificados en tiempo polinomial y reducción polinomial desde otro problema conocido).

### 4.3. Conclusiones
* Reflexión crítica sobre las fortalezas y debilidades de cada técnica de diseño estudiada.
* Compromiso entre optimalidad teórica y costo computacional en problemas de gran escala.

### 4.4. Bibliografía
* Mínimo **5 referencias académicas formales** (libros de texto, artículos de conferencias/revistas indexadas, documentación técnica validada).
* Formato estándar (IEEE o APA 7ma edición).

---

## 5. Estructura Obligatoria de las Diapositivas

Las diapositivas para la exposición oral deben contemplar:
1. **Diapositiva de Presentación / Portada:**
   * Título oficial del tema.
   * Nombre completo de los integrantes del equipo.
   * Nombre de la materia y de la profesora.
   * Fecha de exposición.
2. **Diapositivas de Desarrollo del Tema:**
   * Contexto y definición formal del problema.
   * Esquemas visuales del espacio de soluciones (árboles de expansión, ramificación, tablas dinámicas).
   * Comparativa de técnicas de diseño y tablas de complejidad asintótica.
   * Casos de uso prácticos.
   * Justificación de la clase de complejidad ($P$ vs $NP$).
3. **Diapositiva de Conclusiones:**
   * Hallazgos clave y lecciones aprendidas sobre el diseño algorítmico.
4. **Diapositiva de Referencias:**
   * Listado de al menos 5 fuentes bibliográficas consultadas.

---

## 6. Especificaciones de Entrega y Empaquetado

> [!WARNING]
> El incumplimiento del formato o nomenclatura puede penalizar la calificación o invalidar la entrega.

* **Formato del contenedor comprimido:** Archivo `.rar` o `.zip`.
* **Estructura interna requerida:** El comprimido debe descomprimirse en **una única carpeta principal** que contenga exactamente los dos archivos solicitados:
  ```text
  ApellidoPaterno_ApellidoMaterno_Nombre/
  ├── Reporte_Investigacion.pdf
  └── Presentacion_Exposicion.pdf (o .pptx)
  ```
* **Regla estricta de nomenclatura:**
  * **Nombre del archivo comprimido:** `ApellidoPaterno_ApellidoMaterno_Nombre.rar` (o `.zip`).
  * **Nombre de la carpeta raíz interna:** `ApellidoPaterno_ApellidoMaterno_Nombre`.
  *(En caso de ser dos integrantes, se suele usar los apellidos del integrante que realiza la entrega en plataforma o ambos según acuerdo del equipo).*
