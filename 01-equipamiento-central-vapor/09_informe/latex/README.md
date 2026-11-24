# Fuente LaTeX del expediente

## 1. Estructura

```
latex/
├── main.tex                 Documento principal
├── preambulo.tex            Paquetes, estilo, comandos de trazabilidad
├── portada.tex              Portada universitaria
├── ficha_documento.tex      Ficha de control del documento
├── bibliografia.bib         Base BibTeX (vacía hasta verificar fuentes)
├── compilar.sh              Script de compilación
├── capitulos/
│   ├── cap01_generalidades.tex
│   ├── cap02_fundamentos.tex
│   ├── ...
│   └── cap15_conclusiones.tex
├── anexos/
│   └── anexo_a_nomenclatura.tex
├── figuras/                 Figuras raster o SVG convertidas a PDF
└── build/                   Salida de compilación (no se versiona)
```

Cada capítulo es un archivo independiente, incluido con `\include` para mantener
auxiliares separados. No se duplica contenido entre capítulos: los temas
compartidos se referencian con `\autoref`.

## 2. Compilación

```bash
./compilar.sh            # compila en build/
./compilar.sh --limpia   # borra build/ y recompila
```

Equivale a:

```bash
pdflatex -output-directory=build main.tex
bibtex build/main
pdflatex -output-directory=build main.tex
pdflatex -output-directory=build main.tex
```

Requisitos del entorno verificado: TeX Live 2025 con `pdflatex`, `bibtex`,
`tcolorbox`, `siunitx`, `pgfplots`, `natbib`, `titlesec`, `fancyhdr`,
`booktabs`, `longtable`, `tabularx`, `caption`, `subcaption`, `hyperref`.

## 3. Bibliografía: decisión y justificación

Se usa **`natbib` + BibTeX** (autor--año, estilo `plainnat`) porque el entorno
disponible **no incluye `biblatex.sty` ni `biber`**. La instrucción original
admite BibLaTeX/Biber «si el entorno lo permite»; aquí no lo permite, y forzar
una instalación parcial produciría un documento no reproducible.

Migración futura a BibLaTeX/Biber (si se instala `texlive-bibtex-extra` y
`biber`):

1. Cambiar en `preambulo.tex` `natbib` por
   `\usepackage[backend=biber,style=authoryear]{biblatex}` y
   `\addbibresource{bibliografia.bib}`.
2. Sustituir `\bibliography{bibliografia}` en `main.tex` por `\printbibliography`.
3. Compilar con `biber` en lugar de `bibtex` y actualizar `compilar.sh`.

La base está vacía a propósito: solo se agregarán fuentes verificadas.

## 4. Convenciones de escritura

| Elemento | Convención |
|---|---|
| Unidades | `\qty{}{}` / `\unit{}` de `siunitx` |
| Cifras | coma decimal (babel español) |
| Figuras | `\begin{figure}[H]` + `\caption{}` + `\label{fig:...}` |
| Tablas | `booktabs` (`\toprule`, `\midrule`, `\bottomrule`) |
| Ecuaciones | entorno `equation` con `\label{eq:...}` |
| Referencias | `\autoref{cap:...}`, `\autoref{fig:...}`, `\autoref{tab:...}` |
| Citas | `\citep{clave}` o `\citet{clave}` |
| Fuentes internas | `\srcref{SRC-NNN}` |
| Supuestos | `\hipotesis{...}` |
| Ejemplos | `\ejemplo{...}` |

## 5. Estado de los capítulos

Los 15 capítulos contienen un aviso de estado (`cajaestado`) y el alcance
previsto, sin desarrollo técnico. La tabla de estados está en
`../00_gestion/SEGUIMIENTO_CAPITULOS.md`.

## 6. Figuras

- Las fuentes vectoriales viven en `../../06_diagramas/`.
- Las figuras TikZ se incluyen directamente en el capítulo o en un archivo
  `figuras/FIG-NN_*.tex` con `\input`.
- Las figuras externas se convierten a PDF vectorial (`inkscape --export-type=pdf`)
  y se guardan en `figuras/`.
- Las leyendas indican «Fuente: elaboración propia» o «adaptado de SRC-NNN».

## 7. Limitaciones conocidas de esta versión

- Solo portada, índices, numeración, encabezados y anexo de nomenclatura están
  desarrollados.
- La bibliografía aparece vacía hasta que se registren fuentes verificadas.
- No hay figuras ni tablas técnicas todavía; por eso los índices de figuras y
  tablas están vacíos.
