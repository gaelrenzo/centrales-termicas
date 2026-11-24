# Inventario de diagramas — Trabajo 01

Cada figura se produce en formato vectorial editable y se referencia desde el
capítulo correspondiente. Formatos preferidos: **TikZ** (integración directa en
LaTeX), **SVG** (editable con Inkscape) y **Mermaid** (diagramas de flujo).
Draw.io se exporta a SVG/PDF vectorial.

Estados: `PENDIENTE` · `EN DESARROLLO` · `EN REVISIÓN` · `APROBADO`

## 1. Inventario

| Código | Figura | Tipo | Formato | Archivo | Capítulo | Estado |
|---|---|---|---|---|---|---|
| FIG-01 | Diagrama general de una central a vapor | Esquema de bloques | TikZ / SVG | `FIG-01_diagrama_general` | I, III | PENDIENTE |
| FIG-02 | Diagrama de flujo de proceso (PFD) | PFD | TikZ / SVG | `FIG-02_pfd` | I, V | PENDIENTE |
| FIG-03 | Esquema del ciclo Rankine | Esquema de ciclo | TikZ | `FIG-03_ciclo_rankine` | II | PENDIENTE |
| FIG-04 | Diagrama T-s del ciclo ideal | Gráfico T-s | pgfplots / TikZ | `FIG-04_ts_ideal` | II | PENDIENTE |
| FIG-05 | Diagramas T-s con recalentamiento y regeneración | Gráfico T-s | pgfplots / TikZ | `FIG-05_ts_variantes` | II | PENDIENTE |
| FIG-06 | Diagrama P-h del ciclo | Gráfico P-h | pgfplots / TikZ | `FIG-06_ph_ciclo` | II, VII | PENDIENTE |
| FIG-07 | Esquema de caldera acuotubular | Corte esquemático | TikZ / SVG | `FIG-07_caldera_acuotubular` | V | PENDIENTE |
| FIG-08 | Esquema de turbina con extracciones | Corte esquemático | TikZ / SVG | `FIG-08_turbina_extracciones` | VI | PENDIENTE |
| FIG-09 | Circuito de agua y vapor | Diagrama de circuito | TikZ / SVG | `FIG-09_circuito_agua_vapor` | VIII | PENDIENTE |
| FIG-10 | Circuito de refrigeración | Diagrama de circuito | TikZ / SVG | `FIG-10_circuito_refrigeracion` | VII | PENDIENTE |
| FIG-11 | Sistema de combustible | Diagrama de proceso | TikZ / SVG | `FIG-11_sistema_combustible` | IV | PENDIENTE |
| FIG-12 | P&ID simplificado del ciclo | P&ID | SVG | `FIG-12_pid_simplificado` | X | PENDIENTE |

## 2. Convenciones gráficas

1. Numeración de equipos coherente con `03_equipos/CATALOGO_EQUIPOS.md`
   (EQ-01 … EQ-19).
2. Sentido de flujo indicado con flechas; líneas de vapor, agua, combustible y
   aire diferenciadas por estilo (no solo por color).
3. Leyenda obligatoria con símbolos y abreviaturas.
4. Unidades en los puntos de medición cuando corresponda.
5. Legibilidad en escala de grises y en impresión A4.
6. Leyenda de figura: «Figura NN — Título. Fuente: elaboración propia» o
   «adaptado de SRC-NNN».

## 3. Reglas de calidad

- Cada figura debe estar citada en el texto antes de aparecer.
- El diagrama no introduce equipos que no existan en el catálogo o en el texto.
- Las variables de la figura coinciden con la nomenclatura del capítulo.
- No se usan capturas de pantalla de software como figura final.

## 4. Avance

| Métrica | Valor |
|---|---|
| Figuras planificadas | 12 |
| Aprobadas | 0 |
| Pendientes | 12 |
