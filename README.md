# Análisis y Diseño de Algoritmos

Mtra. Irene Olaya Ayaquica Martínez

Correo: irene.ayaquica@correo.buap.mx

## Materiales de clase
- Notas del curso
- Plataforma Teams
- Lenguajes de programación C++, Java, otros

## Contenido del curso
- Fundamentos teóricos del análisis y diseño de algoritmos
- Técnicas avanzadas de diseño y análisis
- Algoritmos para grafos
- Clases de complejidad

## Criterios de evaluación

| Criterio | Valor |
| --- | --- |
| Exámenes | 25% |
| Proyecto | 35% |
| Trabajo de investigación | 20% |
| Exposición | 10% |
| Tareas | 10% |

## Reglas

- El curso es presencial

Teams es una herramienta de apoyo:

- Como medio de comunicación (chat)
- Para subir el material de clase
- Para hacer entrega de actividades

- Los mensajes a través del chat privado de Teams deberán incluir el nombre del estudiante y el curso que están tomando (esta información no aparece en el chat).

- Las prácticas se tomarán en cuenta sólo cuando el estudiante asistió a clase, excepto cuando al falta sea justificada por escrito.
- Para las exposiciones deberán asistir todos los integrantes del equipo; sólo los integrantes que expongan tendrán calificación.
- Exámenes, entregas de proyectos o actividades de otras materias no son faltas justificables.
- No se permite tomar fotos, videos o audios durante la clase.

### Estructura de reporte

1. Resumen (del documento, no del tema a tratar)
2. Introducción (se describe el tema relacionado y los puntos que se especifiquen en la actividad correspondiente)
3. Descripción de la actividad (cómo se realizó la práctica, qué proceso se llevó a cabo))
4. Resultados (evidencia, capturas de pantalla, tablas comparativas de tiempos de ejecución)
5. Conclusiones
6. Referencias

## Introducción

Una computadora es una máquina capaz de procesar información digital a gran velocidad.

Una computadora está expuesta por un conjunto de componentes electrónicos, mecánicos, interfaces para interactuar con el exterior (usuarios u otros dispositivos) y por un conjunto de programas que determinan qué operaciones llevar a cabo.

Los datos ordenados (**información**) que constituyen esta entrada (**input**) a la computadora se procesan mediante una lógica (**programa**) para producir una salida (**output**).

## Nombres de los órdenes

Si el tiempo necesario para que un algoritmo resuelva un caso del tamaño $n$ nunca es más que $cn$ segundos, en donde $c$ es alguna constante adecuada, diremos que el algoritmo requiere un tiempo en el orden de $n$ o que requiere un **tiempo lineal**.

Si el algortimo nunca necesoita más de $cn^2$ segundos, entonces el algoritmo requiere un tiempo en el orden de $n^2$ o **tiempo cuadrático**.

$n^3 \to $ tiempo cúbico

$n^k \to $ tiempo polinómico
$c^n \to $ tiempo exponencial.

Una operación elemental es aquella cuyo tiempo de ejecución se puede acotar superiormente por una constante que solamente dependerá de la implementación particular:
- de la máquina
- del lenguaje de programación
- etc.

La constante no depende ni del tamaño ni de los parámetros del ejemplar que se está considerando.

## Operaciones elementales (OE)
Consideramos operaciones elementales a:

- las operaciones aritméticas básicas,
- asignaciones a variables de tipo predefinido por el compilador,
- saltos (llamadas a funciones, retorno, etc.),
- comparaciones lógicas,
- acceso a estructuras indexadas básicas

Cada una de ellas contabilizará como una operación elemental.

El tiempo de ejecución de un algoritmo va a ser una función que mide el número de operaciones elementales que realizar el algoritmo para un tamaño de entrada dado.

## Eficiencia y complejidad
Supongamos que cuando se analiza un algoritmo, encontramos que para resolver un caso de un cierto tamaño se necesita efectuar $a$ adicionales, $m$ multiplicaciones y $s$ asignaciones.

Supongamos que también se sabe que una suma nunca requiere más de $t_a$ microsegundos, que una multiplicación nunca requiere más de $t_m$ microsegundos y una asignación nunca requiere más de $t_s$ microsegundos; donde $t_a$, $t_m$ y $t_s$ son constantes que dependen de la máquina utilizada.

El tiempo total $t$ requerido por nuestro algoritmo estará actoado por $t \leq a t_a + m t_m + s t_s \leq max(t_a, t_m, t_s) * (a + m + s)$

esto es, $t$ está acotado por un múltiplo constante del número de operaciones elementales que hay que ejecutar.

Si $T$ es una matriz de $n$ elementos $(n > 0)$, entonces el tiempo requerido para calcular $x \gets min\{T[i] | 1 \leq i \leq n\}$

Crece con $n$, puesto que esto es una abreviatura de:

$x \gets T\{1\}$

para $i \gets 2$ hasta $n$ hacer
si $T[I] < x$ entonces $x \gets T[i]$

$$
función Sum(n)
	sum \gets 0			1 \\
	para i \gets 1 hasta n hacer	4 \\
		sum \gets sum + i	2 \\
	devolver sum			1 \\
$$

Calcula la suma de los enteros de 1 a n.

## Reglas para el cálculo del número OE

El tiempo de una operación elemental (OE) es de orden 1.

El tiempo de ejecución de una secuencia consecutiva de instrucciones se calcula sumando los tiempos de ejecución de cada una de las instrucciones.

El tiempo de ejecución de la sentencia

*Case $C$ of $v_1 : S_1 | v_2 : S_2 | \cdots | v_n : S_n$* es $T = T(C) + max[T(S_1), T_2), \cdots, T(S_n)], T(C)$ incluye el tiempo de comparación con $v_1, v_2, \cdots, v_n$.

El tiempo de ejecución de la sentencia *If C then $S_1$ else $S_2$* es $T = T(C) + max[T(S_1), T(S_2)]$.

El tiempo de ejecución de un bucle de sentencias *While C do S* es $T = t(c) + ($ no iteraciones $) * (T(S) + T(C)$. Tanto $T(S)$ como $T(C)$ pueden variar en cada iteración.

Para calcular el tiempo de ejecución del resto de sentencias iterativas (*For, Repeat, Loop*) basta expresarlas como un bucle *While*.

El tiempo de ejecución de una llamada a un procedimiento o función $F(P_1, P_2, \cdots, P_n)$ es 1 (por llamada) más el tiempo de evaluación de los parámetros $P_1, P_2, \cdots, P_n$ más el tiempo que tarde en ejecutarse $F$.

$T = 1 + T(P_1) + T(P_2) + \cdots + T(P_n) + T(F)$.

El tiempo de ejecución de las llamadas a procedimientos recursivos da lugar a ecuaciones de recurrencia.

También es importante hacer notar que el comportamiento de un algoritmo puede cambiar notablemente para diferentes entradas (por ejemplo, lo ordenados que se encuentren ya los datos a ordenar).

Para muchos programas el tiempo de ejecución es una función de la entrada específica, y no sólo del tamaño de esta.

Suelen estudiarse casos para un mismo algoritmo: *caso peor*, *caso mejor* y *caso medio*.

El *caso mejor* corresponde a la traza (secuencia de sentencias) del algoritmo que realiza menos instrucciones.

El *caso peor* corresponde a la traza del algorutmo que realiza más instrucciones.

El *caso medio* corresponde a la traza del algoritmo que realiza un número de instrucciones igual a la esperanza matemática de la variable aleatorioa definida por todas las posibles trazas del algoritmo para un tamaño de la entrada dado, con las proababilidades de que estas ocurran para esa entrada.

## Eficiencia y complejidad

Es importante observar que no es necesario conocer el propósito del algoritmo para analizar su tiempo de ejecución y determinar sus casos mejor, peor y medio, sino que basta con estudiar su código.

Suele ser un error muy frecuente el determinar tales casos basándose sólo en la funcionalidad para la que el algoritmo fue concebido, olvidando que es el código implementado el que los determina.

- $T(n) = 1 + 1 + [1 + (\sum_{i = 1}^{n} (1 + 2+ 2))] + 1$
- $T(n) = 4 + (\sum_{i=1}^{n}5)$
- $T(n) = 5n + 4$

- $T(n) = 1 +1 +1 + [1 + \sum_{k=1}^{n}(1 + 2 + 2 +2)] + 1$
- $T(n) = 5 + \sum_{k=1}^{n} 7$
- $T(n) = 5 + 7n$
- $T(n) = 7n + 5$

## Ejercicio
```
PROCEDURE Misterio(n)
	var i, j, k, s;
	BEGIN
		s := 0;
		FOR i := 1 TO n - 1 DO
			FOR j := i + 1 TO n DO
				FOR k := 1 TO j DO
					s := s + 2;
	END Misterio
```

```
PROCEDURE Misterio(n)
        var i, j, k, s;
        BEGIN
                s := 0;							// 1
		i := 1;							// 1
                WHILE i < n DO						// 1
                        j := i + 1;					// 2
				WHILE j <= n DO				// 1
                                 	k := 1				// 1
						WHILE K <= J DO      	// 1
                                         		s := s + 2;	// 2
							k := k + 1;	// 2
						j := j + 1;		// 2
						i := i + 1;			// 2
                END Misterio
```
La complejidad sería:

$T(n) = 1 + 1 + [1 + \sum_{i = 1}^{n - 1}(1 + 2 + (1 + \sum_{j = i + 1}^{n} 1 + 1 + (1 + \sum_{k = 1}^{j} 1 + 2 + 2) + 2) + 2)]$

### Recurrencias homogéneas

Una recurrencia es homogénea cuando cada término depende únicamente de términos anteriores, sin una función extra $f(n)$ sumada. La solución general para una recurrencia lineal homogénea de orden $k$ tiene la forma:

$$t_n = \sum_{i=1}^{l}\sum_{j=0}^{m_i-1} c_{ij} \cdot n^{j} \cdot r_{i} ^n$$

Donde $r_1, r_2, \dots, r_l$ son las raíces distintas del polinomio característico y $m_i$ son sus multiplicidades.

#### Ejemplo Práctico: La secuencia de Fibonacci
Considere la recurrencia que define la secuencia de Fibonacci:
$$T(n) = T(n-1) + T(n-2)$$
Con condiciones iniciales $T(0) = 0$ y $T(1) = 1$.

**Pasos para resolverla:**

1.  **Ecuación Característica:** Sustituimos $T(n)$ por $r^n$ para obtener el polinomio:
    $$r^2 - r - 1 = 0$$
2.  **Encontrar las raíces:** Resolviendo la ecuación cuadrática obtenemos:
    $$r_1 = \frac{1 + \sqrt{5}}{2} \approx 1.618 \quad (\text{Número Áureo } \phi)$$
    $$r_2 = \frac{1 - \sqrt{5}}{2} \approx -0.618$$
3.  **Solución General:** La solución tiene la forma:
    $$T(n) = A\left(\frac{1+\sqrt{5}}{2}\right)^n + B\left(\frac{1-\sqrt{5}}{2}\right)^n$$
4.  **Determinación de constantes:** Usando $T(0)=0$ y $T(1)=1$, encontramos que $A = \frac{1}{\sqrt{5}}$ y $B = -\frac{1}{\sqrt{5}}$.

**Análisis de Complejidad:**
Dado que el término con la base mayor domina el crecimiento cuando $n \to \infty$, la complejidad temporal del algoritmo recursivo simple para Fibonacci es:
$$T(n) = O(\phi^n) \approx O(1.618^n)$$
Esto demuestra que un enfoque puramente recursivo sin memorización (memoization) resulta en una complejidad **exponencial**.

## Ejercicios
1. Resuelva las siguientes recurrencias homogéneas y dé su orden de complejidad:
- $a_n = 7a_{n-1} - 10a_{n-2}$, $n \geq 2$, $a_0 = 2$, $a_1 = 1$
- $a_n = 2a_{n-1} - a_{n-2}$, $n \geq 2$, $a_0 = 4$, $a_1 = 1$
- $a_n = 6a_{n-1} - 11a_{n-2} + 6a_{n-3}$, $n \geq 3$, $a_0 = 2$, $a_1 = 5$, $a_2 = 15$

### Soluciones Desarrolladas (Detalladas)
*(Para ver los desarrollos matemáticos completos, consulta el archivo `derivaciones_recurrencias.md`)*

#### Ejercicio 1: $a_n = 7a_{n-1} - 10a_{n-2}$
*Condiciones iniciales: $a_0 = 2, a_1 = 1$*

**1. Obtención de la ecuación característica:**
Sustituimos $a_n = r^n$ en la recurrencia original:
$$r^n = 7r^{n-1} - 10r^{n-2}$$
Dividimos por $r^{n-2}$ para simplificar:
$$r^2 = 7r - 10 \implies \mathbf{r^2 - 7r + 10 = 0}$$

**2. Resolución del polinomio:**
Buscamos dos números que multiplicados den $10$ y sumados den $-7$. Estos son $-2$ y $-5$.
Factorizamos:
$$(r - 2)(r - 5) = 0$$
Las raíces son: **$r_1 = 2$** y **$r_2 = 5$**.

**3. Solución General:**
Como las raíces son reales y distintas, la solución es una combinación lineal de ambas:
$$a_n = A(2^n) + B(5^n)$$

**4. Determinación de constantes:**
Usamos las condiciones iniciales para crear un sistema de ecuaciones:
*   Para $n=0$: $a_0 = A(2^0) + B(5^0) = A + B = 2$
*   Para $n=1$: $a_1 = A(2^1) + B(5^1) = 2A + 5B = 1$

Resolvemos el sistema:
De (1), $A = 2 - B$. Sustituimos en (2):
$$2(2 - B) + 5B = 1$$
$$4 - 2B + 5B = 1$$
$$3B = -3 \implies \mathbf{B = -1}$$
Sustituyendo $B$: $A = 2 - (-1) \implies \mathbf{A = 3}$

**Resultado:** $a_n = 3(2^n) - 5^n$
**Complejidad:** $O(5^n)$

---

#### Ejercicio 2: $a_n = 2a_{n-1} - a_{n-2}$
*Condiciones iniciales: $a_0 = 4, a_1 = 1$*

**1. Obtención de la ecuación característica:**
Sustituimos $a_n = r^n$ en la recurrencia original:
$$r^n = 2r^{n-1} - r^{n-2}$$
Dividimos por $r^{n-2}$ para simplificar:
$$r^2 = 2r - 1 \implies \mathbf{r^2 - 2r + 1 = 0}$$

**2. Resolución del polinomio:**
$$(r - 1)^2 = 0$$
Obtenemos una **raíz repetida**: $r = 1$ con multiplicidad 2.

**3. Solución General:**
Cuando una raíz $r$ se repite, la base de la solución se multiplica por $n$ para mantener la independencia lineal:
$$a_n = A(r^n) + Bn(r^n)$$
Como $r=1$, la solución se simplifica a:
$$a_n = A(1^n) + Bn(1^n) = \mathbf{A + Bn}$$

**4. Determinación de constantes:**
*   Para $n=0$: $a_0 = A + B(0) = 4 \implies \mathbf{A = 4}$
*   Para $n=1$: $a_1 = A + B(1) = 1$
    Sustituyendo $A$: $4 + B = 1 \implies \mathbf{B = -3}$

**Resultado:** $a_n = 4 - 3n$
**Complejidad:** $O(n)$

---

#### Ejercicio 3: $a_n = 6a_{n-1} - 11a_{n-2} + 6a_{n-3}$
*Condiciones iniciales: $a_0 = 2, a_1 = 5, a_2 = 15$*

**1. Obtención de la ecuación característica:**
Sustituimos $a_n = r^n$ en la recurrencia original:
$$r^n = 6r^{n-1} - 11r^{n-2} + 6r^{n-3}$$
Dividimos por $r^{n-3}$ para simplificar:
$$r^3 = 6r^2 - 11r + 6 \implies \mathbf{r^3 - 6r^2 + 11r - 6 = 0}$$

**2. Resolución del polinomio:**
Probamos divisores de 6 ($\pm 1, \pm 2, \pm 3, \pm 6$).
Si $r=1$: $1^3 - 6(1)^2 + 11(1) - 6 = 1 - 6 + 11 - 6 = 0$. (Es raíz).
Dividimos el polinomio $(r^3 - 6r^2 + 11r - 6)$ entre $(r - 1)$ usando regla de Ruffini:
$$1 \quad | \quad 1 \quad -6 \quad 11 \quad -6$$
$$\quad \quad \quad \quad \quad 1 \quad -5 \quad \phantom{-}6$$
$$\quad \quad \quad \quad \quad \quad \quad \quad \quad 0$$
Nos queda $r^2 - 5r + 6 = 0$, que factoriza como $(r-2)(r-3) = 0$.
Las raíces son: **$r_1=1, r_2=2, r_3=3$**.

**3. Solución General:**
$$a_n = A(1^n) + B(2^n) + C(3^n) \implies a_n = A + B(2^n) + C(3^n)$$

**4. Determinación de constantes (Sistema 3x3):**
1. $a_0 = A + B + C = 2$
2. $a_1 = A + 2B + 3C = 5$
3. $a_2 = A + 4B + 9C = 15$

Resolvemos por eliminación:
*   Restamos (2)-(1): $B + 2C = 3$
*   Restamos (3)-(2): $2B + 6C = 10 \implies B + 3C = 5$

Sistema resultante:
- $B + 2C = 3$
- $B + 3C = 5$
Restamos las ecuaciones: $C = 2$.
Sustituyendo: $B + 2(2) = 3 \implies B = -1$.
Sustituyendo en (1): $A + (-1) + 2 = 2 \implies A = 1$.

**Resultado:** $a_n = 1 - 2^n + 2(3^n)$
**Complejidad:** $O(3^n)$
