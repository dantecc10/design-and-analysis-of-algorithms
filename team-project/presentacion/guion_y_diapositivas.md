# Guion y Estructura Diapositiva por Diapositiva para la Exposición

> **Asignatura:** Análisis y Diseño de Algoritmos  
> **Tema:** El Problema del Fontanero Diligente (*Single-Machine Scheduling / Minimización del Tiempo de Espera*)  
> **Docente:** Mtra. Irene Olaya Ayaquica Martínez  
> **Duración estimada:** 12 a 15 minutos de exposición  

---

## Índice General de Diapositivas

1. **Diapositiva 1:** Portada Oficial
2. **Diapositiva 2:** Motivación y Planteamiento del Problema
3. **Diapositiva 3:** Formulación Matemática: Desglose del Tiempo de Espera
4. **Diapositiva 4:** Técnica 1: Fuerza Bruta y la Explosión Combinatoria
5. **Diapositiva 5:** Técnica 2: El Algoritmo Voraz (*Regla SPT*)
6. **Diapositiva 6:** Demostración Matemática Formal de Optimalidad
7. **Diapositiva 7:** Técnicas 3 y 4: Vuelta Atrás y Ramificación y Poda
8. **Diapositiva 8:** Generalizaciones: Clientes con Prioridad y Múltiples Fontaneros
9. **Diapositiva 9:** Comparativa de Rendimiento Teórico vs. Empírico (Benchmark)
10. **Diapositiva 10:** Teoría de Complejidad: Pertenencia a $P$ y la Frontera de lo $NP\text{-Duro}$
11. **Diapositiva 11:** Aplicaciones Prácticas en Sistemas Operativos y la Industria
12. **Diapositiva 12:** Conclusiones
13. **Diapositiva 13:** Referencias Bibliográficas

---

### Diapositiva 1: Portada Oficial
* **Elementos Visuales:**
  * Logotipo institucional de la BUAP y Facultad de Ciencias de la Computación.
  * Título: *Análisis y Diseño de Algoritmos para el Problema del Fontanero Diligente*.
  * Subtítulo: *Técnicas de diseño, demostración de optimalidad voraz y clases de complejidad*.
  * Integrantes:  
    • Dante Castelán Carpinteyro (Matrícula: 202320271)  
    • Yoshua Rameli Adán Pérez  
  * Materia: Análisis y Diseño de Algoritmos.
  * Profesora: Mtra. Irene Olaya Ayaquica Martínez.
* **Notas del Orador (1 minuto):**
  > *"Buenos días profesora y compañeros. En esta exposición analizaremos a fondo el clásico problema del 'Fontanero Diligente', un problema fundamental de optimización de colas y secuenciación de tareas. Estudiaremos cómo formularlo matemáticamente, las técnicas algorítmicas para resolverlo, la demostración rigurosa de optimalidad de la estrategia voraz y su clasificación dentro de la teoría de complejidad computacional."*

---

### Diapositiva 2: Motivación y Planteamiento del Problema
* **Elementos Visuales:**
  * Ilustración de un fontanero con una lista de $n$ clientes esperando su reparación.
  * Planteamiento conceptual:  
    *"Un fontanero tiene $n$ reparaciones urgentes. Conoce el tiempo $t_i$ de cada una. Solo puede atender a un cliente a la vez. ¿En qué orden debe atenderlos para que el tiempo medio de espera de los clientes sea el mínimo posible?"*.
  * Reflexión intuitiva: ¿Conviene atender primero las averías largas o las cortas?
* **Notas del Orador (1 minuto):**
  > *"Imaginemos que un fontanero tiene 3 reparaciones: una de 5 minutos, una de 20 minutos y una de 60 minutos. Si atiende primero la de 60 minutos, los otros dos clientes estarán esperando más de una hora solo para ser atendidos. Si atiende primero la de 5 minutos, ese cliente se va feliz de inmediato y los demás solo esperaron 5 minutos adicionales. Este dilema intuitivo es la base del problema del fontanero diligente."*

---

### Diapositiva 3: Formulación Matemática: Desglose del Tiempo de Espera
* **Elementos Visuales:**
  * Conjunto de tareas con duraciones $\{t_1, t_2, \dots, t_n\}$.
  * Permutación de atención: $\pi = (\pi_1, \dots, \pi_n)$.
  * Tiempo de espera del cliente $k$: $E_k = \sum_{j=1}^k t_{\pi_j}$.
  * Suma total acumulada:
    $$\begin{aligned}
    W(\pi) &= \sum_{k=1}^n \left( \sum_{j=1}^k t_{\pi_j} \right) = \sum_{i=1}^n (n - i + 1) t_{\pi_i} \\
    &= n \cdot t_{\pi_1} + (n - 1) \cdot t_{\pi_2} + \dots + 1 \cdot t_{\pi_n}
    \end{aligned}$$
  * Conclusión: Minimizar el tiempo medio $\bar{W} = \frac{W}{n}$ equivale a minimizar la suma ponderada $W(\pi)$.
* **Notas del Orador (1 minuto):**
  > *"Al desglosar matemáticamente la sumatoria de tiempos, descubrimos un patrón clave: la primera tarea que atiende el fontanero penaliza a los $n$ clientes con su duración, la segunda tarea penaliza a $n-1$ clientes, y la última solo afecta al cliente final. Por tanto, para minimizar la suma total, los coeficientes más grandes ($n, n-1, \dots$) deben multiplicarse obligatoriamente por los tiempos más pequeños."*

---

### Diapositiva 4: Técnica 1: Fuerza Bruta y la Explosión Combinatoria
* **Elementos Visuales:**
  * Esquema de árbol de permutaciones con $n!$ hojas.
  * Costo por permutación: evaluar $n$ aristas $\implies \Theta(n)$ operaciones.
  * Complejidad temporal:
    $$T(n) = n! \cdot \Theta(n) = \Theta(n \cdot n!) = \Theta((n + 1)!)$$
  * Límites prácticos:
    * $n = 4 \implies 24$ permutaciones
    * $n = 10 \implies 3,628,800$ permutaciones ($2.1$ segundos)
    * $n = 11 \implies 39,916,800$ permutaciones ($>15$ minutos)
* **Notas del Orador (1 minuto):**
  > *"Si intentamos resolver este problema por Fuerza Bruta, tendríamos que generar las $n!$ permutaciones posibles y calcular la suma ponderada de cada una. Para 10 tareas toma un par de segundos, pero al llegar a 11 o 12 tareas el tiempo se dispara a minutos y horas debido al crecimiento factorial. La fuerza bruta es completamente impracticable."*

---

### Diapositiva 5: Técnica 2: El Algoritmo Voraz (*Regla SPT*)
* **Elementos Visuales:**
  * Regla **SPT** (*Shortest Processing Time First*):
    $$t_{\pi^*_1} \le t_{\pi^*_2} \le \dots \le t_{\pi^*_n}$$
  * Diagrama de flujo del algoritmo:
    1. Recibir arreglo de duraciones.
    2. Ordenar en orden ascendente (MergeSort / HeapSort).
    3. Retornar la secuencia ordenada.
  * Complejidad Temporal:
    $$T(n) = \Theta(n \log n)$$
  * Complejidad Espacial: $\Theta(n)$.
* **Notas del Orador (1 minuto):**
  > *"Aquí entra la belleza del diseño algorítmico: en lugar de buscar entre millones de combinaciones, la estrategia voraz o ávida establece una regla de selección local inmediata: ordenar las reparaciones de menor a mayor tiempo de duración. Con un algoritmo de ordenamiento óptimo como MergeSort, resolvemos el problema en tiempo $\Theta(n \log n)$."*

---

### Diapositiva 6: Demostración Matemática Formal de Optimalidad
* **Elementos Visuales:**
  * Método del Argumento de Intercambio (*Exchange Argument*).
  * Si $\pi$ tiene una inversión consecutiva $t_{\pi_k} > t_{\pi_{k+1}}$:
  * Intercambiando $k$ y $k+1$ en $\pi'$:
    $$\begin{aligned}
    W(\pi) - W(\pi') &= \left[ (n - k + 1)t_{\pi_k} + (n - k)t_{\pi_{k+1}} \right] - \left[ (n - k + 1)t_{\pi_{k+1}} + (n - k)t_{\pi_k} \right] \\
    &= [(n - k + 1) - (n - k)] (t_{\pi_k} - t_{\pi_{k+1}}) \\
    &= 1 \cdot (t_{\pi_k} - t_{\pi_{k+1}}) > 0
    \end{aligned}$$
  * Conclusión: $W(\pi') < W(\pi) \implies$ Contradicción. SPT es estrictamente óptimo.
* **Notas del Orador (1.5 minutos):**
  > *"No basta con decir que la regla voraz parece lógica; en análisis de algoritmos debemos demostrarlo formalmente. Supongamos que existiera una solución óptima donde una tarea larga se atiende antes que una corta adyacente. Al calcular la resta algebraica entre ambas secuencias, todos los términos se cancelan excepto la diferencia entre esas dos duraciones. Como la resta da estrictamente positiva, intercambiarlas siempre reduce el tiempo de espera, lo que demuestra por contradicción que la ordenación voraz es matemáticamente insuperable."*

---

### Diapositiva 7: Técnicas 3 y 4: Vuelta Atrás y Ramificación y Poda
* **Elementos Visuales:**
  * **Vuelta Atrás (*Backtracking*):**
    * Árbol de decisiones en profundidad (DFS) por etapas.
    * Poda por cota inferior del tiempo residual.
  * **Ramificación y Poda (*Branch and Bound*):**
    * Búsqueda por mejor primero (LC) con Cola de Prioridad (*Min-Heap*).
    * La cota inferior basada en SPT guía al algoritmo directamente a la rama óptima.
* **Notas del Orador (1 minuto):**
  > *"Si abordamos el problema mediante Vuelta Atrás o Ramificación y Poda, podemos calcular en cada nodo una cota inferior matemática del tiempo que faltaría por esperar. En Ramificación y Poda, la cola de prioridad extrae siempre el nodo más prometedor, guiando la búsqueda directo a la solución óptima sin expandir ramas innecesarias."*

---

### Diapositiva 8: Generalizaciones: Clientes con Prioridad y Múltiples Fontaneros
* **Elementos Visuales:**
  * **Generalización 1: Clientes con Pesos / Prioridad ($w_i$):**
    * Regla de Smith (1956): Ordenar por el cociente $\frac{t_i}{w_i}$ de menor a mayor.
    * Complejidad: $\Theta(n \log n) \implies$ Sigue perteneciendo a la clase $P$.
  * **Generalización 2: Múltiples Fontaneros ($m$ cuadrillas paralelas):**
    * Ordenar por SPT y repartir en round-robin a las $m$ máquinas.
    * Complejidad: $\Theta(n \log n) \implies$ Sigue perteneciendo a la clase $P$.
* **Notas del Orador (1 minuto):**
  > *"¿Qué ocurre si un cliente paga una tarifa de urgencia o es un hospital con mayor prioridad $w_i$? En 1956, Wayne Smith demostró que ordenar por la razón duración entre peso ($t_i / w_i$) mantiene la optimalidad matemática. Si además tenemos $m$ fontaneros trabajando en paralelo, ordenamos y distribuimos vorazmente. En ambos casos, el problema sigue resolviéndose en tiempo polinomial $\Theta(n \log n)$."*

---

### Diapositiva 9: Comparativa de Rendimiento Teórico vs. Empírico (Benchmark)
* **Elementos Visuales:**
  * Tabla con datos reales obtenidos de nuestro script en Python:
    | $n$ (Averías) | Fuerza Bruta | Backtracking | Voraz SPT | Optimalidad |
    |:---:|:---:|:---:|:---:|:---:|
    | 4 | $0.000017\text{ s}$ | $0.000010\text{ s}$ | $0.000002\text{ s}$ | 100% Óptimo |
    | 8 | $0.021740\text{ s}$ | $0.000047\text{ s}$ | $0.000003\text{ s}$ | 100% Óptimo |
    | 10 | $2.103323\text{ s}$ | $0.000025\text{ s}$ | $0.000003\text{ s}$ | 100% Óptimo |
    | 100 | Inviable | Inviable | $0.000018\text{ s}$ | Demostrado Óptimo |
    | 10,000 | Inviable | Inviable | $0.002796\text{ s}$ | Demostrado Óptimo |
    | 100,000 | Inviable | Inviable | $0.054299\text{ s}$ | Demostrado Óptimo |
* **Notas del Orador (1 minuto):**
  > *"En pantalla tenemos los datos empíricos de las pruebas que programamos en Python. Noten el contraste brutal: para 10 tareas, la fuerza bruta ya tarda 2 segundos y en 11 colapsa. En cambio, el algoritmo voraz resuelve 100 mil averías en apenas 54 milisegundos, garantizando siempre el 100% de optimalidad. Este es el impacto tangible de un diseño de algoritmos eficiente."*

---

### Diapositiva 10: Teoría de Complejidad: Pertenencia a $P$ y la Frontera de lo $NP\text{-Duro}$
* **Elementos Visuales:**
  * Esquema de Clases: $P \subseteq NP$.
  * **Pertenencia a $P$:**
    * La versión de decisión "¿Espera total $\le K$?" se resuelve en $\Theta(n \log n) = O(n^2)$.
    * Por tanto, **el Fontanero Diligente pertenece a la clase $P$** (y a $NP$).
  * **¿Es $NP\text{-Completo}$?** No, porque implicaría $P = NP$.
  * **La frontera de la complejidad:**
    * Si añadimos plazos de entrega estrictos (*deadlines*) o distancias de viaje en un mapa (*Traveling Repairman Problem*), el problema salta de $P$ y se vuelve **$NP\text{-Completo}$ en decisión y $NP\text{-Duro}$ en optimización**.
* **Notas del Orador (1.5 minutos):**
  > *"En cuanto a las clases de complejidad: el problema del Fontanero Diligente pertenece a la clase $P$ porque existe un algoritmo determinista que lo resuelve en tiempo polinomial $\Theta(n \log n)$. Y como $P$ está contenido en $NP$, también pertenece a $NP$. No es $NP$-Completo. Sin embargo, si al fontanero le agregamos tiempos de viaje en coche entre clientes sobre un mapa, el problema se transforma en el Traveling Repairman Problem y se vuelve inmediatamente $NP$-Completo. El fontanero diligente nos enseña exactamente dónde se encuentra la frontera entre lo tratable y lo intratable."*

---

### Diapositiva 11: Aplicaciones Prácticas en Sistemas Operativos y la Industria
* **Elementos Visuales:**
  * 4 Casos de estudio en viñetas con iconos:
    1. **Planificación de CPU (SJF en Sistemas Operativos):** Minimiza el tiempo de retorno promedio de procesos en cola.
    2. **Triage y Urgencias Hospitalarias:** Atención de consultas ambulatorias rápidas para descongestionar salas de espera.
    3. **Servidores Web y Bases de Datos:** Despacho prioritario de consultas SQL ligeras para reducir latencia global.
    4. **Líneas de Producción y Mantenimiento:** Reducción de tiempos muertos en plantas industriales.
* **Notas del Orador (1 minuto):**
  > *"Este problema no es solo un ejercicio académico. Cuando sus computadoras o servidores ejecutan tareas, el planificador del sistema operativo usa el algoritmo Shortest Job First, que es idéntico al fontanero diligente. En hospitales, el triage prioriza procedimientos rápidos no graves para liberar espacio en salas de espera. Y en servidores de bases de datos, priorizar queries cortas mantiene el sistema ágil para todos los usuarios."*

---

### Diapositiva 12: Conclusiones
* **Elementos Visuales:**
  * Conclusiones destacadas:
    1. **Poder de la Voracidad:** Transforma una búsqueda exponencial $\Theta(n!)$ en un proceso determinista de $\Theta(n \log n)$.
    2. **Optimalidad Demostrable:** El argumento de intercambio garantiza que la solución voraz no es una aproximación, sino el óptimo exacto.
    3. **Tratabilidad Computacional:** Demuestra que existen problemas de secuenciación dentro de la clase $P$, sirviendo de contraste fundamental contra problemas $NP\text{-Completos}$.
* **Notas del Orador (1 minuto):**
  > *"Para concluir: el problema del Fontanero Diligente es la demostración perfecta de que el análisis riguroso de algoritmos puede transformar un problema aparentemente complejo e intratable en una solución elegante, óptima y computacionalmente eficiente en clase $P$. Nos enseña además a reconocer cuándo una propiedad voraz nos protege de la explosión combinatoria. Muchas gracias por su atención."*

---

### Diapositiva 13: Referencias Bibliográficas
* **Elementos Visuales:**
  * Fuentes académicas consultadas:
    1. Guerequeta, R., & Vallecillo, A. (2000). *Técnicas de Diseño de Algoritmos*. Univ. de Málaga.
    2. Brassard, G., & Bratley, P. (1997). *Fundamentos de Algoritmia*. Prentice Hall.
    3. Cormen, T. H. et al. (2022). *Introduction to Algorithms* (4th ed.). MIT Press.
    4. Smith, W. E. (1956). *Various optimizers for single-stage production*. Naval Research Logistics.
    5. Pinedo, M. L. (2016). *Scheduling: Theory, Algorithms, and Systems*. Springer.
    6. Garey, M. R., & Johnson, D. S. (1979). *Computers and Intractability*. W. H. Freeman.
* **Notas del Orador (30 segundos):**
  > *"En pantalla dejamos las referencias bibliográficas que sustentaron nuestro análisis teórico, el código y las demostraciones. Quedamos a su disposición para resolver cualquier pregunta. Gracias."*
