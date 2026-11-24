# Control de calidad — Trabajo 01

Complementa la lista general de `../../CONTROL_CALIDAD.md`. Aquí se registran las
verificaciones específicas del expediente y su evidencia.

## 1. Puertas de calidad por entregable

### 1.1 Ficha de equipo (`EQ-NN`)
- [ ] Los 15 campos obligatorios están presentes.
- [ ] Parámetros con unidad y fuente (o `[HIPÓTESIS]`).
- [ ] Materiales con norma cuando se citen.
- [ ] Fabricantes con documento y fecha de consulta.
- [ ] Esquema identificado y citado en el capítulo.
- [ ] Nomenclatura idéntica al diagrama de flujo.

### 1.2 Memoria de cálculo (`CALC-NN`)
- [ ] Objetivo, datos, hipótesis, ecuaciones, sustitución, resultado, unidades e
      interpretación.
- [ ] Naturaleza de cada dato declarada.
- [ ] Verificación dimensional completa.
- [ ] Límites físicos comprobados (`0 < η < 1`, temperaturas coherentes).
- [ ] Resultado reproducible con los datos declarados.

### 1.3 Diagrama (`FIG-NN`)
- [ ] Fuente vectorial versionada (TikZ, SVG, Mermaid o Draw.io).
- [ ] Numeración de equipos coherente con las fichas.
- [ ] Leyenda, unidades y sentido de flujo.
- [ ] Referenciado en el texto y con leyenda «Fuente: …».
- [ ] Legible en escala de grises.

### 1.4 Presentación (`ENT-0N`)
- [ ] Las siete secciones obligatorias están presentes.
- [ ] Cada dato remite al capítulo, figura o cálculo de origen.
- [ ] Diagramas y tablas coinciden con el expediente.
- [ ] Conclusiones sustentadas y sin datos nuevos.
- [ ] Sin duplicación innecesaria entre presentaciones.
- [ ] Archivo probado y carga con 60 min de margen.

### 1.5 Capítulo
- [ ] Coherencia con los capítulos vecinos y sin duplicación.
- [ ] Ecuaciones numeradas y referenciadas.
- [ ] Tablas y figuras citadas antes de aparecer.
- [ ] Citas resueltas y bibliografía sin huérfanas.
- [ ] Conclusiones parciales coherentes con los datos presentados.

## 2. Matriz de entregables

| Entregable | Código | Estado | Verificado por | Fecha | Observaciones |
|---|---|---|---|---|---|
| Catálogo de equipos | `CATALOGO_EQUIPOS.md` | EN DESARROLLO | — | 2026-11-24 | Estructura creada, fichas pendientes |
| Matriz de combustibles | `MATRIZ_COMPARACION_COMBUSTIBLES.md` | EN DESARROLLO | — | 2026-11-24 | Criterios definidos, datos pendientes |
| Índice de cálculos | `INDICE_CALCULOS.md` | EN DESARROLLO | — | 2026-11-24 | Alcance definido, cálculos pendientes |
| Inventario de diagramas | `INVENTARIO_DIAGRAMAS.md` | EN DESARROLLO | — | 2026-11-24 | Figuras planificadas, fuentes pendientes |
| Esqueleto LaTeX | `09_informe/latex/main.tex` | APROBADO | — | 2026-11-24 | Compila sin errores ni referencias rotas |
| Calendario de entregas | `00_gestion/calendario_entregas.md` | APROBADO | — | 2026-11-24 | Cuatro entregas y alertas registradas |
| Cronograma | `00_gestion/plan_trabajo.md` | APROBADO | — | 2026-11-24 | Fases, ruta crítica y puntos de control |
| Control de avance | `00_gestion/seguimiento.md` | APROBADO | — | 2026-11-24 | Tablero y checklist por entrega |
| ENT-01 presentación individual | `02_presentaciones/trabajo_02/` | PENDIENTE | — | 2026-11-24 | Estructura creada, contenido pendiente |
| ENT-02 presentación grupal | `02_presentaciones/trabajo_03_grupal/` | PENDIENTE | — | 2026-11-24 | Integrantes y rúbrica por confirmar |
| ENT-03 presentación final grupal | `02_presentaciones/trabajo_04_final/` | PENDIENTE | — | 2026-11-24 | Integrantes y rúbrica por confirmar |
| ENT-04 tarea grupal | `03_tarea_grupal/` | PENDIENTE | — | 2026-11-24 | Enunciado no recibido; alcance no definido |

## 3. Registro de no conformidades

| Fecha | Elemento | No conformidad | Acción correctiva | Estado |
|---|---|---|---|---|
| — | — | — | — | — |

## 4. Comprobaciones de integridad antes de cada entrega

```bash
# 1. Compilación limpia
cd 09_informe/latex && latexmk -pdf -outdir=build main.tex

# 2. Referencias y citas sin resolver
grep -Ei "undefined|multiply defined" build/main.log || echo "OK"

# 3. Figuras y tablas declaradas pero no incluidas
grep -rn "FIG-" 06_diagramas/INVENTARIO_DIAGRAMAS.md | wc -l
ls 09_informe/latex/figuras/

# 4. Fuentes citadas sin ficha
grep -rho "SRC-[0-9]\+" 09_informe/latex/ | sort -u
```

## 5. Criterio de aprobación del trabajo

1. Los 15 capítulos en `APROBADO`.
2. Catálogo de equipos completo (todas las fichas requeridas).
3. Memoria de cálculos completa y verificada.
4. Diagramas integrados y coherentes con el texto.
5. PDF final compilado sin errores ni referencias rotas.
