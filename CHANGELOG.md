# Changelog

Todos los cambios relevantes del proyecto se registran aquí.
Formato basado en *Keep a Changelog*; versionado semántico adaptado a un
proyecto documental.

## [Unreleased]

## [0.3.0] — 2026-11-24

### Añadido

- `00_gestion/informacion_academica.md` con asignatura, docente, sección, grupo
  e integrantes del Grupo 7.
- Datos del docente, sección y grupo en la portada, la ficha de control y los
  índices del proyecto.

### Cambiado

- Asignatura actualizada a **Centrales Termoeléctricas**.
- Docente responsable: Paredes Pareja Walter Oswaldo.
- Sección: Grupo A · Grupo: 7.
- Presentaciones ENT-02 y ENT-03 y tarea grupal ENT-04 con los cuatro
  integrantes registrados; los roles de exposición siguen por asignar.
- Condiciones del calendario y del tablero actualizadas: integrantes definidos,
  rúbricas y enunciado aún pendientes.

### Notas

- La autoría del expediente del Trabajo 01 sigue siendo individual (Mamani
  Galindo Renzo Gabriel); la autoría grupal corresponde a ENT-02, ENT-03 y
  ENT-04.
- No se inventaron correos, códigos de estudiante, roles ni rúbricas.

## [0.2.0] — 2026-11-24

### Añadido

- `00_gestion/calendario_entregas.md` con las cuatro actividades académicas,
  horas límite y alertas D-14/D-7/D-3/D-1.
- `00_gestion/plan_trabajo.md`: plan unificado de alcance, productos, cronograma
  por fases, ruta crítica, reutilización y puntos de control.
- `00_gestion/seguimiento.md`: tablero de entregas, checklist de ocho puntos y
  bitácora de avance.
- Estructura `02_presentaciones/` con las entregas ENT-01, ENT-02 y ENT-03.
- Estructura `03_tarea_grupal/` con `enunciado/`, `investigacion/` y
  `entregables/`, bloqueada por enunciado no recibido.
- `PLANTILLA_PRESENTACION.md` en recursos compartidos.
- Sección de control de presentaciones en `CONTROL_CALIDAD.md`.

### Cambiado

- `PLAN_TRABAJO.md` pasa a `plan_trabajo.md` e integra el cronograma académico;
  se conserva todo el contenido de alcance y productos.
- `10_presentacion/` queda como carpeta reasignada y remite a
  `02_presentaciones/`; no se elimina para conservar el historial.
- El README principal y el README del trabajo 01 incluyen el calendario vigente.

### Notas

- Las fechas y horas se transcriben de la comunicación académica; no se
  inventaron rúbricas, duraciones, integrantes ni el enunciado de ENT-04.
- No se modificó la investigación existente.

## [0.1.0] — 2026-11-24

### Añadido

- Estructura del repositorio con los cinco trabajos y los recursos compartidos.
- `README.md` principal con alcance, política de rigor y estructura.
- `PLAN_MAESTRO.md` con las diez fases, hitos, roles, riesgos y convenciones.
- `BIBLIOGRAFIA_GENERAL.md` con jerarquía de fuentes, estados y registro `SRC`.
- `CONTROL_CALIDAD.md` con lista de comprobación y matriz de capítulos.
- Plantillas de ficha de equipo, memoria de cálculo, seguimiento de capítulos y
  registro de fuentes.
- Estructura interna completa del trabajo 01 y documentos de gestión.
- Esqueleto LaTeX compilable: `main.tex`, preámbulo, portada universitaria,
  quince capítulos independientes, anexo, base bibliográfica y script de
  compilación.
- `.gitignore` para LaTeX, temporales, credenciales y material con derechos de
  autor.

### Notas

- Los capítulos I a XV existen como esqueletos con estado `PENDIENTE`; no
  contienen desarrollo técnico todavía.
- La base `bibliografia.bib` está vacía a propósito: solo se incorporarán
  fuentes verificadas.
- No se ha fijado potencia, combustible ganador ni configuración de planta.
