# Control de Calidad del Proyecto

Matriz maestra de revisión técnica. El detalle por capítulo se mantiene en
`01-equipamiento-central-vapor/00_gestion/SEGUIMIENTO_CAPITULOS.md`.

---

## 1. Estados

| Estado | Definición |
|---|---|
| `PENDIENTE` | Sin trabajo iniciado |
| `EN INVESTIGACIÓN` | Búsqueda y registro de fuentes en curso |
| `EN DESARROLLO` | Redacción, cálculo o diagramación en curso |
| `EN REVISIÓN` | Entregable completo esperando verificación técnica |
| `APROBADO` | Verificado contra toda la lista de comprobación |

Un capítulo solo pasa a `APROBADO` con evidencia registrada (fecha, revisor,
observaciones cerradas).

## 2. Lista de comprobación por capítulo

### 2.1 Coherencia física
- [ ] Los procesos descritos respetan el primer y segundo principio.
- [ ] Las temperaturas, presiones y entalpías son compatibles entre sí.
- [ ] No hay flujos de energía o masa sin justificar.
- [ ] Las irreversibilidades se reconocen (no se presenta un ciclo real como ideal).

### 2.2 Exactitud de ecuaciones
- [ ] Cada ecuación está referenciada a su fuente o deducida en el texto.
- [ ] Los símbolos están definidos antes de usarse.
- [ ] No hay errores de signo ni factores omitidos.
- [ ] Las ecuaciones numeradas coinciden con las referenciadas.

### 2.3 Consistencia dimensional
- [ ] Cada resultado declara unidad.
- [ ] Las conversiones son explícitas.
- [ ] Los balances son dimensionalmente homogéneos.
- [ ] Se distingue potencia (kW) de energía (kWh) y de flujo másico (kg/s, t/h).

### 2.4 Texto ↔ diagramas
- [ ] Cada figura está citada en el texto.
- [ ] Cada figura tiene número, título, leyenda y fuente.
- [ ] Los rótulos del diagrama coinciden con la nomenclatura del texto.
- [ ] Numeración de equipos consistente entre diagramas y fichas.

### 2.5 Referencias
- [ ] Toda cita existe en la base bibliográfica.
- [ ] Toda entrada de la base está citada en el texto (sin huérfanas).
- [ ] Ninguna entrada está en estado `PENDIENTE`.
- [ ] Formato homogéneo y completo.

### 2.6 Tablas
- [ ] Encabezados claros y unidades en el encabezado.
- [ ] Sin celdas vacías injustificadas.
- [ ] Fuente indicada.
- [ ] Cifras significativas coherentes.

### 2.7 Datos no inventados
- [ ] Los datos de fabricante tienen modelo y fecha de consulta.
- [ ] Los supuestos están marcados como `[HIPÓTESIS]`.
- [ ] Los ejemplos están marcados como `[EJEMPLO ACADÉMICO]`.
- [ ] No se atribuyen resultados a centrales reales sin fuente.

### 2.8 Nomenclatura
- [ ] Símbolos, subíndices y unidades siguen la tabla del capítulo o la global.
- [ ] Nombres de equipos idénticos en todo el expediente.
- [ ] Siglas definidas en su primera aparición.

### 2.9 Presentaciones y entregas orales

- [ ] Contiene las siete secciones: objetivo, índice, contenido técnico,
      diagramas, tablas comparativas, conclusiones y bibliografía.
- [ ] Cada diapositiva técnica remite al capítulo, figura o cálculo de origen.
- [ ] No introduce datos ausentes en el expediente.
- [ ] No duplica contenido de otra presentación sin justificación.
- [ ] Diagramas y tablas coinciden con los del expediente.
- [ ] Conclusiones sustentadas y sin afirmaciones no verificadas.
- [ ] Archivo fuente y PDF probados; carga con margen horario.

## 3. Matriz de estado — Trabajo 01

| Cap. | Título | Investigación | Redacción | Revisión técnica | Última actualización |
|---|---|---|---|---|---|
| I | Generalidades del proyecto | PENDIENTE | PENDIENTE | PENDIENTE | 2026-11-24 |
| II | Fundamentos termodinámicos | PENDIENTE | PENDIENTE | PENDIENTE | 2026-11-24 |
| III | Clasificación y configuraciones | PENDIENTE | PENDIENTE | PENDIENTE | 2026-11-24 |
| IV | Combustión y combustibles | PENDIENTE | PENDIENTE | PENDIENTE | 2026-11-24 |
| V | Generación de vapor | PENDIENTE | PENDIENTE | PENDIENTE | 2026-11-24 |
| VI | Turbinas de vapor | PENDIENTE | PENDIENTE | PENDIENTE | 2026-11-24 |
| VII | Condensación y refrigeración | PENDIENTE | PENDIENTE | PENDIENTE | 2026-11-24 |
| VIII | Tratamiento y alimentación de agua | PENDIENTE | PENDIENTE | PENDIENTE | 2026-11-24 |
| IX | Generación y transformación eléctrica | PENDIENTE | PENDIENTE | PENDIENTE | 2026-11-24 |
| X | Auxiliares, control e instrumentación | PENDIENTE | PENDIENTE | PENDIENTE | 2026-11-24 |
| XI | Comparación y selección | PENDIENTE | PENDIENTE | PENDIENTE | 2026-11-24 |
| XII | Dimensionamiento y cálculos | PENDIENTE | PENDIENTE | PENDIENTE | 2026-11-24 |
| XIII | Operación, mantenimiento y seguridad | PENDIENTE | PENDIENTE | PENDIENTE | 2026-11-24 |
| XIV | Evaluación ambiental y eficiencia | PENDIENTE | PENDIENTE | PENDIENTE | 2026-11-24 |
| XV | Conclusiones y recomendaciones | PENDIENTE | PENDIENTE | PENDIENTE | 2026-11-24 |
| — | Anexos y bibliografía | PENDIENTE | PENDIENTE | PENDIENTE | 2026-11-24 |

### 3.1 Matriz de entregas calendarizadas

| ID | Entrega | Fecha / hora | Estructura | Contenido | Diagramas | Revisión | Estado |
|---|---|---|---|---|---|---|---|
| ENT-01 | Trabajo 2 — individual | 23/12 08:44 | CREADA | PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE |
| ENT-02 | Trabajo 3 — grupal | 23/12 09:13 | CREADA | PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE |
| ENT-03 | Trabajo 4 — final grupal | 23/12 17:36 | CREADA | PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE |
| ENT-04 | Tarea grupal | 24/12 08:07 | CREADA | BLOQUEADA | — | — | PENDIENTE |

## 4. Controles automatizables

Cuando el expediente tenga contenido se ejecutarán estas comprobaciones:

```bash
# Referencias cruzadas y citas sin resolver (deben ser 0)
grep -c "??" main.log || true
grep -i "undefined" main.log || true

# Citas sin entrada bibliográfica y entradas no citadas
# (las reporta BibTeX en main.blg y el propio log)
grep -i "warning" main.blg || true

# Codificación y caracteres problemáticos
grep -rn "�" . || true
```

Criterio de compilación aceptable: **0 errores**, **0 referencias sin resolver**,
**0 citas indefinidas**. Las advertencias de tipografía se revisan una a una.

## 5. Registro de auditorías

| Fecha | Fase | Alcance | Resultado | Observaciones |
|---|---|---|---|---|
| 2026-11-24 | 1–2 | Infraestructura y esqueleto LaTeX | CONFORME | Compilación limpia del esqueleto; 0 referencias rotas |
| 2026-11-24 | 2 | Calendario, cronograma y estructura de entregas | CONFORME | Fechas registradas; enunciado de ENT-04 no recibido y declarado |

## 6. Criterios de cierre del proyecto

- Todos los capítulos en `APROBADO`.
- Cero fuentes en estado `PENDIENTE` citadas.
- Cero cálculos sin verificación dimensional.
- PDF final compilado sin errores ni referencias rotas.
- Presentación coherente con el expediente aprobado.
