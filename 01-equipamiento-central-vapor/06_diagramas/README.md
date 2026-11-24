# Diagramas

Fuentes vectoriales y editables de las figuras del expediente y de las
presentaciones. Aquí nace cada figura; en el informe solo se referencia.

## 1. Índice

El inventario completo, con códigos, formatos, capítulos y estado, está en
[`INVENTARIO_DIAGRAMAS.md`](INVENTARIO_DIAGRAMAS.md). Son 12 figuras: `FIG-01` a
`FIG-12`.

## 2. Nomenclatura de archivos

```
FIG-NN_nombre.(tex|svg|mmd|drawio)
```

Ejemplos: `FIG-03_ciclo_rankine.tex`, `FIG-10_circuito_refrigeracion.svg`.

## 3. Formatos preferidos

| Formato | Uso | Ventaja |
|---|---|---|
| TikZ (`.tex`) | Esquemas y gráficos integrados | Vectorial y compilable con el informe |
| SVG (`.svg`) | Esquemas editables | Se edita con Inkscape y se exporta a PDF |
| Mermaid (`.mmd`) | Diagramas de flujo | Versionable y legible como texto |
| Draw.io (`.drawio`) | P&ID y diagramas complejos | Exportación vectorial a PDF |

Las capturas de pantalla no se aceptan como figura final.

## 4. Reglas

1. Numeración de equipos coherente con `../03_equipos/CATALOGO_EQUIPOS.md`.
2. Leyenda con símbolos, abreviaturas y unidades.
3. Sentido de flujo con flechas; estilos distintos para vapor, agua,
   combustible y aire (no solo color).
4. Legible en escala de grises y en A4.
5. Leyenda de figura: «Fuente: elaboración propia» o «adaptado de SRC-NNN».
6. Cada figura se cita en el texto antes de aparecer.

## 5. Qué no va aquí

- Imágenes raster finales o capturas (si se requieren, se convierten a PDF
  vectorial en `../09_informe/latex/figuras/`).
- Texto del capítulo que explica la figura.

## 6. Estado

| Métrica | Valor |
|---|---|
| Figuras planificadas | 12 |
| Aprobadas | 0 |
| Pendientes | 12 |

## 7. Próximos pasos

1. `FIG-03` (esquema del ciclo) y `FIG-04` (T-s ideal) para ENT-01.
2. `FIG-01` y `FIG-02` (diagrama general y PFD).
3. `FIG-07` y `FIG-08` (caldera y turbina) al cerrar sus fichas.
