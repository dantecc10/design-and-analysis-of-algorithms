# Fundamentos de Algoritmia

## 1. Definición Formal de Algoritmo

> **Definición**: Un algoritmo es un **conjunto de reglas** para efectuar algún cálculo, bien sea a mano o, más frecuentemente, en una máquina.

> **Definición operativa**: Una **secuencia ordenada de pasos exentos de ambigüedad** tal que, al llevarse a cabo con fidelidad, dará como resultado que se realice la tarea para la que se ha diseñado, **en un tiempo finito**.

### Excepción: Algoritmos Aleatorios
Se admiten como algoritmos procedimientos que efectúan **elecciones aleatorias** acerca de lo que hay que hacer en una situación dada (algoritmos probabilísticos, Monte Carlo, Las Vegas).

### Analogías Cotidianas
- ¿Una receta de cocina es un algoritmo? **Sí**, si es precisa, finita y sin ambigüedad.
- ¿Las instrucciones para armar un mueble? **Sí**, cumplen las propiedades.

---

## 2. Propiedades Fundamentales de un Algoritmo

| Propiedad | Descripción |
|-----------|-------------|
| **Finitud** | La ejecución ha de terminar después de un número finito de etapas. |
| **Precisión** | Cada etapa debe estar especificada rigurosamente. No hay espacio para subjetividad, intuición o creatividad. |
| **Entradas** | Cero o más entradas (valores iniciales). |
| **Salidas** | Una o más salidas (resultados). |

---

## 3. Resolución de Problemas: Fases

```mermaid
graph LR
    A[Diseñar algoritmo] --> B[Expresar como programa]
    B --> C[Ejecutar programa]
```

1. **Diseño**: Crear el algoritmo (parte creativa)
2. **Expresión**: Codificar en lenguaje de programación
3. **Ejecución**: Correr en máquina

---

## 4. Clasificación de Problemas: Complejidad Computacional

### 4.1 Clase **P** (Tiempo Polinómico Determinístico)
> Problemas resolubles en tiempo polinómico con una **Máquina de Turing Determinística (MTD)**.
> El tiempo de ejecución está descrito por una función polinómica: $T(n) = O(n^k)$, $k$ constante.

### 4.2 Clase **NP** (Tiempo Polinómico No Determinístico)
> Problemas resolubles en tiempo polinómico con una **Máquina de Turing No Determinística (MTND)**.
> Equivalentemente: Problemas cuya **solución puede verificarse** en tiempo polinómico por una MTD.

### 4.3 Reducción de Problemas
> Si reducimos un problema $A$ a otro problema $B$, podemos obtener una solución con un algoritmo para $B$ y transformar esa solución en una solución para $A$.

Notación: $A \leq_p B$ ($A$ se reduce a $B$ en tiempo polinómico).

### 4.4 El Problema P vs NP
- **P $\subseteq$ NP** (trivial: toda MTD es MTND que no usa no-determinismo)
- **¿P = NP?** → Problema abierto del milenio (Clay Institute, $1M)
- **NP-Completo**: Problemas en NP tales que todo problema en NP se reduce a ellos en tiempo polinómico.
- **Implicación**: Si $\exists$ algoritmo polinómico para **un** problema NP-completo $\Rightarrow$ **P = NP**

---

## 5. Algoritmia: Tres Pilares

> **Algoritmia**: Ciencia que estudia los algoritmos.

| Pilar | Descripción |
|-------|-------------|
| **Diseño** | Creación de algoritmos. Conocer técnicas: fuerza bruta, divide y vencerás, voraces, programación dinámica, backtracking, ramificación y poda. |
| **Validación** | Demostración de que las respuestas son correctas para **todas** las entradas posibles. Demostración formal (invariantes, inducción, pre/post-condiciones). |
| **Análisis** | Determinación de recursos (tiempo, espacio) que consumen. Permite comparar algoritmos alternativos con criterios cuantitativos. |

---

## 6. Ejemplos Comparativos: Multiplicación de Enteros

**Problema**: Multiplicar dos enteros positivos $a \times b$.
**Ejemplar**: $(981, 1234)$

### 6.1 Algoritmo Clásico (Escolar)

```
      981
   × 1234
   -------
     3924  (981 × 4)
    2943   (981 × 3, desplazado)
   1962    (981 × 2, desplazado)
   981     (981 × 1, desplazado)
   -------
  1210554
```

**Operaciones**: $O(n^2)$ multiplicaciones de dígitos + sumas, donde $n$ = número de dígitos.

---

### 6.2 Algoritmo à la Russe (Campesino Ruso / Egipcio)

Basado en **descomposición binaria** del multiplicador.

| Multiplicando (÷2) | Multiplicador (×2) | Sumar? |
|--------------------|--------------------|--------|
| 981                | 1234               | ✓ (impar) |
| 490                | 2468               | ✗ (par) |
| 245                | 4936               | ✓ |
| 122                | 9872               | ✗ |
| 61                 | 19744              | ✓ |
| 30                 | 39488              | ✗ |
| 15                 | 78976              | ✓ |
| 7                  | 157952             | ✓ |
| 3                  | 315904             | ✓ |
| 1                  | 631808             | ✓ |

**Suma de filas marcadas**:
$$1234 + 4936 + 19744 + 78976 + 157952 + 315904 + 631808 = 1,210,554$$

**Complejidad**: $O(\log b)$ pasos (donde $b$ es el multiplicador), cada paso opera con números de tamaño $O(\log a)$.

---

### 6.3 Algoritmo Divide y Vencerás (Karatsuba-inspirado)

Descomposición: $981 = 9 \cdot 10^2 + 81$, $1234 = 12 \cdot 10^2 + 34$

| Subproblema | Multiplicación | Desplazamiento | Resultado Parcial |
|-------------|----------------|----------------|-------------------|
| $9 \times 12$ | 108 | $10^4$ | 1,080,000 |
| $9 \times 34$ | 306 | $10^2$ | 30,600 |
| $81 \times 12$ | 972 | $10^2$ | 97,200 |
| $81 \times 34$ | 2,754 | $10^0$ | 2,754 |
| **Total** | | | **1,210,554** |

**Idea**: Reducir 4 multiplicaciones de $n/2$ dígitos a 3 (Karatsuba) $\rightarrow O(n^{\log_2 3}) \approx O(n^{1.585})$.

---

## 7. Problemas vs. Ejemplares (Instancias)

| Concepto | Definición |
|----------|------------|
| **Problema** | Descripción general de una tarea (ej. "Multiplicar dos enteros positivos"). |
| **Ejemplar / Instancia / Caso** | Entrada concreta del problema (ej. $(981, 1234)$, $(789, 9742)$). |
| **Dominio de definición** | Conjunto de todos los ejemplares válidos (aquí: $\mathbb{Z}^+ \times \mathbb{Z}^+$). |

### Ejemplos de Tamaño de Ejemplar

| Problema | Medida de Tamaño $n$ |
|----------|----------------------|
| Ordenación | Número de ítems a ordenar |
| Grafos | Número de vértices $\|V\|$ y/o aristas $\|E\|$ |
| Multiplicación | Número de bits/dígitos de los operandos |
| Búsqueda | Longitud del array |

> **Nota**: El tamaño suele ser el número de bits para representar la entrada, pero a menudo se usa una medida "natural" (ítems, vértices) por conveniencia.

---

## 8. Correctitud de Algoritmos

- **Incorrecto**: Basta **un** contraejemplo (un ejemplar donde falla).
- **Correcto**: Requiere **demostración formal** para **todo** el dominio de definición.
- **Técnicas**: Invariantes de bucle, inducción matemática, pre/post-condiciones (Hoare logic).

---

## 9. Ejercicios de Repaso

### Ejercicio 1: Clasificación
Determine si cada uno es un ejemplar válido para "Multiplicar dos enteros positivos":
- $(-12, 83.7)$ → **No** ($-12 \notin \mathbb{Z}^+$, $83.7 \notin \mathbb{Z}$)
- $(0, 5)$ → **No** ($0 \notin \mathbb{Z}^+$ en definición estricta)
- $(10^{100}, 10^{100})$ → **Sí** (enteros positivos, aunque grandes)

### Ejercicio 2: Propiedades
¿Cuál propiedad falla en este "algoritmo"?
```
Mientras x > 0:
    x = x - 1
Imprimir x
```
**Respuesta**: **Finitud** no garantizada si $x$ no es entero o si $x < 0$ inicialmente.

### Ejercicio 3: P vs NP
Si se descubre que **SAT** (satisfacibilidad booleana) $\in$ P, ¿qué se deduce?
**Respuesta**: Como SAT es NP-completo, **todo problema en NP** tendría algoritmo polinómico $\Rightarrow$ **P = NP**.

---

## 10. Resumen: Mapa Conceptual

```
ALGORITMIA
├── DISEÑO (técnicas creativas)
├── VALIDACIÓN (correctitud formal)
└── ANÁLISIS (complejidad tiempo/espacio)
    ├── Enfoques: empírico, teórico, híbrido
    ├── OE (Operaciones Elementales)
    ├── Notación asintótica: O, Ω, Θ
    └── Recurrencias
```

---

> **Siguiente tema**: [Análisis de Complejidad](03-analisis-complejidad.md)