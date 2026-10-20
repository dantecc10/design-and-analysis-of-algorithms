# Ecuaciones de Recurrencia: Métodos de Resolución

## 1. Introducción: ¿Qué es una Recurrencia?

Una **ecuación de recurrencia** define una sucesión $\{t_n\}$ expresando cada término en función de los anteriores:
$$t_n = F(t_{n-1}, t_{n-2}, \dots, t_{n-k})$$

En análisis de algoritmos, surgen al analizar algoritmos **recursivos** (Divide y Vencerás) o iterativos con estructura autoreferencial.

**Ejemplos clásicos**:
- **Fibonacci**: $F_n = F_{n-1} + F_{n-2}$
- **Merge Sort**: $T(n) = 2T(n/2) + n$
- **Torres de Hanoi**: $H(n) = 2H(n-1) + 1$
- **Búsqueda Binaria**: $T(n) = T(n/2) + 1$

---

## 2. Método 1: Suposiciones Inteligentes (4 Etapas)

> **Aplicable cuando**: La recurrencia no es homogénea lineal cte, o cuando $n$ tiene restricciones (potencias de 2).

### 2.1 Las 4 Etapas

1. **Calcular** los primeros valores de la recurrencia (tabla $n$ vs $T(n)$)
2. **Buscar** una regularidad / patrón en los valores
3. **Inventar** una forma general candidata (conjetura)
4. **Demostrar** por **inducción matemática** que la conjetura es correcta

---

### 2.2 Ejemplo Completo: $T(n) = 3T(n/2) + n$, $T(1) = 1$, $n = 2^k$

#### Etapa 1: Calcular valores (restringimos a $n = 2^k$)

| $k$ | $n = 2^k$ | $T(n)$ | Expresión Desplegada |
|-----|-----------|--------|----------------------|
| 0   | 1         | 1      | $1$ |
| 1   | 2         | 5      | $3 \cdot 1 + 2 = 3 + 2$ |
| 2   | 4         | 19     | $3(3+2) + 4 = 3^2 + 3\cdot 2 + 4$ |
| 3   | 8         | 65     | $3(3^2+3\cdot2+4) + 8 = 3^3 + 3^2\cdot2 + 3\cdot4 + 8$ |
| 4   | 16        | 211    | $3^4 + 3^3\cdot2 + 3^2\cdot4 + 3\cdot8 + 16$ |
| 5   | 32        | 665    | $3^5 + 3^4\cdot2 + 3^3\cdot4 + 3^2\cdot8 + 3\cdot16 + 32$ |

#### Etapa 2: Identificar Patrón

Para $n = 2^k$:
$$
T(2^k) = 3^k \cdot \underbrace{1}_{T(1)} + \sum_{i=0}^{k-1} 3^{k-1-i} \cdot 2^{i+1}
$$

Reindexando ($j = k-1-i$):
$$
T(2^k) = 3^k + \sum_{j=0}^{k-1} 3^j \cdot 2^{k-j} = 3^k + 2^k \sum_{j=0}^{k-1} \left(\frac{3}{2}\right)^j
$$

#### Etapa 3: Forma General (Sumatoria Geométrica)

$$
\sum_{j=0}^{k-1} r^j = \frac{r^k - 1}{r - 1},\quad r = \frac{3}{2}
$$

$$
\begin{aligned}
T(2^k) &= 3^k + 2^k \cdot \frac{(3/2)^k - 1}{3/2 - 1} \\
&= 3^k + 2^k \cdot \frac{3^k/2^k - 1}{1/2} \\
&= 3^k + 2 \cdot 2^k \left( \frac{3^k}{2^k} - 1 \right) \\
&= 3^k + 2 \cdot 3^k - 2 \cdot 2^k \\
&= 3 \cdot 3^k - 2 \cdot 2^k \\
&= 3^{k+1} - 2^{k+1}
\end{aligned}
$$

#### Etapa 4: Cambio de Variable $k = \log_2 n$

$$
n = 2^k \implies k = \log_2 n
$$

$$
\begin{aligned}
T(n) &= 3^{\log_2 n + 1} - 2^{\log_2 n + 1} \\
&= 3 \cdot 3^{\log_2 n} - 2 \cdot 2^{\log_2 n}
\end{aligned}
$$

**Propiedad clave**: $a^{\log_b c} = c^{\log_b a}$ (demostración: $\log_b(a^{\log_b c}) = \log_b c \cdot \log_b a = \log_b(c^{\log_b a})$)

Aplicando con $a=3, b=2, c=n$:
$$
3^{\log_2 n} = n^{\log_2 3}
$$

**Solución final**:
$$
\boxed{T(n) = 3 n^{\log_2 3} - 2n}
$$

**Complejidad asintótica**: $\log_2 3 \approx 1.585$, entonces
$$
T(n) \in \Theta(n^{\log_2 3}) \approx \Theta(n^{1.585})
$$

> **Comprobación**: $n=4 (k=2):\ 3\cdot 4^{1.585} - 8 \approx 3\cdot 9.0 - 8 = 19$. ✓

---

### 2.3 Caso General: Master Theorem (Referencia Rápida)

Para recurrencias de la forma $T(n) = aT(n/b) + f(n)$ con $a \geq 1, b > 1$:

| Caso | Condición | Solución |
|------|-----------|----------|
| **1** | $f(n) \in O(n^{\log_b a - \epsilon})$ | $T(n) \in \Theta(n^{\log_b a})$ |
| **2** | $f(n) \in \Theta(n^{\log_b a} \log^k n)$ | $T(n) \in \Theta(n^{\log_b a} \log^{k+1} n)$ |
| **3** | $f(n) \in \Omega(n^{\log_b a + \epsilon})$ y $af(n/b) \leq cf(n)$ | $T(n) \in \Theta(f(n))$ |

*Nuestro ejemplo*: $a=3, b=2, f(n)=n$. $\log_2 3 \approx 1.585$. $f(n)=n \in O(n^{1.585-\epsilon})$ → **Caso 1** → $\Theta(n^{\log_2 3})$. ✓

---

## 3. Recurrencias Homogéneas Lineales con Coeficientes Constantes

### 3.1 Forma General

> **Definición**: Una recurrencia homogénea lineal de orden $k$ con coeficientes constantes:
>
> $$a_0 t_n + a_1 t_{n-1} + a_2 t_{n-2} + \dots + a_k t_{n-k} = 0$$
>
> donde $a_0, a_1, \dots, a_k \in \mathbb{R}$, $a_0 \neq 0$, $a_k \neq 0$.

**Equivalentemente** (forma estándar):
$$t_n = c_1 t_{n-1} + c_2 t_{n-2} + \dots + c_k t_{n-k}$$
con $c_i = -a_i/a_0$.

### 3.2 Condiciones Iniciales

Se necesitan **$k$ valores iniciales** $t_0, t_1, \dots, t_{k-1}$ para determinar la sucesión única.

---

### 3.3 Ecuación Característica

**Ansatz (suposición)**: Buscar soluciones de la forma $t_n = x^n$, $x \in \mathbb{C}$.

Sustituyendo en la recurrencia:
$$a_0 x^n + a_1 x^{n-1} + \dots + a_k x^{n-k} = 0$$

Dividiendo por $x^{n-k}$ ($x \neq 0$):
$$a_0 x^k + a_1 x^{k-1} + \dots + a_k = 0$$

> **Ecuación Característica**: $p(x) = a_0 x^k + a_1 x^{k-1} + \dots + a_k = 0$

> **Polinomio Característico**: $p(x)$

---

### 3.4 Teorema Fundamental: Estructura de la Solución

Sean $r_1, r_2, \dots, r_l$ las **raíces distintas** de $p(x)$ con **multiplicidades** $m_1, m_2, \dots, m_l$ ($\sum m_i = k$).

Entonces la **solución general** es:
$$
\boxed{t_n = \sum_{i=1}^{l} \sum_{j=0}^{m_i-1} c_{ij} n^j r_i^n}
$$

| Tipo de Raíz | Términos en Solución |
|--------------|---------------------|
| Simple ($m=1$) | $c r^n$ |
| Doble ($m=2$) | $c_1 r^n + c_2 n r^n$ |
| Triple ($m=3$) | $c_1 r^n + c_2 n r^n + c_3 n^2 r^n$ |
| Múltiple $m$ | $r^n, n r^n, n^2 r^n, \dots, n^{m-1} r^n$ |

Las $k$ constantes $c_{ij}$ se determinan resolviendo el sistema lineal de $k$ ecuaciones con las $k$ condiciones iniciales.

---

## 4. Caso 1: Raíces Distintas ($m_i = 1\ \forall i$)

### 4.1 Solución General
$$t_n = c_1 r_1^n + c_2 r_2^n + \dots + c_k r_k^n$$

### 4.2 Ejemplo Clásico: Sucesión de Fibonacci

**Recurrencia**: $F_n = F_{n-1} + F_{n-2}$, con $F_0 = 0, F_1 = 1$

**Paso 1**: Forma homogénea
$$F_n - F_{n-1} - F_{n-2} = 0$$

**Paso 2**: Ecuación característica ($x^2 - x - 1 = 0$)
$$x^2 - x - 1 = 0$$

**Paso 3**: Raíces (fórmula cuadrática)
$$
r_{1,2} = \frac{1 \pm \sqrt{1 + 4}}{2} = \frac{1 \pm \sqrt{5}}{2}
$$

$$
\varphi = \frac{1 + \sqrt{5}}{2} \approx 1.618 \quad \text{(Número de Oro)}
$$
$$
\psi = \frac{1 - \sqrt{5}}{2} \approx -0.618
$$

**Paso 4**: Solución general
$$F_n = c_1 \varphi^n + c_2 \psi^n$$

**Paso 5**: Usar condiciones iniciales
$$
\begin{cases}
F_0 = c_1 \varphi^0 + c_2 \psi^0 = c_1 + c_2 = 0 \\
F_1 = c_1 \varphi + c_2 \psi = 1
\end{cases}
$$

**Paso 6**: Resolver sistema $2 \times 2$
De la primera: $c_2 = -c_1$.
Sustituyendo: $c_1 \varphi - c_1 \psi = 1 \implies c_1(\varphi - \psi) = 1$.

$\varphi - \psi = \frac{1+\sqrt{5}}{2} - \frac{1-\sqrt{5}}{2} = \sqrt{5}$.

$$c_1 = \frac{1}{\sqrt{5}},\quad c_2 = -\frac{1}{\sqrt{5}}$$

**Paso 7**: Fórmula de Binet (solución cerrada)
$$\boxed{F_n = \frac{1}{\sqrt{5}} \left( \varphi^n - \psi^n \right) = \frac{1}{\sqrt{5}} \left( \left(\frac{1+\sqrt{5}}{2}\right)^n - \left(\frac{1-\sqrt{5}}{2}\right)^n \right)}$$

**Complejidad**: $|\psi| < 1 \implies \psi^n \to 0$. $F_n \sim \frac{\varphi^n}{\sqrt{5}} \in \Theta(\varphi^n)$.

---

### 4.3 Ejemplo 2: $t_n - 3t_{n-1} - 4t_{n-2} = 0$, $t_0 = 0, t_1 = 5$

**Ecuación característica**: $x^2 - 3x - 4 = 0 = (x+1)(x-4)$

**Raíces**: $r_1 = -1,\ r_2 = 4$ (distintas)

**Solución general**: $t_n = c_1 (-1)^n + c_2 4^n$

**Condiciones iniciales**:
$$
\begin{cases}
t_0 = c_1 + c_2 = 0 \\
t_1 = -c_1 + 4c_2 = 5
\end{cases}
$$

De la primera: $c_1 = -c_2$.
$-(-c_2) + 4c_2 = 5 \implies 5c_2 = 5 \implies c_2 = 1,\ c_1 = -1$.

**Solución**: $\boxed{t_n = 4^n - (-1)^n}$

**Complejidad**: $t_n \sim 4^n \implies t_n \in \Theta(4^n)$.

---

### 4.4 Ejemplo 3: $a_n - 5a_{n-1} - 6a_{n-2} = 0$, $a_0 = 1, a_1 = 3$

**Ecuación característica**: $x^2 - 5x - 6 = (x-6)(x+1) = 0$

**Raíces**: $r_1 = 6,\ r_2 = -1$

**General**: $a_n = c_1 6^n + c_2 (-1)^n$

**Sistema**:
$$
\begin{cases}
c_1 + c_2 = 1 \\
6c_1 - c_2 = 3
\end{cases}
\implies
\begin{cases}
c_1 = \frac{4}{7} \\
c_2 = \frac{3}{7}
\end{cases}
$$

**Solución**: $\boxed{a_n = \frac{4}{7}6^n + \frac{3}{7}(-1)^n \in \Theta(6^n)}$

---

## 5. Caso 2: Raíces Múltiples

### 5.1 Teoría (Demostración Esquemática)

Si $r$ es raíz de multiplicidad $m$ de $p(x)$, entonces $p(x) = (x-r)^m q(x)$.

Se verifica que $t_n = n^j r^n$ satisface la recurrencia para $j = 0, 1, \dots, m-1$:
- $j=0$: $r^n$ (solución base)
- $j=1$: $n r^n$ (derivada respecto a $r$)
- $j=2$: $n^2 r^n$, etc.

**Intuición**: La derivada de la ecuación característica respecto a $x$ genera las soluciones adicionales.

---

### 5.2 Ejemplo 1: $t_n - 5t_{n-1} + 8t_{n-2} - 4t_{n-3} = 0$, $t_0=0, t_1=1, t_2=2$

**Ecuación característica**: $x^3 - 5x^2 + 8x - 4 = 0$

**Factorización**: $(x-1)(x-2)^2 = 0$

**Raíces**: $r_1 = 1\ (m_1=1),\ r_2 = 2\ (m_2=2)$

**Solución general**:
$$t_n = c_1 1^n + c_2 2^n + c_3 n 2^n = c_1 + c_2 2^n + c_3 n 2^n$$

**Sistema ($n=0,1,2$)**:
$$
\begin{cases}
n=0:\ c_1 + c_2 = 0 \\
n=1:\ c_1 + 2c_2 + 2c_3 = 1 \\
n=2:\ c_1 + 4c_2 + 8c_3 = 2
\end{cases}
$$

**Resolución**:
1. $c_1 = -c_2$
2. $-c_2 + 2c_2 + 2c_3 = 1 \implies c_2 + 2c_3 = 1$
3. $-c_2 + 4c_2 + 8c_3 = 2 \implies 3c_2 + 8c_3 = 2$

De (2): $c_2 = 1 - 2c_3$.
Sustituyendo en (3): $3(1-2c_3) + 8c_3 = 2 \implies 3 - 6c_3 + 8c_3 = 2 \implies 2c_3 = -1 \implies c_3 = -\frac{1}{2}$.

$c_2 = 1 - 2(-\frac{1}{2}) = 2$.
$c_1 = -2$.

**Solución**: $\boxed{t_n = 2^{n+1} - n 2^{n-1} - 2}$

**Complejidad**: Término dominante $n 2^n \implies t_n \in \Theta(n 2^n)$.

---

### 5.3 Ejemplo 2: $a_n - 6a_{n-1} + 9a_{n-2} = 0$, $a_0 = 5, a_1 = 12$

**Ecuación característica**: $x^2 - 6x + 9 = (x-3)^2 = 0$

**Raíz**: $r = 3$ con multiplicidad $m = 2$

**Solución general**: $a_n = c_1 3^n + c_2 n 3^n$

**Sistema**:
$$
\begin{cases}
n=0:\ c_1 = 5 \\
n=1:\ 3c_1 + 3c_2 = 12 \implies 3(5) + 3c_2 = 12 \implies 15 + 3c_2 = 12 \implies c_2 = -1
\end{cases}
$$

**Solución**: $\boxed{a_n = 5 \cdot 3^n - n \cdot 3^n = (5-n)3^n}$

**Complejidad**: $a_n \sim -n 3^n \implies a_n \in \Theta(n 3^n)$.

---

## 6. Ejercicios de las Diapositivas (Resueltos)

### Ejercicio 3.a: $a_n = 7a_{n-1} - 10a_{n-2}$, $n \geq 2$, $a_0 = 2, a_1 = 1$

**Paso 1**: Forma homogénea
$$a_n - 7a_{n-1} + 10a_{n-2} = 0$$

**Paso 2**: Ecuación característica
$$x^2 - 7x + 10 = 0 \implies (x-5)(x-2) = 0$$

**Paso 3**: Raíces distintas: $r_1 = 5, r_2 = 2$

**Paso 4**: General
$$a_n = c_1 5^n + c_2 2^n$$

**Paso 5**: Condiciones iniciales
$$
\begin{cases}
a_0 = c_1 + c_2 = 2 \\
a_1 = 5c_1 + 2c_2 = 1
\end{cases}
$$

**Paso 6**: Resolver
$c_2 = 2 - c_1$.
$5c_1 + 2(2-c_1) = 1 \implies 5c_1 + 4 - 2c_1 = 1 \implies 3c_1 = -3 \implies c_1 = -1$.
$c_2 = 3$.

**Solución**: $\boxed{a_n = 3 \cdot 2^n - 5^n}$

**Complejidad**: Término dominante $-5^n \implies a_n \in \Theta(5^n)$.

---

### Ejercicio 3.b: $a_n = 6a_{n-1} - 11a_{n-2} + 6a_{n-3}$, $n \geq 3$, $a_0 = 2, a_1 = 5, a_2 = 15$

**Paso 1**: Forma homogénea
$$a_n - 6a_{n-1} + 11a_{n-2} - 6a_{n-3} = 0$$

**Paso 2**: Ecuación característica
$$x^3 - 6x^2 + 11x - 6 = 0$$

**Paso 3**: Buscar raíces racionales (divisores de 6: $\pm 1, \pm 2, \pm 3, \pm 6$)
$x=1:\ 1 - 6 + 11 - 6 = 0$ ✓ → $(x-1)$ factor.
División sintética: $(x-1)(x^2 - 5x + 6) = (x-1)(x-2)(x-3)$

**Raíces**: $r_1 = 1,\ r_2 = 2,\ r_3 = 3$ (todas simples)

**Paso 4**: General
$$a_n = c_1 1^n + c_2 2^n + c_3 3^n = c_1 + c_2 2^n + c_3 3^n$$

**Paso 5**: Sistema
$$
\begin{cases}
n=0:\ c_1 + c_2 + c_3 = 2 \\
n=1:\ c_1 + 2c_2 + 3c_3 = 5 \\
n=2:\ c_1 + 4c_2 + 9c_3 = 15
\end{cases}
$$

**Paso 6**: Resolver
Restar (1) de (2): $c_2 + 2c_3 = 3$  → (A)
Restar (2) de (3): $2c_2 + 6c_3 = 10 \implies c_2 + 3c_3 = 5$ → (B)

(B) - (A): $c_3 = 2$.
De (A): $c_2 + 4 = 3 \implies c_2 = -1$.
De (1): $c_1 - 1 + 2 = 2 \implies c_1 = 1$.

**Solución**: $\boxed{a_n = 1 - 2^n + 2 \cdot 3^n}$

**Complejidad**: $2 \cdot 3^n$ domina $\implies a_n \in \Theta(3^n)$.

---

## 7. Ejercicios Adicionales de Práctica

### Ejercicio 1: Recurrencia No Homogénea Simple
Resolver: $t_n = 2t_{n-1} + 1$, $t_0 = 0$

**Método**: Suposiciones inteligentes / Iteración
$$
\begin{aligned}
t_1 &= 2\cdot0 + 1 = 1 \\
t_2 &= 2\cdot1 + 1 = 3 \\
t_3 &= 2\cdot3 + 1 = 7 \\
t_4 &= 2\cdot7 + 1 = 15 \\
&\vdots \\
t_n &= 2^n - 1
\end{aligned}
$$

**Verificación por inducción**:
- Base $n=0$: $2^0 - 1 = 0 = t_0$ ✓
- Paso: $t_{n+1} = 2t_n + 1 = 2(2^n - 1) + 1 = 2^{n+1} - 2 + 1 = 2^{n+1} - 1$ ✓

$\boxed{t_n = 2^n - 1 \in \Theta(2^n)}$

---

### Ejercicio 2: Recurrencia con Raíces Complejas
Resolver: $t_n = 2t_{n-1} - 2t_{n-2}$, $t_0 = 1, t_1 = 1$

**Ecuación característica**: $x^2 - 2x + 2 = 0$
Raíces: $x = \frac{2 \pm \sqrt{4-8}}{2} = 1 \pm i$

**Forma polar**: $1+i = \sqrt{2} e^{i\pi/4}$, $1-i = \sqrt{2} e^{-i\pi/4}$

**Solución general** (reales): $t_n = (\sqrt{2})^n (c_1 \cos(n\pi/4) + c_2 \sin(n\pi/4))$

**Condiciones**:
$t_0 = c_1 = 1$
$t_1 = \sqrt{2}(c_1 \cos(\pi/4) + c_2 \sin(\pi/4)) = \sqrt{2}(1\cdot\frac{\sqrt{2}}{2} + c_2\frac{\sqrt{2}}{2}) = 1 + c_2 = 1 \implies c_2 = 0$

**Solución**: $t_n = (\sqrt{2})^n \cos(n\pi/4)$

**Complejidad**: $|t_n| \leq (\sqrt{2})^n \implies t_n \in O((\sqrt{2})^n) = O(2^{n/2})$

---

### Ejercicio 3: Torres de Hanoi
$H(n) = 2H(n-1) + 1$, $H(1) = 1$

**Suposiciones inteligentes**:
$H(1)=1$
$H(2)=2\cdot1+1=3$
$H(3)=2\cdot3+1=7$
$H(4)=15$
Patrón: $H(n) = 2^n - 1$

**Inducción**: Base $n=1$: $2^1-1=1$ ✓.
$H(n+1) = 2(2^n-1)+1 = 2^{n+1}-1$ ✓.

$\boxed{H(n) = 2^n - 1 \in \Theta(2^n)}$

---

### Ejercicio 4: Búsqueda Binaria
$T(n) = T(n/2) + 1$, $T(1) = 1$, $n = 2^k$

**Cambio variable**: $n = 2^k \implies T(2^k) = T(2^{k-1}) + 1$
Definir $S(k) = T(2^k)$: $S(k) = S(k-1) + 1$, $S(0) = 1$

**Solución**: $S(k) = k + 1 \implies T(n) = \log_2 n + 1 \in \Theta(\log n)$

---

### Ejercicio 5: Merge Sort
$T(n) = 2T(n/2) + n$, $T(1) = 1$, $n = 2^k$

**Suposiciones inteligentes**:
$T(2^k) = 2T(2^{k-1}) + 2^k$
$= 2[2T(2^{k-2}) + 2^{k-1}] + 2^k = 2^2 T(2^{k-2}) + 2\cdot2^{k-1} + 2^k = 2^2 T(2^{k-2}) + 2^k + 2^k$
$= 2^k T(1) + k \cdot 2^k = 2^k + k 2^k = 2^k(1+k)$
$k = \log_2 n \implies T(n) = n(1 + \log_2 n) = n\log_2 n + n$

$\boxed{T(n) \in \Theta(n \log n)}$

---

### Ejercicio 6: Recurrencia Mixta
Resolver: $a_n = 4a_{n-1} - 4a_{n-2} + n$, $a_0 = 1, a_1 = 3$

**Parte homogénea**: $x^2 - 4x + 4 = (x-2)^2 \implies a_n^{(h)} = c_1 2^n + c_2 n 2^n$

**Parte particular**: Probar $a_n^{(p)} = An + B$ (polinomio grado 1)
$An+B = 4(A(n-1)+B) - 4(A(n-2)+B) + n$
$= 4An - 4A + 4B - 4An + 8A - 4B + n$
$= 4A + n$

Igualando: $An+B = n + 4A \implies A=1, B=4$.

**Solución general**: $a_n = c_1 2^n + c_2 n 2^n + n + 4$

**Condiciones**:
$a_0 = c_1 + 4 = 1 \implies c_1 = -3$
$a_1 = -3\cdot2 + c_2\cdot2 + 1 + 4 = -6 + 2c_2 + 5 = 2c_2 - 1 = 3 \implies c_2 = 2$

**Solución**: $\boxed{a_n = -3\cdot 2^n + 2n\cdot 2^n + n + 4 = (2n-3)2^n + n + 4 \in \Theta(n 2^n)}$

---

### Ejercicio 7: Recurrencia con División No Entera
$T(n) = T(\lfloor n/2 \rfloor) + T(\lceil n/2 \rceil) + n$, $T(1) = 1$

Para $n=2^k$, $\lfloor n/2 \rfloor = \lceil n/2 \rceil = 2^{k-1}$:
$T(2^k) = 2T(2^{k-1}) + 2^k$ → Igual a Merge Sort → $T(n) = \Theta(n \log n)$

Para $n$ general, por monotonía y suavidad: $T(n) \in \Theta(n \log n)$.

---

## 8. Resumen: Guía de Decisión para Resolver Recurrencias

| Tipo de Recurrencia | Método Recomendado |
|---------------------|-------------------|
| $T(n) = aT(n/b) + f(n)$ | Master Theorem / Árbol de recursión / Suposiciones inteligentes |
| Lineal homogénea cte (orden $k$) | Ecuación característica |
| Lineal no homogénea cte | Homogénea + Parte particular (método coeficientes indeterminados) |
| $T(n) = T(n-1) + f(n)$ | Telescopio / Suma directa |
| $T(n) = T(n/2) + f(n)$ | Cambio variable $n=2^k$ + Suposiciones inteligentes |
| Variable separación no limpia | Sustitución / Inducción / Akra-Bazzi (avanzado) |

---

## 9. Tabla de Referencia: Raíces → Complejidad

| Raíces Características | Forma Solución | Complejidad Típica |
|------------------------|----------------|-------------------|
| $r_1, r_2, \dots, r_k$ (distintas, reales) | $\sum c_i r_i^n$ | $\Theta(\max |r_i|^n)$ |
| $r$ (real, mult. $m$) | $\sum_{j=0}^{m-1} c_j n^j r^n$ | $\Theta(n^{m-1} |r|^n)$ |
| $\alpha \pm i\beta$ (complejas) | $\rho^n (c_1 \cos n\theta + c_2 \sin n\theta)$ | $\Theta(\rho^n)$ |
| $1, 1, \dots, 1$ (m veces) | Polinomio grado $m-1$ | $\Theta(n^{m-1})$ |

---

## 10. Comprobaciones Finales Rápidas

Para cualquier solución candidata $t_n$:
1. **Verificar condiciones iniciales**: ¿$t_0, t_1, \dots$ coinciden?
2. **Verificar recurrencia**: ¿$t_n - c_1 t_{n-1} - \dots = 0$ para $n \geq k$?
3. **Verificar asintótico**: ¿El término dominante coincide con Master Theorem / intuición?

---

> **Siguiente tema**: [Ejercicios Integrados de Práctica](06-ejercicios-practica.md)