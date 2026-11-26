# Informe de limitaciones técnicas y datos pendientes

Las láminas y el motor se mantienen en estado **PRELIMINAR – NO APTO PARA CONSTRUCCIÓN**. Ningún valor declarado en archivos de proyecto se trata como medición verificada por esta generación.

## Datos y definiciones pendientes

- **Topografía:** no se adjuntó ráster DEM/SRTM ni informe de precisión. Las cotas intermedias del perfil son interpolaciones, no levantamientos independientes. Requiere levantamiento de campo, sistema geodésico/EPSG confirmado y verificación de obstáculos, cruces y servidumbre.
- **Estructuras y progresivas:** se preservan nueve estructuras y 816.60 m según planillas. Algunas posiciones se interpolan sobre la poligonal PENZD. Los quiebres sin soporte identificado requieren replanteo/decisión de ubicación.
- **E-04–E-09:** E-04 se representa como ubicación declarada de SAB-1. E-09 es extremo del trazado documentado. Los 511.39 m entre ambos son continuidad de función pendiente; no se declara E-04 terminal ni se asignan cargas a E-05–E-09.
- **Perfil mecánico:** no hay trazabilidad suficiente para calcular catenarias, flechas y gálibos. Faltan ficha certificada del AAAC 35 mm² (masa, diámetro, módulo, coeficiente térmico y resistencia), hipótesis de temperatura/viento/hielo aplicables, tensiones de tendido y condición de regulación. No se dibujan curvas de conductor.
- **Armados:** verificar nomenclatura/aplicabilidad, edición y lámina DGE específica, estándar de concesionaria y materiales. Las representaciones PS-1, PA-1, PR-1 y SAB-1 no afirman dimensiones oficiales. Faltan selección de aisladores, distancias eléctricas, herrajes y cargas admisibles.
- **Protecciones MT:** faltan cortocircuito en el punto de derivación, curvas/fichas, coordinación aguas arriba y criterios de la concesionaria. Cut-outs/fusibles y pararrayos son propuestas representativas sin rating seleccionado.
- **Cimentaciones y retenidas:** faltan geotecnia, cargas de apoyo, geometría aprobada y fichas de cable/anclaje. No se verifica Sulzberger ni tiro/estabilidad.
- **PAT-3:** el plano declara tres electrodos pero su separación y disposición no están sustentadas. El dibujo los separa únicamente para distinguir símbolos. Resistividad Wenner, configuración, materiales, uniones y medición final pendientes. El objetivo 10 Ω es declarado; no se garantiza. Cualquier valor calculado en documentos fuente no equivale a ensayo de campo.

## Software y dependencias en Android/Termux

Se creó un entorno aislado en `/tmp/capachica-cad-venv`. Dependencias disponibles: ezdxf 0.17.2 y pytest 9.1.1. La generación usa además biblioteca estándar Python y `mutool` para SVG → PDF → PNG. No se alteraron paquetes globales.

No fue posible instalar NumPy en este Python 3.14/Android porque pip no encontró wheel binario compatible. Por dependencia transitiva se omiten SciPy y Matplotlib, además de Shapely, PyProj, Pydantic y PyYAML que no necesita la generación actual. La suite heredada completa no colecciona porque `scripts/calculo_mecanico_conductor.py` importa NumPy (`ModuleNotFoundError`). No se cambiaron sus pruebas ni se sustituyeron cálculos mecánicos ausentes.

Para reproducir, instalar requisitos CAD del archivo `requirements-cad.txt`, disponer de `mutool` en PATH y ejecutar:

```sh
python scripts/cad_mejorado.py
python -m pytest -q tests/test_cad_mejorado.py
```
