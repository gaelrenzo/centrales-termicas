# Catálogo de equipos — Trabajo 01

Catálogo mínimo obligatorio. Cada fila se convierte en una ficha
`EQ-NN_nombre_equipo.md` usando
`../../recursos-compartidos/plantillas/PLANTILLA_FICHA_EQUIPO.md`.

Estados: `PENDIENTE` · `EN INVESTIGACIÓN` · `EN DESARROLLO` · `EN REVISIÓN` ·
`APROBADO`

## 1. Generación de vapor

| Código | Equipo | Capítulo | Prioridad | Ficha | Estado |
|---|---|---|---|---|---|
| EQ-01 | Caldera acuotubular | V | Alta | `EQ-01_caldera_acuotubular.md` | PENDIENTE |
| EQ-02 | Caldera pirotubular | V | Alta | `EQ-02_caldera_pirotubular.md` | PENDIENTE |
| EQ-03 | Quemador | IV, V | Alta | `EQ-03_quemador.md` | PENDIENTE |
| EQ-04 | Economizador | V | Alta | `EQ-04_economizador.md` | PENDIENTE |
| EQ-05 | Sobrecalentador | V | Alta | `EQ-05_sobrecalentador.md` | PENDIENTE |
| EQ-06 | Recalentador | V | Alta | `EQ-06_recalentador.md` | PENDIENTE |

## 2. Expansión y condensación

| Código | Equipo | Capítulo | Prioridad | Ficha | Estado |
|---|---|---|---|---|---|
| EQ-07 | Turbina de alta presión | VI | Alta | `EQ-07_turbina_alta_presion.md` | PENDIENTE |
| EQ-08 | Turbina de media presión | VI | Alta | `EQ-08_turbina_media_presion.md` | PENDIENTE |
| EQ-09 | Turbina de baja presión | VI | Alta | `EQ-09_turbina_baja_presion.md` | PENDIENTE |
| EQ-10 | Condensador | VII | Alta | `EQ-10_condensador.md` | PENDIENTE |
| EQ-15 | Torre de enfriamiento | VII | Alta | `EQ-15_torre_enfriamiento.md` | PENDIENTE |

## 3. Agua y calor de alimentación

| Código | Equipo | Capítulo | Prioridad | Ficha | Estado |
|---|---|---|---|---|---|
| EQ-11 | Bomba de alimentación | VIII | Alta | `EQ-11_bomba_alimentacion.md` | PENDIENTE |
| EQ-12 | Bomba de condensado | VIII | Alta | `EQ-12_bomba_condensado.md` | PENDIENTE |
| EQ-13 | Desaireador | VIII | Alta | `EQ-13_desaereador.md` | PENDIENTE |
| EQ-14 | Calentador regenerativo | VIII | Alta | `EQ-14_calentador_regenerativo.md` | PENDIENTE |

## 4. Eléctrico, control y protección

| Código | Equipo | Capítulo | Prioridad | Ficha | Estado |
|---|---|---|---|---|---|
| EQ-16 | Generador síncrono | IX | Alta | `EQ-16_generador_sincrono.md` | PENDIENTE |
| EQ-17 | Transformador | IX | Alta | `EQ-17_transformador.md` | PENDIENTE |
| EQ-18 | Sistemas de protección | IX, X | Alta | `EQ-18_sistemas_proteccion.md` | PENDIENTE |
| EQ-19 | Instrumentación y control | X | Alta | `EQ-19_instrumentacion_control.md` | PENDIENTE |

## 5. Avance

| Métrica | Valor |
|---|---|
| Fichas requeridas | 19 |
| Fichas aprobadas | 0 |
| Fichas en revisión | 0 |
| Fichas en desarrollo | 0 |
| Fichas pendientes | 19 |

## 6. Criterios comunes a todas las fichas

1. Los 15 campos de la plantilla, sin omisiones no justificadas.
2. Rango de operación con unidad y fuente; si es hipótesis, marcarlo.
3. Materiales con norma de material cuando se citen.
4. Fabricantes con documento y fecha de consulta; no se afirma disponibilidad
   comercial local.
5. Esquema propio o adaptado con licencia indicada.
6. Nomenclatura de equipo igual a la usada en el diagrama de flujo y en el P&ID.

## 7. Trazabilidad con capítulos

| Capítulo | Fichas que lo alimentan |
|---|---|
| IV | EQ-03 |
| V | EQ-01, EQ-02, EQ-03, EQ-04, EQ-05, EQ-06 |
| VI | EQ-07, EQ-08, EQ-09 |
| VII | EQ-10, EQ-15 |
| VIII | EQ-11, EQ-12, EQ-13, EQ-14 |
| IX | EQ-16, EQ-17, EQ-18 |
| X | EQ-18, EQ-19 |
