# Evaluación del repositorio SEACE-CAD Intelligence

## Repositorios revisados

- Proyecto principal: `gaelrenzo/instalacion-electricas`, rama `main`.
- Referencia: `gaelrenzo/-seace-cad-intelligence`, rama `main`.

La copia disponible en este entorno no incluía los repositorios. Se inspeccionaron sus árboles públicos y los módulos relevantes de la referencia mediante GitHub. El proyecto principal ya contiene scripts de ingeniería, generadores CAD y un conjunto de resultados; el segundo es un paquete Python independiente.

## Capacidades que existen en la referencia

- `TechnicalPDFParser`: extracción de texto de PDF usando `pdfplumber` o `pypdf`, sección técnica por patrón y extracción heurística de normas/requisitos.
- Adaptadores/crawler SEACE/OCDS y persistencia SQLite para proyectos/documentos.
- `PrimaryLineParametricGenerator`: scripts CadQuery y creación DXF por tipo de armado mediante `ezdxf`.
- Modelos de referencia hechos con `dataclasses` (`ProyectoIngenieria`, `RequisitoTecnico`, `DocumentoAdjunto`).

## Compatibilidad y límites

No existe integración directa demostrada con este proyecto:

- El proyecto Capachica mantiene parámetros en CSV/YAML y genera láminas mediante scripts autónomos; el repositorio SEACE usa modelos y esquema SQLite propios.
- El parser PDF extrae texto y aplica expresiones regulares/heurísticas; no asigna procedencia por fragmento, unidad normalizada, confianza ni verificación normativa. Su salida no debe alimentar cálculos o CAD sin revisión humana.
- El generador de línea crea dibujos por familia de armado, pero no consume la planilla de estructuras Capachica ni conecta con perfil, geometría UTM, cálculo mecánico o control de revisiones. Varias dimensiones están incluidas en el código.
- Las dependencias difieren (incluye pandas, pydantic, Playwright y herramientas CAD opcionales); incorporarlas en bloque no aporta una interfaz compatible.

## Decisión

No se copiaron módulos ni se añadió una dependencia. La extracción SEACE puede utilizarse después como herramienta de investigación con registros de fuente, página, fecha y revisión humana; referencias públicas no son especificaciones del presente diseño. Para CAD, primero conviene definir un esquema compartido para trazado, componentes y procedencia y adaptar un bloque a la vez. La validación añadida localmente (`scripts/auditar_trazado.py`) es una integración pequeña y autónoma que verifica coherencia geométrica de los CSV; no depende del motor de referencia ni pretende importar sus afirmaciones.
