# Informe de calidad gráfica — Capachica / CAD mejorado

**Fecha de generación:** 2026-10-13 · **Revisión:** P0 · **Estado de las seis láminas:** PRELIMINAR – USO ACADÉMICO – NO APTO PARA CONSTRUCCIÓN.

## Resultado por lámina

| Lámina | Salida revisada | Estado visual y geométrico |
|---|---|---|
| LP-01 | A3 horizontal, traza UTM 19S y nueve estructuras | PNG inspeccionado. Nueve IDs, progresivas 0.00–816.60 m, coordenadas UTM derivadas de la poligonal, norte, escala gráfica, ángulos en quiebres coincidentes, cuadros y tramo E-04–E-09 discontinuo con 511.39 m. Quiebres intermedios sin ID marcados para revisar replanteo. |
| PL-01 | A3 horizontal, H 1:2200 / V 1:840 aprox. | PNG inspeccionado tras separar las etiquetas próximas con llamadas. Cotas en vértices fuente diferenciadas de serie intermedia interpolada. No se dibujan catenarias ni gálibos. Alturas nominales se identifican como datos declarados; exposición y sujeciones pendientes. |
| U-01 | A3 horizontal, esquema NTS | PNG inspeccionado. Se muestran punto de derivación, protección MT pendiente, cut-outs/fusibles y pararrayos propuestos con ratings pendientes, transformador declarado, puesta a tierra conceptual y continuidad sin carga asignada. No se afirma coordinación. |
| D-01 | A3 horizontal, esquema NTS | PNG inspeccionado. PS-1 y PA-1 con vistas frontal/lateral/planta esquemáticas, familias de materiales y pendientes de dimensiones y referencias. |
| D-02 | A3 horizontal, esquema NTS | PNG inspeccionado. PR-1 y SAB-1 esquemáticos, transformador conceptual, familias de materiales y dimensiones/montaje pendientes. |
| D-03 | A3 horizontal, esquema NTS | PNG inspeccionado. Cimentación, retenida y tres electrodos PAT-3 identificados como tipológicos; disposición/espaciamiento de electrodos no inferidos. Tabla de parámetros faltantes. |

## Comprobaciones ejecutadas

- Se generaron seis archivos SVG fuente, seis DXF, seis PDF de una página A3 y seis PNG a 180 dpi. El tamaño PDF A3 se corroboró con `mutool info` (mediabox 1190.55 × 841.89 pt); PNG y PDF también se comprueban por firma en pruebas.
- Se leyeron los seis DXF con ezdxf 0.17.2 y `doc.audit()` no reportó errores. Se comprobó el layout `A3_PRELIMINAR`, unidades, capas requeridas y definiciones de bloques.
- Las pruebas CAD nuevas: **5 aprobadas**. Validan estructura/progresivas y longitud, salidas, auditoría DXF, capas/bloques/unidades/layout y advertencias de continuidad.
- Se inspeccionaron visualmente los seis PNG. La inspección identificó agrupamiento de etiquetas en PL-01; se corrigió con llamadas y se volvió a renderizar e inspeccionar.
- El ZIP `paquete_cad_preliminar.zip` contiene DXF, SVG fuente, PDF y PNG de las seis láminas.

## Límites de esta revisión

No se abrió el DXF en AutoCAD. La lectura y auditoría con ezdxf no prueban compatibilidad plena con AutoCAD ni sustituyen una revisión de impresión. El diseño de lámina se representa como geometría editable en layout A3; no usa ventanas gráficas CAD. Los detalles D-01/D-02/D-03 son esquemáticos y no constructivos. No se certifican cotas, escalas de plotter, gálibos, coordinación eléctrica ni estabilidad.
