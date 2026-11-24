# Plan de trabajo — Trabajo 01

| Campo | Valor |
|---|---|
| Trabajo | 01 — Equipamiento de una central a vapor |
| Estudiante | MAMANI GALINDO RENZO GABRIEL |
| Versión | 1.1 |
| Fecha | 2026-11-24 |
| Alcance del plan | Del 2026-11-24 al 2026-12-24 |
| Calendario oficial | `calendario_entregas.md` |
| Control de avance | `seguimiento.md` |
| Estado | VIGENTE |

Este documento reúne el alcance y los productos del trabajo (parte I) y su
programación hacia las entregas del 23 y 24 de diciembre de 2026 (parte II).

---

# Parte I — Alcance y productos

## 1. Objetivo

Producir un expediente técnico que explique y compare el equipamiento de una
central a vapor, y que concluya en una selección justificada de tecnología y
combustible para un caso de estudio definido con criterios técnicos.

## 2. Productos esperados

| Producto | Ubicación | Criterio de aceptación |
|---|---|---|
| Expediente PDF | `../09_informe/latex/main.pdf` → `../12_entregables/` | Compilación sin errores ni referencias rotas |
| Fichas de equipo | `../03_equipos/EQ-NN_*.md` | 15 campos, fuentes, esquema |
| Memoria de cálculos | `../05_calculos/CALC-NN_*.md` | 8 pasos + verificación dimensional |
| Diagramas | `../06_diagramas/FIG-NN_*` | Vectoriales, con leyenda y referencia |
| Presentaciones | `../02_presentaciones/` | Tres entregas con las siete secciones obligatorias |
| Tarea grupal | `../03_tarea_grupal/` | Sujeta al enunciado pendiente |

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
| E8 | Integración, PDF y presentaciones | Todos | E7 |

La programación concreta de estas etapas, con fechas y solapamientos, está en la
parte II.

## 4. Reglas de datos

- Todo dato numérico se etiqueta `[FUENTE]`, `[HIPÓTESIS]` o
  `[EJEMPLO ACADÉMICO]`.
- Los datos de fabricante requieren modelo, catálogo y fecha.
- Las propiedades del agua se toman de una tabla identificada; las
  interpolaciones se documentan.
- Las comparaciones de eficiencia se hacen sobre la misma base (PCI,
  condiciones ISO, carga).

## 5. Control de avance

- `calendario_entregas.md`: fechas, horas límite y alertas.
- `seguimiento.md`: tablero de entregas y actividades.
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
| ENT-01 y ENT-02 con 29 min de diferencia | Cerrar ambas antes del 22/12 y cargar con margen |
| Enunciado de ENT-04 no recibido | No inventar alcance; reservar el 23–24/12 |
| Investigación más lenta que el cronograma | Priorizar la ruta crítica y el alcance mínimo viable |

---

# Parte II — Cronograma hacia el 23 y 24 de diciembre

## 7. Objetivo del periodo

Llegar al **23/12/2026** con:

1. Un núcleo técnico del expediente suficientemente desarrollado para sustentar
   tres presentaciones (ENT-01, ENT-02 y ENT-03).
2. Los diagramas y tablas comparativas reutilizables en las tres entregas.
3. Un plan de ejecución inmediato para ENT-04 en cuanto se reciba su enunciado.

La meta no es terminar los quince capítulos, sino **cerrar el alcance mínimo
viable** que cada entrega exige, sin presentar como terminado lo que está
pendiente.

## 8. Alcance mínimo viable por entrega

| Entrega | Contenido mínimo | Capítulos | Figuras | Cálculos |
|---|---|---|---|---|
| ENT-01 (individual, 08:44) | Panorama del equipamiento y fundamento termodinámico | I, II, III, V, VI | FIG-01, 02, 03, 07, 08 | CALC-03, 04, 07, 08 |
| ENT-02 (grupal, 09:13) | Equipamiento completo y comparación de tecnologías | I–VII, IX, XI | FIG-01 a 05, 07 a 10 | CALC-03 a 09, 11 |
| ENT-03 (grupal, 17:36) | Expediente integrado con selección justificada | I–XV (según avance) | FIG-01 a 12 | CALC-01 a 15 |
| ENT-04 (24/12, 08:07) | **Por definir** | — | — | — |

## 9. Cronograma por fases

Las fases se solapan a propósito: la investigación alimenta fichas, cálculos y
diagramas en paralelo.

| Fase | Actividad | Inicio | Fin | Entregable | Depende de |
|---|---|---|---|---|---|
| F3 | Fundamentos termodinámicos | 2026-11-24 | 2026-11-29 | Caps. II–III; CALC-03…07; FIG-03…05 | Tabla de vapor con fuente |
| F4 | Combustibles y combustión | 2026-11-27 | 2026-12-04 | Cap. IV; CB-01…04; matriz; FIG-11 | Fuentes de caracterización |
| F5 | Fichas de equipos | 2026-12-01 | 2026-12-10 | EQ-01…EQ-19 | F3, F4 |
| F6 | Memoria de cálculos | 2026-12-03 | 2026-12-12 | CALC-01…CALC-15 | F3, F5 |
| F7 | Diagramas | 2026-12-05 | 2026-12-14 | FIG-01…FIG-12 | F3–F6 |
| F8 | Redacción e integración | 2026-12-08 | 2026-12-18 | Caps. I, V–XV; PDF compilado | F3–F7 |
| P1 | Preparar ENT-01 | 2026-12-15 | 2026-12-22 | Presentación individual | F3, F5, F7 |
| P2 | Preparar ENT-02 | 2026-12-16 | 2026-12-22 | Presentación grupal | F4, F6, F7 |
| P3 | Preparar ENT-03 | 2026-12-18 | 2026-12-23 | Presentación final grupal | F8 |
| TG | Tarea grupal | 2026-12-23 | 2026-12-24 | Según enunciado | Enunciado no recibido |

### 9.1 Vista semanal

| Semana | Fechas | Foco principal | Control |
|---|---|---|---|
| S1 | 24–29 nov | Fundamentos, tabla de vapor, ciclo Rankine | Fuentes `SRC` registradas |
| S2 | 30 nov–6 dic | Combustibles, primeras fichas, cálculos del ciclo | Matriz de combustibles con datos |
| S3 | 7–13 dic | Fichas restantes, cálculos completos, primeras figuras | Verificación dimensional |
| S4 | 14–20 dic | Redacción, figuras finales, borradores de presentaciones | Compilación limpia; D-7 |
| S5 | 21–23 dic | Cierre, ensayo, carga de ENT-01/02/03 | D-1 y D-0 |
| S6 | 24 dic | ENT-04 | Enunciado recibido |

## 10. Ruta crítica

```
Tabla de vapor con fuente
   → CALC-03/04 (Rankine)
   → FIG-03/04/05 (esquemas T-s)
   → Cap. II
   → ENT-01 (23/12 08:44)

Fichas EQ + CALC-08/09/11
   → FIG-07/08/09/10
   → Cap. V–VII
   → ENT-02 (23/12 09:13)

Integración completa + selección (Cap. XI)
   → PDF compilado
   → ENT-03 (23/12 17:36)
```

Cualquier retraso en la tabla de vapor o en el ciclo Rankine impacta
directamente en ENT-01. Es la primera prioridad.

## 11. Reutilización y no duplicación

| Recurso | Fuente única | Se reutiliza en |
|---|---|---|
| Marco termodinámico | `../02_fundamentos/` y cap. II | ENT-01, ENT-02, ENT-03 |
| Fichas de equipos | `../03_equipos/EQ-*.md` | ENT-02, ENT-03 |
| Comparación de combustibles | `../04_combustibles/` y cap. XI | ENT-02, ENT-03 |
| Cálculos | `../05_calculos/CALC-*.md` | ENT-01, ENT-02, ENT-03 |
| Diagramas | `../06_diagramas/FIG-*` | Las tres entregas |
| Texto del expediente | `../09_informe/latex/` | Base de todas las presentaciones |

Regla: una presentación **selecciona y resume**; no crea una segunda versión de
los datos. Si una diapositiva necesita un dato nuevo, primero se incorpora al
expediente con su fuente.

## 12. Puntos de control

| Control | Fecha | Criterio de aprobación |
|---|---|---|
| C1 | 2026-12-09 | Caps. II–III en `EN REVISIÓN`; CALC-03…07 verificados |
| C2 | 2026-12-16 | Tres borradores de presentación con las siete secciones |
| C3 | 2026-12-20 | Figuras y tablas definitivas; PDF compilado sin referencias rotas |
| C4 | 2026-12-22 | Ensayo completo; archivos probados en el equipo de exposición |
| C5 | 2026-12-23 | ENT-01, ENT-02 y ENT-03 cargadas |
| C6 | 2026-12-24 | ENT-04 cargada según enunciado recibido |

## 13. Reglas de ejecución

1. Actualizar `seguimiento.md` al cerrar cada jornada de trabajo.
2. No marcar una entrega como lista sin PDF/archivo de respaldo probado.
3. No inventar enunciados, rúbricas, integrantes ni duraciones.
4. Registrar cada fuente nueva antes de usarla en una diapositiva.
5. Los cambios de alcance se reflejan en este plan y en `calendario_entregas.md`.
