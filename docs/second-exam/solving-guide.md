# Guía Completa de Resolución de Recurrencias No Homogéneas y Complejidad
**Asignatura:** Análisis y Diseño de Algoritmos  
**Profesora:** Dra. Irene Olaya Ayaquica Martínez  

---

## Bloque 1: Recurrencias Lineales No Homogéneas con Coeficientes Constantes

### Ejercicio 1
$$a_n - a_{n-1} = 2n + 3, \quad n \ge 0, \quad a_0 = 5$$

1. **Ecuación homogénea asociada:**
   $$a_n - a_{n-1} = 0 \implies P_h(x) = x - 1$$
   * Raíz homogénea: $r_1 = 1$ con multiplicidad $m = 1$.

2. **Polinomio aniquilador para $f(n) = 2n + 3$:**
   Como $f(n)$ es un polinomio de grado $d = 1$, su aniquilador es $P_f(x) = (x - 1)^{d+1} = (x - 1)^2$.

3. **Polinomio característico total y raíces:**
   $$P(x) = P_h(x) \cdot P_f(x) = (x - 1) \cdot (x - 1)^2 = (x - 1)^3 = 0$$
   * Raíz total: $r = 1$ con multiplicidad $m = 3$.

4. **Solución general propuesta:**
   $$a_n = c_1(1)^n + c_2 n(1)^n + c_3 n^2(1)^n = c_1 + c_2 n + c_3 n^2$$

5. **Cálculo de condiciones iniciales:**
   Calculamos términos con la recurrencia original $a_n = a_{n-1} + 2n + 3$:
   * $a_0 = 5$
   * $a_1 = 5 + 2(1) + 3 = 10$
   * $a_2 = 10 + 2(2) + 3 = 17$

   Evaluamos en $a_n$:
   * $n=0: \quad c_1 = 5$
   * $n=1: \quad 5 + c_2 + c_3 = 10 \implies c_2 + c_3 = 5$
   * $n=2: \quad 5 + 2c_2 + 4c_3 = 17 \implies 2c_2 + 4c_3 = 12 \implies c_2 + 2c_3 = 6$

   Restando las ecuaciones: $c_3 = 1$, $c_2 = 4$.

6. **Solución exacta y orden de complejidad:**
   $$a_n = n^2 + 4n + 5$$
   $$\mathbf{a_n \in O(n^2)}$$

---

### Ejercicio 2
$$a_n - a_{n-1} = 3n^2 - n, \quad n \ge 0, \quad a_0 = 3$$

1. **Ecuación homogénea asociada:**
   $$P_h(x) = x - 1$$

2. **Polinomio aniquilador para $f(n) = 3n^2 - n$:**
   Grado $d = 2 \implies P_f(x) = (x - 1)^{2+1} = (x - 1)^3$.

3. **Polinomio característico total y raíces:**
   $$P(x) = (x - 1)^4 = 0 \implies r = 1 \text{ con multiplicidad } m = 4$$

4. **Solución general propuesta:**
   $$a_n = c_1 + c_2 n + c_3 n^2 + c_4 n^3$$

5. **Cálculo de condiciones iniciales:**
   * $a_0 = 3$
   * $a_1 = 3 + 3(1)^2 - 1 = 5$
   * $a_2 = 5 + 3(2)^2 - 2 = 15$
   * $a_3 = 15 + 3(3)^2 - 3 = 39$

   Sistema de ecuaciones:
   $$\begin{aligned}
   c_1 &= 3 \\
   c_2 + c_3 + c_4 &= 2 \\
   c_2 + 2c_3 + 4c_4 &= 6 \\
   c_2 + 3c_3 + 9c_4 &= 12
   \end{aligned}$$

   Resolviendo: $c_4 = 1$, $c_3 = 1$, $c_2 = 0$, $c_1 = 3$.

6. **Solución exacta y orden de complejidad:**
   $$a_n = n^3 + n^2 + 3$$
   $$\mathbf{a_n \in O(n^3)}$$

---

### Ejercicio 3
$$a_n + 4a_{n-1} + 4a_{n-2} = 7, \quad n \ge 0, \quad a_0 = 1, \ a_1 = 2$$

1. **Ecuación homogénea asociada:**
   $$x^2 + 4x + 4 = 0 \implies P_h(x) = (x + 2)^2 \implies r_1 = -2 \text{ (m=2)}$$

2. **Polinomio aniquilador para $f(n) = 7$:**
   Constante $d = 0 \implies P_f(x) = (x - 1)$.

3. **Polinomio característico total y raíces:**
   $$P(x) = (x + 2)^2(x - 1) = 0 \implies \begin{cases} r_1 = -2 & (m=2) \\ r_2 = 1 & (m=1) \end{cases}$$

4. **Solución general propuesta:**
   $$a_n = c_1(-2)^n + c_2 n(-2)^n + c_3(1)^n$$

5. **Cálculo de condiciones iniciales:**
   * $a_0 = 1, \quad a_1 = 2$
   * $a_2 = 7 - 4a_1 - 4a_0 = 7 - 8 - 4 = -5$

   Sistema de ecuaciones:
   $$\begin{aligned}
   c_1 + c_3 &= 1 \\
   -2c_1 - 2c_2 + c_3 &= 2 \\
   4c_1 + 8c_2 + c_3 &= -5
   \end{aligned}$$

   Resolviendo: $c_1 = \frac{2}{9}$, $c_2 = -\frac{5}{6}$, $c_3 = \frac{7}{9}$.

6. **Solución exacta y orden de complejidad:**
   $$a_n = \frac{2}{9}(-2)^n - \frac{5}{6}n(-2)^n + \frac{7}{9}$$
   $$\mathbf{a_n \in O(n \cdot 2^n)}$$

---

### Ejercicio 4
$$a_n - 3a_{n-1} + 3a_{n-2} - a_{n-3} = 3 + 5n, \quad n \ge 0$$

1. **Ecuación homogénea asociada:**
   $$x^3 - 3x^2 + 3x - 1 = 0 \implies P_h(x) = (x - 1)^3 \implies r_1 = 1 \text{ (m=3)}$$

2. **Polinomio aniquilador para $f(n) = 3 + 5n$:**
   Grado $d = 1 \implies P_f(x) = (x - 1)^2$.

3. **Polinomio característico total y raíces:**
   $$P(x) = (x - 1)^3 \cdot (x - 1)^2 = (x - 1)^5 = 0 \implies r = 1 \text{ (m=5)}$$

4. **Solución general propuesta:**
   $$a_n = c_1 + c_2 n + c_3 n^2 + c_4 n^3 + c_5 n^4$$

5. **Orden de complejidad:**
   $$\mathbf{a_n \in O(n^4)}$$

---

### Ejercicio 5
$$a_n = a_{n-1} + 2n - 1, \quad a_1 = 1$$

1. **Reordenando:** $a_n - a_{n-1} = 2n - 1$
2. **Polinomio homogéneo:** $P_h(x) = x - 1$
3. **Aniquilador para $f(n) = 2n - 1$:** $P_f(x) = (x - 1)^2$
4. **Polinomio total:** $P(x) = (x - 1)^3 = 0 \implies r = 1 \text{ (m=3)}$
5. **Solución propuesta:** $a_n = c_1 + c_2 n + c_3 n^2$
6. **Condiciones iniciales:** $a_1 = 1$, $a_2 = 1 + 3 = 4$, $a_3 = 4 + 5 = 9$.
   Resolviendo el sistema se llega a:
   $$a_n = n^2$$
7. **Orden de complejidad:**
   $$\mathbf{a_n \in O(n^2)}$$

---

### Ejercicio 6
$$a_n = a_{n-1} + 3n^2, \quad a_0 = 7$$

1. **Reordenando:** $a_n - a_{n-1} = 3n^2$
2. **Polinomio homogéneo:** $P_h(x) = x - 1$
3. **Aniquilador para $f(n) = 3n^2$:** $P_f(x) = (x - 1)^3$
4. **Polinomio total:** $P(x) = (x - 1)^4 = 0 \implies r = 1 \text{ (m=4)}$
5. **Solución propuesta:** $a_n = c_1 + c_2 n + c_3 n^2 + c_4 n^3$
6. **Orden de complejidad:**
   $$\mathbf{a_n \in O(n^3)}$$

---

### Ejercicio 7
$$a_n = 3a_{n-1} + 5 \cdot 7^n, \quad a_0 = 2$$

1. **Ecuación homogénea asociada:**
   $$a_n - 3a_{n-1} = 0 \implies P_h(x) = x - 3 \implies r_1 = 3 \text{ (m=1)}$$

2. **Polinomio aniquilador para $f(n) = 5 \cdot 7^n$:**
   Para una exponencial $b^n$, el aniquilador es $(x - b)$. Aquí $b = 7 \implies P_f(x) = (x - 7)$.

3. **Polinomio característico total y raíces:**
   $$P(x) = (x - 3)(x - 7) = 0 \implies r_1 = 3, \ r_2 = 7$$

4. **Solución general propuesta:**
   $$a_n = c_1(3)^n + c_2(7)^n$$

5. **Cálculo de condiciones iniciales:**
   * $a_0 = 2$
   * $a_1 = 3(2) + 5(7)^1 = 6 + 35 = 41$

   Sistema de ecuaciones:
   $$\begin{aligned}
   c_1 + c_2 &= 2 \\
   3c_1 + 7c_2 &= 41
   \end{aligned}$$

   Multiplicando la primera por 3: $3c_1 + 3c_2 = 6$.  
   Restando: $4c_2 = 35 \implies c_2 = \frac{35}{4}$.  
   Luego: $c_1 = 2 - \frac{35}{4} = -\frac{27}{4}$.

6. **Solución exacta y orden de complejidad:**
   $$a_n = -\frac{27}{4}(3)^n + \frac{35}{4}(7)^n$$
   $$\mathbf{a_n \in O(7^n)}$$

---

### Ejercicio 8
$$a_n = 3a_{n-1} - 4a_{n-3} + n^2, \quad a_0 = 11, \ a_1 = 1, \ a_2 = -1$$

1. **Ecuación homogénea asociada:**
   $$a_n - 3a_{n-1} + 4a_{n-3} = 0 \implies P_h(x) = x^3 - 3x^2 + 4 = (x + 1)(x - 2)^2$$
   * Raíces homogéneas: $r_1 = -1 \text{ (m=1)}$, $r_2 = 2 \text{ (m=2)}$.

2. **Polinomio aniquilador para $f(n) = n^2$:**
   $P_f(x) = (x - 1)^3$.

3. **Polinomio característico total y raíces:**
   $$P(x) = (x + 1)(x - 2)^2(x - 1)^3 = 0$$

4. **Solución general propuesta:**
   $$a_n = c_1(-1)^n + c_2(2)^n + c_3 n(2)^n + c_4 + c_5 n + c_6 n^2$$

5. **Orden de complejidad:**
   La raíz de mayor magnitud es $r = 2$ con un factor multiplicativo $n$:
   $$\mathbf{a_n \in O(n \cdot 2^n)}$$

---

### Ejercicio 9
$$a_n = 2a_{n-1} - a_{n-2} + 1, \quad a_1 = 2, \ a_2 = 3$$

1. **Reordenando:** $a_n - 2a_{n-1} + a_{n-2} = 1$
2. **Polinomio homogéneo:** $P_h(x) = x^2 - 2x + 1 = (x - 1)^2 \implies r_1 = 1 \text{ (m=2)}$
3. **Aniquilador para $f(n) = 1$:** $P_f(x) = (x - 1)$
4. **Polinomio total:** $P(x) = (x - 1)^3 = 0 \implies r = 1 \text{ (m=3)}$
5. **Solución propuesta:** $a_n = c_1 + c_2 n + c_3 n^2$
6. **Orden de complejidad:**
   $$\mathbf{a_n \in O(n^2)}$$

---

### Ejercicio 10
$$a_n = 3a_{n-1} - 2a_{n-2} + 5 \cdot 2^n, \quad a_0 = 2, \ a_1 = 4$$

1. **Polinomio homogéneo:** $P_h(x) = x^2 - 3x + 2 = (x - 1)(x - 2) \implies r_1 = 1, r_2 = 2$
2. **Aniquilador para $f(n) = 5 \cdot 2^n$:** $P_f(x) = (x - 2)$
3. **Polinomio total:** $P(x) = (x - 1)(x - 2)^2 = 0 \implies r_1 = 1 \text{ (m=1)}, r_2 = 2 \text{ (m=2)}$
4. **Solución propuesta:** $a_n = c_1(1)^n + c_2(2)^n + c_3 n(2)^n$
5. **Orden de complejidad:**
   $$\mathbf{a_n \in O(n \cdot 2^n)}$$

---

## Bloque 2: Recurrencias Proporcionales (Teorema Maestro / Cambio de Variable)

Forma general: $T(n) = a T(n/b) + f(n)$

### Teorema Maestro (Referencia):
Se compara $f(n)$ con $n^{\log_b a}$:
1. Si $f(n) \in O(n^{\log_b a - \epsilon})$, entonces $T(n) \in \Theta(n^{\log_b a})$.
2. Si $f(n) \in \Theta(n^{\log_b a})$, entonces $T(n) \in \Theta(n^{\log_b a} \log n)$.
3. Si $f(n) \in \Omega(n^{\log_b a + \epsilon})$, entonces $T(n) \in \Theta(f(n))$.

---

### Ejercicio 11
$$T(n) = 4T\left(\frac{n}{3}\right) + 5, \quad T(1) = 5$$

* **Parámetros:** $a = 4$, $b = 3$, $f(n) = 5 = \Theta(n^0)$.
* **Cálculo de la cota crítica:** $n^{\log_b a} = n^{\log_3 4} \approx n^{1.26}$.
* **Comparación:** Como $f(n) = O(n^{\log_3 4 - 0.26})$, cae en el **Caso 1** del Teorema Maestro.
* **Resultado de complejidad:**
  $$\mathbf{T(n) \in \Theta\left(n^{\log_3 4}\right)}$$

---

### Ejercicio 12
$$T(n) = T\left(\frac{n}{5}\right) + 7, \quad T(1) = 7$$

* **Parámetros:** $a = 1$, $b = 5$, $f(n) = 7 = \Theta(1)$.
* **Cálculo:** $n^{\log_5 1} = n^0 = 1$.
* **Comparación:** $f(n) = \Theta(n^{\log_5 1})$. Cae en el **Caso 2** del Teorema Maestro.
* **Resultado de complejidad:**
  $$\mathbf{T(n) \in \Theta(\log n)}$$

---

### Ejercicio 13
$$T(n) = 2T\left(\frac{n}{5}\right) + 3, \quad T(1) = 0$$

* **Parámetros:** $a = 2$, $b = 5$, $f(n) = 3$.
* **Cálculo:** $n^{\log_5 2} \approx n^{0.43}$.
* **Comparación:** Cae en el **Caso 1**.
* **Resultado de complejidad:**
  $$\mathbf{T(n) \in \Theta\left(n^{\log_5 2}\right)}$$

---

### Ejercicio 14
$$T(n) = 2T\left(\frac{n}{2}\right) + 1, \quad T(1) = 0$$

* **Parámetros:** $a = 2$, $b = 2$, $f(n) = 1$.
* **Cálculo:** $n^{\log_2 2} = n^1 = n$.
* **Comparación:** $f(n) = O(n^{1 - \epsilon})$. Cae en el **Caso 1**.
* **Resultado de complejidad:**
  $$\mathbf{T(n) \in \Theta(n)}$$

---

### Ejercicio 15
$$T(n) = T\left(\frac{n}{3}\right) + 1, \quad T(1) = 1$$

* **Parámetros:** $a = 1$, $b = 3$, $f(n) = 1$.
* **Cálculo:** $n^{\log_3 1} = n^0 = 1$.
* **Comparación:** Cae en el **Caso 2**.
* **Resultado de complejidad:**
  $$\mathbf{T(n) \in \Theta(\log n)}$$

---

### Ejercicio 16
$$T(n) = 2T\left(\frac{n}{3}\right) + 4, \quad T(1) = 1$$

* **Parámetros:** $a = 2$, $b = 3$, $f(n) = 4$.
* **Cálculo:** $n^{\log_3 2} \approx n^{0.631}$.
* **Comparación:** Cae en el **Caso 1**.
* **Resultado de complejidad:**
  $$\mathbf{T(n) \in \Theta\left(n^{\log_3 2}\right)}$$

---

### Ejercicio 17
$$T(n) = T\left(\frac{n}{5}\right) + 3n^2, \quad T(1) = 4$$

* **Parámetros:** $a = 1$, $b = 5$, $f(n) = 3n^2$.
* **Cálculo:** $n^{\log_5 1} = n^0 = 1$.
* **Comparación:** Como $f(n) = \Omega(n^{0 + 2})$, cae en el **Caso 3** del Teorema Maestro.
* **Resultado de complejidad:**
  $$\mathbf{T(n) \in \Theta(n^2)}$$

---

### Ejercicio 18 (Cambio de variable especial)
$$T(n) = 2T(n^{1/2}) + \log n \quad \text{con } n = 2^{2^k}, \quad T(2) = 1$$

1. **Aplicando el cambio de variable dado $n = 2^{2^k}$:**
   $$\log n = \log(2^{2^k}) = 2^k$$
   $$n^{1/2} = (2^{2^k})^{1/2} = 2^{2^{k-1}}$$

2. **Sustituyendo en la función:**
   $$T(2^{2^k}) = 2 T(2^{2^{k-1}}) + 2^k$$

3. **Renombrando $S(k) = T(2^{2^k})$:**
   $$S(k) = 2S(k - 1) + 2^k$$

4. **Resolviendo la recurrencia no homogénea para $S(k)$:**
   * Homogénea: $S(k) - 2S(k-1) = 0 \implies P_h(x) = x - 2$
   * Aniquilador para $f(k) = 2^k$: $P_f(x) = (x - 2)$
   * Polinomio total: $P(x) = (x - 2)^2 = 0 \implies r = 2 \text{ (m=2)}$
   * Solución para $S(k)$: $S(k) = c_1 2^k + c_2 k 2^k$

5. **Regresando a la variable original $n$:**
   Como $2^k = \log n$ y $k = \log_2(\log_2 n)$:
   $$T(n) = c_1 \log n + c_2 (\log n) \log(\log n)$$

6. **Orden de complejidad:**
   $$\mathbf{T(n) \in O(\log n \cdot \log(\log n))}$$

---

### Ejercicio 19
$$T(n) = 5T\left(\frac{n}{2}\right) + (n \log n)^2, \quad n > 1, \quad T(1) = 1$$

* **Parámetros:** $a = 5$, $b = 2$, $f(n) = n^2 \log^2 n$.
* **Cálculo:** $n^{\log_2 5} \approx n^{2.32}$.
* **Comparación:** $f(n) = n^2 \log^2 n = O(n^{2.32 - \epsilon})$ porque $2.32 > 2$. Cae en el **Caso 1**.
* **Resultado de complejidad:**
  $$\mathbf{T(n) \in \Theta\left(n^{\log_2 5}\right)}$$

---

### Ejercicio 20
$$T(n) = \frac{3}{2}T\left(\frac{n}{2}\right) - \frac{1}{2}T\left(\frac{n}{4}\right) - \frac{1}{n}, \quad n > 2, \quad T(1) = 1, \ T(2) = \frac{3}{2}$$

1. **Cambio de variable $n = 2^k$:**
   $$T(2^k) = \frac{3}{2}T(2^{k-1}) - \frac{1}{2}T(2^{k-2}) - 2^{-k}$$

2. **Renombrando $S(k) = T(2^k)$:**
   $$S(k) - \frac{3}{2}S(k - 1) + \frac{1}{2}S(k - 2) = -2^{-k}$$

3. **Multiplicando por 2 para simplificar:**
   $$2S(k) - 3S(k - 1) + S(k - 2) = -2 \cdot 2^{-k}$$

4. **Polinomio homogéneo:**
   $$2x^2 - 3x + 1 = 0 \implies (2x - 1)(x - 1) = 0 \implies r_1 = 1, \ r_2 = \frac{1}{2}$$

5. **Aniquilador para $f(k) = -2(2^{-1})^k = -2\left(\frac{1}{2}\right)^k$:**
   $P_f(x) = \left(x - \frac{1}{2}\right)$.

6. **Polinomio total:**
   $$P(x) = (x - 1)\left(x - \frac{1}{2}\right)^2 = 0 \implies r_1 = 1 \text{ (m=1)}, \ r_2 = \frac{1}{2} \text{ (m=2)}$$

7. **Solución para $S(k)$:**
   $$S(k) = c_1(1)^k + c_2\left(\frac{1}{2}\right)^k + c_3 k\left(\frac{1}{2}\right)^k$$

8. **Regresando a $n = 2^k$ (donde $\left(\frac{1}{2}\right)^k = \frac{1}{n}$):**
   $$T(n) = c_1 + c_2 \frac{1}{n} + c_3 \frac{\log_2 n}{n}$$

9. **Orden de complejidad:**
   $$\mathbf{T(n) \in O(1)}$$