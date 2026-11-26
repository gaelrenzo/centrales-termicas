# Informe de base geoespacial y estado del planteamiento

**Proyecto:** Capachica–Llachón · **Revisión:** P0 · **Fecha de datos:** 2026-10-13.

## Hallazgos cartográficos

- Los localizadores OpenStreetMap para Capachica y Llachón dan respectivamente WGS84 `(lon, lat) = (-69.830694, -15.642131)` y `(-69.783859, -15.722804)`. Conversión a WGS 84 / UTM 19S (EPSG:32719): `(E,N) = (410963.591, 8270475.406)` y `(416016.796, 8261570.425)` m. Son centros/localizadores cartográficos, no puntos de conexión ni vértices de levantamiento.
- OSRM entregó una geometría de 124 vértices y distancia vial informada de **14,177.3 m**. Longitud geodésica calculada sobre la geometría: **14,201.31 m**, diferencia 24.01 m (~0.17%). Se preserva la geometría íntegra en el DXF de planta; 144 muestras cada 100 m se guardan en CSV y son solo control espacial.
- Como comprobación externa de orden de magnitud, una publicación de la DHN menciona aproximadamente 12 km de carretera Capachica–Llachón. La diferencia de ~2.18 km respecto a OSRM no está resuelta: probablemente cambian puntos terminales/itinerario/método. Se necesita validar el recorrido real antes de usar una longitud de diseño.
- Se consultó SRTM90m mediante OpenTopoData para 144 puntos: rango **3823–3873 m**. El extremo de Llachón consultado resulta 3873 m. Fichas de localidad publican cotas aproximadas de 3841–3855 m, con diferencia de 18–32 m respecto al DEM. Las fuentes no corresponden a control vertical común; confirmar en campo.
- Hallazgo eléctrico de alcance: el **Informe Técnico Osinergmin 092-2024-GRT**, páginas impresas 82–83, describe el circuito 5025 y red MT que atiende Capachica; las figuras 8–9 muestran la topología regional incluyendo Llachón. El documento describe AAAC 50 mm² en la derivación hacia Huata, Coata y Capachica, pero no entrega en estas páginas un punto de empalme local georreferenciado. No se debe asumir que falta red ni plantear una línea nueva paralela: primero se verifica el activo, operación y factibilidad con Electro Puno/GISEM.

## Entregables generados

LP-01, PL-01, U-01, D-01, D-02 y D-03 cuentan con DXF, PDF, PNG y SVG A3 en `entregables/referencia/`. LP-01 representa la polilínea vial en coordenadas UTM en ModelSpace y muestras a 1 km en la hoja; PL-01 es perfil DEM. U-01 deja punto de alimentación, tensión, conductor, protecciones, ubicación/potencia de SED y demanda pendientes. D-01/D-02/D-03 son figuras tipológicas sin dimensión constructiva, código DGE ni metrados aprobados.

Se inspeccionaron los seis PNG. DXF leídos y auditados con ezdxf 0.17.2. Suite local geoespacial: **3 aprobadas**. Los PDF generados por mutool son páginas únicas. AutoCAD no fue ejecutado.

## Condiciones para diseño de ingeniería

La carretera no determina automáticamente el eje eléctrico; los postes pueden requerir desplazamientos por propiedad, seguridad vial, pendientes, drenajes, viviendas, cruces, áreas sensibles o estándares de la concesionaria. Antes de emitir planos de diseño se requiere: punto de suministro Electro Puno con coordenada; punto de entrega/SED; factibilidad eléctrica y demanda; reconocimiento de corredor y derechos de vía; levantamiento topográfico con banco de nivel/precisión; y confirmación de tensión, conductor y configuración. Por eso no se reutilizan aquí 22.9 kV, AAAC 35 mm², 100 kVA ni las estructuras E-01–E-09 del expediente Capachica–Chifrón.

## Fuentes

- [Mapcarta/OpenStreetMap: Capachica](https://mapcarta.com/es/20237072) y [Llachón](https://mapcarta.com/es/20218380), nodos de asentamiento.
- [OSRM](https://router.project-osrm.org/) y [OpenStreetMap](https://www.openstreetmap.org/copyright), geometría vial.
- [OpenTopoData SRTM 90 m](https://api.opentopodata.org/), elevaciones de reconocimiento.
- [Dirección de Hidrografía y Navegación](https://www.dhn.mil.pe/Archivos/avilona_puno/avilonas/2017/12-2017.pdf), referencia aproximada de carretera.
- [Osinergmin, Informe Técnico 092-2024-GRT](https://www.osinergmin.gob.pe/Resoluciones/pdf/2024/Informe-Tecnico-092-2024-GRT.pdf), contexto de red existente 5025 y circuito regional en Capachica/Llachón.
- [Inventario turístico Mincetur de Llachón](https://consultasenlinea.mincetur.gob.pe/fichaInventario/index.aspx?cod_Ficha=1449), distancia/altitud de contexto de localidad (no control topográfico).
