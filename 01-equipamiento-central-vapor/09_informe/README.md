# Informe

Contiene la fuente LaTeX del expediente técnico y su compilación.

| Ruta | Contenido |
|---|---|
| `latex/main.tex` | Documento principal |
| `latex/capitulos/` | Quince capítulos independientes |
| `latex/anexos/` | Anexos (nomenclatura) |
| `latex/bibliografia.bib` | Base bibliográfica (vacía hasta verificar fuentes) |
| `latex/compilar.sh` | Compilación pdfLaTeX + BibTeX |

## Compilación

```bash
cd latex
bash compilar.sh
```

El PDF se genera en `latex/build/main.pdf`. No se versiona: se copia a
`../12_entregables/` solo cuando el expediente esté aprobado.

## Estado

- Portada, ficha de control, índices, numeración, encabezados y anexo de
  nomenclatura: operativos.
- Capítulos I a XV: esqueletos en `PENDIENTE`.
- Bibliografía: desactivada en `main.tex` hasta registrar la primera fuente
  verificada.
- Compilación verificada: 0 errores, 0 referencias o citas sin resolver.

Instrucciones detalladas, convenciones y decisiones sobre el motor bibliográfico
en `latex/README.md`.
