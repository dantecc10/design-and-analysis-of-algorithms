---
marp: true
theme: default
paginate: true
header: 'Análisis y Diseño de Algoritmos — BUAP'
footer: 'Problema del Fontanero Diligente'
style: |
  section {
    font-family: 'Helvetica Neue', Arial, sans-serif;
    font-size: 26px;
  }
  h1 {
    color: #0b3c5d;
  }
  h2 {
    color: #1d2731;
  }
  table {
    font-size: 20px;
  }
---

<!-- _class: lead -->
# Análisis y Diseño de Algoritmos para el Problema del Fontanero Diligente

### Técnicas de diseño, demostración de optimalidad voraz y clases de complejidad

**Integrantes:**
* Dante Castelán Carpinteyro (Matrícula: 202320271)
* Yoshua Rameli Adán Pérez

**Docente:** Mtra. Irene Olaya Ayaquica Martínez  
**Institución:** Benemérita Universidad Autónoma de Puebla (BUAP)  
*Noviembre 2026*

---

## 1. Motivación y Planteamiento del Problema

* **Enunciado Clásico:**
  * Un fontanero tiene $n$ averías urgentes por reparar.
  * Se conoce la duración exacta de cada reparación: $\{t_1, t_2, \dots, t_n\}$.
  * El fontanero trabaja solo (un único servidor) y sin interrupciones.

* **Objetivo de Optimización:**
  * Determinar el orden de atención que **minimice el tiempo medio de espera de los clientes** (o el tiempo total acumulado).

* **Intuitivamente:**
  * Atender averías cortas primero reduce drásticamente la espera acumulada de los clientes posteriores.

---

## 2. Formulación Matemática Rigurosa

* **Tareas:** $T = \{1, 2, \dots, n\}$ con tiempos $t_i > 0$.
* **Secuencia de atención:** Permutación $\pi = (\pi_1, \pi_2, \dots, \pi_n)$.
* **Tiempo de espera del cliente $k$:** $E_k(\pi) = \sum_{j=1}^k t_{\pi_j}$.

* **Tiempo total acumulado de espera:**
  $$\begin{aligned}
  W(\pi) &= \sum_{k=1}^n \left( \sum_{j=1}^k t_{\pi_j} \right) = \sum_{i=1}^n (n - i + 1) t_{\pi_i} \\
  &= n \cdot t_{\pi_1} + (n - 1) \cdot t_{\pi_2} + \dots + 1 \cdot t_{\pi_n}
  \end{aligned}$$

* **Conclusión:** Minimizar el tiempo medio $\bar{W} = \frac{W}{n}$ es equivalente a minimizar la suma ponderada $W(\pi)$.

---

## 3. Técnica 1: Fuerza Bruta (Enumeración)

* **Enfoque:** Generar las $n!$ permutaciones posibles y calcular la suma ponderada de cada una.
* **Costo por permutación:** $n$ productos y $n - 1$ sumas $\implies \Theta(n)$ operaciones.
* **Complejidad Temporal:**
  $$T(n) = n! \cdot \Theta(n) = \Theta(n \cdot n!) = \Theta((n + 1)!)$$
* **Límites prácticos:**
  * Para $n = 10 \implies 3.62$ millones de rutas ($2.1\text{ s}$).
  * Para $n = 11 \implies 39.9$ millones de rutas ($>15\text{ min}$).
  * Para $n \ge 15 \implies$ Inviable.

---

## 4. Técnica 2: El Algoritmo Voraz (*Regla SPT*)

* **Regla SPT (*Shortest Processing Time First*):**
  * Ordenar las tareas en orden no decreciente de duraciones:
    $$t_{\pi^*_1} \le t_{\pi^*_2} \le \dots \le t_{\pi^*_n}$$

* **Estructura del Algoritmo:**
  1. Ordenar el arreglo de duraciones mediante MergeSort o HeapSort: $\Theta(n \log n)$.
  2. Calcular el costo acumulado: $\Theta(n)$.

* **Complejidad:**
  * **Temporal:** $\Theta(n \log n)$ (o $\Theta(n)$ si los tiempos son enteros con Counting Sort).
  * **Espacial:** $\Theta(n)$.

---

## 5. Demostración Matemática Formal de Optimalidad

* **Método del Argumento de Intercambio (*Exchange Argument*):**
  * Supongamos una permutación óptima $\pi$ con inversión: $t_{\pi_k} > t_{\pi_{k+1}}$.
  * Creamos $\pi'$ intercambiando $\pi_k$ y $\pi_{k+1}$.
  * Diferencia de costo paso a paso:
    $$\begin{aligned}
    W(\pi) - W(\pi') &= \left[ (n - k + 1)t_{\pi_k} + (n - k)t_{\pi_{k+1}} \right] - \left[ (n - k + 1)t_{\pi_{k+1}} + (n - k)t_{\pi_k} \right] \\
    &= [(n - k + 1) - (n - k)] (t_{\pi_k} - t_{\pi_{k+1}}) \\
    &= 1 \cdot (t_{\pi_k} - t_{\pi_{k+1}}) > 0
    \end{aligned}$$
  * Como $W(\pi) - W(\pi') > 0 \implies W(\pi') < W(\pi)$ (contradicción con la optimalidad de $\pi$).
  * **Queda demostrado que ordenar de menor a mayor es estrictamente óptimo.**

---

## 6. Técnicas 3 y 4: Vuelta Atrás y Ramificación y Poda

* **Vuelta Atrás (*Backtracking*):**
  * Construcción de la solución por etapas en profundidad (DFS).
  * Poda por cota inferior del tiempo residual de las tareas no asignadas.
  * Reduce el espacio de búsqueda pero mantiene peor caso factorial.

* **Ramificación y Poda (*Branch and Bound*):**
  * Búsqueda por mejor primero (LC) con Cola de Prioridad (*Min-Heap*).
  * La cota inferior ($LB$) basada en SPT guía al algoritmo directamente a la solución óptima.

---

## 7. Generalizaciones Relevantes

1. **Clientes con Prioridades / Pesos ($w_i$):**
   * Regla de Smith (1956): Ordenar en orden no decreciente de $\frac{t_i}{w_i}$.
   * Complejidad: $\Theta(n \log n) \implies$ **Permanece en $P$**.

2. **Múltiples Fontaneros ($m$ máquinas paralelas):**
   * Ordenar tareas por SPT y repartir en round-robin a las $m$ cuadrillas.
   * Complejidad: $\Theta(n \log n) \implies$ **Permanece en $P$**.

3. **Con Tiempos de Traslado Geográfico (*Traveling Repairman Problem*):**
   * Si se añaden distancias en red entre domicilios, el problema pasa de ser polinomial a ser **$NP\text{-Completo}$ en decisión y $NP\text{-Duro}$ en optimización**.

---

## 8. Comparativa Empírica de Rendimiento (Benchmark Real)

| $n$ (Averías) | Fuerza Bruta $\Theta(n \cdot n!)$ | Backtracking con Poda | Voraz SPT $\Theta(n \log n)$ | Optimalidad Garantizada |
|:---:|:---:|:---:|:---:|:---:|
| **4** | $0.000017\text{ s}$ | $0.000010\text{ s}$ | $0.000002\text{ s}$ | 100% Óptimo (Exacto) |
| **8** | $0.021740\text{ s}$ | $0.000047\text{ s}$ | $0.000003\text{ s}$ | 100% Óptimo (Exacto) |
| **10** | $2.103323\text{ s}$ | $0.000025\text{ s}$ | $0.000003\text{ s}$ | 100% Óptimo (Exacto) |
| **11** | $>15\text{ min}$ (Inviable) | Explorando | $0.000003\text{ s}$ | Demostrado Óptimo |
| **100** | Inviable | Inviable | $0.000018\text{ s}$ | Demostrado Óptimo |
| **10,000** | Inviable | Inviable | $0.002796\text{ s}$ | Demostrado Óptimo |
| **100,000** | Inviable | Inviable | $0.054299\text{ s}$ | Demostrado Óptimo |

---

## 9. Clases de Complejidad: Pertenencia a $P$ y $NP$

* **Pertenencia a la Clase $P$:**
  * La versión de decisión "¿Existe un orden con espera total $\le K$?" se resuelve deterministamente en $\Theta(n \log n) = O(n^2)$.
  * Por tanto, **el Fontanero Diligente pertenece a $P$**.
* **Pertenencia a la Clase $NP$:**
  * Dado que $P \subseteq NP$, pertenece a $NP$.
  * Verificador: Dada una permutación (certificado), calcula la espera en tiempo lineal $\Theta(n)$ y compara contra $K$ en $\Theta(1)$.
* **¿Es $NP\text{-Completo}$?**
  * No (suponiendo $P \ne NP$).
* **Frontera de la Complejidad:**
  * Si se introducen ventanas de tiempo, plazos de entrega (*deadlines*) o desplazamientos en grafo (*Traveling Repairman*), se vuelve **$NP\text{-Duro}$**.

---

## 10. Aplicaciones Prácticas en el Mundo Real

1. **Sistemas Operativos (Planificación de CPU - SJF):**
   * Minimiza el tiempo de retorno (*turnaround time*) y espera en la cola de procesos listos.
2. **Triage y Urgencias Hospitalarias:**
   * Despacho rápido de casos ambulatorios leves para descongestionar salas de espera.
3. **Servidores Web y Bases de Datos (Query Scheduling):**
   * Priorización de consultas SQL ligeras para optimizar la latencia media percibida.
4. **Mantenimiento Industrial:**
   * Secuenciación de órdenes mecánicas para minimizar el tiempo de inactividad de maquinaria.

---

## 11. Conclusiones

1. **Poder y Eficiencia de la Voracidad:**
   * Demuestra cómo una regla de selección voraz bien fundamentada transforma una complejidad factorial $\Theta(n \cdot n!)$ en un proceso determinista de $\Theta(n \log n)$.
2. **Optimalidad Teórica Rigurosa:**
   * A diferencia de otros problemas donde la voracidad es una heurística aproximada, en el Fontanero Diligente el argumento de intercambio prueba que la solución es exactamente óptima.
3. **Comprensión de la Frontera $P$ vs. $NP$:**
   * Sirve como modelo ejemplar para contrastar problemas resolubles en tiempo polinomial frente a aquellos que caen en la intratabilidad al añadir restricciones espaciales o temporales.

---

## 12. Referencias Bibliográficas

1. **Guerequeta, R., & Vallecillo, A. (2000).** *Técnicas de Diseño de Algoritmos*. Univ. de Málaga.
2. **Brassard, G., & Bratley, P. (1997).** *Fundamentos de Algoritmia*. Prentice Hall.
3. **Cormen, T. H. et al. (2022).** *Introduction to Algorithms* (4th ed.). MIT Press.
4. **Smith, W. E. (1956).** *Various optimizers for single-stage production*. Naval Research Logistics.
5. **Pinedo, M. L. (2016).** *Scheduling: Theory, Algorithms, and Systems*. Springer.
6. **Garey, M. R., & Johnson, D. S. (1979).** *Computers and Intractability*. W. H. Freeman.
