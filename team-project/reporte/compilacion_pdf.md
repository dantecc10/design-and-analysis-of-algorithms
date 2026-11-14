# Guía de Compilación del Reporte a Formato PDF

Esta guía detalla los métodos disponibles para generar el archivo final `Reporte_Investigacion.pdf` a partir de `reporte_investigacion.md`.

---

## Opción 1: Generación Directa desde la Terminal (Recomendada si usas Linux)

El entorno ya cuenta con herramientas instaladas. Puedes compilarlo con Python y `weasyprint` ejecutando un script de conversión o utilizando `libreoffice`:

```bash
# Desde la carpeta raíz team-project/reporte
python3 -c "
import markdown, weasyprint
with open('reporte_investigacion.md', 'r', encoding='utf-8') as f:
    html_text = markdown.markdown(f.read(), extensions=['tables', 'fenced_code'])
weasyprint.HTML(string=html_text).write_pdf('Reporte_Investigacion.pdf')
"
```

---

## Opción 2: Desde VS Code / Cursor (Fácil e Intuitivo)

1. Abre el archivo `reporte_investigacion.md` en tu editor.
2. Instala la extensión **Markdown PDF** (`yzane.markdown-pdf`) o **Markdown Preview Enhanced**.
3. Haz clic derecho sobre el editor y selecciona:
   * **Markdown PDF: Export (pdf)**
4. Se generará automáticamente el archivo `reporte_investigacion.pdf` en la misma carpeta.
5. Renómbralo si es necesario a: `Reporte_Investigacion.pdf`.

---

## Opción 3: Vía Pandoc con Motor LaTeX

Si tienes instalado `pandoc` y una distribución de LaTeX en tu sistema:
```bash
pandoc reporte_investigacion.md -o Reporte_Investigacion.pdf \
    --pdf-engine=xelatex \
    -V geometry:margin=2.5cm \
    -V colorlinks=true \
    -V linkcolor=blue \
    -V urlcolor=blue
```

---

## Opción 4: A través de Google Docs o Microsoft Word

1. Copia todo el contenido de `reporte_investigacion.md`.
2. Pégalo en un documento nuevo de Google Docs o Microsoft Word (o ábrelo directamente).
3. Asegúrate de que las ecuaciones y tablas mantengan un margen limpio y legible.
4. Dirígete a **Archivo > Descargar > Documento PDF (.pdf)** y guárdalo como `Reporte_Investigacion.pdf`.
