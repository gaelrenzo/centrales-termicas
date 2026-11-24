# Trabajo 01 — Equipamiento de una central a vapor

| Dato | Detalle |
|---|---|
| Estudiante | MAMANI GALINDO RENZO GABRIEL |
| Área | Ingeniería Mecánica Eléctrica |
| Universidad | Universidad Nacional del Altiplano |
| Alcance | Investigación teórica y comparación de tecnologías |
| Formato | Expediente técnico de ingeniería (LaTeX → PDF) |
| Estado global | EN DESARROLLO — infraestructura lista, capítulos en `PENDIENTE` |
| Potencia | **Por definir** (no se fija sin justificación) |

## 1. Alcance

Describir, fundamentar y comparar el equipamiento de una central termoeléctrica
de vapor: desde el sistema de combustión y generación de vapor hasta la
generación y transformación eléctrica, incluyendo condensación, agua de
alimentación, auxiliares y control. Culmina en una comparación técnica que
justifique una configuración y un combustible para un caso de estudio cuyo
tamaño se definirá con criterios técnicos.

Combustibles obligatorios a comparar: **carbón mineral, gas natural, biomasa y
combustibles líquidos**. No se elige ganador antes de la comparación.

## 2. Índice del expediente

| Cap. | Título | Archivo LaTeX | Estado |
|---|---|---|---|
| I | Generalidades del proyecto | `capitulos/cap01_generalidades.tex` | PENDIENTE |
| II | Fundamentos termodinámicos de las centrales a vapor | `capitulos/cap02_fundamentos.tex` | PENDIENTE |
| III | Clasificación y configuraciones tecnológicas | `capitulos/cap03_clasificacion.tex` | PENDIENTE |
| IV | Sistemas de combustión y combustibles | `capitulos/cap04_combustion_combustibles.tex` | PENDIENTE |
| V | Equipamiento de generación de vapor | `capitulos/cap05_generacion_vapor.tex` | PENDIENTE |
| VI | Turbinas de vapor | `capitulos/cap06_turbinas_vapor.tex` | PENDIENTE |
| VII | Condensación y sistemas de refrigeración | `capitulos/cap07_condensacion_refrigeracion.tex` | PENDIENTE |
| VIII | Tratamiento y alimentación de agua | `capitulos/cap08_agua_alimentacion.tex` | PENDIENTE |
| IX | Generación y transformación eléctrica | `capitulos/cap09_generacion_electrica.tex` | PENDIENTE |
| X | Sistemas auxiliares, control e instrumentación | `capitulos/cap10_auxiliares_control.tex` | PENDIENTE |
| XI | Comparación técnica y selección de tecnologías | `capitulos/cap11_comparacion_seleccion.tex` | PENDIENTE |
| XII | Criterios de dimensionamiento y cálculos de ingeniería | `capitulos/cap12_dimensionamiento_calculos.tex` | PENDIENTE |
| XIII | Operación, mantenimiento y seguridad | `capitulos/cap13_operacion_mantenimiento.tex` | PENDIENTE |
| XIV | Evaluación ambiental y eficiencia energética | `capitulos/cap14_ambiente_eficiencia.tex` | PENDIENTE |
| XV | Conclusiones y recomendaciones | `capitulos/cap15_conclusiones.tex` | PENDIENTE |
| — | Anexos y bibliografía | `anexos/anexo_a_nomenclatura.tex` | PENDIENTE |

El detalle de estados, fuentes y pendientes está en
`00_gestion/SEGUIMIENTO_CAPITULOS.md`.

## 3. Organización de carpetas

| Carpeta | Contenido | Documento guía |
|---|---|---|
| `00_gestion/` | Plan, seguimiento, calidad y registro de fuentes | `PLAN_TRABAJO.md` |
| `01_investigacion/` | Notas, matrices y bitácora de búsqueda | `README.md` |
| `02_fundamentos/` | Marco teórico y ecuaciones de referencia | `README.md` |
| `03_equipos/` | Fichas técnicas `EQ-NN` | `CATALOGO_EQUIPOS.md` |
| `04_combustibles/` | Caracterización y comparación de combustibles | `MATRIZ_COMPARACION_COMBUSTIBLES.md` |
| `05_calculos/` | Memorias de cálculo `CALC-NN` | `INDICE_CALCULOS.md` |
| `06_diagramas/` | Fuentes vectoriales de figuras | `INVENTARIO_DIAGRAMAS.md` |
| `07_normativa/` | Normas aplicables y su estado | `README.md` |
| `08_bibliografia/` | Base bibliográfica del trabajo | `README.md` |
| `09_informe/` | Fuente LaTeX del expediente | `latex/README.md` |
| `10_presentacion/` | Exposición y material de apoyo | `README.md` |
| `11_anexos/` | Anexos, planos y memorias extensas | `README.md` |
| `12_entregables/` | PDF y versiones aprobadas | `README.md` |

## 4. Decisiones abiertas

Ninguna de estas decisiones se adopta sin evidencia y registro:

| Decisión | Estado | Se cierra en |
|---|---|---|
| Potencia del caso de estudio | ABIERTA | Cap. I / XI |
| Combustible seleccionado | ABIERTA | Cap. XI |
| Configuración del ciclo (presiones, recalentamiento, regeneración) | ABIERTA | Cap. II / XII |
| Tipo de condensación | ABIERTA | Cap. VII |
| Nivel de automatización | ABIERTA | Cap. X |

## 5. Reglas del trabajo

1. No se redacta un capítulo sin fuentes registradas en `00_gestion/REGISTRO_FUENTES.md`.
2. No se presentan cálculos académicos como datos de una central real.
3. Las fichas de equipo usan la plantilla común y los 15 campos obligatorios.
4. Cada figura nace en `06_diagramas/` y se referencia desde el texto.
5. El capítulo solo se aprueba con la lista de `CONTROL_CALIDAD.md` completa.

## 6. Estado actual

- Estructura creada y documentada.
- Esqueleto LaTeX compilable con portada, índices, 15 capítulos y anexo.
- Sin desarrollo técnico ni fuentes cargadas: los capítulos son esqueletos con
  estado `PENDIENTE`.
- Siguiente fase: fundamentos termodinámicos (capítulos II y III).
