# Plan Maestro del Proyecto «Centrales Térmicas»

**Estudiante:** MAMANI GALINDO RENZO GABRIEL
**Universidad:** Universidad Nacional del Altiplano
**Área:** Ingeniería Mecánica Eléctrica
**Versión del plan:** 0.1.0 (fase de infraestructura)
**Última actualización:** 2026-11-24

---

## 1. Propósito

Construir un expediente técnico universitario riguroso, verificable y
progresivamente desarrollado sobre centrales térmicas, compuesto por cinco
trabajos independientes alojados en un único repositorio Git. El repositorio es
el registro central de investigación, cálculo, diagramación, redacción y
entregables.

El proyecto no persigue aparentar resultados de una central existente: los
cálculos son académicos y así se declaran siempre.

## 2. Alcance de los cinco trabajos

| N.º | Carpeta | Título | Alcance | Estado |
|---|---|---|---|---|
| 01 | `01-equipamiento-central-vapor/` | Equipamiento de una central a vapor | Investigación teórica y comparación de tecnologías | EN DESARROLLO |
| 02 | `02-trabajo-pendiente/` | Por definir | Por definir | PENDIENTE |
| 03 | `03-trabajo-pendiente/` | Por definir | Por definir | PENDIENTE |
| 04 | `04-trabajo-pendiente/` | Por definir | Por definir | PENDIENTE |
| 05 | `05-trabajo-pendiente/` | Por definir | Por definir | PENDIENTE |

**Regla:** los títulos, alcances y potencias de los trabajos 02 a 05 no se
inventan. Se incorporan solo cuando exista la consigna académica correspondiente
y quede registrada en este plan mediante un commit `docs:`.

### 2.1 Trabajo 01 — decisiones abiertas (no anticipar)

Estas decisiones permanecen abiertas hasta que la investigación las sustente;
no se adoptan por conveniencia narrativa:

| Decisión | Criterio para cerrarla | Estado |
|---|---|---|
| Potencia de la central | Caso de estudio definido y justificado | ABIERTA |
| Combustible seleccionado | Matriz multicriterio técnica, económica y ambiental | ABIERTA |
| Nivel de presión / recalentamiento | Análisis termodinámico comparativo | ABIERTA |
| Tipo de condensación (húmeda/seca) | Disponibilidad de agua y clima del sitio | ABIERTA |
| Configuración de turbina | Potencia, vapor disponible y régimen de operación | ABIERTA |

Combustibles obligatorios a comparar: carbón mineral, gas natural, biomasa y
combustibles líquidos. Ninguno se declara ganador de antemano.

## 3. Principios de trabajo

1. **Trazabilidad:** todo dato técnico relevante apunta a una fuente
   identificable registrada en `BIBLIOGRAFIA_GENERAL.md` o en el registro de
   fuentes del trabajo.
2. **Honestidad documental:** no se inventan referencias, autores, DOI, números
   de norma, páginas ni datos de fabricante.
3. **Separación de naturalezas:** se etiqueta cada dato como `[FUENTE]`,
   `[HIPÓTESIS]` o `[EJEMPLO ACADÉMICO]`.
4. **Unidades:** SI como sistema base; las unidades industriales se acompañan de
   su equivalencia.
5. **Trabajo por fases:** no se redactan todos los capítulos de golpe ni de
   forma superficial; cada fase se verifica antes de avanzar.
6. **Revisión por pares internos:** cada capítulo pasa por revisión técnica
   registrada en `CONTROL_CALIDAD.md` antes de `APROBADO`.

## 4. Fases de implementación

Cada fase termina con un commit (o conjunto de commits) y una verificación. Una
fase no se considera cerrada si su criterio de aceptación no se cumple.

### FASE 1 — Infraestructura del repositorio
- **Actividades:** verificar entorno; crear repositorio y estructura de cinco
  trabajos; configurar Git; publicar si hay permisos.
- **Entregables:** árbol de carpetas, `README.md`, `.gitignore`, repositorio
  remoto.
- **Aceptación:** estructura completa, primer commit, remoto verificado.
- **Estado:** COMPLETADA (ver `CHANGELOG.md`).

### FASE 2 — Documentación maestra y plantillas
- **Actividades:** `PLAN_MAESTRO.md`, `BIBLIOGRAFIA_GENERAL.md`,
  `CONTROL_CALIDAD.md`, plantillas de ficha de equipo, memoria de cálculo,
  seguimiento de capítulos y registro de fuentes; esqueleto LaTeX compilable.
- **Entregables:** documentos maestros y plantillas aprobadas.
- **Aceptación:** el esqueleto LaTeX compila sin errores y las plantillas son
  usables sin modificar su estructura.
- **Estado:** COMPLETADA (infraestructura LaTeX verificada).

### FASE 3 — Fundamentos termodinámicos (capítulos II y III)
- **Actividades:** investigar ciclo Rankine (ideal, real, recalentado,
  regenerativo), clasificación de centrales y configuraciones; registrar fuentes.
- **Entregables:** notas de investigación, capítulos II y III redactados,
  diagramas T-s base.
- **Aceptación:** ecuaciones verificadas dimensionalmente, fuentes registradas,
  revisión técnica en `EN REVISIÓN` → `APROBADO`.

### FASE 4 — Combustibles y tecnologías de combustión (capítulos IV y V parcial)
- **Actividades:** caracterizar carbón, gas natural, biomasa y combustibles
  líquidos; comparar quemadores, parrillas, lecho fluidizado y pulverizado.
- **Entregables:** fichas de combustibles, matriz comparativa, capítulo IV.
- **Aceptación:** cada propiedad con fuente; sin selección anticipada.

### FASE 5 — Fichas de equipos (capítulos V a X)
- **Actividades:** desarrollar las fichas del catálogo mínimo con la plantilla
  aprobada (calderas, quemadores, economizadores, sobrecalentadores,
  recalentadores, turbinas, condensador, bombas, desaireador, calentadores
  regenerativos, torre de enfriamiento, generador, transformador, protecciones,
  instrumentación).
- **Entregables:** fichas completas en `03_equipos/`.
- **Aceptación:** ficha con los 15 campos, fuentes y esquema identificado;
  revisión técnica registrada.

### FASE 6 — Memoria de cálculos (capítulo XII)
- **Actividades:** balances de masa y energía, ciclos Rankine, eficiencias,
  potencias, consumos, condensador y refrigeración, rendimiento global.
- **Entregables:** memoria de cálculos con datos, hipótesis, ecuaciones,
  sustitución, resultados, unidades e interpretación.
- **Aceptación:** verificación dimensional de cada cálculo y trazabilidad
  dato–hipótesis–resultado.

### FASE 7 — Diagramas
- **Actividades:** diagrama general, PFD, ciclo Rankine, T-s, P-h, esquemas de
  caldera y turbina, circuitos de agua/vapor, refrigeración y combustible, P&ID
  según alcance.
- **Entregables:** fuentes vectoriales (TikZ/SVG/Mermaid/Draw.io) con leyenda y
  numeración.
- **Aceptación:** coherencia entre diagrama y texto; referencias cruzadas
  funcionando en LaTeX.

### FASE 8 — Redacción integrada del expediente (capítulos I, XI, XIII–XV)
- **Actividades:** generalidades, comparación y selección justificada,
  operación/mantenimiento/seguridad, evaluación ambiental y eficiencia,
  conclusiones y recomendaciones; integración de todos los capítulos.
- **Entregables:** expediente completo en LaTeX.
- **Aceptación:** sin duplicación entre capítulos; nomenclatura y unidades
  consistentes; bibliografía sin entradas sin verificar.

### FASE 9 — PDF y presentación
- **Actividades:** compilar el PDF final, generar la presentación, revisar
  paginación, índices y referencias.
- **Entregables:** `12_entregables/*.pdf` y `10_presentacion/*`.
- **Aceptación:** compilación limpia (sin errores, sin referencias rotas),
  revisión visual completa.

### FASE 10 — Auditoría técnica y publicación
- **Actividades:** auditoría de calidad integral, checklist de `CONTROL_CALIDAD.md`,
  cierre de pendientes, etiqueta de versión.
- **Entregables:** versión `v1.0.0` publicada.
- **Aceptación:** todos los capítulos en `APROBADO`; ninguna fuente sin
  verificar citada como verificada.

## 5. Flujo de trabajo por capítulo

```
PENDIENTE → EN INVESTIGACIÓN → EN DESARROLLO → EN REVISIÓN → APROBADO
```

1. **Investigar:** llenar `01_investigacion/` y registrar fuentes.
2. **Desarrollar:** redactar el capítulo en `09_informe/latex/capitulos/`.
3. **Diagramar:** crear figuras en `06_diagramas/` e incluirlas con referencia.
4. **Calcular:** si aplica, agregar la memoria en `05_calculos/`.
5. **Revisar:** aplicar la lista de verificación de `CONTROL_CALIDAD.md`.
6. **Aprobar:** actualizar estado, fecha y evidencia de revisión.

## 6. Convenciones

### 6.1 Nombres de archivo
- Carpetas: `NN_nombre_en_minusculas` (ya establecidas).
- Capítulos LaTeX: `capNN_titulo_corto.tex`.
- Fichas de equipo: `EQ-NN_nombre_equipo.md`.
- Cálculos: `CALC-NN_nombre.md`.
- Diagramas: `FIG-NN_nombre.(tex|svg|mmd)`.
- Fuentes: `SRC-NNN` como identificador único en el registro.

### 6.2 Commits
Prefijos: `init:`, `docs:`, `research:`, `equipos:`, `calc:`, `diagrams:`,
`report:`, `latex:`, `fix:`, `chore:`.

### 6.3 Ramas
- `main`: línea estable.
- Ramas de trabajo: `cap-<nn>-<tema>` para capítulos extensos.
- Integración por fusión con historial lineal preferido (`--no-ff` permitido
  solo si aporta contexto).

## 7. Roles del equipo de trabajo

| Rol | Responsabilidad |
|---|---|
| Ingeniería mecánica (centrales) | Configuración de planta, equipos, materiales, mantenimiento |
| Termodinámica y máquinas térmicas | Ciclos, balances, eficiencias, validación física |
| Ingeniería eléctrica | Generador, transformador, protecciones, servicios auxiliares |
| Investigación documental | Búsqueda, verificación y registro de fuentes |
| Documentación LaTeX | Estructura, tipografía, referencias cruzadas, compilación |
| Ingeniería de software / Git | Repositorio, ramas, commits, publicación, integridad |

## 8. Riesgos y mitigación

| Riesgo | Impacto | Mitigación |
|---|---|---|
| Fuentes no verificables | Alto | Registro `SRC` con estado; no citar como verificado |
| Datos de fabricante desactualizados | Medio | Fecha de consulta y versión del documento |
| Cálculos con unidades inconsistentes | Alto | Verificación dimensional obligatoria |
| Crecimiento desordenado del repositorio | Medio | Estructura fija + `.gitignore` + revisión en cada fase |
| Duplicación de contenido entre capítulos | Medio | Responsabilidad única por capítulo y referencias cruzadas |
| Uso de material con derechos de autor | Alto | Solo registro bibliográfico, nunca el archivo |

## 9. Hitos verificables

- [x] H1 — Repositorio y estructura creados.
- [x] H2 — Documentación maestra y plantillas aprobadas.
- [x] H3 — Esqueleto LaTeX compilable.
- [ ] H4 — Capítulos II y III aprobados.
- [ ] H5 — Fichas de equipos completas.
- [ ] H6 — Memoria de cálculos verificada.
- [ ] H7 — Diagramas integrados.
- [ ] H8 — Expediente completo compilado.
- [ ] H9 — Auditoría final y versión `v1.0.0`.

## 10. Calendario académico vigente

El periodo del 24/11/2026 al 24/12/2026 queda gobernado por el calendario
académico, que comprime las fases 3 a 9. El detalle operativo está en
`01-equipamiento-central-vapor/00_gestion/calendario_entregas.md` y
`01-equipamiento-central-vapor/00_gestion/plan_trabajo.md`.

| ID | Actividad | Fecha | Hora límite | Fase asociada |
|---|---|---|---|---|
| ENT-01 | Trabajo 2 — presentación individual | 2026-12-23 | 08:44 a. m. | FASE 9 |
| ENT-02 | Trabajo 3 — presentación grupal | 2026-12-23 | 09:13 a. m. | FASE 9 |
| ENT-03 | Trabajo 4 — presentación final grupal | 2026-12-23 | 05:36 p. m. | FASE 9 |
| ENT-04 | Tarea grupal (enunciado no recibido) | 2026-12-24 | 08:07 a. m. | FASE 10 |

Reglas derivadas:

1. La prioridad es el **alcance mínimo viable** de cada entrega, no la
   terminación superficial de los quince capítulos.
2. Las tres presentaciones reutilizan el expediente y los diagramas; no generan
   contenido paralelo.
3. El enunciado de ENT-04 no se inventa: permanece bloqueado hasta su recepción.
4. Las fases 3 a 8 se solapan para llegar al 20/12/2026 con el material
   presentable cerrado.
5. Los hitos H4 a H8 se reinterpretan como avances parciales verificables dentro
   de ese periodo.

## 11. Próxima fase recomendada

**FASE 3 — Fundamentos termodinámicos.** Antes de redactar, definir con el
docente o la consigna: potencia del caso de estudio y entregable de la primera
unidad, para no fijar supuestos prematuros. Mientras tanto puede avanzarse la
investigación bibliográfica del ciclo Rankine y la clasificación de centrales,
que no depende de esas decisiones.

**Acción inmediata:** cerrar ACT-01 (tabla de propiedades del agua con fuente
verificada), por ser requisito de los cálculos y de la ruta crítica de ENT-01.
