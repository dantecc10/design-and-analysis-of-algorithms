# Guía de Estudio: Primer Examen - Análisis y Diseño de Algoritmos

> **Curso**: Análisis y Diseño de Algoritmos  
> **Profesora**: Dra. Irene Olaya Ayaquica Martínez  
> **Facultad**: Facultad de Ciencias de la Computación, BUAP  
> **Periodo**: Otoño 2026  
> **Bibliografía**: Cormen et al. (CLRS), Brassard & Bratley, Levitin, MIT OCW 6.046J

---

## 📚 Índice de Contenidos

| # | Archivo | Tema | Páginas aprox. | Prioridad |
|---|---------|------|----------------|-----------|
| 00 | [`00-presentacion-curso.md`](00-presentacion-curso.md) | Presentación, bibliografía, evaluación | 1 | 📋 Referencia |
| 01 | [`01-historia-computacion.md`](01-historia-computacion.md) | Historia: Ábaco → von Neumann | 3 | 📖 Contexto |
| 02 | [`02-fundamentos-algoritmia.md`](02-fundamentos-algoritmia.md) | Definición, propiedades, P vs NP, algoritmia, ejemplos multiplicación | 6 | ⭐ **Fundamental** |
| 03 | [`03-analisis-complejidad.md`](03-analisis-complejidad.md) | Enfoques, OE, Selection Sort (3 casos), MaxElement, triple bucle | 12 | ⭐⭐⭐ **Núcleo** |
| 04 | [`04-notacion-asintotica.md`](04-notacion-asintotica.md) | O, Ω, Θ, propiedades, límites, jerarquía, demostraciones | 10 | ⭐⭐⭐ **Núcleo** |
| 05 | [`05-recurrencias.md`](05-recurrencias.md) | Suposiciones inteligentes, homogéneas (raíces distintas/múltiples), Master Theorem | 14 | ⭐⭐⭐ **Núcleo** |
| 06 | [`06-ejercicios-practica.md`](06-ejercicios-practica.md) | 25+ ejercicios integrados con soluciones ocultas | 18 | 🏋️ **Práctica** |

---

## 🎯 Mapa de Conceptos del Examen

```
PRIMER EXAMEN ADA
├── FUNDAMENTOS (Tema 02)
│   ├── Definición y propiedades de algoritmo
│   ├── Clases P, NP, NP-completo, reducción
│   ├── Algoritmia: Diseño, Validación, Análisis
│   ├── Ejemplos: multiplicación (clásico, ruso, DyV)
│   └── Problemas vs ejemplares, tamaño, correctitud
│
├── ANÁLISIS DE COMPLEJIDAD (Tema 03)
│   ├── Enfoques: empírico, teórico, híbrido
│   ├── Principio de Invarianza
│   ├── Operaciones Elementales (OE) - lista canónica
│   ├── Análisis detallado Selection Sort
│   │   ├── Caso mejor: Ω(n²)
│   │   ├── Caso peor: O(n²)
│   │   └── Caso medio: Θ(n²)
│   ├── MaxElement (2 variables)
│   └── Bucles anidados (sumatorias)
│
├── NOTACIÓN ASINTÓTICA (Tema 04)
│   ├── O-grande: definición, propiedades, testigos
│   ├── Ω-grande: definición, propiedades
│   ├── Θ-grande: definición, intersección
│   ├── Método del límite (L = lim f/g)
│   ├── Jerarquía de crecimiento
│   └── Demostraciones formales
│
└── RECURRENCIAS (Tema 05)
    ├── Suposiciones Inteligentes (4 etapas)
    │   └── Ejemplo: T(n) = 3T(n/2) + n → Θ(n^log₂3)
    ├── Homogéneas lineales cte
    │   ├── Ecuación característica
    │   ├── Raíces distintas: Fibonacci, ejemplos
    │   └── Raíces múltiples: n^j r^n
    ├── Master Theorem (3 casos)
    └── No homogéneas (parte particular)
```

---

## 📅 Plan de Estudio Sugerido (5 días)

### Día 1: Fundamentos + Inicio Complejidad
- [ ] Leer `00-presentacion-curso.md` (rápido)
- [ ] Leer `01-historia-computacion.md` (contexto, 30 min)
- [ ] **Estudiar a fondo** `02-fundamentos-algoritmia.md`
  - Definiciones formales
  - P vs NP (entender reducción)
  - 3 algoritmos multiplicación (traza 981×1234)
- [ ] Empezar `03-analisis-complejidad.md`: Secciones 1-4 (OE, principios)

### Día 2: Complejidad Profunda
- [ ] **Dominar** `03-analisis-complejidad.md` completo
  - Derivación paso a paso Selection Sort (3 casos) — **CRÍTICO**
  - MaxElement (caso mejor/peor/medio)
  - Ejercicios A.1–A.5 (hacer antes de ver soluciones)
- [ ] Repasar sumatorias: $\sum i$, $\sum i^2$, serie geométrica, armónica

### Día 3: Notación Asintótica
- [ ] **Estudiar a fondo** `04-notacion-asintotica.md`
  - Definiciones formales con cuantificadores ($\exists c, n_0$)
  - Propiedades 1-8 (saber aplicar regla suma/producto)
  - Método del límite (ejemplos 5.1)
  - Encontrar testigos $(c, n_0)$ (Ejercicios B.2)
  - Jerarquía de crecimiento (memorizar orden)

### Día 4: Recurrencias
- [ ] **Estudiar a fondo** `05-recurrencias.md`
  - Suposiciones inteligentes: 4 etapas + ejemplo completo T(n)=3T(n/2)+n
  - Ecuación característica: Fibonacci (derivación completa Binet)
  - Raíces distintas: 3 ejemplos resueltos
  - Raíces múltiples: teoría + 2 ejemplos
  - Master Theorem: tabla de casos + 5 ejercicios C.5
  - No homogéneas: método coeficientes indeterminados

### Día 5: Práctica Integrada + Repaso
- [ ] **Resolver** `06-ejercicios-practica.md` **sin ver soluciones**
  - Sección A: Complejidad (5 ejercicios)
  - Sección B: Notación asintótica (5 ejercicios)
  - Sección C: Recurrencias (6 ejercicios)
  - Sección D: Problemas tipo examen (5 ejercicios)
- [ ] Revisar soluciones, identificar errores
- [ ] Repaso rápido de fórmulas clave (hoja de referencia abajo)

---

## 📝 Hoja de Referencia Rápida (Para Memorizar)

### Sumatorias Básicas
$$\sum_{i=1}^n 1 = n \quad \sum_{i=1}^n i = \frac{n(n+1)}{2} \quad \sum_{i=1}^n i^2 = \frac{n(n+1)(2n+1)}{6} \quad \sum_{i=1}^n i^3 = \left[\frac{n(n+1)}{2}\right]^2$$

### Serie Geométrica
$$\sum_{i=0}^{k-1} r^i = \frac{r^k - 1}{r - 1},\quad r \neq 1$$

### Serie Armónica
$$H_n = \sum_{i=1}^n \frac{1}{i} = \ln n + \gamma + O(1/n),\quad \gamma \approx 0.577$$

### Master Theorem: $T(n) = aT(n/b) + f(n)$
| Caso | Condición | Solución |
|------|-----------|----------|
| 1 | $f(n) \in O(n^{\log_b a - \epsilon})$ | $\Theta(n^{\log_b a})$ |
| 2 | $f(n) \in \Theta(n^{\log_b a} \log^k n)$ | $\Theta(n^{\log_b a} \log^{k+1} n)$ |
| 3 | $f(n) \in \Omega(n^{\log_b a + \epsilon})$ y $af(n/b) \leq cf(n)$ | $\Theta(f(n))$ |

### Raíces Características → Complejidad
| Raíces | Solución | Complejidad |
|--------|----------|-------------|
| $r_1, \dots, r_k$ distintas | $\sum c_i r_i^n$ | $\Theta((\max|r_i|)^n)$ |
| $r$ mult. $m$ | $\sum_{j=0}^{m-1} c_j n^j r^n$ | $\Theta(n^{m-1}|r|^n)$ |
| $\alpha \pm i\beta$ | $\rho^n(c_1\cos n\theta + c_2\sin n\theta)$ | $\Theta(\rho^n)$ |

### Fibonacci (Fórmula de Binet)
$$F_n = \frac{\varphi^n - \psi^n}{\sqrt{5}},\quad \varphi = \frac{1+\sqrt{5}}{2} \approx 1.618,\quad \psi = \frac{1-\sqrt{5}}{2} \approx -0.618$$
$$F_n \in \Theta(\varphi^n)$$

---

## ⚠️ Temas "Trampa" / Frecuentemente Examinados

1. **Contar OE correctamente**: Incluir evaluaciones de condición de bucle, no solo cuerpo.
2. **Caso mejor ≠ mejor entrada**: A veces el algoritmo hace lo mismo (ej. Selection Sort, triple bucle D.1).
3. **Testigos en $O/\Omega$**: Deben ser **constantes** (no depender de $n$).
4. **Límite $f/g$**: Si $L=0 \implies f \in O(g)$ PERO $f \notin \Omega(g)$.
5. **Raíces múltiples**: Generan factores $n, n^2, \dots$ (no solo $r^n$).
6. **Master Theorem Caso 2**: $f(n) = \Theta(n^{\log_b a} \log^k n) \implies \Theta(n^{\log_b a} \log^{k+1} n)$.
7. **Inducción en recurrencias**: Cambio de variable $n=2^k$ → probar $S(k)$, no $T(n)$ directo.
8. **Parte particular no homogénea**: Si forma de $f(n)$ coincide con solución homogénea → multiplicar por $n^m$ ($m$ = multiplicidad).

---

## 🔗 Referencias Cruzadas entre Archivos

| Concepto | Archivo Principal | Refuerzo en |
|----------|-------------------|-------------|
| OE (Operaciones Elementales) | 03 Sección 2 | 03 Sección 4-10, 06 Sección A |
| Sumatorias | 03 Sección 5-7 | 05 Sección 2, 06 Sección A, C |
| Notación asintótica | 04 (completo) | 03 Sección 5-7 (resultados en $\Omega, O, \Theta$), 06 Sección B |
| Recurrencias Divide y Vencerás | 05 Sección 2 | 03 Sección 10 (ejercicios), 06 Sección C |
| Recurrencias Homogéneas | 05 Secciones 3-5 | 06 Sección C |
| Master Theorem | 05 Sección 2.3 | 06 Sección C.5 |

---

## ✅ Checklist Final Antes del Examen

- [ ] Puedo definir algoritmo, finitud, precisión, entradas/salidas
- [ ] Entiendo P, NP, NP-completo, reducción, implicación P=NP
- [ ] Puedo trazar los 3 algoritmos de multiplicación (981×1234)
- [ ] Sé listar 5 categorías de OE y contar OE en pseudocódigo
- [ ] Derivo $T(n)$ exacto para Selection Sort (3 casos) **sin mirar**
- [ ] Derivo $T(n)$ para MaxElement (mejor/peor/medio)
- [ ] Resuelvo sumatorias dobles/triples paso a paso
- [ ] Escribo definición formal de $O, \Omega, \Theta$ con cuantificadores
- [ ] Aplico propiedades (suma, producto, límite) correctamente
- [ ] Encuentro testigos $(c, n_0)$ para ejemplos dados
- [ ] Ordeno funciones por crecimiento asintótico
- [ ] Aplico 4 etapas de Suposiciones Inteligentes
- [ ] Resuelvo recurrencia homogénea: caracteristicas → raíces → general → sistema → cerrada
- [ ] Distingo raíces distintas vs múltiples y escribo forma correcta
- [ ] Aplico Master Theorem identificando $a, b, f(n), n^{\log_b a}$ y caso
- [ ] Resuelvo no homogéneas con coeficientes indeterminados
- [ ] Hago inducción matemática completa (base + paso)
- [ ] He resuelto ≥ 15 ejercicios del archivo 06 sin ayuda

---

## 💡 Consejos de Examen

1. **Muestre todo el trabajo**: "Paso a paso, sin saltos algebraicos" (según instrucciones del curso).
2. **Use LaTeX mental**: Escriba sumatorias con $\sum$, límites con $\lim$, alinee igualdades.
3. **Compruebe siempre**: Sustituya $n=1,2$ en su fórmula cerrada; verifique caso base en inducción.
4. **Notación correcta**: $O(n^2)$ no es lo mismo que $\Theta(n^2)$. Use $\in$ para pertenencia a conjuntos.
5. **Tiempo**: Asigne ~15 min por problema de análisis, ~10 min por recurrencia, ~5 min por teoría.

---

## 📞 Contacto y Recursos

- **Profesora**: Dra. Irene Olaya Ayaquica Martínez — `irene.ayaquica@correo.buap.mx`
- **MIT OCW 6.046J**: [Lecture Notes](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-046j-design-and-analysis-of-algorithms-spring-2015/lecture-notes/)
- **CLRS**: Capítulos 1-4 (Fundamentos, Crecimiento de funciones, Divide y Vencerás, Recurrencias)

---

> **Última actualización**: Septiembre 2026  
> **Generado desde**: Diapositivas oficiales del curso (6 PDFs)  
> **Formato**: Markdown con LaTeX matemático ($$...$$)  
> **Licencia**: Uso educativo personal

---

**¡Mucho éxito en el examen!** 🎓📐

*Recuerde: La práctica deliberada con los ejercicios del archivo 06 es la mejor preparación.*