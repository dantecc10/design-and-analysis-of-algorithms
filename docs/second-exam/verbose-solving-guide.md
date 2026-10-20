# Guía Completa de Resolución de Recurrencias No Homogéneas y Complejidad
**Asignatura:** Análisis y Diseño de Algoritmos  
**Profesora:** Dra. Irene Olaya Ayaquica Martínez  
**Material de Estudio Detallado Paso a Paso**

---

## Bloque 1: Recurrencias Lineales No Homogéneas con Coeficientes Constantes

---

### Ejercicio 1

$$a_n - a_{n-1} = 2n + 3, \quad n \ge 0, \quad a_0 = 5$$

#### **Paso 1: Identificar y resolver la parte homogénea $P_h(x)$**
Primero, ignoramos temporalmente la parte no homogénea $f(n) = 2n + 3$ e igualamos el lado izquierdo a cero para analizar el comportamiento homogéneo de la recurrencia:
$$a_n - a_{n-1} = 0$$

* **Determinación del orden ($m$):** El índice más alto es $n$ y el más bajo es $n-1$. La distancia es $n - (n-1) = 1$. Por lo tanto, es de orden $m = 1$.
* **Polinomio característico homogéneo:** Reemplazamos los términos por potencias de $x$:
  $$P_h(x) = x - 1 = 0$$
* **Raíz homogénea:** $r_1 = 1$ con multiplicidad $m_1 = 1$.

#### **Paso 2: Encontrar el polinomio aniquilador $P_f(x)$ para $f(n)$**
Analizamos la función no homogénea $f(n) = 2n + 3$:
* La función es un polinomio en $n$ de **grado $d = 1$** (ya que el exponente máximo de $n$ es $1$).
* La regla del aniquilador para un polinomio de grado $d$ establece que su operador aniquilador es de la forma:
  $$P_f(x) = (x - 1)^{d + 1}$$
* Sustituyendo $d = 1$:
  $$P_f(x) = (x - 1)^{1 + 1} = (x - 1)^2$$

#### **Paso 3: Construir el polinomio característico total $P(x)$ y determinar multiplicidades**
Multiplicamos el polinomio homogéneo $P_h(x)$ por el polinomio aniquilador $P_f(x)$ para convertir la ecuación en una homogénea equivalente de mayor orden:
$$P(x) = P_h(x) \cdot P_f(x) = (x - 1) \cdot (x - 1)^2 = (x - 1)^3 = 0$$

* Obtenemos una única raíz $r = 1$ que se repite $3$ veces.
* Por lo tanto, la raíz es $r = 1$ con **multiplicidad total $m = 3$**.

#### **Paso 4: Formular la plantilla de la solución general $a_n$**
Aplicamos la regla de multiplicidad para la raíz $r = 1$ repetida 3 veces (multiplicando por $n^0, n^1, n^2$):
$$a_n = c_1(1)^n + c_2 n (1)^n + c_3 n^2 (1)^n$$
Como $(1)^n = 1$ para cualquier $n$:
$$a_n = c_1 + c_2 n + c_3 n^2$$

#### **Paso 5: Calcular las constantes $c_1, c_2, c_3$ usando las condiciones iniciales**
Como tenemos 3 constantes desconocidas, necesitamos un sistema de 3 ecuaciones. Generamos los primeros 3 términos de la secuencia usando la ecuación de recurrencia original $a_n = a_{n-1} + 2n + 3$:
1. Para $n = 0$: $a_0 = 5$ (dado por el enunciado).
2. Para $n = 1$: $a_1 = a_0 + 2(1) + 3 = 5 + 2 + 3 = 10$.
3. Para $n = 2$: $a_2 = a_1 + 2(2) + 3 = 10 + 4 + 3 = 17$.

Ahora evaluamos nuestra plantilla $a_n = c_1 + c_2 n + c_3 n^2$ en $n = 0, 1, 2$:

* **Para $n = 0$ ($a_0 = 5$):**
  $$c_1 + c_2(0) + c_3(0)^2 = 5 \implies \mathbf{c_1 = 5}$$

* **Para $n = 1$ ($a_1 = 10$):**
  $$c_1 + c_2(1) + c_3(1)^2 = 10$$
  Sustituyendo $c_1 = 5$:
  $$5 + c_2 + c_3 = 10 \implies \mathbf{c_2 + c_3 = 5} \quad \text{--- (Ecuación A)}$$

* **Para $n = 2$ ($a_2 = 17$):**
  $$c_1 + c_2(2) + c_3(2)^2 = 17$$
  Sustituyendo $c_1 = 5$:
  $$5 + 2c_2 + 4c_3 = 17 \implies 2c_2 + 4c_3 = 12 \implies \mathbf{c_2 + 2c_3 = 6} \quad \text{--- (Ecuación B)}$$

**Resolviendo el sistema $2 \times 2$:**
Restamos la Ecuación B menos la Ecuación A:
$$(c_2 + 2c_3) - (c_2 + c_3) = 6 - 5 \implies \mathbf{c_3 = 1}$$

Sustituimos $c_3 = 1$ en la Ecuación A:
$$c_2 + 1 = 5 \implies \mathbf{c_2 = 4}$$

#### **Paso 6: Escribir la solución exacta y determinar el orden de complejidad**
Sustituimos $c_1 = 5$, $c_2 = 4$ y $c_3 = 1$ en la plantilla:
$$\mathbf{a_n = n^2 + 4n + 5}$$

Para la complejidad asintótica $O(g(n))$, tomamos el término dominante de la solución exacta (el término cuadrático $n^2$):
$$\mathbf{a_n \in O(n^2)}$$

---

### Ejercicio 2

$$a_n - a_{n-1} = 3n^2 - n, \quad n \ge 0, \quad a_0 = 3$$

#### **Paso 1: Identificar y resolver la parte homogénea $P_h(x)$**
Igualamos el lado izquierdo a cero:
$$a_n - a_{n-1} = 0$$
* **Orden:** $n - (n-1) = 1$.
* **Polinomio homogéneo:** $P_h(x) = x - 1 = 0$.
* **Raíz homogénea:** $r_1 = 1$ con multiplicidad $m_1 = 1$.

#### **Paso 2: Encontrar el polinomio aniquilador $P_f(x)$ para $f(n)$**
Analizamos $f(n) = 3n^2 - n$:
* Es un polinomio de **grado $d = 2$** (por el término $3n^2$).
* Aplicamos la fórmula del aniquilador para polinomios $(x - 1)^{d+1}$:
  $$P_f(x) = (x - 1)^{2 + 1} = (x - 1)^3$$

#### **Paso 3: Construir el polinomio característico total $P(x)$ y determinar multiplicidades**
Multiplicamos la parte homogénea por el aniquilador:
$$P(x) = P_h(x) \cdot P_f(x) = (x - 1) \cdot (x - 1)^3 = (x - 1)^4 = 0$$
* Obtenemos la raíz $r = 1$ repetida 4 veces.
* Multiplicidad total: $m = 4$.

#### **Paso 4: Formular la plantilla de la solución general $a_n$**
Multiplicamos por potencias sucesivas de $n$ ($1, n, n^2, n^3$):
$$a_n = c_1(1)^n + c_2 n (1)^n + c_3 n^2 (1)^n + c_4 n^3 (1)^n$$
$$\mathbf{a_n = c_1 + c_2 n + c_3 n^2 + c_4 n^3}$$

#### **Paso 5: Calcular las constantes $c_1, c_2, c_3, c_4$ usando condiciones iniciales**
Necesitamos 4 ecuaciones. Calculamos $a_0, a_1, a_2, a_3$ mediante $a_n = a_{n-1} + 3n^2 - n$:
1. $a_0 = 3$
2. $a_1 = a_0 + 3(1)^2 - (1) = 3 + 3 - 1 = 5$
3. $a_2 = a_1 + 3(2)^2 - (2) = 5 + 12 - 2 = 15$
4. $a_3 = a_2 + 3(3)^2 - (3) = 15 + 27 - 3 = 39$

Evaluamos $a_n = c_1 + c_2 n + c_3 n^2 + c_4 n^3$ en $n = 0, 1, 2, 3$:

* **Para $n = 0$ ($a_0 = 3$):**
  $$c_1 = 3$$

* **Para $n = 1$ ($a_1 = 5$):**
  $$3 + c_2(1) + c_3(1)^2 + c_4(1)^3 = 5 \implies \mathbf{c_2 + c_3 + c_4 = 2} \quad \text{--- (Ecuación A)}$$

* **Para $n = 2$ ($a_2 = 15$):**
  $$3 + c_2(2) + c_3(4) + c_4(8) = 15 \implies 2c_2 + 4c_3 + 8c_4 = 12 \implies \mathbf{c_2 + 2c_3 + 4c_4 = 6} \quad \text{--- (Ecuación B)}$$

* **Para $n = 3$ ($a_3 = 39$):**
  $$3 + c_2(3) + c_3(9) + c_4(27) = 39 \implies 3c_2 + 9c_3 + 27c_4 = 36 \implies \mathbf{c_2 + 3c_3 + 9c_4 = 12} \quad \text{--- (Ecuación C)}$$

**Resolución del sistema $3 \times 3$:**
1. Restamos Ecuación B $-$ Ecuación A:
   $$(c_2 + 2c_3 + 4c_4) - (c_2 + c_3 + c_4) = 6 - 2 \implies \mathbf{c_3 + 3c_4 = 4} \quad \text{--- (Ecuación D)}$$

2. Restamos Ecuación C $-$ Ecuación B:
   $$(c_2 + 3c_3 + 9c_4) - (c_2 + 2c_3 + 4c_4) = 12 - 6 \implies \mathbf{c_3 + 5c_4 = 6} \quad \text{--- (Ecuación E)}$$

3. Restamos Ecuación E $-$ Ecuación D:
   $$(c_3 + 5c_4) - (c_3 + 3c_4) = 6 - 4 \implies 2c_4 = 2 \implies \mathbf{c_4 = 1}$$

4. Sustituimos $c_4 = 1$ en la Ecuación D:
   $$c_3 + 3(1) = 4 \implies \mathbf{c_3 = 1}$$

5. Sustituimos $c_3 = 1$ y $c_4 = 1$ en la Ecuación A:
   $$c_2 + 1 + 1 = 2 \implies \mathbf{c_2 = 0}$$

#### **Paso 6: Solución exacta y complejidad**
Sustituyendo $c_1 = 3, c_2 = 0, c_3 = 1, c_4 = 1$:
$$\mathbf{a_n = n^3 + n^2 + 3}$$

Dominante cúbico $n^3$:
$$\mathbf{a_n \in O(n^3)}$$

---

### Ejercicio 3

$$a_n + 4a_{n-1} + 4a_{n-2} = 7, \quad n \ge 0, \quad a_0 = 1, \ a_1 = 2$$

#### **Paso 1: Identificar y resolver la parte homogénea $P_h(x)$**
Igualamos el lado izquierdo a cero:
$$a_n + 4a_{n-1} + 4a_{n-2} = 0$$
* **Orden:** $n - (n-2) = 2$.
* **Polinomio homogéneo:** $P_h(x) = x^2 + 4x + 4 = 0$.
* Factorizamos como un trinomio cuadrado perfecto: $(x + 2)^2 = 0$.
* **Raíz homogénea:** $r_1 = -2$ con multiplicidad $m_1 = 2$.

#### **Paso 2: Encontrar el polinomio aniquilador $P_f(x)$ para $f(n)$**
Analizamos la función constante $f(n) = 7$:
* Es un polinomio de **grado $d = 0$** (término independiente).
* Su aniquilador es $(x - 1)^{0 + 1} = (x - 1)$.
  $$P_f(x) = x - 1$$

#### **Paso 3: Construir el polinomio característico total $P(x)$**
Multiplicamos la parte homogénea por el aniquilador:
$$P(x) = P_h(x) \cdot P_f(x) = (x + 2)^2 (x - 1) = 0$$
* Raíz $r_1 = -2$ con multiplicidad $m_1 = 2$.
* Raíz $r_2 = 1$ con multiplicidad $m_2 = 1$.

#### **Paso 4: Formular la plantilla de la solución general $a_n$**
Escribimos los términos correspondientes a cada raíz:
$$a_n = c_1(-2)^n + c_2 n (-2)^n + c_3(1)^n$$
$$\mathbf{a_n = c_1(-2)^n + c_2 n (-2)^n + c_3}$$

#### **Paso 5: Calcular las constantes $c_1, c_2, c_3$**
Necesitamos 3 ecuaciones. Obtenemos $a_2$ con la ecuación original $a_n = 7 - 4a_{n-1} - 4a_{n-2}$:
1. $a_0 = 1$
2. $a_1 = 2$
3. $a_2 = 7 - 4(2) - 4(1) = 7 - 8 - 4 = -5$

Evaluamos $a_n$ en $n = 0, 1, 2$:

* **Para $n = 0$ ($a_0 = 1$):**
  $$c_1(-2)^0 + c_2(0)(-2)^0 + c_3(1)^0 = 1 \implies \mathbf{c_1 + c_3 = 1} \quad \text{--- (Ecuación 1)}$$

* **Para $n = 1$ ($a_1 = 2$):**
  $$c_1(-2)^1 + c_2(1)(-2)^1 + c_3(1)^1 = 2 \implies \mathbf{-2c_1 - 2c_2 + c_3 = 2} \quad \text{--- (Ecuación 2)}$$

* **Para $n = 2$ ($a_2 = -5$):**
  $$c_1(-2)^2 + c_2(2)(-2)^2 + c_3(1)^2 = -5 \implies \mathbf{4c_1 + 8c_2 + c_3 = -5} \quad \text{--- (Ecuación 3)}$$

**Resolviendo el sistema $3 \times 3$:**
De la Ecuación 1 despejamos $c_3 = 1 - c_1$. Sustituimos en la 2 y en la 3:

* En Ecuación 2:
  $$-2c_1 - 2c_2 + (1 - c_1) = 2 \implies -3c_1 - 2c_2 = 1 \implies \mathbf{3c_1 + 2c_2 = -1} \quad \text{--- (Ecuación 4)}$$

* En Ecuación 3:
  $$4c_1 + 8c_2 + (1 - c_1) = -5 \implies 3c_1 + 8c_2 = -6 \quad \text{--- (Ecuación 5)}$$

* Restamos Ecuación 5 $-$ Ecuación 4:
  $$(3c_1 + 8c_2) - (3c_1 + 2c_2) = -6 - (-1) \implies 6c_2 = -5 \implies \mathbf{c_2 = -\frac{5}{6}}$$

* Sustituimos $c_2 = -\frac{5}{6}$ en Ecuación 4:
  $$3c_1 + 2\left(-\frac{5}{6}\right) = -1 \implies 3c_1 - \frac{5}{3} = -1 \implies 3c_1 = \frac{2}{3} \implies \mathbf{c_1 = \frac{2}{9}}$$

* Calculamos $c_3$:
  $$c_3 = 1 - \frac{2}{9} \implies \mathbf{c_3 = \frac{7}{9}}$$

#### **Paso 6: Solución exacta y complejidad**
$$\mathbf{a_n = \frac{2}{9}(-2)^n - \frac{5}{6}n(-2)^n + \frac{7}{9}}$$

Para la complejidad, la base de mayor magnitud es $|-2| = 2$, acompañada del factor lineal $n$:
$$\mathbf{a_n \in O(n \cdot 2^n)}$$

---

### Ejercicio 4

$$a_n - 3a_{n-1} + 3a_{n-2} - a_{n-3} = 3 + 5n, \quad n \ge 0$$

#### **Paso 1: Identificar y resolver la parte homogénea $P_h(x)$**
Igualamos el lado izquierdo a cero:
$$a_n - 3a_{n-1} + 3a_{n-2} - a_{n-3} = 0$$
* **Orden:** $n - (n-3) = 3$.
* **Polinomio homogéneo:** $P_h(x) = x^3 - 3x^2 + 3x - 1 = 0$.
* Reconocemos el desarrollo del binomio al cubo: $(x - 1)^3 = 0$.
* **Raíz homogénea:** $r_1 = 1$ con multiplicidad $m_1 = 3$.

#### **Paso 2: Encontrar el polinomio aniquilador $P_f(x)$ para $f(n)$**
Analizamos $f(n) = 3 + 5n$:
* Es un polinomio en $n$ de **grado $d = 1$**.
* Su aniquilador es $(x - 1)^{1 + 1} = (x - 1)^2$.
  $$P_f(x) = (x - 1)^2$$

#### **Paso 3: Construir el polinomio característico total $P(x)$**
Multiplicamos $P_h(x)$ por $P_f(x)$:
$$P(x) = (x - 1)^3 \cdot (x - 1)^2 = (x - 1)^5 = 0$$
* Obtenemos la raíz $r = 1$ repetida 5 veces.
* Multiplicidad total: $m = 5$.

#### **Paso 4: Formular la plantilla de la solución general $a_n$**
Asignamos los coeficientes multiplicando por potencias $1, n, n^2, n^3, n^4$:
$$\mathbf{a_n = c_1 + c_2 n + c_3 n^2 + c_4 n^3 + c_5 n^4}$$

#### **Paso 5: Determinación del orden de complejidad $O(g(n))$**
Dado que el término algebraico de mayor potencia en la plantilla es $n^4$, sin importar los valores numéricos específicos de las constantes $c_i$, el comportamiento asintótico dominante estará regido por la potencia $n^4$:
$$\mathbf{a_n \in O(n^4)}$$

---

### Ejercicio 5

$$a_n = a_{n-1} + 2n - 1, \quad a_1 = 1$$

#### **Paso 1: Identificar y resolver la parte homogénea $P_h(x)$**
Reordenamos la ecuación enviando los términos de $a$ al lado izquierdo:
$$a_n - a_{n-1} = 2n - 1$$
Igualamos a cero el lado izquierdo:
$$a_n - a_{n-1} = 0 \implies P_h(x) = x - 1 = 0$$
* **Raíz homogénea:** $r_1 = 1$ con multiplicidad $m_1 = 1$.

#### **Paso 2: Encontrar el polinomio aniquilador $P_f(x)$ para $f(n)$**
Analizamos $f(n) = 2n - 1$:
* Polinomio de **grado $d = 1$**.
* Aniquilador: $P_f(x) = (x - 1)^{1+1} = (x - 1)^2$.

#### **Paso 3: Construir el polinomio característico total $P(x)$**
$$P(x) = (x - 1) \cdot (x - 1)^2 = (x - 1)^3 = 0$$
* Raíz única $r = 1$ con multiplicidad $m = 3$.

#### **Paso 4: Formular la plantilla de la solución general $a_n$**
$$a_n = c_1 + c_2 n + c_3 n^2$$

#### **Paso 5: Calcular las constantes $c_1, c_2, c_3$**
Usamos la relación $a_n = a_{n-1} + 2n - 1$ partiendo de $a_1 = 1$:
1. $a_1 = 1$
2. $a_2 = a_1 + 2(2) - 1 = 1 + 4 - 1 = 4$
3. $a_3 = a_2 + 2(3) - 1 = 4 + 6 - 1 = 9$

Evaluamos la plantilla en $n = 1, 2, 3$:

* **Para $n = 1$ ($a_1 = 1$):**
  $$c_1 + c_2(1) + c_3(1)^2 = 1 \implies \mathbf{c_1 + c_2 + c_3 = 1} \quad \text{--- (Ecuación 1)}$$

* **Para $n = 2$ ($a_2 = 4$):**
  $$c_1 + c_2(2) + c_3(2)^2 = 4 \implies \mathbf{c_1 + 2c_2 + 4c_3 = 4} \quad \text{--- (Ecuación 2)}$$

* **Para $n = 3$ ($a_3 = 9$):**
  $$c_1 + c_2(3) + c_3(3)^2 = 9 \implies \mathbf{c_1 + 3c_2 + 9c_3 = 9} \quad \text{--- (Ecuación 3)}$$

**Resolviendo el sistema:**
* Ecuación 2 $-$ Ecuación 1: $c_2 + 3c_3 = 3$  --- (A)
* Ecuación 3 $-$ Ecuación 2: $c_2 + 5c_3 = 5$  --- (B)
* Restamos (B) $-$ (A): $2c_3 = 2 \implies \mathbf{c_3 = 1}$.
* Sustituimos en (A): $c_2 + 3(1) = 3 \implies \mathbf{c_2 = 0}$.
* Sustituimos en Ecuación 1: $c_1 + 0 + 1 = 1 \implies \mathbf{c_1 = 0}$.

#### **Paso 6: Solución exacta y complejidad**
$$\mathbf{a_n = n^2}$$
$$\mathbf{a_n \in O(n^2)}$$

---

### Ejercicio 6

$$a_n = a_{n-1} + 3n^2, \quad a_0 = 7$$

#### **Paso 1: Identificar y resolver la parte homogénea $P_h(x)$**
Reordenamos: $a_n - a_{n-1} = 3n^2$.
Homogénea: $a_n - a_{n-1} = 0 \implies P_h(x) = x - 1 = 0$.
* Raíz homogénea: $r_1 = 1$ ($m_1 = 1$).

#### **Paso 2: Encontrar el polinomio aniquilador $P_f(x)$**
Para $f(n) = 3n^2$, es de **grado $d = 2$**:
$$P_f(x) = (x - 1)^{2+1} = (x - 1)^3$$

#### **Paso 3: Polinomio total y raíces**
$$P(x) = (x - 1) \cdot (x - 1)^3 = (x - 1)^4 = 0 \implies r = 1 \text{ (multiplicidad } m = 4)$$

#### **Paso 4: Plantilla de solución general**
$$a_n = c_1 + c_2 n + c_3 n^2 + c_4 n^3$$

#### **Paso 5: Complejidad Asintótica**
Al desarrollarse en un polinomio de grado 3 dominado por el término $n^3$:
$$\mathbf{a_n \in O(n^3)}$$

---

### Ejercicio 7

$$a_n = 3a_{n-1} + 5 \cdot 7^n, \quad a_0 = 2$$

#### **Paso 1: Identificar y resolver la parte homogénea $P_h(x)$**
Reordenamos: $a_n - 3a_{n-1} = 5 \cdot 7^n$.
Ecuación homogénea: $a_n - 3a_{n-1} = 0$.
* **Polinomio homogéneo:** $P_h(x) = x - 3 = 0$.
* **Raíz homogénea:** $r_1 = 3$ con multiplicidad $m_1 = 1$.

#### **Paso 2: Encontrar el polinomio aniquilador $P_f(x)$ para funciones exponenciales**
Analizamos la parte no homogénea $f(n) = 5 \cdot 7^n$:
* Es de la forma exponencial $C \cdot b^n$, donde la base es $b = 7$.
* La regla del aniquilador para una función exponencial $b^n$ establece que su aniquilador es:
  $$P_f(x) = (x - b)$$
* Sustituyendo $b = 7$:
  $$P_f(x) = x - 7$$

#### **Paso 3: Polinomio total y raíces**
Multiplicamos el polinomio homogéneo por el aniquilador exponencial:
$$P(x) = P_h(x) \cdot P_f(x) = (x - 3)(x - 7) = 0$$
* Raíz $r_1 = 3$ con multiplicidad $m_1 = 1$.
* Raíz $r_2 = 7$ con multiplicidad $m_2 = 1$.

#### **Paso 4: Plantilla de solución general**
Como son dos raíces distintas simples, la plantilla es:
$$a_n = c_1(3)^n + c_2(7)^n$$

#### **Paso 5: Calcular las constantes $c_1, c_2$**
Generamos $a_1$ con $a_n = 3a_{n-1} + 5 \cdot 7^n$:
1. $a_0 = 2$
2. $a_1 = 3(2) + 5(7)^1 = 6 + 35 = 41$

Evaluamos en $n = 0$ y $n = 1$:

* **Para $n = 0$ ($a_0 = 2$):**
  $$c_1(3)^0 + c_2(7)^0 = 2 \implies \mathbf{c_1 + c_2 = 2} \quad \text{--- (Ecuación 1)}$$

* **Para $n = 1$ ($a_1 = 41$):**
  $$c_1(3)^1 + c_2(7)^1 = 41 \implies \mathbf{3c_1 + 7c_2 = 41} \quad \text{--- (Ecuación 2)}$$

**Resolviendo el sistema $2 \times 2$:**
Multiplicamos la Ecuación 1 por 3:
$$3c_1 + 3c_2 = 6$$
Restamos Ecuación 2 $-$ (Ecuación 1 multiplicada por 3):
$$(3c_1 + 7c_2) - (3c_1 + 3c_2) = 41 - 6 \implies 4c_2 = 35 \implies \mathbf{c_2 = \frac{35}{4}}$$

Sustituimos en Ecuación 1:
$$c_1 + \frac{35}{4} = 2 \implies c_1 = \frac{8}{4} - \frac{35}{4} \implies \mathbf{c_1 = -\frac{27}{4}}$$

#### **Paso 6: Solución exacta y complejidad**
$$\mathbf{a_n = -\frac{27}{4}(3)^n + \frac{35}{4}(7)^n}$$

Comparamos las bases en magnitud: $|7| > |3|$. La base 7 domina completamente el crecimiento:
$$\mathbf{a_n \in O(7^n)}$$

---

### Ejercicio 8

$$a_n = 3a_{n-1} - 4a_{n-3} + n^2, \quad a_0 = 11, \ a_1 = 1, \ a_2 = -1$$

#### **Paso 1: Identificar y resolver la parte homogénea $P_h(x)$**
Reordenamos enviando los términos $a_k$ a la izquierda:
$$a_n - 3a_{n-1} + 4a_{n-3} = n^2$$
Homogénea: $a_n - 3a_{n-1} + 4a_{n-3} = 0$.
* **Polinomio homogéneo:** $P_h(x) = x^3 - 3x^2 + 4 = 0$.
* Buscamos raíces probando divisores de 4: para $x = -1 \implies (-1)^3 - 3(-1)^2 + 4 = -1 - 3 + 4 = 0 \checkmark$.
* Dividimos por división sintética entre $(x + 1)$ y obtenemos $(x^2 - 4x + 4) = (x - 2)^2$.
* **Raíces homogéneas:**
  * $r_1 = -1$ con multiplicidad $m_1 = 1$.
  * $r_2 = 2$ con multiplicidad $m_2 = 2$.

#### **Paso 2: Encontrar el polinomio aniquilador $P_f(x)$ para $f(n) = n^2$**
Como $f(n) = n^2$ es un polinomio de grado $d = 2$:
$$P_f(x) = (x - 1)^{2+1} = (x - 1)^3$$

#### **Paso 3: Polinomio total y raíces**
$$P(x) = (x + 1)(x - 2)^2 (x - 1)^3 = 0$$
* Raíz $r_1 = -1$ ($m_1 = 1$).
* Raíz $r_2 = 2$ ($m_2 = 2$).
* Raíz $r_3 = 1$ ($m_3 = 3$).

#### **Paso 4: Plantilla de solución general**
$$a_n = c_1(-1)^n + c_2(2)^n + c_3 n(2)^n + c_4(1)^n + c_5 n(1)^n + c_6 n^2(1)^n$$
$$\mathbf{a_n = c_1(-1)^n + c_2(2)^n + c_3 n(2)^n + c_4 + c_5 n + c_6 n^2}$$

#### **Paso 5: Determinación del orden de complejidad $O(g(n))$**
Comparamos los órdenes de crecimiento de los términos presentes:
* $(-1)^n$ oscila con magnitud 1.
* $n^2$ crece de forma polinomial.
* $n \cdot 2^n$ crece exponencialmente multiplicado por $n$.

El término con la tasa de crecimiento asintótico más alta es $n \cdot 2^n$:
$$\mathbf{a_n \in O(n \cdot 2^n)}$$

---

### Ejercicio 9

$$a_n = 2a_{n-1} - a_{n-2} + 1, \quad a_1 = 2, \ a_2 = 3$$

#### **Paso 1: Identificar y resolver la parte homogénea $P_h(x)$**
Reordenamos: $a_n - 2a_{n-1} + a_{n-2} = 1$.
Homogénea: $a_n - 2a_{n-1} + a_{n-2} = 0$.
* **Polinomio homogéneo:** $P_h(x) = x^2 - 2x + 1 = (x - 1)^2 = 0$.
* **Raíz homogénea:** $r_1 = 1$ con multiplicidad $m_1 = 2$.

#### **Paso 2: Encontrar el polinomio aniquilador $P_f(x)$ para $f(n) = 1$**
La constante $1$ es un polinomio de grado $d = 0$:
$$P_f(x) = (x - 1)^{0+1} = (x - 1)$$

#### **Paso 3: Polinomio total y raíces**
$$P(x) = (x - 1)^2 \cdot (x - 1) = (x - 1)^3 = 0$$
* Raíz $r = 1$ con multiplicidad $m = 3$.

#### **Paso 4: Plantilla de solución general**
$$a_n = c_1 + c_2 n + c_3 n^2$$

#### **Paso 5: Calcular las constantes $c_1, c_2, c_3$**
Necesitamos 3 condiciones. Usamos $a_1 = 2, a_2 = 3$ y calculamos $a_3 = 2a_2 - a_1 + 1 = 2(3) - 2 + 1 = 5$:

* **Para $n = 1$ ($a_1 = 2$):** $c_1 + c_2 + c_3 = 2$  --- (1)
* **Para $n = 2$ ($a_2 = 3$):** $c_1 + 2c_2 + 4c_3 = 3$  --- (2)
* **Para $n = 3$ ($a_3 = 5$):** $c_1 + 3c_2 + 9c_3 = 5$  --- (3)

Resolviendo:
* (2) $-$ (1): $c_2 + 3c_3 = 1$
* (3) $-$ (2): $c_2 + 5c_3 = 2$
* Restando ambas: $2c_3 = 1 \implies \mathbf{c_3 = 1/2}$.
* $c_2 + 3(1/2) = 1 \implies \mathbf{c_2 = -1/2}$.
* $c_1 - 1/2 + 1/2 = 2 \implies \mathbf{c_1 = 2}$.

#### **Paso 6: Solución exacta y complejidad**
$$\mathbf{a_n = \frac{1}{2}n^2 - \frac{1}{2}n + 2}$$
$$\mathbf{a_n \in O(n^2)}$$

---

### Ejercicio 10

$$a_n = 3a_{n-1} - 2a_{n-2} + 5 \cdot 2^n, \quad a_0 = 2, \ a_1 = 4$$

#### **Paso 1: Identificar y resolver la parte homogénea $P_h(x)$**
Reordenamos: $a_n - 3a_{n-1} + 2a_{n-2} = 5 \cdot 2^n$.
Homogénea: $a_n - 3a_{n-1} + 2a_{n-2} = 0$.
* **Polinomio homogéneo:** $P_h(x) = x^2 - 3x + 2 = (x - 1)(x - 2) = 0$.
* **Raíces homogéneas:** $r_1 = 1 \ (m_1 = 1)$ y $r_2 = 2 \ (m_2 = 1)$.

#### **Paso 2: Encontrar el polinomio aniquilador $P_f(x)$ para $f(n) = 5 \cdot 2^n$**
Es una función exponencial con base $b = 2$:
$$P_f(x) = (x - 2)$$

#### **Paso 3: Polinomio total y raíces**
$$P(x) = (x - 1)(x - 2) \cdot (x - 2) = (x - 1)(x - 2)^2 = 0$$
* Raíz $r_1 = 1$ con multiplicidad $m_1 = 1$.
* Raíz $r_2 = 2$ con multiplicidad $m_2 = 2$ (¡al coincidir con la raíz homogénea, su multiplicidad aumentó!).

#### **Paso 4: Plantilla de solución general**
$$a_n = c_1(1)^n + c_2(2)^n + c_3 n(2)^n$$
$$\mathbf{a_n = c_1 + c_2(2)^n + c_3 n(2)^n}$$

#### **Paso 5: Complejidad Asintótica**
El término con mayor orden de crecimiento es $n \cdot 2^n$:
$$\mathbf{a_n \in O(n \cdot 2^n)}$$

---

## Bloque 2: Recurrencias por División y Cambios de Variable (Teorema Maestro)

---

### Explicación Metodológica del Teorema Maestro

Para recurrencias de la forma $T(n) = a T(n/b) + f(n)$:
1. **$a \ge 1$:** Número de subproblemas recursivos.
2. **$b > 1$:** Factor de división del tamaño del problema.
3. **$f(n)$:** Costo del trabajo realizado fuera de las llamadas recursivas (dividir y combinar).

Se compara la función $f(n)$ contra la función crítica $n^{\log_b a}$:

* **Caso 1:** Si $f(n) = O(n^{\log_b a - \epsilon})$ para algún $\epsilon > 0$, entonces la parte recursiva domina:
  $$\mathbf{T(n) \in \Theta\left(n^{\log_b a}\right)}$$
* **Caso 2:** Si $f(n) = \Theta(n^{\log_b a})$, el costo se distribuye equitativamente en los niveles del árbol:
  $$\mathbf{T(n) \in \Theta\left(n^{\log_b a} \log n\right)}$$
* **Caso 3:** Si $f(n) = \Omega(n^{\log_b a + \epsilon})$ y cumple la condición de regularidad $a f(n/b) \le c f(n)$ con $c < 1$, el costo en la raíz domina:
  $$\mathbf{T(n) \in \Theta(f(n))}$$

---

### Ejercicio 11

$$T(n) = 4T\left(\frac{n}{3}\right) + 5, \quad T(1) = 5$$

#### **Paso 1: Identificar parámetros**
* $a = 4$
* $b = 3$
* $f(n) = 5$ (es una función constante, $f(n) = \Theta(n^0)$)

#### **Paso 2: Calcular el exponente crítico $\log_b a$**
$$\log_b a = \log_3 4 \approx 1.2618$$
La función crítica es $n^{\log_3 4} \approx n^{1.2618}$.

#### **Paso 3: Comparar $f(n)$ con $n^{\log_b a}$**
Comparamos $f(n) = 5 = \Theta(n^0)$ contra $n^{1.2618}$:
* Como $0 < 1.2618$, elegimos $\epsilon = 1.2618$:
  $$f(n) = 5 = O\left(n^{\log_3 4 - 1.2618}\right)$$
* Esto corresponde exactamente al **Caso 1 del Teorema Maestro**.

#### **Paso 4: Conclusión del orden de complejidad**
$$\mathbf{T(n) \in \Theta\left(n^{\log_3 4}\right)}$$

---

### Ejercicio 12

$$T(n) = T\left(\frac{n}{5}\right) + 7, \quad T(1) = 7$$

#### **Paso 1: Identificar parámetros**
* $a = 1$
* $b = 5$
* $f(n) = 7 = \Theta(n^0)$

#### **Paso 2: Calcular $\log_b a$**
$$\log_b a = \log_5 1 = 0 \implies n^{\log_5 1} = n^0 = 1$$

#### **Paso 3: Comparar $f(n)$ con $n^{\log_b a}$**
$$f(n) = 7 = \Theta(1) = \Theta(n^{\log_5 1})$$
* La función $f(n)$ tiene exactamente el mismo orden que $n^{\log_b a}$.
* Corresponde al **Caso 2 del Teorema Maestro**.

#### **Paso 4: Conclusión**
$$T(n) \in \Theta(n^{\log_b a} \log n) = \Theta(n^0 \log n)$$
$$\mathbf{T(n) \in \Theta(\log n)}$$

---

### Ejercicio 13

$$T(n) = 2T\left(\frac{n}{5}\right) + 3, \quad T(1) = 0$$

#### **Paso 1: Identificar parámetros**
* $a = 2$, $b = 5$, $f(n) = 3 = \Theta(n^0)$.

#### **Paso 2: Calcular $\log_b a$**
$$\log_5 2 \approx 0.4307 \implies n^{\log_5 2} \approx n^{0.4307}$$

#### **Paso 3: Comparar $f(n)$**
Como $f(n) = 3 = O(n^{0.4307 - 0.4307})$, $f(n)$ crece polinomialmente más lento que $n^{\log_5 2}$.
* Corresponde al **Caso 1 del Teorema Maestro**.

#### **Paso 4: Conclusión**
$$\mathbf{T(n) \in \Theta\left(n^{\log_5 2}\right)}$$

---

### Ejercicio 14

$$T(n) = 2T\left(\frac{n}{2}\right) + 1, \quad T(1) = 0$$

#### **Paso 1: Identificar parámetros**
* $a = 2$, $b = 2$, $f(n) = 1 = \Theta(n^0)$.

#### **Paso 2: Calcular $\log_b a$**
$$\log_2 2 = 1 \implies n^{\log_2 2} = n^1 = n$$

#### **Paso 3: Comparar $f(n)$**
$f(n) = 1 = O(n^{1 - 1})$, lo cual es polinomialmente menor que $n^1$.
* Corresponde al **Caso 1 del Teorema Maestro**.

#### **Paso 4: Conclusión**
$$\mathbf{T(n) \in \Theta(n)}$$

---

### Ejercicio 15

$$T(n) = T\left(\frac{n}{3}\right) + 1, \quad T(1) = 1$$

#### **Paso 1: Identificar parámetros**
* $a = 1$, $b = 3$, $f(n) = 1$.

#### **Paso 2: Calcular $\log_b a$**
$$\log_3 1 = 0 \implies n^0 = 1$$

#### **Paso 3: Comparar**
$f(n) = 1 = \Theta(1) = \Theta(n^{\log_3 1})$.
* **Caso 2 del Teorema Maestro**.

#### **Paso 4: Conclusión**
$$\mathbf{T(n) \in \Theta(\log n)}$$

---

### Ejercicio 16

$$T(n) = 2T\left(\frac{n}{3}\right) + 4, \quad T(1) = 1$$

#### **Paso 1: Identificar parámetros**
* $a = 2$, $b = 3$, $f(n) = 4$.

#### **Paso 2: Calcular $\log_b a$**
$$\log_3 2 \approx 0.6309$$

#### **Paso 3: Comparar**
$f(n) = 4 = O(n^{0.6309 - \epsilon})$. Cae en el **Caso 1**.

#### **Paso 4: Conclusión**
$$\mathbf{T(n) \in \Theta\left(n^{\log_3 2}\right)}$$

---

### Ejercicio 17

$$T(n) = T\left(\frac{n}{5}\right) + 3n^2, \quad T(1) = 4$$

#### **Paso 1: Identificar parámetros**
* $a = 1$, $b = 5$, $f(n) = 3n^2$.

#### **Paso 2: Calcular $\log_b a$**
$$\log_5 1 = 0 \implies n^0 = 1$$

#### **Paso 3: Comparar $f(n)$ con $n^{\log_b a}$**
Comparamos $f(n) = 3n^2$ contra $1$:
* $f(n) = 3n^2 = \Omega(n^{0 + 2})$ para $\epsilon = 2$.
* Cae en el **Caso 3 del Teorema Maestro**.

#### **Paso 4: Verificar condición de regularidad del Caso 3**
Debemos verificar si $a f(n/b) \le c f(n)$ para alguna constante $c < 1$:
$$1 \cdot f\left(\frac{n}{5}\right) = 3\left(\frac{n}{5}\right)^2 = \frac{3n^2}{25} = \frac{1}{25} (3n^2) = \frac{1}{25} f(n)$$
Eligiendo $c = \frac{1}{25} < 1$, se cumple estrictamente la condición de regularidad.

#### **Paso 5: Conclusión**
$$\mathbf{T(n) \in \Theta(n^2)}$$

---

### Ejercicio 18 (Cambio de variable especial)

$$T(n) = 2T(n^{1/2}) + \log n \quad \text{con } n = 2^{2^k}, \quad T(2) = 1$$

#### **Paso 1: Realizar la transformación de variable**
El enunciado nos da la sustitución $n = 2^{2^k}$.
Calculamos las expresiones que aparecen en la recurrencia:
1. $\log_2 n = \log_2\left(2^{2^k}\right) = 2^k$.
2. $n^{1/2} = \left(2^{2^k}\right)^{1/2} = 2^{2^k \cdot \frac{1}{2}} = 2^{2^{k-1}}$.

#### **Paso 2: Reescribir la recurrencia en términos de $k$**
Sustituimos estas expresiones en $T(n) = 2T(n^{1/2}) + \log n$:
$$T\left(2^{2^k}\right) = 2 T\left(2^{2^{k-1}}\right) + 2^k$$

Definimos una nueva función $S(k) = T\left(2^{2^k}\right)$:
$$\mathbf{S(k) = 2 S(k - 1) + 2^k}$$

#### **Paso 3: Resolver la recurrencia no homogénea para $S(k)$**
Ahora tenemos una recurrencia lineal no homogénea estándar en la variable $k$:
$$S(k) - 2S(k - 1) = 2^k$$

1. **Polinomio homogéneo:** $S(k) - 2S(k - 1) = 0 \implies P_h(x) = x - 2 = 0 \implies r_1 = 2$.
2. **Aniquilador para $f(k) = 2^k$:** Como la base es $b = 2$, $P_f(x) = (x - 2)$.
3. **Polinomio total:**
   $$P(x) = (x - 2) \cdot (x - 2) = (x - 2)^2 = 0$$
   * Raíz $r = 2$ con multiplicidad $m = 2$.
4. **Plantilla para $S(k)$:**
   $$S(k) = c_1(2)^k + c_2 k (2)^k$$

#### **Paso 4: Volver a la variable original $n$**
Recordamos nuestras definiciones iniciales:
* $n = 2^{2^k} \implies \log_2 n = 2^k$.
* Tomando logaritmo base 2 nuevamente: $\log_2(\log_2 n) = \log_2(2^k) = k$.

Sustituimos $2^k = \log_2 n$ y $k = \log_2(\log_2 n)$ en la función $S(k)$:
$$T(n) = c_1 (\log_2 n) + c_2 \log_2(\log_2 n) \cdot (\log_2 n)$$

#### **Paso 5: Conclusión del orden de complejidad**
Tomamos el término asintóticamente dominante:
$$\mathbf{T(n) \in O(\log n \cdot \log(\log n))}$$

---

### Ejercicio 19

$$T(n) = 5T\left(\frac{n}{2}\right) + (n \log n)^2, \quad n > 1, \quad T(1) = 1$$

#### **Paso 1: Identificar parámetros**
* $a = 5$
* $b = 2$
* $f(n) = (n \log n)^2 = n^2 \log^2 n$

#### **Paso 2: Calcular $\log_b a$**
$$\log_2 5 \approx 2.3219 \implies n^{\log_2 5} \approx n^{2.3219}$$

#### **Paso 3: Comparar $f(n) = n^2 \log^2 n$ contra $n^{2.3219}$**
A pesar de tener un término logarítmico $\log^2 n$, la potencia polinomial de $f(n)$ es $n^2$.
Como $2 < 2.3219$, existe un $\epsilon \approx 0.3219 > 0$ tal que:
$$f(n) = n^2 \log^2 n = O\left(n^{2.3219 - \epsilon}\right)$$
* Corresponde al **Caso 1 del Teorema Maestro**.

#### **Paso 4: Conclusión**
$$\mathbf{T(n) \in \Theta\left(n^{\log_2 5}\right)}$$

---

### Ejercicio 20

$$T(n) = \frac{3}{2}T\left(\frac{n}{2}\right) - \frac{1}{2}T\left(\frac{n}{4}\right) - \frac{1}{n}, \quad n > 2, \quad T(1) = 1, \ T(2) = \frac{3}{2}$$

#### **Paso 1: Cambio de variable $n = 2^k$**
Reescribimos la ecuación sustituyendo $n = 2^k$ (por lo que $n/2 = 2^{k-1}$ y $n/4 = 2^{k-2}$):
$$T(2^k) = \frac{3}{2}T(2^{k-1}) - \frac{1}{2}T(2^{k-2}) - \frac{1}{2^k}$$

Definimos $S(k) = T(2^k)$:
$$S(k) - \frac{3}{2}S(k - 1) + \frac{1}{2}S(k - 2) = -2^{-k}$$

Multiplicamos toda la ecuación por 2 para eliminar las fracciones de los coeficientes:
$$\mathbf{2S(k) - 3S(k - 1) + S(k - 2) = -2 \cdot 2^{-k}}$$

#### **Paso 2: Resolver la parte homogénea**
$$2x^2 - 3x + 1 = 0$$
Factorizamos por la fórmula general o inspección:
$$(2x - 1)(x - 1) = 0 \implies r_1 = 1, \quad r_2 = \frac{1}{2}$$

#### **Paso 3: Encontrar el aniquilador de $f(k) = -2 \cdot 2^{-k} = -2 \left(\frac{1}{2}\right)^k$**
Es una función exponencial con base $b = 1/2$. Su aniquilador es:
$$P_f(x) = \left(x - \frac{1}{2}\right)$$

#### **Paso 4: Polinomio total y raíces**
$$P(x) = (x - 1)\left(x - \frac{1}{2}\right) \cdot \left(x - \frac{1}{2}\right) = (x - 1)\left(x - \frac{1}{2}\right)^2 = 0$$
* Raíz $r_1 = 1$ ($m_1 = 1$).
* Raíz $r_2 = 1/2$ ($m_2 = 2$).

#### **Paso 5: Plantilla para $S(k)$**
$$S(k) = c_1(1)^k + c_2\left(\frac{1}{2}\right)^k + c_3 k \left(\frac{1}{2}\right)^k$$

#### **Paso 6: Regresar a la variable original $n$**
Recordamos que $n = 2^k \implies k = \log_2 n$ y $\left(\frac{1}{2}\right)^k = \frac{1}{2^k} = \frac{1}{n}$:
$$T(n) = c_1 + c_2 \left(\frac{1}{n}\right) + c_3 \left(\frac{\log_2 n}{n}\right)$$

#### **Paso 7: Conclusión del orden de complejidad**
Conforme $n \to \infty$, los términos $\frac{1}{n}$ y $\frac{\log_2 n}{n}$ tienden a cero. Por lo tanto, el término dominante es la constante $c_1$:
$$\mathbf{T(n) \in O(1)}$$