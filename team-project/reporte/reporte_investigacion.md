# Reporte de Investigación: Análisis y Diseño de Algoritmos para el Problema del Fontanero Diligente

> **Asignatura:** Análisis y Diseño de Algoritmos  
> **Docente:** Mtra. Irene Olaya Ayaquica Martínez  
> **Institución:** Benemérita Universidad Autónoma de Puebla (BUAP)  
> **Integrantes:**  
> • Dante Castelán Carpinteyro (Matrícula: 202320271)  
> • Yoshua Rameli Adán Pérez  
> **Fecha:** Noviembre de 2026  

---

## 1. Resumen

El presente trabajo expone una investigación exhaustiva, teórica y aplicada sobre el **Problema del Fontanero Diligente** (*Diligent Plumber Problem*), formulación clásica de secuenciación de tareas sobre un único procesador o servidor (*Single-Machine Scheduling to Minimize Total Completion Time*, denotado en la literatura de investigación de operaciones como $1 \parallel \sum C_j$). El objetivo primordial radica en determinar el orden óptimo de atención de $n$ reparaciones pendientes cuyas duraciones son conocidas a priori, con el propósito de minimizar el tiempo acumulado total o el tiempo medio de espera de los clientes.

Se examinan formalmente diversas técnicas de diseño algorítmico: **Fuerza Bruta**, **Vuelta Atrás (*Backtracking*)**, **Ramificación y Poda (*Branch and Bound*)** y la técnica canónica por excelencia para este problema, el **Algoritmo Voraz (*Greedy Algorithm*)** bajo la regla SPT (*Shortest Processing Time First*). Para cada paradigma se desarrolla un análisis de complejidad temporal y espacial paso a paso, sin saltos algebraicos, mediante conteo de operaciones elementales y propiedades algebraicas detalladas. Asimismo, se proporciona la demostración matemática formal de optimalidad del enfoque voraz mediante el argumento de intercambio (*Exchange Argument*).

En el ámbito de la teoría de la complejidad computacional, se demuestra que la versión de decisión del Fontanero Diligente pertenece a la clase **$P$** (y en consecuencia a **$NP$**), desmitificando la concepción de que todos los problemas de secuenciación y optimización son intratables, y contrastándolo rigurosamente con sus generalizaciones métricas y con plazos de entrega (*Traveling Repairman Problem*), las cuales transicionan a la clase **$NP\text{-Completo}$**. Finalmente, se exponen casos prácticos en planificación de procesos en sistemas operativos, salas de emergencias hospitalarias y servidores de bases de datos, concluyendo con una evaluación comparativa teórica y empírica.

---

## 2. Desarrollo del Tema Seleccionado

### 2.1. Descripción Formal del Problema del Fontanero Diligente

El problema del Fontanero Diligente se modela a partir de un conjunto finito de $n$ tareas o averías independientes:

$$T = \left\{ 1, 2, \dots, n \right\}$$

Para cada tarea $i \in T$, se conoce con exactitud su tiempo de ejecución o duración del servicio, representado por una constante real estrictamente positiva:

$$t_i \in \mathbb{R}^+, \quad \forall i \in \{1, 2, \dots, n\}$$

Se asume un modelo determinista donde:
1. El fontanero (servidor único) solo puede atender una única reparación a la vez.
2. Las tareas no son interrumpibles (ejecución sin apropiación o *non-preemptive*).
3. Todas las tareas están disponibles simultáneamente en el instante inicial $t = 0$.

#### 2.1.1. Modelado Matemático de los Tiempos de Espera
Una solución factible se define como una biyección o permutación de los índices de las tareas:

$$\pi = \left( \pi_1, \pi_2, \dots, \pi_n \right) \in \Pi_n$$

donde $\pi_k$ denota la tarea que es ejecutada en la posición $k$-ésima de la secuencia.

* **Tiempo de finalización (o espera) del cliente atendido en la posición $k$ ($E_k$):**  
  El cliente cuya reparación ocupa el turno $k$ debe esperar a que concluyan todas las tareas precedentes más el tiempo que dura su propia reparación:
  $$E_k(\pi) = \sum_{j=1}^k t_{\pi_j}$$

* **Tiempo total acumulado de espera de todos los clientes ($W(\pi)$):**  
  Corresponde a la sumatoria de los tiempos individuales de los $n$ clientes:
  $$W(\pi) = \sum_{k=1}^n E_k(\pi) = \sum_{k=1}^n \left( \sum_{j=1}^k t_{\pi_j} \right)$$

* **Desglose algebraico paso a paso de la doble sumatoria:**  
  Expandimos término a término la expresión para revelar la ponderación intrínseca de cada posición:
  $$\begin{aligned}
  W(\pi) &= E_1(\pi) + E_2(\pi) + E_3(\pi) + \dots + E_n(\pi) \\
  &= \left( t_{\pi_1} \right) \\
  &\quad + \left( t_{\pi_1} + t_{\pi_2} \right) \\
  &\quad + \left( t_{\pi_1} + t_{\pi_2} + t_{\pi_3} \right) \\
  &\quad \quad \vdots \\
  &\quad + \left( t_{\pi_1} + t_{\pi_2} + t_{\pi_3} + \dots + t_{\pi_n} \right)
  \end{aligned}$$

  Agrupamos los coeficientes asociados a cada tarea $t_{\pi_i}$ según las veces que aparece en las sumas parciales:
  * El término $t_{\pi_1}$ aparece en las $n$ sumas parciales $\implies n \cdot t_{\pi_1}$.
  * El término $t_{\pi_2}$ aparece en $n - 1$ sumas parciales $\implies (n - 1) \cdot t_{\pi_2}$.
  * En general, el término $t_{\pi_i}$ aparece en exactamente $n - i + 1$ sumas parciales.

  Por lo tanto, simplificamos la doble sumatoria en una suma ponderada lineal única:
  $$\begin{aligned}
  W(\pi) &= n \cdot t_{\pi_1} + (n - 1) \cdot t_{\pi_2} + (n - 2) \cdot t_{\pi_3} + \dots + 1 \cdot t_{\pi_n} \\
  &= \sum_{i=1}^n (n - i + 1) \cdot t_{\pi_i}
  \end{aligned}$$

* **Tiempo medio de espera ($\bar{W}(\pi)$):**
  $$\bar{W}(\pi) = \frac{W(\pi)}{n} = \frac{1}{n} \sum_{i=1}^n (n - i + 1) \cdot t_{\pi_i}$$
  Dado que $n$ es una constante positiva fija para una instancia dada, **minimizar el tiempo medio $\bar{W}(\pi)$ es matemáticamente equivalente a minimizar la suma acumulada $W(\pi)$**:
  $$\arg\min_{\pi \in \Pi_n} \bar{W}(\pi) = \arg\min_{\pi \in \Pi_n} W(\pi)$$

#### 2.1.2. Versión de Decisión del Fontanero Diligente ($FD_{\text{dec}}$)
Dada una instancia conformada por los tiempos $\{t_1, \dots, t_n\}$ y una cota real o entera $K \in \mathbb{R}^+$, la versión de decisión responde:
$$\text{¿Existe una permutación } \pi \in \Pi_n \text{ tal que } W(\pi) \le K \text{?}$$

---

### 2.2. Técnicas de Diseño Algorítmico Aplicables

---

#### 2.2.1. Técnica 1: Fuerza Bruta (Enumeración Exhaustiva)

**Descripción Teórica:**  
Consiste en generar de forma sistemática las $n!$ permutaciones posibles del conjunto de tareas $\{1, 2, \dots, n\}$. Para cada permutación generada, se evalúa la función de costo ponderado $W(\pi)$ y se mantiene un registro de la permutación que produzca el menor valor.

**Deducción Paso a Paso de la Complejidad Temporal:**  
1. **Número de permutaciones:** Para un conjunto de $n$ elementos, existen:
   $$N_{\text{perm}} = n!$$
2. **Costo por permutación evaluada:**  
   Calcular $W(\pi) = \sum_{i=1}^n (n - i + 1) t_{\pi_i}$ requiere realizar $n$ multiplicaciones y $n - 1$ adiciones. Por lo tanto, el cómputo de la función objetivo toma $\Theta(n)$ operaciones elementales por cada permutación.
3. **Cálculo de la función de tiempo total $T_{\text{FB}}(n)$:**
   $$\begin{aligned}
   T_{\text{FB}}(n) &= n! \cdot \Theta(n) \\
   &= \Theta\left( n \cdot n! \right) \\
   &= \Theta((n + 1)!)
   \end{aligned}$$
4. **Comportamiento Asintótico:** Por la aproximación de Stirling:
   $$\begin{aligned}
   n! &\sim \sqrt{2 \pi n} \left( \frac{n}{e} \right)^n
   \end{aligned}$$
   Para $n = 12$, $12! = 479,001,600$ permutaciones, lo que requiere miles de millones de operaciones elementales. Para $n \ge 15$, la fuerza bruta resulta completamente inviable.
* **Complejidad Temporal:** $\Theta(n \cdot n!)$
* **Complejidad Espacial:** $\Theta(n)$ para almacenar la permutación en curso.

---

#### 2.2.2. Técnica 2: Algoritmo Voraz (*Greedy* / Regla SPT) — Enfoque Canónico

**Descripción Teórica:**  
La estrategia voraz resuelve el problema ordenando las tareas según la regla **SPT** (*Shortest Processing Time First*): atender las tareas en orden no decreciente de sus tiempos de duración:

$$t_{\pi^*_1} \le t_{\pi^*_2} \le \dots \le t_{\pi^*_n}$$

**Demostración Formal de Optimalidad (Argumento de Intercambio / *Exchange Argument*):**  
Demostraremos por contradicción que cualquier permutación óptima debe ordenar las tareas de menor a mayor duración.

1. **Hipótesis:** Supongamos que existe una permutación óptima $\pi$ que no sigue el orden no decreciente de duraciones.
2. Entonces, deben existir forzosamente dos tareas adyacentes en las posiciones $k$ y $k + 1$ tales que:
   $$t_{\pi_k} > t_{\pi_{k+1}}$$
3. Construimos una nueva permutación $\pi'$ idéntica a $\pi$, excepto que intercambiamos de lugar las tareas de las posiciones $k$ y $k + 1$:
   $$\pi' = \left( \pi_1, \dots, \pi_{k-1}, \pi_{k+1}, \pi_k, \pi_{k+2}, \dots, \pi_n \right)$$
4. Evaluamos la diferencia de costos $W(\pi) - W(\pi')$.  
   Las tareas en las posiciones $1, \dots, k - 1$ y $k + 2, \dots, n$ conservan exactamente sus mismos coeficientes ponderadores en ambas permutaciones, por lo que su aporte se anula en la resta:
   $$\begin{aligned}
   W(\pi) - W(\pi') &= \left[ (n - k + 1) t_{\pi_k} + (n - (k + 1) + 1) t_{\pi_{k+1}} \right] \\
   &\quad - \left[ (n - k + 1) t_{\pi_{k+1}} + (n - (k + 1) + 1) t_{\pi_k} \right]
   \end{aligned}$$
5. Simplificamos los índices algebraicamente paso a paso:
   * Notamos que $n - (k + 1) + 1 = n - k$.
   * Sustituyendo:
     $$\begin{aligned}
     W(\pi) - W(\pi') &= \left[ (n - k + 1) t_{\pi_k} + (n - k) t_{\pi_{k+1}} \right] - \left[ (n - k + 1) t_{\pi_{k+1}} + (n - k) t_{\pi_k} \right] \\
     &= (n - k + 1) t_{\pi_k} - (n - k) t_{\pi_k} + (n - k) t_{\pi_{k+1}} - (n - k + 1) t_{\pi_{k+1}}
     \end{aligned}$$
6. Factorizamos término a término:
   $$\begin{aligned}
   W(\pi) - W(\pi') &= \left[ (n - k + 1) - (n - k) \right] t_{\pi_k} - \left[ (n - k + 1) - (n - k) \right] t_{\pi_{k+1}} \\
   &= [1] \cdot t_{\pi_k} - [1] \cdot t_{\pi_{k+1}} \\
   &= t_{\pi_k} - t_{\pi_{k+1}}
   \end{aligned}$$
7. Como por hipótesis $t_{\pi_k} > t_{\pi_{k+1}}$, se deduce rigurosamente que:
   $$W(\pi) - W(\pi') > 0 \implies W(\pi') < W(\pi)$$
   Esto demuestra que la nueva permutación $\pi'$ tiene un tiempo de espera estrictamente menor que $\pi$, lo cual contradice la suposición de que $\pi$ era óptima.
8. En conclusión, en toda solución óptima no puede existir ninguna inversión de duraciones, por lo que **la ordenación no decreciente (SPT) es estrictamente óptima**. $\blacksquare$

**Deducción Paso a Paso de la Complejidad Temporal:**  
1. El algoritmo voraz se compone de dos fases:
   * **Fase 1 (Ordenamiento):** Ordenar el arreglo de $n$ tareas según sus duraciones $t_i$. Utilizando un algoritmo de ordenamiento por comparación óptimo (como *MergeSort* o *HeapSort*), la complejidad es:
     $$T_{\text{sort}}(n) = \Theta(n \log n)$$
   * **Fase 2 (Cálculo del costo acumulado):** Recorrer el arreglo ordenado de $n$ elementos evaluando la suma ponderada:
     $$T_{\text{calc}}(n) = \sum_{i=1}^n 1 = \Theta(n)$$
2. Sumando ambas fases:
   $$\begin{aligned}
   T_{\text{Voraz}}(n) &= T_{\text{sort}}(n) + T_{\text{calc}}(n) \\
   &= \Theta(n \log n) + \Theta(n) \\
   &= \Theta(n \log n)
   \end{aligned}$$
3. **Optimización con tiempos enteros acotados:** Si los tiempos de reparación son enteros y están acotados por un valor máximo $M$ ($t_i \in \{1, 2, \dots, M\}$), se puede utilizar *Counting Sort*, alcanzando una complejidad lineal de $\Theta(n + M) = \Theta(n)$.
* **Complejidad Temporal:** $\Theta(n \log n)$ en caso general; $\Theta(n)$ con ordenamiento no comparativo.
* **Complejidad Espacial:** $\Theta(n)$ para almacenar los índices y tiempos ordenados.

---

#### 2.2.3. Técnica 3: Vuelta Atrás (*Backtracking*)

**Descripción Teórica:**  
Aunque el problema cuenta con una solución voraz óptima y eficiente, el estudio mediante Vuelta Atrás es didácticamente fundamental para comprender la formulación en árbol de expansión de soluciones por etapas y el impacto de las cotas podadoras.

* **Estructura del árbol:** En la etapa $k$, se decide qué tarea colocar en la posición $k$.
* **Cota Inferior Residual:** Para podar ramas subóptimas, en cualquier etapa intermedia $k$ con tareas asignadas $(\pi_1, \dots, \pi_k)$, se calcula una cota inferior ($LB$) del costo mínimo completable:
  $$LB = \sum_{i=1}^k (n - i + 1) t_{\pi_i} + \sum_{j=1}^{n-k} (n - (k + j) + 1) t'_{(j)}$$
  donde $t'_{(j)}$ son las tareas no asignadas ordenadas en forma no decreciente.
* **Criterio de Poda:** Si $LB \ge \text{MejorCostoActual}$, se poda el subárbol.
* **Complejidad:** Peor caso $\Theta(n!)$, pero con poda por cota inferior reduce significativamente el espacio explorado. Espacio $\Theta(n)$ en pila de recursión.

---

#### 2.2.4. Técnica 4: Ramificación y Poda (*Branch and Bound*)

**Descripción Teórica:**  
Aplica una estrategia de exploración de costo mínimo (*Best-First Search* o búsqueda **LC**) mediante una Cola de Prioridad (*Min-Heap*).
* Cada nodo del árbol almacena la tupla $(\text{rutaParcial}, \text{tareasRestantes}, LB)$.
* Al extraer siempre el nodo con menor cota inferior $LB$, la primera solución completa que alcanza la longitud $n$ coincide exactamente con la solución voraz óptima.
* **Complejidad:** En presencia de una cota inferior basada en SPT, el algoritmo se dirige directamente hacia la rama óptima en $\Theta(n \log n)$ pasos de extracción del heap, confirmando la convergencia entre la ramificación óptima y la voracidad.

---

#### 2.2.5. Técnica 5: Generalizaciones y Extensiones del Fontanero

El problema del Fontanero Diligente sirve como punto de partida para estudiar escenarios más complejos:

1. **Generalización con Prioridades o Pesos de Clientes (Regla de Smith, 1956):**  
   Si cada cliente tiene asignado un peso $w_i > 0$ que mide su urgencia o penalización económica por unidad de tiempo de espera, el objetivo es minimizar:
   $$\min_{\pi \in \Pi_n} \sum_{i=1}^n w_{\pi_i} \cdot E_i(\pi)$$
   Por la **Regla de Smith**, la solución óptima exacta se obtiene ordenando vorazmente las tareas en orden no decreciente de sus cocientes duración/peso:
   $$\frac{t_{\pi_1}}{w_{\pi_1}} \le \frac{t_{\pi_2}}{w_{\pi_2}} \le \dots \le \frac{t_{\pi_n}}{w_{\pi_n}}$$
   Complejidad: $\Theta(n \log n) \implies$ **Permanece en la clase $P$**.

2. **Generalización con Múltiples Fontaneros ($m$ Procesadores Paralelos):**  
   Si hay $m$ cuadrillas de fontaneros ($P \parallel \sum C_j$), la solución óptima voraz consiste en ordenar todas las tareas de menor a mayor duración y asignarlas secuencialmente en orden *round-robin* a los $m$ fontaneros.  
   Complejidad: $\Theta(n \log n) \implies$ **Permanece en la clase $P$**.

3. **Generalización con Tiempos de Desplazamiento en Red (*Traveling Repairman Problem* - TRP):**  
   Si el fontanero no solo invierte tiempo reparando, sino que debe desplazarse a través de una red geográfica o grafo métrico entre los domicilios de los clientes, el problema se convierte en el *Minimum Latency Problem*. Esta generalización **transiciona drásticamente de $P$ a ser $NP\text{-Completo}$ en decisión y $NP\text{-Duro}$ en optimización**.

---

### 2.3. Tabla Comparativa de Rendimiento Teórico y Empírico

A partir de los experimentos controlados ejecutados en el script de soporte (`team-project/src/benchmark.py`), se obtuvieron las siguientes mediciones reales:

| $n$ (Averías) | Fuerza Bruta $\Theta(n \cdot n!)$ | Backtracking con Poda | Voraz SPT $\Theta(n \log n)$ | Optimalidad Garantizada |
|:---:|:---:|:---:|:---:|:---:|
| **4** | $0.000017\text{ s}$ | $0.000010\text{ s}$ | $0.000002\text{ s}$ | 100% Óptimo (Exacto) |
| **6** | $0.000281\text{ s}$ | $0.000007\text{ s}$ | $0.000002\text{ s}$ | 100% Óptimo (Exacto) |
| **8** | $0.021740\text{ s}$ | $0.000047\text{ s}$ | $0.000003\text{ s}$ | 100% Óptimo (Exacto) |
| **10** | $2.103323\text{ s}$ | $0.000025\text{ s}$ | $0.000003\text{ s}$ | 100% Óptimo (Exacto) |
| **11** | $>15\text{ min}$ (Inviable) | Explorando | $0.000003\text{ s}$ | Demostrado Óptimo |
| **100** | Inviable | Inviable | $0.000018\text{ s}$ | Demostrado Óptimo |
| **1,000** | Inviable | Inviable | $0.000234\text{ s}$ | Demostrado Óptimo |
| **10,000** | Inviable | Inviable | $0.002796\text{ s}$ | Demostrado Óptimo |
| **100,000** | Inviable | Inviable | $0.054299\text{ s}$ | Demostrado Óptimo |

*Nota destacada:* Mientras la Fuerza Bruta colapsa totalmente al llegar a $n = 11$, el Algoritmo Voraz es capaz de ordenar y secuenciar óptimamente **100,000 reparaciones en apenas 54 milisegundos**.

---

### 2.4. Ejemplos de Aplicación en las Diferentes Áreas del Conocimiento

1. **Sistemas Operativos (Planificación de Procesos en CPU):**  
   El algoritmo SJF (*Shortest Job First*) sin desalojo utilizado en el planificador de la CPU es idéntico al Fontanero Diligente. Al seleccionar el proceso listo con la ráfaga de CPU (*CPU burst*) más corta, el sistema operativo garantiza matemáticamente el menor tiempo medio de espera (*average waiting time*) y tiempo medio de retorno (*average turnaround time*) para todos los procesos del sistema.

2. **Salud y Triage Hospitalario:**  
   En consultas médicas ambulatorias o servicios de diagnóstico rápido donde no hay riesgo vital inmediato, atender primero los procedimientos breves (e.g. retiro de puntos, lectura rápida de laboratorio) minimiza la congestión en las salas de espera y reduce el tiempo promedio que los pacientes permanecen en las instalaciones sanitarias.

3. **Centros de Cómputo y Servidores Web (Query Scheduling):**  
   En servidores de bases de datos relacionales (como PostgreSQL o MySQL) sometidos a alta concurrencia de transacciones de solo lectura, despachar primero las consultas con menor costo estimado de ejecución en disco y memoria reduce la saturación de los canales de comunicación y mejora la percepción de latencia global del usuario.

4. **Operaciones Industriales y Mantenimiento de Maquinaria:**  
   En plantas manufactureras con un solo equipo de mecánicos especializados, planificar las órdenes de mantenimiento preventivo de menor a mayor duración reduce el tiempo muerto acumulado de las líneas de producción dependientes de dichas reparaciones.

---

### 2.5. Clases de Complejidad Computacional y Clasificación del Problema

#### 2.5.1. Definición Teórica de las Clases Fundamentales

* **Clase $P$ (Tiempo Polinomial Determinista):**  
  Conjunto de lenguajes o problemas de decisión que admiten un algoritmo determinista cuya función de complejidad temporal en el peor caso está acotada por un polinomio $O(n^c)$ para alguna constante fija $c > 0$. Representa la clase de los problemas computacionalmente eficientes o tratables.
* **Clase $NP$ (Tiempo Polinomial No Determinista):**  
  Conjunto de problemas de decisión para los cuales existe un algoritmo verificador determinista $V(x, y)$ que, dada una instancia $x$ y un certificado de tamaño polinomial $y$, verifica si $y$ es una prueba válida de que $x \in L$ en tiempo acotado polinomialmente $O(|x|^c)$.
* **Clase $NP\text{-Duro}$ (*NP-Hard*):**  
  Un problema $L$ es $NP\text{-Duro}$ si todo lenguaje $L' \in NP$ es reducible en tiempo polinomial a $L$ ($L' \le_P L$). No requiere pertenecer a $NP$ ni ser un problema de decisión.
* **Clase $NP\text{-Completo}$ (*NP-Complete*):**  
  Problemas que pertenecen a $NP$ y simultáneamente son $NP\text{-Duros}$. Representan los problemas más difíciles de la clase $NP$.

---

#### 2.5.2. Clasificación Formal del Fontanero Diligente

#### Teorema 1: La versión de decisión del Fontanero Diligente ($FD_{\text{dec}}$) pertenece a la clase $P$.

**Demostración:**  
Para demostrar que un problema de decisión pertenece a la clase $P$, es condición suficiente exhibir un algoritmo determinista que resuelva cualquier instancia en tiempo estrictamente polinomial.
1. **Algoritmo Determinista Propuesto:**
   * Dada una instancia con duraciones $\{t_1, \dots, t_n\}$ y cota $K$:
     * **Paso 1:** Ordenar las duraciones mediante un algoritmo de ordenación por comparación (e.g. *MergeSort*):
       $$T_1(n) = \Theta(n \log n)$$
     * **Paso 2:** Calcular el tiempo total acumulado de la permutación ordenada $\pi^*$:
       $$W(\pi^*) = \sum_{i=1}^n (n - i + 1) t_{\pi^*_i} \implies T_2(n) = \Theta(n)$$
     * **Paso 3:** Comparar si $W(\pi^*) \le K$. Si se cumple, responder **SÍ**; en caso contrario, responder **NO**:
       $$T_3(n) = \Theta(1)$$
2. **Complejidad Temporal Global:**
   $$\begin{aligned}
   T(n) &= T_1(n) + T_2(n) + T_3(n) \\
   &= \Theta(n \log n) + \Theta(n) + \Theta(1) \\
   &= \Theta(n \log n)
   \end{aligned}$$
3. Como $\Theta(n \log n) = O(n^2)$, el tiempo de ejecución está estrictamente acotado por un polinomio de grado 2.
4. Como la regla SPT garantiza que $W(\pi^*)$ es el mínimo global absoluto posible, responder SÍ si y sólo si $W(\pi^*) \le K$ es completamente correcto.
Por lo tanto, **queda formalmente demostrado que el Fontanero Diligente pertenece a la clase $P$**. $\blacksquare$

---

#### Teorema 2: El Fontanero Diligente pertenece a la clase $NP$.

**Demostración:**  
1. **Por Inclusión Teórica Fundamental:** Es un teorema cardinal de la computación que:
   $$P \subseteq NP$$
   Dado que en el Teorema 1 se probó que $FD_{\text{dec}} \in P$, se sigue de manera inmediata y necesaria que **$FD_{\text{dec}} \in NP$**.
2. **Por Construcción Explícita del Verificador:**  
   * **Certificado:** Se presenta una permutación candidata de tareas $y = (\pi_1, \pi_2, \dots, \pi_n)$.
   * **Algoritmo Verificador $V(x, y)$:**
     1. Comprobar que $y$ es una permutación válida de los elementos $\{1, \dots, n\}$ usando un arreglo booleano en tiempo $\Theta(n)$.
     2. Calcular la suma acumulada $W(y) = \sum_{i=1}^n (n - i + 1) t_{\pi_i}$ en tiempo $\Theta(n)$.
     3. Verificar si $W(y) \le K$ en tiempo $\Theta(1)$.
   * El tiempo total de verificación determinista es $\Theta(n)$, que es lineal y por ende polinomial.  
Esto ratifica independientemente que **$FD_{\text{dec}} \in NP$**. $\blacksquare$

---

#### Teorema 3: ¿Es el Fontanero Diligente $NP\text{-Completo}$ o $NP\text{-Duro}$?

**Análisis Teórico:**  
* Por definición, un problema es $NP\text{-Completo}$ si pertenece a $NP$ y es $NP\text{-Duro}$.
* Si el problema del Fontanero Diligente fuera $NP\text{-Completo}$, dado que puede resolverse en tiempo polinomial $\Theta(n \log n)$, implicaría que todo problema de la clase $NP$ podría resolverse en tiempo polinomial por reducción, lo que acarrearía la consecuencia teórica:
  $$P = NP$$
* Bajo la conjetura y consenso unánime de las ciencias de la computación contemporáneas de que $P \ne NP$:  
  **El problema clásico del Fontanero Diligente NO es $NP\text{-Completo}$ ni $NP\text{-Duro}$, sino que reside firmemente en la clase $P$**.

---

#### Teorema 4: La Frontera de la Complejidad — ¿Cuándo se vuelve $NP\text{-Duro}$?

El valor pedagógico del Fontanero Diligente radica en entender con precisión quirúrgica qué restricciones transforman un problema polinomial tratable en un problema intratable $NP\text{-Duro}$:

| Variante del Problema | Restricciones Adicionales | Clase de Complejidad |
|---|---|:---:|
| **Fontanero Diligente Clásico** ($1 \parallel \sum C_j$) | Sin desplazamientos, un servidor | **$P$** ($\Theta(n \log n)$) |
| **Con Pesos / Prioridades** ($1 \parallel \sum w_j C_j$) | Regla de Smith ($t_i / w_i$) | **$P$** ($\Theta(n \log n)$) |
| **Múltiples Fontaneros** ($P \parallel \sum C_j$) | $m$ procesadores paralelos | **$P$** ($\Theta(n \log n)$) |
| **Con Tiempos de Llegada** ($1 \mid r_j \mid \sum C_j$) | Las tareas no están disponibles al inicio | **$NP\text{-Duro}$** (Lenstra et al., 1977) |
| **Con Plazos Límite Estrictos** ($1 \parallel \sum T_j$) | Tardanzas y penalizaciones por fecha límite | **$NP\text{-Duro}$** |
| **Con Desplazamiento Geográfico en Red** (*Traveling Repairman*) | Costo de traslado métrico entre clientes | **$NP\text{-Completo}$** (Decisión) / **$NP\text{-Duro}$** |

---

## 3. Conclusiones

1. **La Elegancia y Poder de la Voracidad:**  
   El problema del Fontanero Diligente constituye el ejemplo paradigmático de que no todos los problemas combinatorios requieren la búsqueda exhaustiva en espacios factoriales. Demuestra cómo una elección voraz local simple y bien fundamentada (ordenar por tiempos de menor a mayor) garantiza matemáticamente la optimalidad global, reduciendo el costo de resolución de $\Theta(n \cdot n!)$ a $\Theta(n \log n)$.

2. **Tratabilidad Computacional vs. Intratabilidad:**  
   Al clasificar rigurosamente el problema dentro de la clase **$P$**, se ilustra el contraste fundamental con otros problemas del curso (como el Agente Viajero o la Mochila 0/1). Sin embargo, el análisis de sus extensiones revela la extrema fragilidad de la tratabilidad algorítmica: añadir tiempos de llegada o distancias geográficas rompe la propiedad voraz y catapulta el problema al dominio de lo **$NP\text{-Duro}$**.

3. **Relevancia Práctica Transversal:**  
   Desde los algoritmos de planificación de la CPU (SJF) en sistemas operativos modernos hasta los protocolos de atención en emergencias y balanceo de carga en servidores de bases de datos, el principio matemático del Fontanero Diligente sigue siendo el estándar universal para maximizar la satisfacción del usuario y minimizar la latencia acumulada.

---

## 4. Bibliografía

1. **Guerequeta, R., & Vallecillo, A. (2000).** *Técnicas de Diseño de Algoritmos*. Servicio de Publicaciones de la Universidad de Málaga. (Capítulo 4: Algoritmos Voraces, Sección 4.3: El fontanero diligente, pp. 89-94).
2. **Brassard, G., & Bratley, P. (1997).** *Fundamentos de Algoritmia*. Prentice Hall. (Capítulo 6: Algoritmos voraces y problemas de secuenciación).
3. **Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2022).** *Introduction to Algorithms* (4th ed.). MIT Press. (Capítulo 16: Greedy Algorithms, Capítulo 34: NP-Completeness).
4. **Smith, W. E. (1956).** *Various optimizers for single-stage production*. Naval Research Logistics Quarterly, 3(1‐2), 59-66. (Artículo seminal de la regla SPT y pesos ponderados).
5. **Pinedo, M. L. (2016).** *Scheduling: Theory, Algorithms, and Systems* (5th ed.). Springer. (Capítulo 3: Single Machine Models - Total Completion Time).
6. **Garey, M. R., & Johnson, D. S. (1979).** *Computers and Intractability: A Guide to the Theory of NP-Completeness*. W. H. Freeman and Company.
