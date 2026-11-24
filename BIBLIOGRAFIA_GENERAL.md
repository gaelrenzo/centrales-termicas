# Bibliografía General y Política de Fuentes

Este documento fija **qué fuentes se aceptan**, **cómo se registran** y **cómo se
citan**. Es de aplicación obligatoria en los cinco trabajos del repositorio.

---

## 1. Jerarquía de fuentes

Se prioriza en este orden:

| Nivel | Tipo de fuente | Uso |
|---|---|---|
| 1 | ASME (p. ej. PTC, BPVC, normas de tubería) | Diseño, ensayos de prestaciones, recipientes a presión |
| 2 | IEC | Equipos eléctricos, generadores, transformadores, instrumentación |
| 3 | API | Combustibles, tanques, quemadores, prácticas de refinería |
| 4 | NFPA | Protección contra incendios, combustibles, seguridad |
| 5 | ASHRAE | Tratamiento de aire, torres de enfriamiento, cuando corresponda |
| 6 | U.S. Department of Energy (DOE) | Eficiencia, tecnologías, guías de planta |
| 7 | U.S. Environmental Protection Agency (EPA) | Emisiones, control ambiental |
| 8 | IEA | Estadísticas y prospectiva energética |
| 9 | IRENA | Energías renovables y bioenergía |
| 10 | Fabricantes de equipos industriales | Catálogos, curvas, datos de placa |
| 11 | Libros universitarios especializados | Fundamentos y teoría |
| 12 | Artículos científicos y publicaciones técnicas | Estado del arte y datos específicos |

Regla práctica: ante discrepancia entre un catálogo comercial y una norma, se
documenta la discrepancia; no se promedian silenciosamente.

## 2. Estados de una fuente

| Estado | Significado | ¿Se puede citar? |
|---|---|---|
| `VERIFICADA` | Documento consultado; datos bibliográficos confirmados | Sí |
| `CONSULTADA` | Leída parcialmente o sin todos los datos bibliográficos | Sí, indicando alcance |
| `PENDIENTE` | Referencia conocida pero no confirmada (edición, año, número) | **No** como cita formal |
| `DESCARTADA` | No confiable, obsoleta o no pertinente | No |

## 3. Registro de fuentes

Cada fuente recibe un identificador único `SRC-NNN` y una ficha según
`recursos-compartidos/plantillas/PLANTILLA_FUENTE.md`. El registro vive en:

- Proyecto: este archivo (`BIBLIOGRAFIA_GENERAL.md`), sección 6.
- Trabajo: `01-equipamiento-central-vapor/00_gestion/REGISTRO_FUENTES.md`.

La base BibTeX del expediente está en
`01-equipamiento-central-vapor/09_informe/latex/bibliografia.bib`. **Solo se
incluyen en la base las fuentes `VERIFICADA` o `CONSULTADA`**, con los datos
exactamente como aparecen en el documento.

## 4. Plantilla de entrada BibTeX

```bibtex
@book{claveAutorAnio,
  author    = {Apellido, Nombre and Apellido, Nombre},
  title     = {Título exacto de la obra},
  edition   = {N},
  publisher = {Editorial},
  address   = {Ciudad},
  year      = {AAAA},
  isbn      = {---},
  note      = {SRC-000; verificado el AAAA-MM-DD}
}
```

Convención de claves: `primerAutorAnioPalabraClave` (p. ej. `moran2018fundamentals`).
No se agregan campos que no aparezcan en el documento (DOI, páginas, ISBN) por
deducción.

## 5. Normas de referencia previstas (a verificar)

Esta lista es de **planificación**: los números se confirman contra el catálogo
oficial de cada organismo antes de citarlos. No se asume vigencia ni título.

| Organismo | Familia / tema | Uso previsto | Estado |
|---|---|---|---|
| ASME | PTC 4 — prestaciones de generadores de vapor | Eficiencia de caldera | PENDIENTE |
| ASME | PTC 6 — turbinas de vapor | Ensayos de turbina | PENDIENTE |
| ASME | PTC 12.2 — condensadores de superficie | Balance del condensador | PENDIENTE |
| ASME | BPVC Sección I — calderas de potencia | Diseño de caldera | PENDIENTE |
| ASME | B31.1 — tuberías de potencia | Circuito de vapor | PENDIENTE |
| IEC | IEC 60034 — máquinas eléctricas rotativas | Generador síncrono | PENDIENTE |
| IEC | IEC 60076 — transformadores de potencia | Transformador principal | PENDIENTE |
| IEC | IEC 61508 / IEC 61511 — seguridad funcional | Protecciones e instrumentación | PENDIENTE |
| API | API 560 / API 530 — calentadores y tubos de horno | Equipos de intercambio | PENDIENTE |
| API | API 620 / API 650 — tanques de almacenamiento | Combustibles líquidos | PENDIENTE |
| NFPA | NFPA 85 — prevención de explosiones en calderas | Seguridad de combustión | PENDIENTE |
| NFPA | NFPA 850 — protección contra incendios en plantas de generación | Seguridad de planta | PENDIENTE |
| ASHRAE | Sistemas de enfriamiento y torres | Condensación | PENDIENTE |

> Ningún número de norma, año ni título de esta tabla debe citarse en el
> expediente hasta pasar a `VERIFICADA` con el enlace o la edición consultada.

## 6. Registro de fuentes (proyecto)

| ID | Autor / Organismo | Título | Tipo | Año | Estado | Fecha de consulta | Notas |
|---|---|---|---|---|---|---|---|
| — | — | — | — | — | — | — | Sin fuentes registradas aún |

## 7. Criterios de citación en el texto

- Cita numérica o autor-año según el sistema adoptado en el preámbulo LaTeX
  (`natbib` autor-año por defecto).
- Toda tabla o figura tomada de una fuente lleva la leyenda «Fuente: …».
- Los datos de fabricante incluyen modelo, versión del catálogo y fecha de
  consulta.
- Las afirmaciones de eficiencia o emisiones comparan siempre en la misma base
  (PCI, condiciones ISO, carga nominal) y declaran la base usada.

## 8. Advertencia sobre derechos de autor

No se almacenan en el repositorio libros, normas ni catálogos protegidos. Solo se
registran sus datos bibliográficos y, cuando la licencia lo permite, enlaces
oficiales. `recursos-compartidos/` contiene documentación propia y material de
libre distribución.
