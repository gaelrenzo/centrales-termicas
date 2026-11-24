# Cálculos

Memoria de cálculos de ingeniería del ciclo y de los equipos. Cada cálculo debe
poder reproducirse con los datos e hipótesis declarados.

## 1. Índice

El alcance completo, dependencias y orden de ejecución están en
[`INDICE_CALCULOS.md`](INDICE_CALCULOS.md). Son 15 cálculos: `CALC-01` a
`CALC-15`.

## 2. Nomenclatura de archivos

```
CALC-NN_nombre.md
```

Ejemplos: `CALC-03_rankine_ideal.md`, `CALC-11_balance_condensador.md`.

## 3. Plantilla obligatoria

[`PLANTILLA_MEMORIA_CALCULO.md`](../../recursos-compartidos/plantillas/PLANTILLA_MEMORIA_CALCULO.md)

Pasos mínimos: objetivo, datos, hipótesis, ecuaciones, sustitución numérica,
resultados, comprobación de unidades e interpretación física.

## 4. Reglas

1. Cada dato se clasifica como `[FUENTE]`, `[HIPÓTESIS]` o
   `[EJEMPLO ACADÉMICO]`.
2. Las propiedades del agua provienen de una tabla identificada; toda
   interpolación se documenta.
3. Los resultados son dimensionalmente homogéneos y físicamente plausibles.
4. Los cálculos de ciclos ideales no se presentan como el comportamiento de una
   central real.
5. El caso de estudio (potencia, presiones, temperaturas) se fija en el capítulo
   XI y se propaga a toda la memoria.

## 5. Qué no va aquí

- Fichas descriptivas de equipos (van en `../03_equipos/`).
- Figuras T-s o P-h como imagen final (se producen en `../06_diagramas/`).
- Hojas de cálculo temporales o archivos de software sin documentar.

## 6. Estado

| Métrica | Valor |
|---|---|
| Cálculos requeridos | 15 |
| Aprobados | 0 |
| Pendientes | 15 |

## 7. Próximos pasos

1. Cerrar la tabla de vapor (ACT-01), requisito de todos los cálculos.
2. `CALC-03` y `CALC-04` (Rankine ideal y real) para la ruta crítica de ENT-01.
3. `CALC-08` (potencia de turbina) al cerrar las fichas de turbinas.
