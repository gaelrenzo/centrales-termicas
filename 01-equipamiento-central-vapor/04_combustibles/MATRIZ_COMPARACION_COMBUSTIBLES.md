# Matriz de comparación de combustibles

Documento de trabajo para el capítulo IV y la selección del capítulo XI. **No
contiene datos todavía**: define qué se va a comparar, cómo y con qué criterio,
para evitar conclusiones anticipadas.

## 1. Combustibles en comparación

| Código | Combustible | Estado de caracterización |
|---|---|---|
| CB-01 | Carbón mineral | PENDIENTE |
| CB-02 | Gas natural | PENDIENTE |
| CB-03 | Biomasa | PENDIENTE |
| CB-04 | Combustibles líquidos | PENDIENTE |

## 2. Ficha de caracterización (por combustible)

Cada combustible se documenta con estos campos, todos con fuente:

| Campo | Unidad | CB-01 | CB-02 | CB-03 | CB-04 |
|---|---|---|---|---|---|
| Poder calorífico inferior (PCI) | MJ/kg o MJ/Nm³ | | | | |
| Poder calorífico superior (PCS) | MJ/kg o MJ/Nm³ | | | | |
| Composición elemental (C, H, O, N, S) | % masa | | | | |
| Humedad | % masa | | | | |
| Cenizas | % masa | | | | |
| Azufre | % masa | | | | |
| Densidad | kg/m³ o kg/Nm³ | | | | |
| Relación aire/combustible estequiométrica | kg/kg o Nm³/Nm³ | | | | |
| Temperatura de fusión de cenizas | °C | | | | |
| Contenido de inertes / poder comburente | — | | | | |
| Estado de agregación y condiciones de suministro | — | | | | |
| Fuente (`SRC-NNN`) y base | — | | | | |

> Los valores deben corresponder a un combustible real documentado (norma,
> informe oficial o ficha de fabricante). Se declara la base: masa seca, masa
> húmeda, base seca libre de cenizas, etc.

## 3. Criterios de comparación

### 3.1 Técnicos
- Eficiencia alcanzable del ciclo según el combustible.
- Tecnología de combustión requerida (parrilla, pulverizado, lecho fluidizado,
  quemador de gas, quemador de líquidos).
- Rango de potencia viable.
- Flexibilidad de carga y velocidad de arranque.
- Requerimientos de tratamiento de gases.
- Confiabilidad y madurez tecnológica.

### 3.2 Económicos
- Costo del combustible por unidad de energía útil (no solo por tonelada).
- Inversión en sistema de combustión y manejo.
- Costos de operación y mantenimiento.
- Sensibilidad a la variación de precio.

### 3.3 Ambientales
- Emisiones específicas de CO₂ por kWh.
- SO₂, NOₓ y material particulado; necesidad de sistemas de control.
- Gestión de cenizas y residuos.
- Consumo de agua.

### 3.4 Logística y disponibilidad
- Disponibilidad regional y estacionalidad.
- Transporte y almacenamiento.
- Infraestructura requerida (gasoducto, ducto, acopio).
- Vulnerabilidad de suministro.

### 3.5 Operativos y de seguridad
- Riesgo de incendio y explosión (NFPA aplicable).
- Complejidad de operación y mantenimiento.
- Necesidades de personal y repuestos.

## 4. Matriz multicriterio (estructura)

Los pesos se definen **antes** de calificar y se justifican en el capítulo XI.
La escala de calificación y su conversión también se declaran antes de usarla.

| Criterio | Peso | CB-01 | CB-02 | CB-03 | CB-04 | Justificación del peso |
|---|---|---|---|---|---|---|
| Eficiencia del ciclo | — | | | | | |
| Inversión | — | | | | | |
| Costo de combustible | — | | | | | |
| Emisiones de CO₂ | — | | | | | |
| SO₂ / NOₓ / partículas | — | | | | | |
| Disponibilidad logística | — | | | | | |
| Complejidad operativa | — | | | | | |
| Seguridad | — | | | | | |
| Madurez tecnológica | — | | | | | |
| **Total** | 100 % | | | | | |

## 5. Reglas de honestidad técnica

1. No se califica un criterio sin fuente o sin justificación explícita.
2. Las comparaciones de emisiones se hacen por unidad de energía generada, no
   por unidad de masa de combustible.
3. Se declara la sensibilidad: qué pasaría si el peso dominante cambia.
4. La conclusión debe resistir el cambio razonable de pesos; si no, se informa
   como resultado dependiente de supuestos.
5. Ningún combustible se descarta por preferencia previa; el descarte requiere
   causa documentada.

## 6. Avance

| Métrica | Valor |
|---|---|
| Combustibles caracterizados | 0 de 4 |
| Criterios con peso definido | 0 |
| Estado de la matriz | EN DESARROLLO (estructura) |
