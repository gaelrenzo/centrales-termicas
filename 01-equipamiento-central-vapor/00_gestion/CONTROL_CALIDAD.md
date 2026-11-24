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

### 1.4 Capítulo
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
