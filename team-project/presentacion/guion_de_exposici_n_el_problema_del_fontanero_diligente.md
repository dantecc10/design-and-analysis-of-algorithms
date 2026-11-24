# Guion de Exposición: El Problema del Fontanero Diligente

**Curso:** Análisis y Diseño de Algoritmos (ISCO 201-003)  
**Docente:** Dra. Irene Olaya Ayaquica Martínez  
**Autores:** Dante Castelán Carpinteyro, Yoshua Rameli Adán Pérez  

---

## Diapositiva 1: Portada
* **Qué decir:**
  > "Buenos días, Dra. Ayaquica y compañeros. Hoy vamos a analizar un problema clásico de la optimización combinatoria y planificación de tareas: **El Problema del Fontanero Diligente**. Lo abordaremos desde tres ejes fundamentales: técnicas de diseño de algoritmos, demostración formal de optimalidad voraz y su frontera dentro de la teoría de complejidad computacional."

---

## Diapositiva 2: 01 / Contexto
* **Qué decir:**
  > "Imaginemos un escenario simple: un solo fontanero tiene 3 reparaciones pendientes (de 60, 20 y 5 minutos) y todos los clientes llegan al mismo tiempo, en el instante cero. Nuestro objetivo es encontrar el orden de atención que minimice el tiempo medio hasta terminar cada reparación (conocido en la literatura como *flow time*)."
  > * **Orden Largo $\to$ Corto (60, 20, 5):** El primer cliente espera 60 minutos, el segundo $60 + 20 = 80$, y el tercero $80 + 5 = 85$. La suma total de terminación es de **225 minutos**, con una media de **75 minutos** por cliente.
  > * **Orden Corto $\to$ Largo (5, 20, 60):** Los tiempos acumulados son 5, 25 y 85 minutos. La suma cae a **115 minutos** y la media baja a **38.3 minutos** —casi la mitad de espera, realizando exactamente el mismo trabajo."

---

## Diapositiva 3: 02 / Formulación
* **Lectura matemática:**
  * $W(\pi) = n t_{\pi_1} + (n-1) t_{\pi_2} + \dots + t_{\pi_n}$  
    *Se lee:* *"W de pi es igual a n por t sub pi uno, más n menos uno por t sub pi dos, y así sucesivamente hasta t sub pi n"* (donde $\pi$ representa una permutación o secuencia de atención, y $t_{\pi_k}$ es la duración de la tarea en la $k$-ésima posición).
  * $\sum C_i$  
    *Se lee:* *"La sumatoria de los tiempos de finalización C sub i"*.
* **Qué decir:**
  > "Al desarrollar la sumatoria de los tiempos de terminación, observamos un patrón algebraico clave: la primera tarea ejecutada retrasa a las $n$ tareas (incluida ella misma), por lo que su duración se multiplica por $n$. La segunda retrasa a $n-1$ tareas, y la última solo se cuenta una vez. Como $n$ es una constante, minimizar la suma total $W(\pi)$ es matemáticamente equivalente a minimizar el promedio. Para minimizar esta suma ponderada, debemos asignar los tiempos más pequeños a los coeficientes más grandes."

---

## Diapositiva 4: 03 / Técnica 1: Fuerza Bruta
* **Lectura matemática:**
  * $T(n) = \Theta(n \cdot n!)$  
    *Se lee:* *"T de n pertenece a Theta de n por n factorial"*.
* **Qué decir:**
  > "La aproximación ingenua consiste en generar el árbol completo de permutaciones y evaluar $W(\pi)$ en cada hoja. Existen $n!$ órdenes posibles y evaluar cada secuencia toma tiempo lineal $\Theta(n)$, lo que resulta en una complejidad temporal de $\Theta(n \cdot n!)$. Esto produce una explosión combinatoria intratable: pasar de 10 a apenas 11 tareas multiplica por 11 el espacio de búsqueda, rozando los 40 millones de permutaciones."

---

## Diapositiva 5: 04 / Técnica 2: La solución voraz (SPT)
* **Lectura matemática:**
  * $\Theta(n \log n)$  
    *Se lee:* *"Theta de n logaritmo de n"*.
* **Qué decir:**
  > "Para evitar la explosión factorial, diseñamos un algoritmo voraz (*greedy*) conocido en teoría de planificación como **SPT** (*Shortest Processing Time*). La regla de decisión local es directa: ordenar las reparaciones de menor a mayor duración y atender siempre primero la más breve. El costo computacional queda dominado únicamente por el ordenamiento, reduciendo la complejidad de factorial a $\Theta(n \log n)$."

---

## Diapositiva 6: 05 / Prueba por intercambio
* **Lectura matemática:**
  * $W(\pi) - W(\pi') = t_{\pi_k} - t_{\pi_{k+1}} > 0$  
    *Se lee:* *"W de pi menos W de pi prima es igual a t sub pi k menos t sub pi k más uno, lo cual es estrictamente mayor que cero"*.
* **Qué decir:**
  > "Que un algoritmo sea voraz no garantiza por sí solo que sea óptimo; debemos demostrarlo formalmente mediante un **argumento de intercambio** (*exchange argument*). Supongamos una secuencia $\pi$ que no sigue SPT; entonces debe contener al menos una inversión adyacente: una tarea larga en la posición $k$ seguida inmediatamente por una corta en $k+1$ (es decir, $t_{\pi_k} > t_{\pi_{k+1}}$). Si las intercambiamos para obtener $\pi'$, los tiempos de finalización de todas las demás tareas permanecen intactos. La diferencia en la función objetivo es exactamente $t_{\pi_k} - t_{\pi_{k+1}}$, que es estrictamente positiva. Por lo tanto, $W(\pi') < W(\pi)$. Eliminar cualquier inversión siempre mejora el resultado, demostrando que la secuencia ordenada SPT es el óptimo global."

---

## Diapositiva 7: 06 / Técnicas 3 y 4: Búsqueda con poda
* **Qué decir:**
  > "Para contrastar enfoques de diseño algorítmico, también evaluamos métodos de búsqueda exacta con poda sobre el árbol de estados:
  > * **Backtracking (DFS):** Explora ramas en profundidad y descarta aquellas cuya suma parcial acumulada ya supera el mejor valor conocido hasta ese momento.
  > * **Branch & Bound (Ramificación y Poda):** Utiliza una cola de prioridad para expandir primero el nodo más prometedor según una cota inferior. Aunque ambos reducen drásticamente los nodos visitados frente a la fuerza bruta, siguen siendo algoritmos de búsqueda frente a la solución directa $\Theta(n \log n)$ del método voraz."

---

## Diapositiva 8: 07 / Generalizaciones
* **Lectura matemática:**
  * $t_i / w_i$  
    *Se lee:* *"t sub i sobre w sub i"* (cociente entre la duración y el peso o prioridad de la tarea $i$).
  * $O(n \log n)$  
    *Se lee:* *"Orden n logaritmo de n"*.
* **Qué decir:**
  > "¿Qué ocurre si relajamos las hipótesis del problema base?
  > 1. **Prioridad de clientes (Regla de Smith):** Si cada cliente tiene un peso o urgencia $w_i$, ya no ordenamos solo por duración, sino de forma ascendente por la razón $t_i / w_i$. En nuestro ejemplo: A tiene un ratio de $10/5 = 2$, C tiene $3/1 = 3$, y B tiene $8/2 = 4$, generando el orden óptimo $A \to C \to B$.
  > 2. **Cuadrillas paralelas:** Si contamos con $m$ equipos idénticos, ordenamos por SPT y distribuimos las tareas en ronda (*round-robin*) al equipo que se libere primero. Ambas variantes conservan una complejidad de $O(n \log n)$, siempre que no existan tiempos de traslado ni fechas de llegada distintas."

---

## Diapositiva 9: 08 / Benchmark
* **Qué decir:**
  > "En esta tabla observamos el contraste empírico de ejecución. Para $n = 10$, fuerza bruta ya requiere más de 2.1 segundos, mientras que SPT tarda apenas 3 microsegundos. Lo más relevante es la escalabilidad: para **100,000 reparaciones** —un tamaño donde fuerza bruta y backtracking son computacionalmente inviables— el algoritmo voraz SPT encuentra el **óptimo exacto en 54.3 milisegundos**."

---

## Diapositiva 10: 09 / Teoría de Complejidad
* **Qué decir:**
  > "Desde la perspectiva de la teoría de complejidad, el problema del fontanero en un solo sitio pertenece a la clase **P**, al resolverse en tiempo polinomial $\Theta(n \log n)$. Sin embargo, existe una frontera muy estrecha: en cuanto introducimos ubicaciones geográficas y tiempos de desplazamiento entre clientes, el problema se transforma en el *Traveling Repairman Problem* (o problema de latencia mínima), el cual es **NP-duro**. Un solo parámetro adicional basta para sacarnos de la tratabilidad polinomial."

---

## Diapositiva 11: 10 / Aplicaciones
* **Qué decir:**
  > "Aunque utilizamos la analogía del fontanero, este modelo sustenta sistemas críticos en ingeniería y computación:
  > * **Sistemas Operativos:** Corresponde al planificador de CPU *Shortest Job First* (SJF) para minimizar el tiempo de espera promedio en cola.
  > * **Servidores y Bases de Datos:** Priorizar consultas breves evita el efecto convoy y reduce la latencia promedio.
  > * **Servicios de Salud e Industria:** Se emplea en gestión de turnos hospitalarios (combinado con la Regla de Smith para triaje) y en secuenciación de órdenes en líneas de producción."

---

## Diapositiva 12: 11 / Conclusiones
* **Qué decir:**
  > "Para concluir, resumimos nuestra presentación en tres puntos clave:
  > 1. **Eficiencia:** Reducir un espacio de búsqueda factorial $n!$ a una complejidad $\Theta(n \log n)$ mediante el criterio de ordenamiento adecuado.
  > 2. **Rigor:** La demostración por intercambio garantiza que la elección voraz aquí no es una aproximación heurística, sino un óptimo exacto.
  > 3. **Tratabilidad:** Identificar qué restricciones mantienen un problema en **P** y cuáles lo llevan a **NP-duro** es fundamental al diseñar soluciones reales. Muchas gracias."

---

## Diapositiva 13: 12 / Fuentes y Créditos
* **Qué decir (en caso de detenerse en esta lámina):**
  > "Nuestras fuentes incluyen textos clásicos de algoritmia como Cormen, Brassard y Bratley, el artículo seminal de Wayne Smith de 1956 sobre optimización en una etapa, y el trabajo de Blum sobre el problema de latencia mínima. Quedamos atentos a sus preguntas y comentarios."