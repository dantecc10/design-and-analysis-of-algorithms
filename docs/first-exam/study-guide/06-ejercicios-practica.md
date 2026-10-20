# Ejercicios Integrados de Práctica para el Examen

> **Instrucciones**: Resuelva cada ejercicio **antes** de consultar la solución. Las soluciones están al final del documento, separadas por `--- SOLUCIÓN ---`.

---

## Sección A: Análisis de Complejidad y Operaciones Elementales

### Ejercicio A.1: Bucle Simple con Paso Variable
```python
def algo_a1(n):
    s = 0
    i = 1
    while i < n:
        s += i
        i *= 2
    return s
```

**Preguntas**:
1. Cuente las OE exactas por iteración (incluya evaluaciones de condición).
2. Derive $T(n)$ en forma cerrada (use $\lfloor \log_2 n \rfloor$).
3. Exprese la complejidad en notación $\Theta$.

---

### Ejercicio A.2: Bucles Anidados con Límite Dependiente
```python
def algo_a2(n):
    count = 0
    for i in range(1, n+1):
        for j in range(i, n+1):
            count += 1
    return count
```

**Preguntas**:
1. Escriba la sumatoria doble exacta para el número de iteraciones del cuerpo.
2. Resuelva la sumatoria paso a paso.
3. ¿Cuál es el valor retornado como función de $n$?
4. Complejidad $\Theta$.

---

### Ejercicio A.3: Tres Bucles Anidados (Variación)
```python
def algo_a3(n):
    total = 0
    for i in range(1, n+1):
        for j in range(1, i+1):
            for k in range(1, j+1):
                total += 1
    return total
```

**Preguntas**:
1. Sumatoria triple para las iteraciones.
2. Resuelva usando fórmulas de sumas de potencias ($\sum i$, $\sum i^2$, $\sum i^3$).
3. Valor retornado y complejidad $\Theta$.

---

### Ejercicio A.4: Análisis de Insertion Sort (Caso Mejor/Peor/Medio)
Considere el pseudocódigo estándar de Insertion Sort:
```
for j = 2 to n:
    key = A[j]
    i = j - 1
    while i > 0 and A[i] > key:
        A[i+1] = A[i]
        i = i - 1
    A[i+1] = key
```

**Preguntas**:
1. Identifique las OE en el bucle `while` (línea de condición + cuerpo).
2. **Caso mejor** (array ya ordenado): Derive $T_{\text{mejor}}(n)$.
3. **Caso peor** (array ordenado inverso): Derive $T_{\text{peor}}(n)$.
4. **Caso medio** (asuma que el `while` itera $j/2$ veces en promedio): Derive $T_{\text{medio}}(n)$.
5. Clasifique cada caso en $O, \Omega, \Theta$.

---

### Ejercicio A.5: Algoritmo con Dos Variables de Entrada
```python
def algo_a5(A, m, n):  # A es matriz m x n
    max_val = A[0][0]
    for i in range(m):
        for j in range(n):
            if A[i][j] > max_val:
                max_val = A[i][j]
    return max_val
```

**Preguntas**:
1. Derive $T(m,n)$ exacto (OE).
2. Complejidad en términos de $m$ y $n$.
3. Si $m = n$, ¿cuál es la complejidad en $n$?

---

## Sección B: Notación Asintótica

### Ejercicio B.1: Clasificación de Funciones
Ordene las siguientes funciones por **crecimiento asintótico** (de menor a mayor). Indique si hay empates ($\Theta$).

$$
\begin{aligned}
f_1(n) &= n^2 \\
f_2(n) &= n \log n \\
f_3(n) &= 2^n \\
f_4(n) &= n! \\
f_5(n) &= (\log n)^2 \\
f_6(n) &= n^{1.5} \\
f_7(n) &= 100 n \\
f_8(n) &= 2^{\log n} \\
f_9(n) &= n^{\log n} \\
f_{10}(n) &= \log(n!)
\end{aligned}
$$

**Pista**: Simplifique $f_8$ y use Stirling para $f_{10}$.

---

### Ejercicio B.2: Demostrar Pertenencia por Definición
Para cada par $(f, g)$, determine si $f \in O(g)$, $f \in \Omega(g)$, $f \in \Theta(g)$. **Encuentre testigos explícitos $(c, n_0)$** donde aplique.

1. $f(n) = 7n^2 + 3n$, $g(n) = n^2$
2. $f(n) = 5n \log n$, $g(n) = n^2$
3. $f(n) = 2^{n+3}$, $g(n) = 2^n$
4. $f(n) = n^2 + 1000n$, $g(n) = n^2$
5. $f(n) = \sqrt{n}$, $g(n) = \log n$

---

### Ejercicio B.3: Límites para Clasificación
Use el **método del límite** $\lim_{n\to\infty} f(n)/g(n)$ para clasificar:

1. $f(n) = n^3 + 2^n$, $g(n) = 2^n$
2. $f(n) = n \log n$, $g(n) = n^{1.5}$
3. $f(n) = \log(n^2)$, $g(n) = \log n$
4. $f(n) = n!$, $g(n) = n^n$
5. $f(n) = 3^n$, $g(n) = 2^n$

---

### Ejercicio B.4: Propiedades - Verdadero/Falso con Justificación
1. Si $f \in O(g)$ y $g \in O(h)$, entonces $f \in O(h)$.
2. Si $f \in O(g)$ y $f \in O(h)$, entonces $f \in O(g + h)$.
3. Si $f \in \Theta(g)$, entonces $g \in \Theta(f)$.
4. $n^2 \in O(n^2 + n)$.
5. $n^2 + n \in O(n^2)$.
6. $2n^2 + 3n \in \Omega(n^2)$.
7. $\log_2 n \in \Theta(\log_{10} n)$.
8. $n^k \in O(c^n)$ para cualquier $k > 0, c > 1$.

---

### Ejercicio B.5: Simplificación Asintótica
Simplifique cada expresión a su forma $\Theta$ más simple:

1. $3n^2 + 5n \log n + 1000 \in \Theta(\dots)$
2. $\frac{n^3 + 2n^2}{n+1} \in \Theta(\dots)$
3. $\sum_{k=1}^n (k^2 + k) \in \Theta(\dots)$
4. $\log(n^2 + 3n) \in \Theta(\dots)$
5. $2^{n+1} + 3^n \in \Theta(\dots)$

---

## Sección C: Recurrencias

### Ejercicio C.1: Suposiciones Inteligentes (Divide y Vencerás)
Resuelva exactamente (para $n = 2^k$) y dé complejidad $\Theta$:

1. $T(n) = 2T(n/2) + 1$, $T(1) = 1$
2. $T(n) = 4T(n/2) + n$, $T(1) = 1$
3. $T(n) = 2T(n/2) + n \log n$, $T(1) = 1$ *(pista: expanda 3-4 niveles)*
4. $T(n) = 3T(n/3) + n$, $T(1) = 1$

---

### Ejercicio C.2: Recurrencias Homogéneas Lineales (Raíces Distintas)
Resuelva completamente (solución cerrada + complejidad $\Theta$):

1. $a_n = 5a_{n-1} - 6a_{n-2}$, $a_0 = 1, a_1 = 4$
2. $a_n = 4a_{n-1} - 3a_{n-2}$, $a_0 = 2, a_1 = 5$
3. $a_n = 2a_{n-1} + 3a_{n-2}$, $a_0 = 1, a_1 = 2$
4. $F_n = F_{n-1} + F_{n-2}$, $F_0 = 0, F_1 = 1$ (re-verificar Fibonacci)

---

### Ejercicio C.3: Recurrencias Homogéneas (Raíces Múltiples)
Resuelva completamente:

1. $a_n = 4a_{n-1} - 4a_{n-2}$, $a_0 = 1, a_1 = 4$
2. $a_n = 6a_{n-1} - 9a_{n-2}$, $a_0 = 2, a_1 = 6$
3. $a_n = 3a_{n-1} - 3a_{n-2} + a_{n-3}$, $a_0 = 0, a_1 = 1, a_2 = 3$
   *(Pista: $x^3 - 3x^2 + 3x - 1 = (x-1)^3$)*

---

### Ejercicio C.4: Recurrencias No Homogéneas (Coeficientes Indeterminados)
Resuelva (solución general = homogénea + particular):

1. $a_n = 2a_{n-1} + 1$, $a_0 = 0$
2. $a_n = 3a_{n-1} + 2^n$, $a_0 = 1$
3. $a_n = 2a_{n-1} + n$, $a_0 = 1$
4. $a_n = 4a_{n-1} - 4a_{n-2} + 2^n$, $a_0 = 1, a_1 = 4$
   *(Pista: parte particular $A n 2^n$ porque $2$ es raíz doble de la homogénea)*

---

### Ejercicio C.5: Aplicación Master Theorem
Para cada recurrencia, identifique $a, b, f(n)$, calcule $n^{\log_b a}$, determine el caso y dé $\Theta$:

1. $T(n) = 8T(n/2) + n^2$
2. $T(n) = 2T(n/2) + n \log n$
3. $T(n) = 7T(n/2) + n^2$
4. $T(n) = T(n/2) + 1$
5. $T(n) = 4T(n/2) + n^2 \log n$

---

### Ejercicio C.6: Recurrencias Mixtas / Tipo Examen
1. **Búsqueda binaria con costo lineal**: $T(n) = T(n/2) + n$, $T(1)=1$. Resuelva por suposiciones inteligentes.
2. **Algoritmo recursivo extraño**: $T(n) = T(n-1) + n$, $T(1)=1$. Resuelva por telescopio.
3. **Karatsuba**: $T(n) = 3T(n/2) + n$, $T(1)=1$. Resuelva (ya visto en teoría).
4. **Multiplicación matrices Strassen**: $T(n) = 7T(n/2) + n^2$. Aplique Master Theorem.

---

## Sección D: Problemas Integrados (Tipo Examen)

### Ejercicio D.1: Análisis Completo de Algoritmo
Analice el siguiente algoritmo:
```python
def mystery(A):
    n = len(A)
    count = 0
    for i in range(n):
        for j in range(i, n):
            for k in range(j, n):
                if A[i] + A[j] == A[k]:
                    count += 1
    return count
```

**Preguntas**:
a) ¿Qué hace el algoritmo? (Descripción en palabras)
b) Derive $T(n)$ exacto (OE) en el peor caso.
c) Complejidad $\Theta$.
d) ¿Cambia la complejidad en el mejor caso? Justifique.

---

### Ejercicio D.2: Recurrencia de Algoritmo Recursivo
Considere este algoritmo recursivo:
```python
def rec(n):
    if n <= 1:
        return 1
    total = 0
    for i in range(n):
        total += rec(n-1)
    return total
```

**Preguntas**:
a) Escriba la recurrencia para $T(n)$ (tiempo de ejecución).
b) Resuelva la recurrencia exactamente.
c) Complejidad $\Theta$.
d) ¿Qué retorna `rec(n)` como función matemática?

---

### Ejercicio D.3: Comparación de Algoritmos
Algoritmo A: $T_A(n) = 100 n \log_2 n$
Algoritmo B: $T_B(n) = 0.01 n^2$

**Preguntas**:
a) ¿Para qué valores de $n$ es A más rápido que B?
b) Resuelva $100 n \log_2 n < 0.01 n^2$ (aprox. numérico).
c) Explique por qué la notación asintótica "oculta" este cruce.

---

### Ejercicio D.4: Demostración por Inducción
Demuestre por inducción que la solución de $T(n) = 2T(n/2) + n$, $T(1)=1$, $n=2^k$ es $T(n) = n \log_2 n + n$.

**Pasos requeridos**:
1. Cambio de variable $n=2^k$, $S(k)=T(2^k)$.
2. Hipótesis de inducción para $S(k)$.
3. Paso base $k=0$.
4. Paso inductivo $k \to k+1$.
5. Conclusión para $T(n)$.

---

### Ejercicio D.5: Diseño de Algoritmo y Análisis
**Problema**: Dado un array $A[1..n]$ de enteros positivos, encontrar si existe un par $(i,j)$ con $i < j$ tal que $A[i] + A[j] = K$ (valor dado).

**Preguntas**:
a) Algoritmo fuerza bruta: pseudocódigo + análisis $\Theta$.
b) Algoritmo con ordenación + dos punteros: pseudocódigo + análisis $\Theta$.
c) Algoritmo con hash set: pseudocódigo + análisis $\Theta$ (caso medio).
d) Compare los tres: ¿cuándo usar cada uno?

---

---

# SOLUCIONES

---

## SOLUCIONES Sección A

### Solución A.1
**1. OE por iteración**:
- `i < n`: 1 OE (comparación)
- `s += i`: 2 OE (suma + asignación)
- `i *= 2`: 2 OE (multiplicación + asignación)
- Total por iteración: **5 OE**
- Inicialización: `s=0` (1), `i=1` (1) = 2 OE
- Evaluación final falsa: 1 OE

**2. Número de iteraciones**: $i$ toma valores $1, 2, 4, 8, \dots, 2^k < n \Rightarrow k = \lfloor \log_2 n \rfloor$. Iteraciones = $\lfloor \log_2 n \rfloor + 1$ (incluyendo $i=1$).

**3. $T(n)$ exacto**:
$$T(n) = 2 + 5(\lfloor \log_2 n \rfloor + 1) + 1 = 5\lfloor \log_2 n \rfloor + 8$$

**4. Complejidad**: $\boxed{\Theta(\log n)}$

---

### Solución A.2
**1. Sumatoria**:
$$\sum_{i=1}^n \sum_{j=i}^n 1$$

**2. Resolución**:
$$\sum_{i=1}^n (n - i + 1) = \sum_{i=1}^n (n+1) - \sum_{i=1}^n i = n(n+1) - \frac{n(n+1)}{2} = \frac{n(n+1)}{2}$$

**3. Valor retornado**: $\frac{n(n+1)}{2}$ (número triangular $T_n$)

**4. Complejidad**: $\boxed{\Theta(n^2)}$

---

### Solución A.3
**1. Sumatoria triple**:
$$\sum_{i=1}^n \sum_{j=1}^i \sum_{k=1}^j 1 = \sum_{i=1}^n \sum_{j=1}^i j = \sum_{i=1}^n \frac{i(i+1)}{2} = \frac{1}{2}\sum_{i=1}^n (i^2 + i)$$

**2. Fórmulas**:
$$\sum_{i=1}^n i = \frac{n(n+1)}{2},\quad \sum_{i=1}^n i^2 = \frac{n(n+1)(2n+1)}{6}$$

$$\frac{1}{2}\left[ \frac{n(n+1)(2n+1)}{6} + \frac{n(n+1)}{2} \right] = \frac{n(n+1)}{12}\left[ (2n+1) + 3 \right] = \frac{n(n+1)(2n+4)}{12} = \frac{n(n+1)(n+2)}{6}$$

**3. Valor retornado**: $\binom{n+2}{3} = \frac{n(n+1)(n+2)}{6}$ (números tetraédricos)

**4. Complejidad**: $\boxed{\Theta(n^3)}$

---

### Solución A.4 (Insertion Sort)
**1. OE en `while`**:
- Condición `i > 0 and A[i] > key`: 2 comparaciones + 1 acceso = 3 OE (eval. cortocircuito)
- Cuerpo: `A[i+1] = A[i]` (2 OE: acceso + asignación), `i = i - 1` (2 OE) = 4 OE

**2. Caso mejor** (ya ordenado): `while` nunca entra (condición falsa en primera eval).
- Por $j$: 1 (key) + 1 (i=j-1) + 1 (eval while falsa) + 1 (asignación final) = 4 OE + overhead bucle for
- $T_{\text{mejor}}(n) = \Theta(n)$ (lineal)

**3. Caso peor** (inverso): `while` itera $j-1$ veces.
- Por $j$: overhead + $(j-1)\times(3+4) + 1 \approx 7j$
- $T_{\text{peor}}(n) = \sum_{j=2}^n 7j = 7\frac{n(n+1)}{2} - 7 \in \Theta(n^2)$

**4. Caso medio**: `while` itera $\approx j/2$ veces.
- $T_{\text{medio}}(n) \approx \sum_{j=2}^n 3.5j \in \Theta(n^2)$

**5. Clasificación**:
| Caso | Complejidad |
|------|-------------|
| Mejor | $\Theta(n)$ (también $O(n), \Omega(n)$) |
| Peor | $\Theta(n^2)$ (también $O(n^2), \Omega(n^2)$) |
| Medio | $\Theta(n^2)$ |

---

### Solución A.5
**1. $T(m,n)$**:
- Inicialización: 2 OE
- Bucle externo: $m$ iteraciones × (evaluación + asignación $i$) ≈ 2m
- Bucle interno: $\sum_{i=1}^m \sum_{j=1}^n$ [eval + cuerpo]
- Cuerpo: acceso A[i][j] (1), comparación (1), posible asignación (1) → 3 OE promedio
- Total: $T(m,n) = 3mn + O(m+n)$

**2. Complejidad**: $\Theta(mn)$

**3. Si $m=n$**: $\boxed{\Theta(n^2)}$

---

## SOLUCIONES Sección B

### Solución B.1: Ordenación por Crecimiento

Simplificaciones previas:
- $f_8(n) = 2^{\log n} = n$ (asumiendo $\log = \log_2$)
- $f_{10}(n) = \log(n!) \sim \log(\sqrt{2\pi n}(n/e)^n) = \Theta(n \log n)$ (Stirling)
- $f_9(n) = n^{\log n} = e^{(\log n)^2}$ (cuasi-polinómico)

Orden (con $\Theta$-equivalencias):
1. $f_5(n) = (\log n)^2$ — **polilogarítmico**
2. $f_7(n) = 100n \in \Theta(n)$, $f_8(n) = n \in \Theta(n)$ — **lineal** (empate)
3. $f_2(n) = n \log n$, $f_{10}(n) = \log(n!) \in \Theta(n \log n)$ — **linealítmico** (empate)
4. $f_6(n) = n^{1.5}$ — **polinómico grado 1.5**
5. $f_1(n) = n^2$ — **cuadrático**
6. $f_9(n) = n^{\log n}$ — **cuasi-polinómico** ($e^{(\log n)^2}$)
7. $f_3(n) = 2^n$ — **exponencial base 2**
8. $f_4(n) = n!$ — **factorial** (super-exponencial)

---

### Solución B.2: Testigos Explícitos

1. $7n^2 + 3n \leq 7n^2 + 3n^2 = 10n^2$ para $n \geq 1$. $\boxed{c=10, n_0=1, \in O(n^2)}$. También $\Omega(n^2)$ con $c=7$. $\boxed{\Theta(n^2)}$.

2. $\lim \frac{5n \log n}{n^2} = 5\lim \frac{\log n}{n} = 0$. $\boxed{\in O(n^2), \notin \Omega(n^2), \notin \Theta(n^2)}$.
   Testigo $O$: $5n\log n \leq 5n^2$ para $n \geq 2$ ($c=5, n_0=2$).

3. $2^{n+3} = 8 \cdot 2^n$. $\boxed{c=8, n_0=1, \in \Theta(2^n)}$.

4. $n^2 \leq n^2 + 1000n \leq n^2 + 1000n^2 = 1001n^2$ para $n \geq 1$. $\boxed{\Theta(n^2)}$.

5. $\lim \frac{\sqrt{n}}{\log n} = \infty$. $\boxed{\in \Omega(\log n), \notin O(\log n)}$.

---

### Solución B.3: Límites

1. $\lim \frac{n^3 + 2^n}{2^n} = \lim \frac{n^3}{2^n} + 1 = 0 + 1 = 1 \in (0,\infty) \implies \boxed{\Theta(2^n)}$

2. $\lim \frac{n \log n}{n^{1.5}} = \lim \frac{\log n}{n^{0.5}} \overset{H}{=} \lim \frac{1/n}{0.5 n^{-0.5}} = \lim \frac{2}{\sqrt{n}} = 0 \implies \boxed{O(n^{1.5}), \notin \Omega}$

3. $\log(n^2) = 2\log n \implies \lim = 2 \implies \boxed{\Theta(\log n)}$

4. Stirling: $n! \sim \sqrt{2\pi n}(n/e)^n$. $\frac{n!}{n^n} \sim \sqrt{2\pi n} e^{-n} \to 0 \implies \boxed{O(n^n), \notin \Omega}$

5. $\lim \frac{3^n}{2^n} = \lim (1.5)^n = \infty \implies \boxed{\Omega(2^n), \notin O(2^n)}$

---

### Solución B.4: Verdadero/Falso

1. **V** (Transitividad de $O$)
2. **V** ($f \leq c_1 g$, $f \leq c_2 h \implies f \leq \max(c_1,c_2)(g+h)$)
3. **V** (Simetría de $\Theta$)
4. **V** ($n^2 \leq 1\cdot(n^2+n)$ para $n\geq 0$)
5. **V** ($n^2+n \leq 2n^2$ para $n\geq 1$)
6. **V** ($2n^2+3n \geq 2n^2$ para $n\geq 0$)
7. **V** ($\log_2 n = \frac{\log_{10} n}{\log_{10} 2}$, factor constante)
8. **V** (Exponencial domina a polinómico)

---

### Solución B.5: Simplificación

1. $3n^2 + 5n \log n + 1000 \in \boxed{\Theta(n^2)}$ (término dominante $n^2$)
2. $\frac{n^3 + 2n^2}{n+1} = \frac{n^2(n+2)}{n+1} \sim n^2 \implies \boxed{\Theta(n^2)}$
3. $\sum_{k=1}^n (k^2 + k) = \frac{n(n+1)(2n+1)}{6} + \frac{n(n+1)}{2} \sim \frac{2n^3}{6} = \frac{n^3}{3} \implies \boxed{\Theta(n^3)}$
4. $\log(n^2 + 3n) = \log[n^2(1 + 3/n)] = 2\log n + \log(1+3/n) \sim 2\log n \implies \boxed{\Theta(\log n)}$
5. $2^{n+1} + 3^n = 2\cdot 2^n + 3^n$. Como $3^n$ domina: $\boxed{\Theta(3^n)}$

---

## SOLUCIONES Sección C

### Solución C.1: Suposiciones Inteligentes

**1. $T(n) = 2T(n/2) + 1$**:
$n=2^k$: $T(2^k) = 2T(2^{k-1}) + 1 = 2[2T(2^{k-2})+1]+1 = 2^2 T(2^{k-2}) + 2 + 1 = \dots = 2^k T(1) + \sum_{i=0}^{k-1} 2^i = 2^k + (2^k - 1) = 2^{k+1} - 1$
$T(n) = 2n - 1 \in \boxed{\Theta(n)}$

**2. $T(n) = 4T(n/2) + n$**:
$T(2^k) = 4T(2^{k-1}) + 2^k = 4[4T(2^{k-2})+2^{k-1}]+2^k = 4^2 T(2^{k-2}) + 2\cdot 2^k + 2^k = \dots = 4^k T(1) + k 2^k = 2^{2k} + k 2^k = n^2 + n \log_2 n$
$\boxed{\Theta(n^2)}$ (Master Theorem: $a=4,b=2, \log_2 4 = 2, f(n)=n \in O(n^{2-\epsilon})$ → Caso 1)

**3. $T(n) = 2T(n/2) + n \log n$**:
Expandir:
$T(2^k) = 2T(2^{k-1}) + 2^k k$
$= 2[2T(2^{k-2}) + 2^{k-1}(k-1)] + 2^k k = 2^2 T(2^{k-2}) + 2^k(k-1) + 2^k k$
$= 2^k T(1) + 2^k \sum_{i=1}^k i = 2^k + 2^k \frac{k(k+1)}{2} = n + n \frac{\log n (\log n + 1)}{2}$
$\boxed{\Theta(n \log^2 n)}$ (Master Theorem Caso 2 con $k=1$: $f(n)=n \log n = \Theta(n^{\log_2 2} \log^1 n)$)

**4. $T(n) = 3T(n/3) + n$**:
$a=3,b=3, \log_3 3 = 1, f(n)=n = \Theta(n^1 \log^0 n)$ → **Caso 2** con $k=0$
$\boxed{\Theta(n \log n)}$

---

### Solución C.2: Homogéneas Raíces Distintas

**1. $a_n - 5a_{n-1} + 6a_{n-2} = 0$**:
$x^2 - 5x + 6 = (x-2)(x-3) = 0 \implies r=2,3$
$a_n = c_1 2^n + c_2 3^n$
$a_0 = c_1 + c_2 = 1$
$a_1 = 2c_1 + 3c_2 = 4 \implies 2(1-c_2) + 3c_2 = 4 \implies c_2 = 2, c_1 = -1$
$\boxed{a_n = 2\cdot 3^n - 2^n \in \Theta(3^n)}$

**2. $a_n - 4a_{n-1} + 3a_{n-2} = 0$**:
$x^2 - 4x + 3 = (x-1)(x-3) = 0 \implies r=1,3$
$a_n = c_1 + c_2 3^n$
$a_0 = c_1 + c_2 = 2$
$a_1 = c_1 + 3c_2 = 5 \implies (2-c_2) + 3c_2 = 5 \implies c_2 = 1.5, c_1 = 0.5$
$\boxed{a_n = \frac{1}{2} + \frac{3}{2}3^n = \frac{1 + 3^{n+1}}{2} \in \Theta(3^n)}$

**3. $a_n - 2a_{n-1} - 3a_{n-2} = 0$**:
$x^2 - 2x - 3 = (x-3)(x+1) = 0 \implies r=3, -1$
$a_n = c_1 3^n + c_2 (-1)^n$
$a_0 = c_1 + c_2 = 1$
$a_1 = 3c_1 - c_2 = 2 \implies 3(1-c_2) - c_2 = 2 \implies 3 - 4c_2 = 2 \implies c_2 = 1/4, c_1 = 3/4$
$\boxed{a_n = \frac{3}{4}3^n + \frac{1}{4}(-1)^n = \frac{3^{n+1} + (-1)^n}{4} \in \Theta(3^n)}$

**4. Fibonacci**: Ver Sección 4.2 del tema 5. $\boxed{F_n = \frac{\varphi^n - \psi^n}{\sqrt{5}} \in \Theta(\varphi^n)}$, $\varphi \approx 1.618$

---

### Solución C.3: Raíces Múltiples

**1. $a_n - 4a_{n-1} + 4a_{n-2} = 0$**:
$x^2 - 4x + 4 = (x-2)^2 \implies r=2$ (mult. 2)
$a_n = c_1 2^n + c_2 n 2^n$
$a_0 = c_1 = 1$
$a_1 = 2c_1 + 2c_2 = 4 \implies 2 + 2c_2 = 4 \implies c_2 = 1$
$\boxed{a_n = 2^n + n 2^n = (n+1)2^n \in \Theta(n 2^n)}$

**2. $a_n - 6a_{n-1} + 9a_{n-2} = 0$**:
$x^2 - 6x + 9 = (x-3)^2 \implies r=3$ (mult. 2)
$a_n = c_1 3^n + c_2 n 3^n$
$a_0 = c_1 = 2$
$a_1 = 3c_1 + 3c_2 = 6 \implies 6 + 3c_2 = 6 \implies c_2 = 0$
$\boxed{a_n = 2\cdot 3^n \in \Theta(3^n)}$ (caso degenerado: $c_2=0$ elimina el factor $n$)

**3. $a_n - 3a_{n-1} + 3a_{n-2} - a_{n-3} = 0$**:
$x^3 - 3x^2 + 3x - 1 = (x-1)^3 \implies r=1$ (mult. 3)
$a_n = c_1 + c_2 n + c_3 n^2$
$a_0 = c_1 = 0$
$a_1 = c_1 + c_2 + c_3 = 1 \implies c_2 + c_3 = 1$
$a_2 = c_1 + 2c_2 + 4c_3 = 3 \implies 2c_2 + 4c_3 = 3$
Resolviendo: $c_2 = 1 - c_3$, $2(1-c_3) + 4c_3 = 3 \implies 2 + 2c_3 = 3 \implies c_3 = 1/2, c_2 = 1/2$
$\boxed{a_n = \frac{n}{2} + \frac{n^2}{2} = \frac{n(n+1)}{2} \in \Theta(n^2)}$ (números triangulares)

---

### Solución C.4: No Homogéneas

**1. $a_n = 2a_{n-1} + 1$**:
Homogénea: $a_n^{(h)} = c 2^n$
Particular: probar constante $A$: $A = 2A + 1 \implies A = -1$
General: $a_n = c 2^n - 1$
$a_0 = c - 1 = 0 \implies c = 1$
$\boxed{a_n = 2^n - 1 \in \Theta(2^n)}$

**2. $a_n = 3a_{n-1} + 2^n$**:
Homogénea: $c 3^n$
Particular: probar $A 2^n$: $A 2^n = 3A 2^{n-1} + 2^n = \frac{3}{2}A 2^n + 2^n \implies A = \frac{3}{2}A + 1 \implies -\frac{1}{2}A = 1 \implies A = -2$
General: $a_n = c 3^n - 2^{n+1}$
$a_0 = c - 2 = 1 \implies c = 3$
$\boxed{a_n = 3^{n+1} - 2^{n+1} \in \Theta(3^n)}$

**3. $a_n = 2a_{n-1} + n$**:
Homogénea: $c 2^n$
Particular: probar $An + B$: $An+B = 2(A(n-1)+B) + n = 2An - 2A + 2B + n$
$An+B = (2A+1)n + (2B-2A)$
$A = 2A+1 \implies A = -1$
$B = 2B - 2A = 2B + 2 \implies B = -2$
General: $a_n = c 2^n - n - 2$
$a_0 = c - 2 = 1 \implies c = 3$
$\boxed{a_n = 3\cdot 2^n - n - 2 \in \Theta(2^n)}$

**4. $a_n = 4a_{n-1} - 4a_{n-2} + 2^n$**:
Homogénea: $(x-2)^2=0 \implies c_1 2^n + c_2 n 2^n$
Particular: $2^n$ es solución homogénea (raíz doble) → probar $A n^2 2^n$
$a_n^{(p)} = A n^2 2^n$
Sustituir y resolver para $A$... (cálculo omitido por brevedad, $A = 1/2$)
General: $a_n = c_1 2^n + c_2 n 2^n + \frac{1}{2}n^2 2^n$
Con $a_0=1, a_1=4$: $c_1=1, c_2=1/2$
$\boxed{a_n = 2^n + \frac{1}{2}n 2^n + \frac{1}{2}n^2 2^n = \frac{1}{2}(n^2 + n + 2)2^n \in \Theta(n^2 2^n)}$

---

### Solución C.5: Master Theorem

| Recurrencia | $a$ | $b$ | $f(n)$ | $n^{\log_b a}$ | Caso | $\Theta$ |
|-------------|-----|-----|--------|----------------|------|----------|
| $8T(n/2)+n^2$ | 8 | 2 | $n^2$ | $n^3$ | 1 ($n^2 \in O(n^{3-\epsilon})$) | $\Theta(n^3)$ |
| $2T(n/2)+n\log n$ | 2 | 2 | $n\log n$ | $n^1$ | 2 ($k=1$) | $\Theta(n \log^2 n)$ |
| $7T(n/2)+n^2$ | 7 | 2 | $n^2$ | $n^{\log_2 7} \approx n^{2.807}$ | 1 | $\Theta(n^{\log_2 7})$ |
| $T(n/2)+1$ | 1 | 2 | $1$ | $n^0=1$ | 2 ($k=0$) | $\Theta(\log n)$ |
| $4T(n/2)+n^2\log n$ | 4 | 2 | $n^2\log n$ | $n^2$ | 2 ($k=1$) | $\Theta(n^2 \log^2 n)$ |

---

### Solución C.6: Mixtas

**1. Búsqueda binaria con costo lineal**: $T(n) = T(n/2) + n$
$n=2^k$: $T(2^k) = T(2^{k-1}) + 2^k = 2^k + 2^{k-1} + \dots + 2^0 = 2^{k+1} - 1 = 2n - 1$
$\boxed{\Theta(n)}$ (no $\log n$ porque el "combine" cuesta $n$)

**2. $T(n) = T(n-1) + n$**:
Telescopio: $T(n) = T(n-1) + n = T(n-2) + (n-1) + n = \dots = T(1) + \sum_{i=2}^n i = 1 + \frac{n(n+1)}{2} - 1 = \frac{n(n+1)}{2}$
$\boxed{\Theta(n^2)}$

**3. Karatsuba**: $T(n) = 3T(n/2) + n$ → Ver Tema 5, Sección 2.2 → $\boxed{\Theta(n^{\log_2 3}) \approx \Theta(n^{1.585})}$

**4. Strassen**: $T(n) = 7T(n/2) + n^2$ → Master Theorem: $a=7, b=2, \log_2 7 \approx 2.807, f(n)=n^2 \in O(n^{2.807-\epsilon})$ → **Caso 1** → $\boxed{\Theta(n^{\log_2 7}) \approx \Theta(n^{2.807})}$

---

## SOLUCIONES Sección D

### Solución D.1: Análisis Completo

**a) Qué hace**: Cuenta el número de tríadas $(i,j,k)$ con $i \leq j \leq k$ tales que $A[i] + A[j] = A[k]$. (Variación de 3SUM con restricción de índices).

**b) OE peor caso**:
- Bucles: $i=1..n$, $j=i..n$, $k=j..n$
- Iteraciones: $\sum_{i=1}^n \sum_{j=i}^n \sum_{k=j}^n 1 = \sum_{i=1}^n \sum_{j=i}^n (n-j+1) = \sum_{i=1}^n \frac{(n-i+1)(n-i+2)}{2} = \binom{n+2}{3} = \frac{n(n+1)(n+2)}{6}$
- Cuerpo: 2 accesos + 1 suma + 1 comparación + (posible incremento) = 4-5 OE
- $T(n) = \frac{5}{6}n^3 + O(n^2)$ OE

**c) Complejidad**: $\boxed{\Theta(n^3)}$

**d) Mejor caso**: El `if` puede ser falso siempre, pero **los bucles se ejecutan igual**. La complejidad **no cambia**: $\Theta(n^3)$. (A diferencia de Insertion Sort, aquí no hay salida temprana del bucle).

---

### Solución D.2: Recursivo Extraño

**a) Recurrencia**:
- Base: $T(1) = O(1)$
- Recursivo: bucle `for i in range(n)` → $n$ llamadas a `rec(n-1)` + $O(n)$ overhead
- $T(n) = n T(n-1) + O(n)$, $T(1) = 1$

**b) Resolución**:
$T(n) = n T(n-1) + n$
$= n[(n-1)T(n-2) + (n-1)] + n = n(n-1)T(n-2) + n(n-1) + n$
$= n(n-1)(n-2)T(n-3) + n(n-1)(n-2) + n(n-1) + n$
$\dots$
$= n! T(1) + \sum_{k=1}^n \frac{n!}{k!} = n! + n!\sum_{k=1}^n \frac{1}{k!}$
$= n! \left(1 + \sum_{k=1}^n \frac{1}{k!}\right) \to n! (e - 1 + o(1))$ cuando $n \to \infty$

$\boxed{T(n) \sim (e-1)n! \in \Theta(n!)}$

**c) Complejidad**: $\boxed{\Theta(n!)}$

**d) Valor retornado**: `total` acumula $n$ copias de `rec(n-1)`.
- `rec(1)` = 1
- `rec(2)` = 2 × 1 = 2
- `rec(3)` = 3 × 2 = 6
- `rec(4)` = 4 × 6 = 24
- **Patrón**: `rec(n) = n!`

---

### Solución D.3: Cruce de Algoritmos

**a) Desigualdad**:
$100 n \log_2 n < 0.01 n^2 \implies 10000 \log_2 n < n$

**b) Solución numérica**:
Probar valores:
- $n=10^5$: LHS = 10000 × 16.6 = 166,000; RHS = 100,000 → LHS > RHS
- $n=2\times 10^5$: LHS = 10000 × 17.6 = 176,000; RHS = 200,000 → LHS < RHS
- **Cruce aprox**: $n \approx 1.5 \times 10^5$

**c) Explicación**: La notación asintótica $\Theta$ describe comportamiento **para $n \to \infty$**. Aquí $n \log n \in o(n^2)$, así que **eventualmente** A gana. Pero las **constantes ocultas** (100 vs 0.01) hacen que B sea mejor para $n$ "pequeños" (hasta ~150,000). En la práctica, siempre considerar constantes y $n$ realista.

---

### Solución D.4: Inducción Formal

**1. Cambio variable**: $n = 2^k$, $S(k) = T(2^k)$.
Recurrencia: $S(k) = 2S(k-1) + 2^k$, $S(0) = 1$.

**2. Hipótesis**: $S(k) = (k+1)2^k$ para todo $k \geq 0$.
(Equivale a $T(n) = n(\log_2 n + 1) = n\log_2 n + n$)

**3. Base $k=0$**: $S(0) = (0+1)2^0 = 1$. ✓ Coincide con $T(1)=1$.

**4. Paso inductivo**: Asumir verdadero para $k$. Probar para $k+1$:
$$
\begin{aligned}
S(k+1) &= 2S(k) + 2^{k+1} & \text{(recurrencia)} \\
&= 2[(k+1)2^k] + 2^{k+1} & \text{(hipótesis)} \\
&= (k+1)2^{k+1} + 2^{k+1} \\
&= (k+2)2^{k+1} & \text{(factor común)}
\end{aligned}
$$
Que es exactamente la fórmula para $k+1$. ✓

**5. Conclusión**: Por inducción, $S(k) = (k+1)2^k$ para todo $k \geq 0$.
Retornando: $T(n) = S(\log_2 n) = (\log_2 n + 1)n = n\log_2 n + n$. $\quad \blacksquare$

---

### Solución D.5: Pareja con Suma K

**a) Fuerza Bruta**:
```python
def pair_sum_brute(A, K):
    n = len(A)
    for i in range(n):
        for j in range(i+1, n):
            if A[i] + A[j] == K:
                return True
    return False
```
- Análisis: $\sum_{i=0}^{n-1} \sum_{j=i+1}^{n-1} 1 = \binom{n}{2} \in \boxed{\Theta(n^2)}$

**b) Ordenación + Dos Punteros**:
```python
def pair_sum_sort(A, K):
    A.sort()  # O(n log n)
    left, right = 0, len(A)-1
    while left < right:
        s = A[left] + A[right]
        if s == K:
            return True
        elif s < K:
            left += 1
        else:
            right -= 1
    return False
```
- Análisis: Sort $\Theta(n \log n)$ + while lineal $\Theta(n)$ → $\boxed{\Theta(n \log n)}$
- **Requiere**: Array modificable (ordena in-place) o copia.

**c) Hash Set (caso medio)**:
```python
def pair_sum_hash(A, K):
    seen = set()
    for x in A:
        if K - x in seen:
            return True
        seen.add(x)
    return False
```
- Análisis: $n$ iteraciones, cada una $O(1)$ promedio (hash) → $\boxed{\Theta(n)}$ caso medio
- **Requiere**: $O(n)$ espacio extra. Peor caso hash: $\Theta(n^2)$ (colisiones).

**d) Comparación y Cuándo Usar**:

| Algoritmo | Tiempo | Espacio | Mejor Para |
|-----------|--------|---------|------------|
| Fuerza bruta | $\Theta(n^2)$ | $O(1)$ | $n$ muy pequeño (< 50), memoria extremadamente limitada |
| Sort + 2 punteros | $\Theta(n \log n)$ | $O(1)$ o $O(n)$ | Necesitas orden final, memoria limitada, caso peor garantizado |
| Hash Set | $\Theta(n)$ prom. | $O(n)$ | **Caso general**, máximo rendimiento, memoria disponible |

> **Conclusión práctica**: Hash Set es óptimo en tiempo promedio. Sort+2 punteros da garantía $\Theta(n \log n)$ en peor caso y no requiere hash.

---

---

## 📋 Checklist Final de Preparación

- [ ] **Complejidad**: Saber contar OE en bucles anidados, derivar sumatorias, identificar caso mejor/peor/medio.
- [ ] **Notación asintótica**: Definiciones formales $O, \Omega, \Theta$, propiedades, método del límite, encontrar testigos $(c,n_0)$.
- [ ] **Recurrencias**: 
  - Suposiciones inteligentes (Divide y Vencerás)
  - Ecuación característica (homogéneas lineales cte)
  - Raíces distintas vs múltiples
  - Master Theorem (casos 1, 2, 3)
  - No homogéneas (parte particular)
- [ ] **Inducción matemática**: Estructura base + paso inductivo para validar soluciones.
- [ ] **Algoritmos clásicos**: Selection/Insertion/Merge/Quick Sort, Búsqueda binaria, Fibonacci, Hanoi, Strassen, Karatsuba.
- [ ] **Demostraciones**: Transitividad, regla suma/producto, simplificación asintótica.

---

> **¡Éxito en el examen!** 🎓

*Documento generado como guía de estudio para "Análisis y Diseño de Algoritmos" - Primer Examen - Dra. Irene Olaya Ayaquica Martínez*