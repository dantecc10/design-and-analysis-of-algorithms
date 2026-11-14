# Proyecto en Equipo: Trabajo de Investigación y Exposición
## Análisis y Diseño de Algoritmos — BUAP

> **Docente:** Mtra. Irene Olaya Ayaquica Martínez  
> **Tema Seleccionado:** El Problema del Fontanero Diligente (*Single-Machine Scheduling / Minimización del Tiempo de Espera*)  
> **Integrantes:**  
> • **Dante Castelán Carpinteyro** (Matrícula: 202320271)  
> • **Yoshua Rameli Adán Pérez**  
> **Ponderación:** 30% de la calificación final (20% Reporte escrito + 10% Exposición oral)  
> **Formato de Entrega:** Carpeta comprimida `ApellidoPaterno_ApellidoMaterno_Nombre.rar` con el reporte en PDF y el archivo de las diapositivas.

---

## 📁 Estructura del Proyecto

El repositorio está organizado de forma modular para facilitar el trabajo colaborativo y la culminación del proyecto:

```text
team-project/
├── README.md                          # Visión general y guía rápida del proyecto (este archivo)
├── task.md                            # Especificación y requerimientos oficiales de la materia
├── PLAN_DE_TRABAJO.md                 # Plan maestro y guía de relevo para tu compañero (RACI y Checklist)
│
├── reporte/                           # Entregable 1: Reporte de Investigación Escrito (20%)
│   ├── reporte_investigacion.md       # Documento formal completo con rigor matemático y demostraciones
│   ├── reporte_base_yoshua.md         # Insumo en Markdown limpio para el trabajo de Yoshua
│   └── compilacion_pdf.md             # Instrucciones para compilar el reporte a 'Reporte_Investigacion.pdf'
│
├── presentacion/                      # Entregable 2: Material para la Exposición Oral (10%)
│   ├── guion_y_diapositivas.md        # Estructura diapositiva por diapositiva con contenido y notas del orador
│   └── plantilla_presentacion.md      # Diapositivas formateadas en Marp (exportables a PDF, PPTX o Canva)
│
└── src/                               # Soporte Computacional y Evidencia Empírica
    ├── fontanero_solvers.py           # Algoritmos: Fuerza Bruta, Voraz SPT, Backtracking, Pesos y Paralelo
    └── benchmark.py                   # Script de evaluación empírica de tiempos de ejecución y calidad
```

---

## 🚀 Estado Actual y Flujo de Trabajo (Handover)

### Lo que ya está realizado:
1. **Especificación oficial estructurada:** Requisitos, rúbrica y reglas de entrega documentadas en [task.md](file:///media/darkseid/DATA/Repos/design-and-analysis-of-algorithms/team-project/task.md).
2. **Marco teórico y matemático completo:** [reporte_investigacion.md](file:///media/darkseid/DATA/Repos/design-and-analysis-of-algorithms/team-project/reporte/reporte_investigacion.md) y [reporte_base_yoshua.md](file:///media/darkseid/DATA/Repos/design-and-analysis-of-algorithms/team-project/reporte/reporte_base_yoshua.md) cuentan con:
   * Resumen formal del problema.
   * Formulación matemática rigurosa y demostración de equivalencia del tiempo medio ponderado: $W(\pi) = \sum_{i=1}^n (n - i + 1) t_{\pi_i}$.
   * Análisis exhaustivo de 5 técnicas de diseño (Fuerza Bruta, Voraz SPT, Vuelta Atrás, Ramificación y Poda, Regla de Smith con pesos y $m$ fontaneros paralelos).
   * **Demostración matemática formal de optimalidad voraz** por el argumento de intercambio (*Exchange Argument*).
   * 4 aplicaciones interdisciplinarias reales (Planificación de CPU - SJF, Triage hospitalario, Servidores web/SQL y Mantenimiento industrial).
   * Demostración formal de pertenencia a las clases **$P$** y **$NP$**, y análisis de la frontera donde se vuelve **$NP\text{-Duro}$** (*Traveling Repairman Problem*).
   * 6 referencias bibliográficas canónicas (Guerequeta & Vallecillo, Brassard & Bratley, Cormen, Smith, Pinedo, Garey & Johnson).
3. **Código de algoritmos y benchmark funcional:** [fontanero_solvers.py](file:///media/darkseid/DATA/Repos/design-and-analysis-of-algorithms/team-project/src/fontanero_solvers.py) y [benchmark.py](file:///media/darkseid/DATA/Repos/design-and-analysis-of-algorithms/team-project/src/benchmark.py) ejecutados con éxito, comprobando que el método voraz resuelve 100,000 tareas en 54 milisegundos.
4. **Guion y diapositivas preparadas:** [guion_y_diapositivas.md](file:///media/darkseid/DATA/Repos/design-and-analysis-of-algorithms/team-project/presentacion/guion_y_diapositivas.md) y [plantilla_presentacion.md](file:///media/darkseid/DATA/Repos/design-and-analysis-of-algorithms/team-project/presentacion/plantilla_presentacion.md) listos con 13 diapositivas y guion de exposición.

### Lo que le corresponde realizar a tu compañero:
1. **Revisar [PLAN_DE_TRABAJO.md](file:///media/darkseid/DATA/Repos/design-and-analysis-of-algorithms/team-project/PLAN_DE_TRABAJO.md)** para entender el checklist y las responsabilidades.
2. **Generar el archivo de presentación visual:** Trasladar las diapositivas a PowerPoint, Canva, Google Slides o compilar la plantilla Marp a PDF/PPTX.
3. **Exportar el reporte a PDF:** Generar `Reporte_Investigacion.pdf` siguiendo [compilacion_pdf.md](file:///media/darkseid/DATA/Repos/design-and-analysis-of-algorithms/team-project/reporte/compilacion_pdf.md).
4. **Empaquetar y verificar:** Crear la carpeta y el comprimido `.rar` o `.zip` con el formato:
   * **Si sube Dante:** `Castelan_Carpinteyro_Dante.rar` conteniendo la carpeta `Castelan_Carpinteyro_Dante/`
   * **Si sube Yoshua:** `Adan_Perez_YoshuaRameli.rar` conteniendo la carpeta `Adan_Perez_YoshuaRameli/`
   ```text
   Castelan_Carpinteyro_Dante/   (o Adan_Perez_YoshuaRameli/)
   ├── Reporte_Investigacion.pdf
   └── Presentacion_Exposicion.pdf (o .pptx)
   ```

---

## ⚡ Comprobación Rápida de los Algoritmos

Para replicar las pruebas de rendimiento en cualquier máquina:
```bash
cd team-project/src
python3 benchmark.py
```
El script generará en consola la tabla comparativa con los tiempos de ejecución y porcentajes de error de las aproximaciones.
