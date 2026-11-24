# Plan de trabajo — Trabajo 01

| Campo | Valor |
|---|---|
| Trabajo | 01 — Equipamiento de una central a vapor |
| Estudiante | MAMANI GALINDO RENZO GABRIEL |
| Versión | 0.1 |
| Fecha | 2026-11-24 |
| Estado | Infraestructura completada |

## 1. Objetivo

Producir un expediente técnico que explique y compare el equipamiento de una
central a vapor, y que concluya en una selección justificada de tecnología y
combustible para un caso de estudio definido con criterios técnicos.

## 2. Productos esperados

| Producto | Ubicación | Criterio de aceptación |
|---|---|---|
| Expediente PDF | `09_informe/latex/main.pdf` → `12_entregables/` | Compilación sin errores ni referencias rotas |
| Fichas de equipo | `03_equipos/EQ-NN_*.md` | 15 campos, fuentes, esquema |
| Memoria de cálculos | `05_calculos/CALC-NN_*.md` | 8 pasos + verificación dimensional |
| Diagramas | `06_diagramas/FIG-NN_*` | Vectoriales, con leyenda y referencia |
| Presentación | `10_presentacion/` | Coherente con el expediente aprobado |

## 3. Secuencia de trabajo

| Etapa | Contenido | Capítulos | Depende de |
|---|---|---|---|
| E1 | Marco termodinámico y clasificación | II, III | Fuentes de termodinámica |
| E2 | Combustibles y combustión | IV | Matriz de combustibles |
| E3 | Generación de vapor y turbinas | V, VI | E1, E2 |
| E4 | Condensación, agua, electricidad, auxiliares | VII, VIII, IX, X | E3 |
| E5 | Cálculos de dimensionamiento | XII | E1–E4 |
| E6 | Comparación y selección | XI | E2, E5 |
| E7 | Generalidades, operación, ambiente, conclusiones | I, XIII, XIV, XV | E6 |
| E8 | Integración, PDF y presentación | Todos | E7 |

## 4. Reglas de datos

- Todo dato numérico se etiqueta `[FUENTE]`, `[HIPÓTESIS]` o
  `[EJEMPLO ACADÉMICO]`.
- Los datos de fabricante requieren modelo, catálogo y fecha.
- Las propiedades del agua se toman de una tabla identificada; las
  interpolaciones se documentan.
- Las comparaciones de eficiencia se hacen sobre la misma base (PCI,
  condiciones ISO, carga).

## 5. Control de avance

- `SEGUIMIENTO_CAPITULOS.md`: estado y pendientes por capítulo.
- `CONTROL_CALIDAD.md`: verificación técnica del trabajo.
- `REGISTRO_FUENTES.md`: alta de cada fuente `SRC-NNN`.
- `CHANGELOG.md` raíz: hitos relevantes.

## 6. Riesgos específicos

| Riesgo | Mitigación |
|---|---|
| Fijar potencia sin justificación | Mantenerla como decisión abierta hasta el cap. XI |
| Elegir combustible por preferencia | Matriz multicriterio con pesos declarados |
| Datos de fabricante sin respaldo | Exigir documento y fecha de consulta |
| Cálculos no reproducibles | Plantilla de memoria con sustitución explícita |
| Capítulos duplicados | Un tema, un capítulo; referencias cruzadas |
