# Gestión del Trabajo 01

Documentación de control del trabajo: qué se entrega, cuándo, en qué estado y
con qué calidad. **No contiene desarrollo técnico**; eso vive en las carpetas
`01_` a `09_`.

## 1. Archivos

| Archivo | Para qué sirve | Se actualiza |
|---|---|---|
| `informacion_academica.md` | Asignatura, docente, sección, grupo e integrantes | Al cambiar un dato académico |
| `calendario_entregas.md` | Fechas, horas límite, alertas y recepción de enunciados | Al cambiar una fecha o recibir información |
| `plan_trabajo.md` | Alcance, productos, cronograma, ruta crítica y riesgos | Al cambiar el alcance o el cronograma |
| `seguimiento.md` | Tablero de entregas, checklist y bitácora de avance | Al cerrar cada jornada |
| `SEGUIMIENTO_CAPITULOS.md` | Estado por capítulo (investigación, redacción, revisión) | Al avanzar un capítulo |
| `CONTROL_CALIDAD.md` | Puertas de calidad y matriz de entregables | Al revisar un entregable |
| `REGISTRO_FUENTES.md` | Alta de fuentes `SRC-NNN` | Al consultar una fuente |

## 2. Orden de lectura recomendado

1. `informacion_academica.md` — contexto del curso y del grupo.
2. `calendario_entregas.md` — qué vence y cuándo.
3. `plan_trabajo.md` — cómo se llega a esas fechas.
4. `seguimiento.md` — qué está hecho y qué sigue.
5. `SEGUIMIENTO_CAPITULOS.md` y `CONTROL_CALIDAD.md` — detalle técnico.

## 3. Qué no va aquí

- Capítulos, cálculos, fichas o diagramas (van en su carpeta propia).
- Copias de normas, libros o catálogos.
- Archivos compilados (`build/`) ni PDF intermedios.

## 4. Reglas

1. Una fecha o estado se cambia en un solo lugar y se propaga a los demás
   documentos; no se crean versiones paralelas.
2. Todo cambio de estado lleva fecha y evidencia.
3. Los estados permitidos son `PENDIENTE`, `EN INVESTIGACIÓN`, `EN DESARROLLO`,
   `EN REVISIÓN` y `APROBADO`.
4. No se registran datos académicos, rúbricas ni enunciados supuestos.

## 5. Estado

| Documento | Estado |
|---|---|
| Información académica | Registrada (2026-11-24) |
| Calendario | Vigente |
| Cronograma | Vigente |
| Seguimiento | Activo |
| Control de calidad | Activo |
| Registro de fuentes | Vacío (sin fuentes consultadas) |

## 6. Próxima acción

Cerrar ACT-01 (tabla de propiedades del agua con fuente) y registrar la fuente en
`REGISTRO_FUENTES.md`.
