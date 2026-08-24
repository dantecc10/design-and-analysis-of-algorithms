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
