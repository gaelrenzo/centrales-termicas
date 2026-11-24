# Centrales Térmicas

Expediente técnico de ingeniería desarrollado como proyecto académico de la
Escuela Profesional de Ingeniería Mecánica Eléctrica de la Universidad Nacional
del Altiplano (Puno, Perú).

| Dato | Detalle |
|---|---|
| Proyecto | Centrales Térmicas |
| Estudiante | MAMANI GALINDO RENZO GABRIEL |
| Área académica | Ingeniería Mecánica Eléctrica |
| Universidad | Universidad Nacional del Altiplano |
| Idioma | Español técnico |
| Formato principal | Expediente técnico de ingeniería (LaTeX → PDF) |
| Documento compilable | `01-equipamiento-central-vapor/09_informe/latex/main.tex` |

## Objeto del repositorio

Reunir en un solo lugar, versionado con Git, el desarrollo progresivo de cinco
trabajos universitarios independientes sobre centrales térmicas. Cada trabajo
conserva su propia documentación, cálculos, diagramas y entregables, y puede
reutilizar los recursos comunes del repositorio.

| Carpeta | Trabajo | Estado |
|---|---|---|
| `01-equipamiento-central-vapor/` | Equipamiento de una central a vapor | EN DESARROLLO — 4 entregas hasta el 24/12/2026 |
| `02-trabajo-pendiente/` | Pendiente de definición | PENDIENTE |
| `03-trabajo-pendiente/` | Pendiente de definición | PENDIENTE |
| `04-trabajo-pendiente/` | Pendiente de definición | PENDIENTE |
| `05-trabajo-pendiente/` | Pendiente de definición | PENDIENTE |

Los títulos de los trabajos 02 a 05 no se inventan: sus carpetas quedan
preparadas y se renombrarán cuando el alcance académico sea definido y
documentado en `PLAN_MAESTRO.md`.

## Estructura general

```
centrales-termicas/
├── README.md                  Presentación, alcance y estado
├── PLAN_MAESTRO.md            Fases, hitos y reglas de trabajo
├── BIBLIOGRAFIA_GENERAL.md    Jerarquía de fuentes y registro bibliográfico
├── CONTROL_CALIDAD.md         Matriz de revisión técnica del proyecto
├── CHANGELOG.md               Historial de cambios relevantes
├── recursos-compartidos/      Normas, libros, tablas, plantillas, referencias
├── 01-equipamiento-central-vapor/
├── 02-trabajo-pendiente/
├── 03-trabajo-pendiente/
├── 04-trabajo-pendiente/
└── 05-trabajo-pendiente/
```

El trabajo 01 añade dos carpetas propias de entregas —
`02_presentaciones/` (ENT-01 a ENT-03) y `03_tarea_grupal/` (ENT-04)— que no
forman parte de la secuencia `00_…12_` del expediente.

Cada trabajo numerado replica la misma organización interna:

```
<nn-trabajo>/
├── README.md            Alcance, índice y estado del trabajo
├── 00_gestion/          Plan, cronograma, control de calidad, registro de fuentes
├── 01_investigacion/    Notas de investigación y matriz de fuentes
├── 02_fundamentos/      Marco teórico
├── 03_equipos/          Fichas técnicas de equipos
├── 04_combustibles/     Combustibles y sistemas de combustión
├── 05_calculos/         Memoria de cálculos de ingeniería
├── 06_diagramas/        Diagramas vectoriales y esquemas
├── 07_normativa/        Normas y reglamentos aplicables
├── 08_bibliografia/     Base bibliográfica del trabajo
├── 09_informe/          Fuente LaTeX del expediente
├── 10_presentacion/     Material de exposición
├── 11_anexos/           Anexos del trabajo
└── 12_entregables/      Versiones finales aprobadas (PDF, PPTX)
```

## Entregas vigentes (Trabajo 01)

| ID | Actividad | Fecha | Hora límite | Estado |
|---|---|---|---|---|
| ENT-01 | Trabajo 2 — presentación individual | 2026-12-23 | 08:44 a. m. | PENDIENTE |
| ENT-02 | Trabajo 3 — presentación grupal | 2026-12-23 | 09:13 a. m. | PENDIENTE |
| ENT-03 | Trabajo 4 — presentación final grupal | 2026-12-23 | 05:36 p. m. | PENDIENTE |
| ENT-04 | Tarea grupal | 2026-12-24 | 08:07 a. m. | PENDIENTE — enunciado no recibido |

Calendario y alertas: `01-equipamiento-central-vapor/00_gestion/calendario_entregas.md`.
Cronograma: `01-equipamiento-central-vapor/00_gestion/plan_trabajo.md`.
Control de avance: `01-equipamiento-central-vapor/00_gestion/seguimiento.md`.

## Política de rigor técnico

1. Toda información técnica relevante debe tener una fuente identificable
   (norma, manual de fabricante, publicación científica o libro universitario).
2. No se inventan referencias, autores, DOI, números de norma ni páginas. Si un
   documento no puede verificarse, se registra como *consulta pendiente* en
   `BIBLIOGRAFIA_GENERAL.md` y no se cita como si estuviera verificado.
3. Se distingue explícitamente entre **dato real de fuente**, **hipótesis de
   cálculo** y **ejemplo académico**. Ningún cálculo ilustrativo se presenta
   como resultado de una central existente.
4. Las unidades siguen el Sistema Internacional; cuando se usen unidades
   industriales (bar, °C, t/h, kcal/kg) se indica la equivalencia.
5. Los archivos de normas y libros con derechos de autor no se almacenan en el
   repositorio: solo se registran sus datos bibliográficos y la ubicación de
   consulta.

## Estado de la documentación

El avance real por capítulo se controla en
`01-equipamiento-central-vapor/00_gestion/SEGUIMIENTO_CAPITULOS.md` y en
`CONTROL_CALIDAD.md`. Los estados permitidos son:

`PENDIENTE` · `EN INVESTIGACIÓN` · `EN DESARROLLO` · `EN REVISIÓN` · `APROBADO`

En la fase actual (infraestructura) todos los capítulos están en `PENDIENTE`;
existen únicamente los esqueletos LaTeX compilables.

## Compilación del expediente

Requisitos: TeX Live con `pdflatex`, `bibtex` (o `biber`, si está disponible) y
los paquetes listados en `01-equipamiento-central-vapor/09_informe/latex/README.md`.

```bash
cd 01-equipamiento-central-vapor/09_informe/latex
bash compilar.sh
```

El PDF se genera en `09_informe/latex/build/main.pdf` y se copia a
`12_entregables/` solo cuando el expediente esté aprobado. Compilación verificada
de la versión 0.1.0: 0 errores y 0 referencias sin resolver.

## Control de versiones

- Ramas: `main` (versión estable).
- Mensajes de commit con prefijo de área: `init:`, `docs:`, `research:`,
  `equipos:`, `calc:`, `diagrams:`, `report:`, `latex:`, `fix:`.
- No se versionan archivos temporales, credenciales ni material con derechos de
  autor. Ver `.gitignore`.

## Autoría y uso

Trabajo académico de MAMANI GALINDO RENZO GABRIEL. El material de terceros
citado conserva la autoría y licencia de sus fuentes originales.
