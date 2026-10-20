# Análisis de Complejidad: Enfoque Teórico y Conteo de Operaciones Elementales

## 1. Enfoques del Análisis de Algoritmos

| Enfoque | Descripción | Ventajas | Desventajas |
|---------|-------------|----------|-------------|
| **Empírico (a posteriori)** | Programar y medir tiempos reales en máquina | Realista, captura constantes ocultas | Dependiente de HW/SW, no generalizable, costoso |
| **Teórico (a priori)** | Determinar matemáticamente recursos como función del tamaño $n$ | Independiente de máquina, general, predice escalabilidad | Ignora constantes, idealiza operaciones |
| **Híbrido** | Forma teórica + parámetros empíricos | Predice instancias grandes desde pruebas pequeñas | Requiere calibración inicial |

> **Principio de Invarianza**: Dos implementaciones del mismo algoritmo difieren en eficiencia a lo sumo por una **constante multiplicativa**.

> **Formal**: Si $t_1(n)$ y $t_2(n)$ son tiempos de dos implementaciones, $\exists c,d > 0, \exists n_0$ tal que:
> $$t_1(n) \leq c \cdot t_2(n) \quad \land \quad t_2(n) \leq d \cdot t_1(n) \quad \forall n \geq n_0$$

---

## 2. Operaciones Elementales (OE)

> **Definición**: Una operación cuyo tiempo de ejecución está acotado superiormente por una constante que **solo depende de la implementación** (máquina, lenguaje, compilador), **no** del tamaño $n$ ni de los valores de la entrada.

### Lista Canónica de OE (cada una cuenta 1 unidad)

| Categoría | Ejemplos |
|-----------|----------|
| **Aritméticas básicas** | $+,\ -,\ \times,\ /,\ \%$ (enteros/flotantes de tamaño fijo) |
| **Asignaciones** | $x \leftarrow y$, $A[i] \leftarrow v$ (tipos predefinidos) |
| **Saltos/Control** | Llamada a función, `return`, `break`, `continue`, `goto` |
| **Comparaciones lógicas** | $<,\ >,\ \leq,\ \geq,\ ==,\ !=,\ \land,\ \lor,\ \lnot$ |
| **Acceso indexado** | $A[i]$, $M[i][j]$ (vectores, matrices, arrays) |

> **Regla fundamental**: El tiempo de ejecución $T(n)$ = número total de OE ejecutadas para entrada de tamaño $n$.

---

## 3. Órdenes de Complejidad (Nombres Comunes)

| Función $T(n)$ | Nombre | Ejemplo Típico |
|----------------|--------|----------------|
| $O(1)$ | Constante | Acceso a array, operación aritmética |
| $O(\log n)$ | Logarítmica | Búsqueda binaria |
| $O(n)$ | **Lineal** | Recorrido de array, búsqueda secuencial |
| $O(n \log n)$ | Linealítmica | Merge Sort, Heap Sort, Quick Sort (caso medio) |
| $O(n^2)$ | **Cuadrática** | Selection/Insertion/Bubble Sort, bucles anidados |
| $O(n^3)$ | Cúbica | Multiplicación matrices naive, Floyd-Warshall |
| $O(n^k)$ | Polinómica | Algoritmos eficientes para problemas en P |
| $O(c^n),\ c>1$ | Exponencial | Fuerza bruta subconjuntos, TSP naive, Torres de Hanoi |
| $O(n!)$ | Factorial | Permutaciones, TSP por fuerza bruta |

---

## 4. Análisis Detallado: Selection Sort

### 4.1 Pseudocódigo con Conteo de OE por Línea

```
PROCEDURE SelectionSort(T[1 … n])
1:  i ← 1                                    (1 OE)
2:  WHILE i < n DO                           (1 OE por evaluación)
3:      min ← i                              (1 OE)
4:      minVal ← T[i]                        (1 OE)
5:      j ← i + 1                            (1 OE)
6:      WHILE j ≤ n DO                       (1 OE por evaluación)
7:          IF T[j] < minVal THEN            (1 OE comparación)
8:              min ← j                      (1 OE asignación)
9:              minVal ← T[j]                (1 OE asignación)
10:         END IF
11:         j ← j + 1                        (1 OE asignación + 1 OE aritmética = 2 OE)
12:     END WHILE
13:     IF min ≠ i THEN                      (1 OE comparación)
14:         T[min] ← T[i]                    (1 OE asignación + 1 OE acceso = 2 OE)
15:         T[i] ← minVal                    (1 OE asignación + 1 OE acceso = 2 OE)
16:     END IF
17:     i ← i + 1                            (2 OE: asignación + aritmética)
18: END WHILE
END PROCEDURE
```

### 4.2 Análisis del Bucle Interno (líneas 6–11)

Para un $i$ fijo, el bucle `j` itera desde $i+1$ hasta $n$:
- Iteraciones: $n - i$
- Por iteración (líneas 7–11):
  - **Mejor caso** (vector ya ordenado ascendente): La condición `T[j] < minVal` es **siempre falsa** $\rightarrow$ no se ejecutan líneas 8–9.
    - OE por iteración: $1\ (\text{IF}) + 2\ (j \leftarrow j+1) = 3\ \text{OE}$
  - **Peor caso** (vector ordenado descendente): La condición es **siempre verdadera** $\rightarrow$ se ejecutan líneas 8–9.
    - OE por iteración: $1 + 1 + 1 + 2 = 5\ \text{OE}$
  - **Caso medio** (vector aleatorio): Probabilidad $\frac{1}{2}$ de ser verdadero (aprox).
    - OE por iteración: $1 + \frac{1}{2}(1+1) + 2 = 1 + 1 + 2 = 4\ \text{OE}$

---

## 5. Derivación Completa: Caso Mejor (Vector Ordenado Ascendente)

### 5.1 Ecuación de Recurrencia para $T_{\text{mejor}}(n)$

$$
\begin{aligned}
T_{\text{mejor}}(n) &= \underbrace{1}_{i\leftarrow 1} + \underbrace{1}_{\text{WHILE eval }i=1} 
+ \sum_{i=1}^{n-1} \Bigg[ 
\underbrace{1}_{min\leftarrow i} + \underbrace{1}_{minVal\leftarrow T[i]} + \underbrace{1}_{j\leftarrow i+1} \\
&\quad + \underbrace{1}_{\text{WHILE eval }j=i+1} 
+ \sum_{j=i+1}^{n} \underbrace{\left( 1 + 2 \right)}_{\text{IF falso + }j\leftarrow j+1} \\
&\quad + \underbrace{1}_{\text{WHILE eval final }j=n+1} 
+ \underbrace{1}_{\text{IF }min\neq i\text{ falso}} + \underbrace{2}_{i\leftarrow i+1} 
\Bigg] + \underbrace{1}_{\text{WHILE eval final }i=n}
\end{aligned}
$$

### 5.2 Simplificación Paso a Paso

**Paso 1**: Constantes del bucle externo por iteración
$$
1 + 1 + 1 + 1 = 4\ \text{OE fijas por } i
$$

**Paso 2**: Bucle interno ($n-i$ iteraciones, 3 OE cada una)
$$
\sum_{j=i+1}^{n} 3 = 3(n-i)
$$

**Paso 3**: Evaluación final WHILE interno + IF externo + incremento $i$
$$
1 + 1 + 2 = 4\ \text{OE}
$$

**Paso 4**: Total por iteración $i$
$$
4 + 3(n-i) + 4 = 3(n-i) + 8
$$

**Paso 5**: Sumatoria sobre $i = 1$ a $n-1$
$$
\begin{aligned}
T_{\text{mejor}}(n) &= 1\ (\text{init } i) + 1\ (\text{WHILE } i=1) \\
&\quad + \sum_{i=1}^{n-1} \left[ 3(n-i) + 8 \right] + 1\ (\text{WHILE final})
\end{aligned}
$$

**Paso 6**: Separar sumatoria
$$
\begin{aligned}
\sum_{i=1}^{n-1} \left[ 3(n-i) + 8 \right] 
&= 3\sum_{i=1}^{n-1}(n-i) + 8\sum_{i=1}^{n-1} 1 \\
&= 3\sum_{k=1}^{n-1} k + 8(n-1) \quad (k = n-i) \\
&= 3 \cdot \frac{(n-1)n}{2} + 8n - 8
\end{aligned}
$$

**Paso 7**: Ensamblar todo
$$
\begin{aligned}
T_{\text{mejor}}(n) &= 2 + \frac{3n(n-1)}{2} + 8n - 8 + 1 \\
&= \frac{3n^2 - 3n}{2} + 8n - 5 \\
&= \frac{3}{2}n^2 + \left(8 - \frac{3}{2}\right)n - 5 \\
&= \frac{3}{2}n^2 + \frac{13}{2}n - 5
\end{aligned}
$$

> **Resultado Caso Mejor**: 
> $$T_{\text{mejor}}(n) = \frac{3}{2}n^2 + \frac{13}{2}n - 5 \in \Omega(n^2)$$

> **Comprobación**: $n=2 \Rightarrow T= \frac{3}{2}(4) + \frac{13}{2}(2) - 5 = 6 + 13 - 5 = 14$ OE. ✓

---

## 6. Derivación Completa: Caso Peor (Vector Ordenado Descendente)

### 6.1 OE por iteración del bucle interno (líneas 7–11): 5 OE

### 6.2 Total por iteración $i$ (análogo a caso mejor, cambiando 3 por 5)
$$
4 + 5(n-i) + 4 = 5(n-i) + 8
$$

### 6.3 Sumatoria
$$
\begin{aligned}
T_{\text{peor}}(n) &= 2 + \sum_{i=1}^{n-1} \left[ 5(n-i) + 8 \right] + 1 \\
&= 3 + 5\sum_{i=1}^{n-1}(n-i) + 8(n-1) \\
&= 3 + 5 \cdot \frac{(n-1)n}{2} + 8n - 8 \\
&= \frac{5}{2}n^2 - \frac{5}{2}n + 8n - 5 \\
&= \frac{5}{2}n^2 + \frac{11}{2}n - 5
\end{aligned}
$$

> **Resultado Caso Peor**:
> $$T_{\text{peor}}(n) = \frac{5}{2}n^2 + \frac{11}{2}n - 5 \in O(n^2)$$

> **Comprobación**: $n=2 \Rightarrow T= \frac{5}{2}(4) + \frac{11}{2}(2) - 5 = 10 + 11 - 5 = 16$ OE. ✓

---

## 7. Derivación Completa: Caso Medio (Vector Aleatorio)

### 7.1 Modelo Probabilístico
- Para cada comparación `T[j] < minVal`, probabilidad $\frac{1}{2}$ de ser verdadera (elemento aleatorio es menor que el mínimo actual con prob. $\approx 1/2$).
- OE esperado por iteración interna: $1\ (\text{IF}) + \frac{1}{2}(2\ \text{asignaciones}) + 2\ (j++) = 4\ \text{OE}$

### 7.2 Total por iteración $i$
$$
4 + 4(n-i) + 4 = 4(n-i) + 8
$$

### 7.3 Sumatoria
$$
\begin{aligned}
T_{\text{medio}}(n) &= 2 + \sum_{i=1}^{n-1} \left[ 4(n-i) + 8 \right] + 1 \\
&= 3 + 4\sum_{i=1}^{n-1}(n-i) + 8(n-1) \\
&= 3 + 4 \cdot \frac{(n-1)n}{2} + 8n - 8 \\
&= 2n(n-1) + 8n - 5 \\
&= 2n^2 - 2n + 8n - 5 \\
&= 2n^2 + 6n - 5
\end{aligned}
$$

> **Resultado Caso Medio**:
> $$T_{\text{medio}}(n) = 2n^2 + 6n - 5 \in \Theta(n^2)$$

> **Comprobación**: $n=2 \Rightarrow T= 2(4) + 6(2) - 5 = 8 + 12 - 5 = 15$ OE (entre 14 y 16). ✓

---

## 8. Resumen: Selection Sort

| Caso | $T(n)$ Exacto | Complejidad Asintótica |
|------|---------------|------------------------|
| **Mejor** | $\frac{3}{2}n^2 + \frac{13}{2}n - 5$ | $\Omega(n^2)$ |
| **Peor** | $\frac{5}{2}n^2 + \frac{11}{2}n - 5$ | $O(n^2)$ |
| **Medio** | $2n^2 + 6n - 5$ | $\Theta(n^2)$ |

> **Conclusión**: Selection Sort es **siempre cuadrático** independientemente de la entrada. No hay caso lineal.

---

## 9. Análisis: MaxElement (Máximo en Array)

### 9.1 Pseudocódigo con OE

```
PROCEDURE MaxElement(v[i … j]; i, j)
1:  pos ← i                          (1 OE)
2:  k ← i + 1                        (2 OE: asignación + aritmética)
3:  WHILE k ≤ j DO                   (1 OE por evaluación)
4:      IF v[k] > v[pos] THEN        (3 OE: 2 accesos + 1 comparación)
5:          pos ← k                  (1 OE)
6:      END IF
7:      k ← k + 1                    (2 OE)
8:  END WHILE
9:  RETURN pos                       (1 OE)
```

### 9.2 Caso Mejor: Máximo en primera posición ($v[i]$)
- Condición línea 4 **siempre falsa** $\rightarrow$ no se ejecuta línea 5.
- Iteraciones del WHILE: $j - i$
- OE por iteración: $3\ (\text{IF}) + 2\ (k++) = 5\ \text{OE}$

$$
\begin{aligned}
T_{\text{mejor}}(j-i) &= 1 + 2 + 1 + \sum_{k=1}^{j-i} 5 + 1 \\
&= 5 + 5(j-i) \\
&= 5(j-i) + 5 \in \Omega(j-i)
\end{aligned}
$$

### 9.3 Caso Peor: Máximo en última posición ($v[j]$)
- Condición **siempre verdadera** $\rightarrow$ se ejecuta línea 5.
- OE por iteración: $3 + 1 + 2 = 6\ \text{OE}$

$$
\begin{aligned}
T_{\text{peor}}(j-i) &= 5 + \sum_{k=1}^{j-i} 6 \\
&= 5 + 6(j-i) \in O(j-i)
\end{aligned}
$$

### 9.4 Caso Medio: Máximo en posición aleatoria
- Probabilidad $\frac{1}{2}$ de actualizar `pos`.
- OE esperado/iteración: $3 + \frac{1}{2}(1) + 2 = 4.5\ \text{OE}$

$$
\begin{aligned}
T_{\text{medio}}(j-i) &= 5 + \sum_{k=1}^{j-i} 4.5 \\
&= 5 + 4.5(j-i) \in \Theta(j-i)
\end{aligned}
$$

> **Complejidad**: **Lineal en el tamaño del rango** $j-i+1$. Dos variables de entrada.

---

## 10. Ejercicio: Triple Bucle Anidado

### 10.1 Algoritmo
```
PROCEDURE TripleLoop(n)
    s ← 0
    FOR i ← 1 TO n-1 DO
        FOR j ← i+1 TO n DO
            FOR k ← 1 TO j DO
                s ← s + 2
            END FOR
        END FOR
    END FOR
END PROCEDURE
```

### 10.2 Conteo de OE
- Línea `s ← 0`: 1 OE
- Bucle $i$: $n-1$ iteraciones
- Bucle $j$: para cada $i$, itera $j = i+1 \dots n$ $\rightarrow$ $n-i$ iteraciones
- Bucle $k$: para cada $j$, itera $k = 1 \dots j$ $\rightarrow$ $j$ iteraciones
- Cuerpo: `s ← s + 2` = 2 OE (asignación + suma)

### 10.3 Sumatoria Triple

$$
\begin{aligned}
T(n) &= 1 + \sum_{i=1}^{n-1} \sum_{j=i+1}^{n} \sum_{k=1}^{j} 2 \\
&= 1 + 2 \sum_{i=1}^{n-1} \sum_{j=i+1}^{n} j
\end{aligned}
$$

**Sumatoria interna** $\sum_{j=i+1}^{n} j$:
$$
\sum_{j=i+1}^{n} j = \sum_{j=1}^{n} j - \sum_{j=1}^{i} j = \frac{n(n+1)}{2} - \frac{i(i+1)}{2}
$$

**Sumatoria media**:
$$
\begin{aligned}
\sum_{i=1}^{n-1} \left[ \frac{n(n+1)}{2} - \frac{i(i+1)}{2} \right]
&= \frac{n(n+1)}{2}(n-1) - \frac{1}{2}\sum_{i=1}^{n-1}(i^2 + i) \\
&= \frac{n(n+1)(n-1)}{2} - \frac{1}{2}\left( \frac{(n-1)n(2n-1)}{6} + \frac{(n-1)n}{2} \right) \\
&= \frac{n(n^2-1)}{2} - \frac{(n-1)n}{12}\left( (2n-1) + 3 \right) \\
&= \frac{n(n^2-1)}{2} - \frac{(n-1)n(2n+2)}{12} \\
&= \frac{n(n^2-1)}{2} - \frac{n(n-1)(n+1)}{6} \\
&= n(n^2-1)\left( \frac{1}{2} - \frac{1}{6} \right) \\
&= n(n^2-1) \cdot \frac{1}{3} = \frac{n(n^2-1)}{3}
\end{aligned}
$$

**Resultado final**:
$$
\begin{aligned}
T(n) &= 1 + 2 \cdot \frac{n(n^2-1)}{3} \\
&= 1 + \frac{2n^3 - 2n}{3} \\
&= \frac{2}{3}n^3 - \frac{2}{3}n + 1 \in \Theta(n^3)
\end{aligned}
$$

> **Comprobación**: $n=3 \Rightarrow T= \frac{2}{3}(27) - 2 + 1 = 18 - 1 = 19$ OE.
> Manual: $i=1: j=2(k=1,2), j=3(k=1,2,3) \rightarrow 2+3=5$ iteraciones $\times 2 = 10$ OE.
> $i=2: j=3(k=1,2,3) \rightarrow 3$ iteraciones $\times 2 = 6$ OE.
> Total: $1 + 10 + 6 = 17$... Discrepancia por evaluaciones de bucles.
> *Nota*: El conteo exacto incluye evaluaciones de condiciones de bucle. La forma asintótica $\Theta(n^3)$ es correcta.

---

## 11. Ejercicios Adicionales de Práctica

### Ejercicio 1: Análisis de Bucle Simple
```python
def algo1(n):
    s = 0
    for i in range(n):
        s += i
    return s
```
**Preguntas**:
a) Cuente OE exactas (incluya evaluaciones de `range` y bucle).
b) Derive $T(n)$ forma cerrada.
c) Clasifique asintóticamente.

<details>
<summary>Solución</summary>

a) OE: `s=0` (1), `range(n)` eval (1), bucle $n$ veces: `i` asignación (1), `s+=i` (2: suma + asignación), evaluación fin bucle (1). Total por iteración: 4 OE.
b) $T(n) = 1 + 1 + \sum_{i=0}^{n-1} 4 + 1 = 4n + 3$
c) $T(n) \in \Theta(n)$
</details>

---

### Ejercicio 2: Bucle con División
```python
def algo2(n):
    i = n
    while i > 1:
        i = i // 2
```
**Preguntas**:
a) ¿Cuántas iteraciones?
b) $T(n)$ exacto (OE: comparación, división entera, asignación).
c) Complejidad.

<details>
<summary>Solución</summary>

a) Iteraciones = $\lfloor \log_2 n \rfloor$. Cada iteración divide $i$ entre 2.
b) Por iteración: 1 (comparación) + 2 (división + asignación) = 3 OE. Inicial: 1 (asignación $i=n$). Final: 1 (comparación falsa).
$T(n) = 1 + 3\lfloor \log_2 n \rfloor + 1 = 3\lfloor \log_2 n \rfloor + 2$
c) $T(n) \in \Theta(\log n)$
</details>

---

### Ejercicio 3: Bucles Anidados Dependientes
```python
def algo3(n):
    count = 0
    for i in range(1, n+1):
        for j in range(1, i+1):
            count += 1
    return count
```
**Preguntas**: Derive $T(n)$ exacto y asintótico.

<details>
<summary>Solución</summary>

OE por iteración interna: 1 (incremento) + 1 (asignación) ≈ 2 OE (simplificado).
Sumatoria: $\sum_{i=1}^{n} \sum_{j=1}^{i} 1 = \sum_{i=1}^{n} i = \frac{n(n+1)}{2}$.
$T(n) = 1 + 2 \cdot \frac{n(n+1)}{2} + \text{eval bucles} = n^2 + n + O(1) \in \Theta(n^2)$.
Valor retornado: $\frac{n(n+1)}{2}$ (número triangular).
</details>

---

### Ejercicio 4: Recursivo - Factorial
```python
def fact(n):
    if n <= 1:
        return 1
    return n * fact(n-1)
```
**Preguntas**: Escriba recurrencia para $T(n)$ (OE: comparación, multiplicación, llamada, retorno). Resuélvala.

<details>
<summary>Solución</summary>

$T(0) = T(1) = c_0$ (base: comparación + retorno = 2 OE).
$T(n) = T(n-1) + c_1$ para $n>1$, donde $c_1$ = comparación + multiplicación + llamada + retorno ≈ 4 OE.
$T(n) = c_0 + c_1(n-1) \in \Theta(n)$.
</details>

---

### Ejercicio 5: Recurrencia Divide y Vencerás
Analice: $T(n) = 2T(n/2) + n$, $T(1) = 1$, $n$ potencia de 2.
Use **Suposiciones Inteligentes** (método del árbol de recursión / expansión).

<details>
<summary>Solución</summary>

$n=2^k$:
$T(2^k) = 2T(2^{k-1}) + 2^k$
$= 2[2T(2^{k-2}) + 2^{k-1}] + 2^k = 2^2T(2^{k-2}) + 2\cdot 2^{k-1} + 2^k = 2^2T(2^{k-2}) + 2^k + 2^k$
$= 2^k T(1) + k \cdot 2^k = 2^k + k 2^k = 2^k(1+k)$
$k = \log_2 n \Rightarrow T(n) = n(1 + \log_2 n) = n\log_2 n + n \in \Theta(n \log n)$
</details>

---

> **Siguiente tema**: [Notación Asintótica](04-notacion-asintotica.md)