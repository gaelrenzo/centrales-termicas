# Índice de cálculos — Trabajo 01

Cada cálculo se desarrolla con
`../../recursos-compartidos/plantillas/PLANTILLA_MEMORIA_CALCULO.md` y se guarda
como `CALC-NN_nombre.md`.

Estados: `PENDIENTE` · `EN DESARROLLO` · `EN REVISIÓN` · `APROBADO`

## 1. Balances y ciclo

| Código | Cálculo | Entradas principales | Salidas | Depende de | Cap. | Estado |
|---|---|---|---|---|---|---|
| CALC-01 | Balance de masa del ciclo | Caudales de vapor, extracciones, purgas | Caudal de alimentación, agua de reposición | — | XII | PENDIENTE |
| CALC-02 | Balance de energía global | Flujos entálpicos, potencias, pérdidas | Calor aportado, calor rechazado, trabajo neto | CALC-01 | XII | PENDIENTE |
| CALC-03 | Ciclo Rankine ideal | Presiones, temperaturas, estados | Trabajo de turbina y bomba, η térmica | Tablas de vapor | II, XII | PENDIENTE |
| CALC-04 | Ciclo Rankine real | Rendimientos isoentrópicos, pérdidas de presión | Trabajo real, η térmica | CALC-03 | II, XII | PENDIENTE |
| CALC-05 | Rankine con recalentamiento | Presión y temperatura de recalentamiento | Trabajo adicional, η térmica | CALC-04 | II, XII | PENDIENTE |
| CALC-06 | Rankine regenerativo | Extracciones, calentadores | Ahorro de calor, η térmica | CALC-04 | II, XII | PENDIENTE |
| CALC-07 | Eficiencia térmica del ciclo | Calores y trabajos | η térmica | CALC-03…06 | XII | PENDIENTE |

## 2. Potencias y consumos

| Código | Cálculo | Entradas principales | Salidas | Depende de | Cap. | Estado |
|---|---|---|---|---|---|---|
| CALC-08 | Potencia de turbina | Caudal, salto entálpico, η isoentrópico | Potencia mecánica/eléctrica | CALC-03…06 | VI, XII | PENDIENTE |
| CALC-09 | Consumo de vapor | Potencia objetivo, salto entálpico | Caudal másico de vapor | CALC-08 | XII | PENDIENTE |
| CALC-10 | Potencia de bombas | Caudal, altura, rendimiento | Potencia de accionamiento | CALC-01 | VIII, XII | PENDIENTE |
| CALC-13 | Eficiencia de caldera | Calor absorbido, PCI, caudal de combustible | η de caldera | CALC-14 | V, XII | PENDIENTE |
| CALC-14 | Consumo de combustible | Calor aportado, PCI, η de caldera | Caudal de combustible | CALC-02, CALC-13 | IV, XII | PENDIENTE |
| CALC-15 | Rendimiento global de la central | Potencia neta, energía del combustible | η global, consumo específico | CALC-08…14 | XII, XIV | PENDIENTE |

## 3. Condensador y refrigeración

| Código | Cálculo | Entradas principales | Salidas | Depende de | Cap. | Estado |
|---|---|---|---|---|---|---|
| CALC-11 | Balance del condensador | Vapor condensado, entalpías | Calor rechazado | CALC-09 | VII, XII | PENDIENTE |
| CALC-12 | Caudal de agua de refrigeración | Calor rechazado, ΔT admisible | Caudal de refrigeración | CALC-11 | VII, XII | PENDIENTE |

## 4. Orden de ejecución

```
CALC-01 → CALC-03 → CALC-04 → CALC-05 → CALC-06 → CALC-07
CALC-02 → CALC-08 → CALC-09 → CALC-11 → CALC-12
CALC-10 → CALC-13 → CALC-14 → CALC-15
```

## 5. Reglas

1. Todo cálculo declara el origen de sus datos y separa `[FUENTE]`,
   `[HIPÓTESIS]` y `[EJEMPLO ACADÉMICO]`.
2. Las propiedades del agua provienen de una tabla identificada; la interpolación
   se documenta.
3. Cada resultado se comprueba dimensionalmente y se compara con el orden de
   magnitud típico de la literatura.
4. Los cálculos de ciclos ideales no se presentan como el comportamiento de una
   central real.
5. El caso de estudio (potencia, presiones, temperaturas) se fija recién en el
   capítulo XI y se propaga a toda la memoria.

## 6. Avance

| Métrica | Valor |
|---|---|
| Cálculos requeridos | 15 |
| Aprobados | 0 |
| Pendientes | 15 |
