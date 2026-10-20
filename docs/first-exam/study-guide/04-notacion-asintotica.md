# Notación Asintótica: Cotas de Complejidad

## 1. Introducción y Propósito

Una vez calculado el tiempo exacto $T(n)$ (como función del tamaño $n$), necesitamos **clasificar** y **comparar** funciones según su **crecimiento asintótico** (comportamiento para $n \to \infty$).

> **Idea central**: Agrupar funciones que "crecen de la misma forma" en **clases de equivalencia**.

- $\mathbb{N} = \{0, 1, 2, \dots\}$ (números naturales)
- $\mathbb{R}$ (números reales)
- Funciones $f, g : \mathbb{N} \to [0, \infty)$ (no negativas)

---

## 2. Cota Superior: Notación **O-grande** ($O$)

### 2.1 Definición Formal

> **Definición**: Dada $f : \mathbb{N} \to [0, \infty)$, el conjunto $O(f)$ (cota superior de $f$) es:
>
> $$O(f) = \left\{ g : \mathbb{N} \to [0, \infty) \ \middle|\ \exists c \in \mathbb{R}^+,\ \exists n_0 \in \mathbb{N} : g(n) \leq c \cdot f(n),\ \forall n \geq n_0 \right\}$$

**Lectura**: "$g \in O(f)$" significa "$g$ está acotada superiormente por algún múltiplo constante de $f$ para $n$ lo suficientemente grande".

### 2.2 Interpretación Gráfica

```
g(n) ≤ c·f(n)  para todo n ≥ n₀

      ↑
      |           g(n)
      |          /
g,c·f|         / 
      |    c·f(n)──────
      |       /
      |      /
      |_____/
      n₀    → n
```

### 2.3 Ejemplos Canónicos

| $g(n)$ | $f(n)$ | ¿$g \in O(f)$? | Testigos $(c, n_0)$ |
|--------|--------|----------------|---------------------|
| $3n^2 + 2n + 1$ | $n^2$ | **Sí** | $c=6, n_0=1$ |
| $n^2$ | $3n^2 + 2n + 1$ | **Sí** | $c=1, n_0=1$ |
| $n^3$ | $n^2$ | **No** | — |
| $100n + 5$ | $n$ | **Sí** | $c=105, n_0=1$ |
| $\log n$ | $n$ | **Sí** | $c=1, n_0=1$ |
| $n$ | $\log n$ | **No** | — |

### 2.4 Propiedades Fundamentales de $O$

| # | Propiedad | Enunciado |
|---|-----------|-----------|
| **1** | Reflexividad | $\forall f:\ f \in O(f)$ |
| **2** | Transitividad (incl.) | $f \in O(g) \implies O(f) \subset O(g)$ |
| **3** | Simetría de clases | $O(f) = O(g) \iff f \in O(g) \land g \in O(f)$ |
| **4** | Transitividad (elem.) | $f \in O(g) \land g \in O(h) \implies f \in O(h)$ |
| **5** | Mínimo de cotas | $f \in O(g) \land f \in O(h) \implies f \in O(\min(g,h))$ |
| **6** | **Regla de la Suma** | $f_1 \in O(g) \land f_2 \in O(h) \implies f_1 + f_2 \in O(\max(g,h))$ |
| **7** | **Regla del Producto** | $f_1 \in O(g) \land f_2 \in O(h) \implies f_1 \cdot f_2 \in O(g \cdot h)$ |
| **8** | **Regla del Límite** | Si $\exists \lim_{n\to\infty} \frac{f(n)}{g(n)} = k$: <br>• $k \neq 0, k < \infty \implies O(f) = O(g)$ <br>• $k = 0 \implies f \in O(g),\ O(f) \subset O(g),\ g \notin O(f)$ <br>• $k = \infty \implies f \notin O(g),\ g \in O(f)$ |

> **Consejo práctico**: Siempre usar el **representante más simple** de cada clase: $O(1),\ O(n),\ O(n^2),\ O(n \log n),\ O(2^n)$, etc.

---

## 3. Cota Inferior: Notación **Ω-grande** ($\Omega$)

### 3.1 Definición Formal

> **Definición**: Dada $f : \mathbb{N} \to [0, \infty)$, el conjunto $\Omega(f)$ (cota inferior de $f$) es:
>
> $$\Omega(f) = \left\{ g : \mathbb{N} \to [0, \infty) \ \middle|\ \exists c \in \mathbb{R}^+,\ \exists n_0 \in \mathbb{N} : g(n) \geq c \cdot f(n),\ \forall n \geq n_0 \right\}$$

**Lectura**: "$g \in \Omega(f)$" significa "$g$ crece **al menos tan rápido** como algún múltiplo de $f$".

### 3.2 Propiedades de $\Omega$

| # | Propiedad | Enunciado |
|---|-----------|-----------|
| **1** | Reflexividad | $\forall f:\ f \in \Omega(f)$ |
| **2** | Transitividad (incl.) | $f \in \Omega(g) \implies \Omega(f) \subset \Omega(g)$ |
| **3** | Simetría de clases | $\Omega(f) = \Omega(g) \iff f \in \Omega(g) \land g \in \Omega(f)$ |
| **4** | Transitividad (elem.) | $f \in \Omega(g) \land g \in \Omega(h) \implies f \in \Omega(h)$ |
| **5** | Máximo de cotas | $f \in \Omega(g) \land f \in \Omega(h) \implies f \in \Omega(\max(g,h))$ |
| **6** | **Regla de la Suma** | $f_1 \in \Omega(g) \land f_2 \in \Omega(h) \implies f_1 + f_2 \in \Omega(\max(g,h))$ |
| **7** | **Regla del Producto** | $f_1 \in \Omega(g) \land f_2 \in \Omega(h) \implies f_1 \cdot f_2 \in \Omega(g \cdot h)$ |
| **8** | **Regla del Límite** | Si $\lim_{n\to\infty} \frac{f(n)}{g(n)} = k$: <br>• $k \neq 0, k < \infty \implies \Omega(f) = \Omega(g)$ <br>• $k = 0 \implies f \notin \Omega(g),\ g \in \Omega(f)$ <br>• $k = \infty \implies f \in \Omega(g),\ \Omega(f) \supset \Omega(g)$ |

---

## 4. Cota Ajustada: Notación **Θ-grande** ($\Theta$)

### 4.1 Definición Formal

> **Definición**: $\Theta(f) = O(f) \cap \Omega(f)$.
>
> $$g \in \Theta(f) \iff g \in O(f) \land g \in \Omega(f)$$
>
> Equivalentemente: $\exists c_1, c_2 > 0,\ \exists n_0:\ c_1 f(n) \leq g(n) \leq c_2 f(n),\ \forall n \geq n_0$.

**Interpretación**: $g$ crece **exactamente a la misma tasa** que $f$ (hasta factores constantes).

### 4.2 Relación entre las Tres Notaciones

```
           g ∈ Θ(f)
         ╔═════════╗
         ║  g ∈ O(f)  ║
         ║  g ∈ Ω(f)  ║
         ╚═════════╝

g ∈ O(f)     →     "g crece NO MÁS RÁPIDO que f"
g ∈ Ω(f)     →     "g crece NO MÁS LENTO que f"
g ∈ Θ(f)     →     "g crece A LA MISMA VELOCIDAD que f"
```

### 4.3 Jerarquía de Crecimiento (Orden Estricto)

$$
1 \ \prec\ \log n \ \prec\ \sqrt{n} \ \prec\ n \ \prec\ n \log n \ \prec\ n^2 \ \prec\ n^3 \ \prec\ 2^n \ \prec\ n! \ \prec\ n^n
$$

Donde $f \prec g$ significa $f \in O(g)$ pero $g \notin O(f)$ (crecimiento estrictamente menor).

---

## 5. Método del Límite (Criterio Práctico)

> **Teorema**: Para $f, g > 0$ eventualmente, si existe $L = \lim_{n \to \infty} \frac{f(n)}{g(n)}$:
>
> | Valor de $L$ | Conclusión |
> |--------------|------------|
> | $0 < L < \infty$ | $f \in \Theta(g)$ ($O(f) = O(g)$, $\Omega(f) = \Omega(g)$) |
> | $L = 0$ | $f \in O(g)$ y $f \notin \Omega(g)$ ($f$ crece más lento) |
> | $L = \infty$ | $f \in \Omega(g)$ y $f \notin O(g)$ ($f$ crece más rápido) |

### 5.1 Ejemplos de Aplicación

**Ejemplo 1**: $f(n) = 3n^2 + 2n + 1$, $g(n) = n^2$
$$
L = \lim_{n\to\infty} \frac{3n^2 + 2n + 1}{n^2} = \lim_{n\to\infty} \left( 3 + \frac{2}{n} + \frac{1}{n^2} \right) = 3 \in (0,\infty)
\implies f \in \Theta(n^2)
$$

**Ejemplo 2**: $f(n) = \log n$, $g(n) = n$
$$
L = \lim_{n\to\infty} \frac{\log n}{n} \overset{\text{H}}{=} \lim_{n\to\infty} \frac{1/n}{1} = 0
\implies \log n \in O(n),\ \log n \notin \Omega(n)
$$

**Ejemplo 3**: $f(n) = n^2$, $g(n) = n \log n$
$$
L = \lim_{n\to\infty} \frac{n^2}{n \log n} = \lim_{n\to\infty} \frac{n}{\log n} \overset{\text{H}}{=} \lim_{n\to\infty} \frac{1}{1/n} = \infty
\implies n^2 \in \Omega(n \log n),\ n^2 \notin O(n \log n)
$$

---

## 6. Órdenes Comunes y sus Relaciones

| Clase | Notación | Ejemplos Típicos |
|-------|----------|------------------|
| Constante | $\Theta(1)$ | Acceso array, hash lookup |
| Logarítmica | $\Theta(\log n)$ | Búsqueda binaria, altura árbol balanceado |
| Lineal | $\Theta(n)$ | Recorrido array, búsqueda secuencial |
| Linealítmica | $\Theta(n \log n)$ | Merge Sort, Heap Sort, Quick Sort (promedio) |
| Cuadrática | $\Theta(n^2)$ | Selection/Insertion/Bubble Sort, bucles anidados |
| Cúbica | $\Theta(n^3)$ | Multiplicación matrices naive, Floyd-Warshall |
| Polinómica | $\Theta(n^k)$ | Algoritmos en P |
| Exponencial | $\Theta(c^n)$ | Subconjuntos, TSP fuerza bruta, Hanoi |
| Factorial | $\Theta(n!)$ | Permutaciones, TSP exacto |

---

## 7. Demostraciones Formales: Encontrar Testigos $(c, n_0)$

### 7.1 Ejemplo: $3n^2 + 2n + 1 \in O(n^2)$

**Objetivo**: Encontrar $c, n_0$ tales que $3n^2 + 2n + 1 \leq c n^2$ para $n \geq n_0$.

**Paso 1**: Para $n \geq 1$, $2n \leq 2n^2$ y $1 \leq n^2$.
**Paso 2**: $3n^2 + 2n + 1 \leq 3n^2 + 2n^2 + n^2 = 6n^2$.
**Paso 3**: Tomar $c = 6$, $n_0 = 1$.
**Verificación**: $\forall n \geq 1:\ 3n^2 + 2n + 1 \leq 6n^2$. ✓

### 7.2 Ejemplo: $n^2 \in \Omega(n^2)$

**Objetivo**: $n^2 \geq c n^2$.
**Trivial**: $c = 1$, $n_0 = 1$. ✓

### 7.3 Ejemplo: $n \notin O(\log n)$ (por contradicción)

**Supongamos** $\exists c, n_0: n \leq c \log n\ \forall n \geq n_0$.
**Entonces** $\frac{n}{\log n} \leq c$.
Pero $\lim_{n\to\infty} \frac{n}{\log n} = \infty$. **Contradicción**. ✓

---

## 8. Manipulación Algebraica con Notación Asintótica

### 8.1 Reglas de Simplificación (para encontrar la forma $\Theta$)

| Regla | Ejemplo |
|-------|---------|
| **Eliminar términos de menor orden** | $3n^2 + 5n \log n + 100 \in \Theta(n^2)$ |
| **Eliminar coeficientes constantes** | $1000n^2 \in \Theta(n^2)$ |
| **Suma: domina el mayor** | $n^3 + n^2 \in \Theta(n^3)$ |
| **Producto: multiplican** | $n \cdot \log n \in \Theta(n \log n)$ |
| **Logaritmos: cambio de base es constante** | $\log_2 n = \frac{\ln n}{\ln 2} \in \Theta(\log n)$ |

### 8.2 Cuidado: No se puede "sumar dentro de O" incorrectamente

> **Incorrecto**: $O(n) + O(n^2) = O(n + n^2) = O(n^2)$ ✓ (correcto por regla suma)
> **Peligroso**: $\sum_{i=1}^n O(i) \neq O(\sum i)$ en general — la constante puede depender de $i$.

---

## 9. Ejercicios Resueltos Paso a Paso

### Ejercicio 1: Clasificar $f(n) = \frac{n^3 + 2n}{n+1}$

**Paso 1**: Simplificar algebraicamente
$$
f(n) = \frac{n(n^2 + 2)}{n+1} = \frac{n^3 + 2n}{n+1}
$$

**Paso 2**: División polinomial o límite
$$
\lim_{n\to\infty} \frac{f(n)}{n^2} = \lim_{n\to\infty} \frac{n^3 + 2n}{n^3 + n^2} = \lim_{n\to\infty} \frac{1 + 2/n^2}{1 + 1/n} = 1
$$

**Conclusión**: $f(n) \in \Theta(n^2)$.

---

### Ejercicio 2: Ordenar por crecimiento
$f_1(n) = 2^n,\quad f_2(n) = n!,\quad f_3(n) = n^{\log n},\quad f_4(n) = n^3,\quad f_5(n) = (\log n)^{\log n}$

**Análisis**:
- $f_4(n) = n^3$ (polinómico)
- $f_5(n) = (\log n)^{\log n} = e^{\log n \cdot \log \log n} = n^{\log \log n}$ (subpolinómico, superpolinomial en $\log$)
- $f_3(n) = n^{\log n} = e^{(\log n)^2}$ (cuasi-polinómico)
- $f_1(n) = 2^n = e^{n \log 2}$ (exponencial)
- $f_2(n) = n! \sim \sqrt{2\pi n}(n/e)^n$ (Stirling) $\approx n^n e^{-n}$ (super-exponencial)

**Orden**: $n^3 \prec n^{\log \log n} \prec n^{\log n} \prec 2^n \prec n!$

Es decir: $f_4 \prec f_5 \prec f_3 \prec f_1 \prec f_2$.

---

### Ejercicio 3: Demostrar $n! \notin O(2^n)$

**Método 1**: Límite (Stirling)
$$
\frac{n!}{2^n} \sim \frac{\sqrt{2\pi n}(n/e)^n}{2^n} = \sqrt{2\pi n} \left(\frac{n}{2e}\right)^n \to \infty
$$

**Método 2**: Razón sucesiva
$$
\frac{(n+1)!}{2^{n+1}} \cdot \frac{2^n}{n!} = \frac{n+1}{2} \xrightarrow{n\to\infty} \infty
$$
La secuencia crece sin cota $\Rightarrow$ no acotada por constante.

---

### Ejercicio 4: ¿Es $\log(n!) \in \Theta(n \log n)$?

**Usando Stirling**: $n! \sim \sqrt{2\pi n}(n/e)^n$
$$
\log(n!) \sim \log(\sqrt{2\pi n}) + n\log n - n\log e = \frac{1}{2}\log n + n\log n - n + O(1)
$$
Término dominante: $n \log n$.
**Conclusión**: **Sí**, $\log(n!) \in \Theta(n \log n)$.

---

### Ejercicio 5: Analizar $\sum_{k=1}^n k^2$

**Fórmula exacta**: $\sum_{k=1}^n k^2 = \frac{n(n+1)(2n+1)}{6} = \frac{2n^3 + 3n^2 + n}{6}$

**Asintótico**: $\frac{2}{6}n^3 + \dots = \frac{1}{3}n^3 + \dots \in \Theta(n^3)$.

---

## 10. Ejercicios Adicionales de Práctica

### Ejercicio A: Verdadero/Falso con Justificación
1. $n^2 \in O(n^3)$ → **V** ($c=1, n_0=1$)
2. $n^3 \in O(n^2)$ → **F** (límite $\infty$)
3. $2^{n+1} \in O(2^n)$ → **V** ($2^{n+1} = 2 \cdot 2^n$, $c=2$)
4. $2^{2n} \in O(2^n)$ → **F** ($2^{2n} = 4^n$, crece más)
5. $\log(n!) \in \Theta(n \log n)$ → **V** (Stirling)
6. $n^{\log n} \in O(2^n)$ → **V** (comparar exponentes: $(\log n)^2$ vs $n$)
7. $n! \in O(n^n)$ → **V** ($n! \leq n^n$)

---

### Ejercicio B: Encontrar $c, n_0$ para cada uno
1. $5n^2 + 3n \in O(n^2)$ → $c=8, n_0=1$ ($5n^2+3n \leq 5n^2+3n^2=8n^2$)
2. $n^2 + 100n \in \Omega(n^2)$ → $c=1, n_0=1$ ($n^2+100n \geq n^2$)
3. $\frac{n^2}{2} - 3n \in \Theta(n^2)$ → $c_1=1/4, c_2=1/2, n_0=12$ (para $n\geq 12$, $\frac{n^2}{2}-3n \geq \frac{n^2}{4}$)

---

### Ejercicio C: Demostrar por definición formal
**Probar**: Si $f(n) \in O(g(n))$ y $g(n) \in O(h(n))$, entonces $f(n) \in O(h(n))$.

**Demostración**:
- $f \in O(g) \implies \exists c_1, n_1: f(n) \leq c_1 g(n)\ \forall n \geq n_1$
- $g \in O(h) \implies \exists c_2, n_2: g(n) \leq c_2 h(n)\ \forall n \geq n_2$
- Para $n \geq \max(n_1, n_2)$: $f(n) \leq c_1 g(n) \leq c_1 c_2 h(n)$
- Tomar $c = c_1 c_2$, $n_0 = \max(n_1, n_2)$. ✓

---

## 11. Resumen: Cuándo Usar Cada Notación

| Notación | Uso | Interpretación Algorítmica |
|----------|-----|----------------------------|
| **$O$** | **Cota superior** (garantía peor caso) | "El algoritmo **nunca tarda más** que $c\cdot f(n)$" |
| **$\Omega$** | **Cota inferior** (límite inferior intrínseco) | "El algoritmo **siempre tarda al menos** $c\cdot f(n)$" |
| **$\Theta$** | **Cota ajustada** (caso típico/ajustado) | "El algoritmo tarda **exactamente** $\sim f(n)$" |

> **En análisis de algoritmos**:
> - **Peor caso** $\to$ se expresa en **$O$**
> - **Mejor caso** $\to$ se expresa en **$\Omega$**
> - **Caso medio / exacto** $\to$ se expresa en **$\Theta$** (si coincide)

---

## 12. Tabla de Referencia Rápida: Límites Útiles

| Límite | Valor | Aplicación |
|--------|-------|------------|
| $\lim \frac{\log n}{n^p}$ ($p>0$) | 0 | Log crece menos que cualquier polinomio |
| $\lim \frac{n^p}{c^n}$ ($c>1$) | 0 | Polinómico crece menos que exponencial |
| $\lim \frac{c^n}{n!}$ | 0 | Exponencial crece menos que factorial |
| $\lim \frac{n^k}{n^{\log n}}$ | 0 | Polinómico vs cuasi-polinómico |
| $\lim \frac{n^{\log n}}{c^n}$ | 0 | Cuasi-polinómico vs exponencial |

---

> **Siguiente tema**: [Recurrencias](05-recurrencias.md)