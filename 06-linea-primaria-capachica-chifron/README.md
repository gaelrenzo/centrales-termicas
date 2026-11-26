# Expediente Técnico - Línea Primaria 22.9 kV Capachica - Chifrón

**Proyecto:** Instalación de línea primaria en media tensión 22.9 kV y subestación biposte SAB-1 100 kVA para el sector Chifrón, distrito de Capachica, Puno.  
**Alcance final:** Línea primaria, subestación de distribución, protecciones MT, retenidas, cimentaciones y puesta a tierra.  
**No incluido en esta entrega:** redes secundarias, acometidas domiciliarias ni alumbrado público.  

**Estudiante:** Br. Renzo Gabriel Mamani Galindo (Cód. 228447)  
**Curso:** MEC330 - Instalaciones Eléctricas II  
**Institución:** Universidad Nacional del Altiplano - FIME  
**Docentes:** Ing. Leonidas Vilca Callata / Ing. Marcos José Villanueva Cornejo  

---

## 1. Entrega Principal Para Presentar

| Orden | Archivo | Uso recomendado |
| ---: | --- | --- |
| 1 | [`REVISION_FINAL_SUPERVISOR.md`](REVISION_FINAL_SUPERVISOR.md) | Auto-revisión final y guía de defensa. |
| 2 | [`expediente/expediente_linea_primaria_22_9kv_compilado.pdf`](expediente/expediente_linea_primaria_22_9kv_compilado.pdf) | Expediente técnico compilado para revisión del ingeniero. |
| 3 | [`entregables/planos/plano_LP01_planta_linea_primaria.pdf`](entregables/planos/plano_LP01_planta_linea_primaria.pdf) | Plano de planta, traza, servidumbre y estructuras. |
| 4 | [`entregables/planos/plano_PL01_perfil_longitudinal.pdf`](entregables/planos/plano_PL01_perfil_longitudinal.pdf) | Perfil longitudinal, catenaria, spotting y gálibos. |
| 5 | [`entregables/planos/plano_U01_diagrama_unifilar_detalles.pdf`](entregables/planos/plano_U01_diagrama_unifilar_detalles.pdf) | Diagrama unifilar de media tensión y límite de alcance. |
| 6 | [`entregables/planos/plano_D01_armados_dge_ps1_pa1.pdf`](entregables/planos/plano_D01_armados_dge_ps1_pa1.pdf) | Armados DGE PS-1 y PA-1. |
| 7 | [`entregables/planos/plano_D02_armados_dge_pr1_sab1.pdf`](entregables/planos/plano_D02_armados_dge_pr1_sab1.pdf) | Armados DGE PR-1 y SAB-1. |
| 8 | [`entregables/planos/plano_D03_detalles_cimentacion_retenida_pat.pdf`](entregables/planos/plano_D03_detalles_cimentacion_retenida_pat.pdf) | Cimentación Sulzberger, retenida R-1 y PAT-3. |
| 9 | [`entregables/planos/planos_autocad_linea_primaria_capachica.zip`](entregables/planos/planos_autocad_linea_primaria_capachica.zip) | Paquete DXF A3 para AutoCAD. |

> Para una presentación limpia, abrir primero el expediente compilado y luego sustentar los planos en el orden LP-01, PL-01, U-01, D-01, D-02 y D-03.

---

## 2. Datos Técnicos Declarados (Pendientes de Validación)

| Parámetro | Valor |
| --- | --- |
| Nivel de tensión | 22.9 kV, trifásico, 3 hilos, 60 Hz |
| Longitud de eje | 0.8166 km, consistente con progresivas declaradas |
| Número de estructuras | 9 estructuras listadas, E-01 a E-09 |
| Conductor | AAAC 35 mm², parámetros de fabricante aún no adjuntos |
| Vano crítico | E-05 a E-06, 115.59 m según planilla |
| Punto de derivación | E-01, coordenada/cota declaradas; requiere conformidad de Electro Puno |
| SED | E-04, SAB-1 100 kVA según planilla |
| Estructura terminal | E-09, prog. 0+816.60 m; continuidad después de E-04 no explicada |
| Puesta a tierra | PAT-3 y R <= 10 ohm son objetivo declarado; faltan resistividad medida y prueba de campo |

**Estado técnico de los planos: preliminar, no aprobado para construcción.** La topografía disponible no acredita método ni precisión de levantamiento. El perfil y los cálculos mecánicos muestran resultados que aún no se pueden validar con evidencia primaria. Ver [auditoría de datos](documentacion/auditoria_datos_trazado.md) y [revisión de planos](documentacion/informe_revision_planos.md).

---

## 3. Planos AutoCAD

El paquete AutoCAD está en:

[`entregables/planos/autocad_lp/`](entregables/planos/autocad_lp/)

Incluye 6 archivos DXF A3:

- `LP-01_PLANTA_LINEA_PRIMARIA_A3_AUTOCAD.dxf`
- `PL-01_PERFIL_LONGITUDINAL_A3_AUTOCAD.dxf`
- `U-01_DIAGRAMA_UNIFILAR_MT_A3_AUTOCAD.dxf`
- `D-01_ARMADOS_PS1_PA1_A3_AUTOCAD.dxf`
- `D-02_ARMADOS_PR1_SAB1_A3_AUTOCAD.dxf`
- `D-03_CIMENTACION_RETENIDA_PAT3_A3_AUTOCAD.dxf`

Recomendación de ploteo: abrir cada DXF en AutoCAD, ejecutar `ZOOM EXTENTS`, configurar hoja A3 horizontal y plotear con CTB monocromo o por color según indique el docente.

---

## 4. Archivos Que No Deben Sustentar La Entrega Final

No usar como entrega principal:

- `plano_P01_redes_planta.pdf`
- `PLANO_PLANTA_REDES_Y_ACOMETIDAS_CAPACHICA.dxf`
- `TABLA_CUADRO_DE_CARGAS.dxf`
- archivos antiguos con prefijo `#` o `##`

Se conservan en el repositorio por trazabilidad, pero el paquete final defendible es el de línea primaria indicado arriba.

---

## 5. Automatización Reproducible

Scripts principales:

- [`scripts/generar_planos_ejecutivos_lp_capachica.py`](scripts/generar_planos_ejecutivos_lp_capachica.py): genera las láminas PDF, PNG y DXF base.
- [`scripts/generar_planos_autocad_lp.py`](scripts/generar_planos_autocad_lp.py): genera el paquete AutoCAD A3 y el ZIP final.
- [`scripts/compilar_expediente_lp.py`](scripts/compilar_expediente_lp.py): compila el expediente PDF final.
- [`scripts/auditar_trazado.py`](scripts/auditar_trazado.py): revisa progresivas, longitud y correspondencia entre estaciones y coordenadas; genera `documentacion/auditoria_datos_trazado.md`.

Validación heredada:

```bash
pytest proyectos/renzo-linea-primaria-capachica/tests -q
```

La suite histórica no se considera verificada: en Android/Termux su colección falla al importar `numpy` desde `scripts/calculo_mecanico_conductor.py`. La interoperabilidad DXF con AutoCAD no se comprobó. La nueva prueba CAD se ejecuta por separado, según las instrucciones de la sección 7.

## 6. Revisión e integración de fuentes

- [Auditoría de datos del trazado](documentacion/auditoria_datos_trazado.md)
- [Estado técnico y visual de los planos](documentacion/informe_revision_planos.md)
- [Evaluación de integración SEACE-CAD](documentacion/integracion_seace.md)

## 7. Láminas CAD mejoradas (revisión P0)

Los archivos revisados en esta fase están en [`entregables/mejorados/`](entregables/mejorados/). Incluye LP-01, PL-01, U-01, D-01, D-02 y D-03 en DXF/PDF/PNG, sus SVG editables como fuente gráfica y `paquete_cad_preliminar.zip`. El estado de las seis láminas es **PRELIMINAR – USO ACADÉMICO – NO APTO PARA CONSTRUCCIÓN**. Ver [informe de calidad gráfica](entregables/mejorados/informe_calidad_grafica.md), [limitaciones técnicas](entregables/mejorados/informe_limitaciones_tecnicas.md) y [resultados de pruebas](entregables/mejorados/resultados_pruebas.txt).

Motor reproducible: `scripts/cad_mejorado.py`. Instalación aislada descrita en `requirements-cad.txt`; para PDF/PNG se requiere MuPDF `mutool` en PATH. Las pruebas CAD nuevas están en `tests/test_cad_mejorado.py`. La suite heredada completa sigue bloqueada en este entorno Android por NumPy no disponible para Python 3.14; AutoCAD tampoco se ejecutó. Los DXF originales en `entregables/planos/` se conservaron.
