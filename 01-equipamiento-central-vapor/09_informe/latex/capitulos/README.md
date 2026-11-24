# Capítulos del expediente

Un archivo LaTeX por capítulo. El documento principal los incorpora con
`\input` desde `../main.tex`; aquí no se escribe el preámbulo ni la portada.

## 1. Archivos

| Cap. | Archivo | Título | Estado |
|---|---|---|---|
| I | `cap01_generalidades.tex` | Generalidades del proyecto | PENDIENTE |
| II | `cap02_fundamentos.tex` | Fundamentos termodinámicos | PENDIENTE |
| III | `cap03_clasificacion.tex` | Clasificación y configuraciones | PENDIENTE |
| IV | `cap04_combustion_combustibles.tex` | Combustión y combustibles | PENDIENTE |
| V | `cap05_generacion_vapor.tex` | Generación de vapor | PENDIENTE |
| VI | `cap06_turbinas_vapor.tex` | Turbinas de vapor | PENDIENTE |
| VII | `cap07_condensacion_refrigeracion.tex` | Condensación y refrigeración | PENDIENTE |
| VIII | `cap08_agua_alimentacion.tex` | Tratamiento y alimentación de agua | PENDIENTE |
| IX | `cap09_generacion_electrica.tex` | Generación y transformación eléctrica | PENDIENTE |
| X | `cap10_auxiliares_control.tex` | Auxiliares, control e instrumentación | PENDIENTE |
| XI | `cap11_comparacion_seleccion.tex` | Comparación y selección | PENDIENTE |
| XII | `cap12_dimensionamiento_calculos.tex` | Dimensionamiento y cálculos | PENDIENTE |
| XIII | `cap13_operacion_mantenimiento.tex` | Operación, mantenimiento y seguridad | PENDIENTE |
| XIV | `cap14_ambiente_eficiencia.tex` | Ambiente y eficiencia energética | PENDIENTE |
| XV | `cap15_conclusiones.tex` | Conclusiones y recomendaciones | PENDIENTE |

## 2. Estructura de cada archivo

1. Comentario de cabecera con capítulo, estado y fecha.
2. `\chapter{...}` y `\label{cap:NN}`.
3. Caja de estado (`cajaestado`) mientras el capítulo no esté aprobado.
4. Secciones y contenido técnico.
5. Figuras, tablas y ecuaciones con `\label` y referencia en el texto.

## 3. Reglas

1. Un tema, un capítulo: no se duplica contenido; se referencia con `\autoref`.
2. Al iniciar un capítulo se actualiza la caja de estado y
   `../../00_gestion/SEGUIMIENTO_CAPITULOS.md`.
3. Las figuras se producen en `../../06_diagramas/` y se incluyen, no se dibujan
   aquí salvo TikZ simple.
4. Las ecuaciones se numeran y se referencian; los símbolos nuevos se agregan al
   anexo de nomenclatura.
5. Se compila tras cada cambio relevante (`bash ../compilar.sh`).

## 4. Qué no va aquí

- Preámbulo, portada o bibliografía (están en el nivel superior de `latex/`).
- Fuentes o notas de investigación (van en `../../01_investigacion/`).
- Cálculos completos (van en `../../05_calculos/`; aquí solo se resumen y citan).

## 5. Estado

Los 15 archivos existen como esqueletos con alcance previsto y estado
`PENDIENTE`. No contienen desarrollo técnico todavía.
