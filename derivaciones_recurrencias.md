# Desarrollos Detallados: Recurrencias Homogéneas

Este documento contiene el desglose paso a paso de las recurrencias homogéneas del repositorio.

## Fundamento Teórico: La Ecuación Característica

Para una recurrencia lineal homogénea de la forma $a_n = c_1 a_{n-1} + c_2 a_{n-2} + \dots + c_k a_{n-k}$, suponemos una solución de la forma $a_n = r^n$.

Al sustituir en la recurrencia:
$$r^n = c_1 r^{n-1} + c_2 r^{n-2} + \dots + c_k r^{n-k}$$

Dividiendo entre $r^{n-k}$:
$$r^k = c_1 r^{k-1} + c_2 r^{k-2} + \dots + c_k$$
$$r^k - c_1 r^{k-1} - c_2 r^{k-2} - \dots - c_k = 0$$

Este es el **Polinomio Característico**. Las raíces $r$ de este polinomio nos dan las bases de las soluciones exponenciales.

---

## Ejercicios Resueltos

### Ejercicio 1: $a_n = 7a_{n-1} - 10a_{n-2}$
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

### Ejercicio 2: $a_n = 2a_{n-1} - a_{n-2}$
*Condiciones iniciales: $a_0 = 4, a_1 = 1$*

**1. Obtención de la ecuación característica:**
Sustituimos $a_n = r^n$:
$$r^n = 2r^{n-1} - r^{n-2}$$
Dividimos por $r^{n-2}$:
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

### Ejercicio 3: $a_n = 6a_{n-1} - 11a_{n-2} + 6a_{n-3}$
*Condiciones iniciales: $a_0 = 2, a_1 = 5, a_2 = 15$*

**1. Obtención de la ecuación característica:**
Sustituimos $a_n = r^n$:
$$r^n = 6r^{n-1} - 11r^{n-2} + 6r^{n-3}$$
Dividimos por $r^{n-3}$:
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
