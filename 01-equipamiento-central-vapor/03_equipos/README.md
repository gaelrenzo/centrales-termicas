# Equipos

Fichas técnicas de los equipos de la central a vapor. Cada ficha explica qué hace
el equipo, cómo funciona, cómo se selecciona y cómo se mantiene, siempre con
fuente identificable.

## 1. Índice

El catálogo completo, con códigos, capítulos y estado, está en
[`CATALOGO_EQUIPOS.md`](CATALOGO_EQUIPOS.md). Contiene 19 fichas obligatorias:
`EQ-01` a `EQ-19`.

## 2. Nomenclatura de archivos

```
EQ-NN_nombre_equipo.md
```

Ejemplos: `EQ-01_caldera_acuotubular.md`, `EQ-10_condensador.md`.

## 3. Plantilla obligatoria

[`PLANTILLA_FICHA_EQUIPO.md`](../../recursos-compartidos/plantillas/PLANTILLA_FICHA_EQUIPO.md)

Los 15 campos no se eliminan; si un campo no aplica, se escribe «No aplica» y se
justifica.

## 4. Reglas

1. Todo parámetro lleva unidad y fuente, o la marca `[HIPÓTESIS]`.
2. Los datos de fabricante requieren modelo, documento y fecha de consulta.
3. Los materiales citados llevan su norma de material.
4. El esquema del equipo se referencia con su código `FIG-NN` de
   `../06_diagramas/`.
5. La nomenclatura coincide con el diagrama de flujo y con el P&ID.
6. No se afirma disponibilidad comercial local sin fuente.

## 5. Qué no va aquí

- Cálculos del ciclo (van en `../05_calculos/`).
- Figuras fuente (van en `../06_diagramas/`; aquí solo se referencian).
- Texto del capítulo (va en `../09_informe/latex/capitulos/`).

## 6. Estado

| Métrica | Valor |
|---|---|
| Fichas requeridas | 19 |
| Fichas aprobadas | 0 |
| Fichas pendientes | 19 |

## 7. Próximos pasos

1. `EQ-01` y `EQ-02` (calderas) tras cerrar los fundamentos.
2. `EQ-03` (quemador) al completar la matriz de combustibles.
3. `EQ-07` a `EQ-09` (turbinas) para alimentar ENT-01.
