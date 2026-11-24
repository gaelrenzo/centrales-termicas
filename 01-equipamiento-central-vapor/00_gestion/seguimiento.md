# Control de avance — Trabajo 01

| Campo | Valor |
|---|---|
| Documento | Tablero de seguimiento de actividades y entregas |
| Trabajo | 01 — Equipamiento de una central a vapor |
| Versión | 1.0 |
| Fecha de corte | 2026-11-24 |
| Calendario | `calendario_entregas.md` |
| Cronograma | `plan_trabajo.md` |
| Estado de capítulos | `SEGUIMIENTO_CAPITULOS.md` |

Estados permitidos: `PENDIENTE` · `EN INVESTIGACIÓN` · `EN DESARROLLO` ·
`EN REVISIÓN` · `APROBADO`.

## 1. Tablero de entregas

| ID | Entrega | Fecha / hora | Estado | Avance | Semáforo | Próxima acción |
|---|---|---|---|---|---|---|
| ENT-01 | Trabajo 2 — presentación individual | 23/12 08:44 | PENDIENTE | 0 % | 🔴 Rojo | Cerrar cap. II y FIG-03 |
| ENT-02 | Trabajo 3 — presentación grupal | 23/12 09:13 | PENDIENTE | 0 % | 🔴 Rojo | Definir integrantes y reparto |
| ENT-03 | Trabajo 4 — presentación final grupal | 23/12 17:36 | PENDIENTE | 0 % | 🔴 Rojo | Cerrar cap. XI (selección) |
| ENT-04 | Tarea grupal | 24/12 08:07 | PENDIENTE | 0 % | ⚫ Bloqueado | Esperar enunciado |

Criterio del semáforo:

| Color | Significado |
|---|---|
| 🟢 Verde | En fecha según `plan_trabajo.md` y sin bloqueos |
| 🟡 Ámbar | Retraso menor a 3 días o dependencia en riesgo |
| 🔴 Rojo | Retraso mayor a 3 días o insumo crítico inexistente |
| ⚫ Bloqueado | No puede avanzar por información externa faltante |

## 2. Checklist por entrega

Cada entrega se considera lista solo con los ocho puntos cerrados.

### ENT-01 — Trabajo 2 (individual, 23/12 08:44)

- [ ] Objetivo definido y alineado con la rúbrica
- [ ] Índice cerrado
- [ ] Contenido técnico desde caps. I, II, III, V y VI
- [ ] Diagramas FIG-01, 02, 03, 07 y 08 integrados
- [ ] Tablas comparativas (configuraciones y equipos)
- [ ] Conclusiones sustentadas en el expediente
- [ ] Bibliografía con fuentes verificadas
- [ ] Archivo probado y cargado con 60 min de margen

### ENT-02 — Trabajo 3 (grupal, 23/12 09:13)

- [ ] Integrantes y roles registrados
- [ ] Objetivo e índice acordados con el grupo
- [ ] Contenido técnico desde caps. I–VII, IX y XI
- [ ] Diagramas FIG-01 a 05 y 07 a 10
- [ ] Tablas comparativas de combustibles y tecnologías
- [ ] Conclusiones grupales consensuadas
- [ ] Bibliografía común
- [ ] Archivo probado y cargado con 60 min de margen

### ENT-03 — Trabajo 4 (grupal, 23/12 17:36)

- [ ] Integrantes y roles registrados
- [ ] Objetivo e índice del trabajo final
- [ ] Contenido integrado con la selección justificada (cap. XI)
- [ ] Diagramas FIG-01 a 12 (según alcance)
- [ ] Tablas resumen de cálculos (CALC-01 a 15)
- [ ] Conclusiones y recomendaciones
- [ ] Bibliografía completa y verificada
- [ ] Archivo probado y cargado con 60 min de margen

### ENT-04 — Tarea grupal (24/12 08:07)

- [ ] Enunciado recibido y archivado en `../03_tarea_grupal/enunciado/`
- [ ] Alcance y entregable identificados
- [ ] Reparto de tareas del grupo
- [ ] Desarrollo
- [ ] Revisión
- [ ] Entrega cargada
- [ ] Evidencia de recepción guardada
- [ ] (Los criterios definitivos se fijan al recibir el enunciado)

## 3. Actividades técnicas en curso

| ID | Actividad | Fase | Estado | Avance | Bloqueo | Responsable |
|---|---|---|---|---|---|---|
| ACT-01 | Tabla de propiedades del agua con fuente | F3 | PENDIENTE | 0 % | Requiere fuente verificada | Individual |
| ACT-02 | Caps. II–III (fundamentos y clasificación) | F3 | PENDIENTE | 0 % | Depende de ACT-01 | Individual |
| ACT-03 | CALC-03…07 (ciclos y eficiencia) | F3/F6 | PENDIENTE | 0 % | Depende de ACT-01 | Individual |
| ACT-04 | Matriz de combustibles con datos | F4 | PENDIENTE | 0 % | Requiere fuentes CB-01…04 | Individual |
| ACT-05 | Fichas EQ-01…19 | F5 | PENDIENTE | 0 % | Depende de ACT-02/04 | Individual |
| ACT-06 | CALC-01…15 | F6 | PENDIENTE | 0 % | Depende de ACT-05 | Individual |
| ACT-07 | FIG-01…12 | F7 | PENDIENTE | 0 % | Depende de ACT-03/06 | Individual |
| ACT-08 | Redacción e integración del expediente | F8 | PENDIENTE | 0 % | Depende de ACT-02…07 | Individual |
| ACT-09 | ENT-01 | P1 | PENDIENTE | 0 % | Depende de ACT-02/07 | Individual |
| ACT-10 | ENT-02 | P2 | PENDIENTE | 0 % | Integrantes por confirmar | Grupal |
| ACT-11 | ENT-03 | P3 | PENDIENTE | 0 % | Integrantes por confirmar | Grupal |
| ACT-12 | ENT-04 | TG | PENDIENTE | 0 % | Enunciado no recibido | Grupal |

## 4. Bitácora de avance

| Fecha | Actividad | Avance registrado | Evidencia | Estado resultante |
|---|---|---|---|---|
| 2026-11-24 | Infraestructura del repositorio | Estructura, plantillas, LaTeX compilable, calendario y cronograma | Commits en `main` | Completado |
| 2026-11-24 | Calendarización | Cuatro entregas registradas con alertas D-14/D-7/D-3/D-1 | `calendario_entregas.md` | Completado |

## 5. Reglas de actualización

1. El avance se calcula como checklist cerrado / checklist total; no se estima
   «a ojo».
2. Un cambio de estado se registra en la bitácora con fecha y evidencia.
3. Si una entrega pasa a 🟡 o 🔴, se escribe la causa y la acción correctiva en
   la bitácora.
4. ENT-04 permanece ⚫ hasta que el enunciado esté archivado.
5. Al cerrar cada jornada: actualizar avance, semáforo y próxima acción.

## 6. Próxima acción inmediata

Cerrar **ACT-01**: seleccionar y registrar una tabla de propiedades del agua con
fuente verificada, requisito de todos los cálculos y de ENT-01.
