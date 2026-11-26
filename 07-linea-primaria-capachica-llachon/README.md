# Línea primaria Capachica–Llachón — base geoespacial

Proyecto nuevo e independiente del expediente Capachica–Chifrón. Se conservó el expediente anterior en su carpeta original; sus coordenadas, estructuras, longitudes y cálculos no se usan para este recorrido.

## Coordenadas de referencia

- Inicio referencial: centro/localizador de Capachica, WGS84 `lon -69.830694, lat -15.642131`; UTM 19S `E 410963.591, N 8270475.406`.
- Fin referencial: centro/localizador de Llachón, WGS84 `lon -69.783859, lat -15.722804`; UTM 19S `E 416016.796, N 8261570.425`.
- La línea vial calculada mide 14,177.3 m según OSRM. La polilínea geográfica muestreada mide 14,201.31 m; diferencia 24.01 m. Usar solo como orden de magnitud de reconocimiento, no para metrados.
- Se generaron 144 puntos a intervalos de aproximadamente 100 m. Son muestras del corredor vial, **no ubicaciones de postes**.
- Las cotas son consulta SRTM 90 m. No son puntos topográficos ni elevaciones aprobadas para cálculo de gálibo.

## Archivos generados

`entregables/referencia/` contiene las seis láminas LP-01, PL-01, U-01, D-01, D-02 y D-03 en DXF, PDF, PNG y SVG, además de `paquete_capachica_llachon_preliminar.zip`. Los DXF incluyen la ruta en UTM 19S en espacio modelo; las láminas A3 están en layout `A3_PRELIMINAR`. U-01 y D-01/D-02/D-03 son tipológicos y dejan sus decisiones pendientes, no son diseño constructivo.

`datos/topografia/estaciones_referencia_100m.csv` contiene progresiva de geometría, coordenadas geográficas y UTM, cota DEM y clasificación de cada punto. `traza_referencia.geojson` se puede abrir en QGIS; `ruta_osrm_osm_2026-10-13.json` conserva la respuesta de ruta; `metadatos_traza.json` registra fuentes y longitudes.

Reproducir desde la raíz de esta carpeta:

```sh
python scripts/preparar_traza.py
python scripts/generar_planos_referencia.py
python -m pytest -q tests
```

La descarga SRTM necesita conexión a Internet. Para CAD/PDF/PNG se requiere `ezdxf` y `mutool` en PATH.

## Datos por definir antes del diseño eléctrico

1. Punto real de derivación/alimentación de Electro Puno y su coordenada confirmada.
2. Punto exacto de entrega o subestación en Llachón, demanda/usuarios y tensión de servicio autorizada.
3. Alineamiento eléctrico respecto a la ruta vial, servidumbre, cruces y restricciones comunitarias/ambientales.
4. Levantamiento topográfico con progresivas, quiebres, perfiles, obstáculos y cotas verificadas.
5. Potencia, conductor, criterio de caída de tensión, cortocircuito y coordinación con la concesionaria.
6. Selección de estructuras, armados, retenidas, cimentaciones y PAT con datos mecánicos/geotécnicos.

**Hallazgo que afecta el alcance:** el [Informe Técnico Osinergmin 092-2024-GRT](https://www.osinergmin.gob.pe/Resoluciones/pdf/2024/Informe-Tecnico-092-2024-GRT.pdf) describe el alimentador 5025 y red MT para Capachica, y su topología regional incluye Llachón (figuras 8–9). Por tanto, antes de proyectar una nueva línea paralela a la carretera hay que comprobar el punto de suministro y activos locales en GISEM/Electro Puno; la fuente no aporta coordenada verificable de empalme en este expediente.

No se han conservado como hipótesis el conductor AAAC 35 mm², la SED 100 kVA, E-01–E-09 ni la traza 816.60 m del proyecto anterior.

## Fuentes y atribución

- Ubicadores de Capachica y Llachón basados en OpenStreetMap, consultados por [Mapcarta Capachica](https://mapcarta.com/es/20237072) y [Mapcarta Llachón](https://mapcarta.com/es/20218380); los valores de coordenadas corresponden a nodos/localizadores de asentamiento.
- Geometría vial solicitada al [servicio OSRM](https://router.project-osrm.org/) sobre datos de [OpenStreetMap](https://www.openstreetmap.org/copyright), 2026-10-13.
- Elevación: API [OpenTopoData SRTM 90 m](https://api.opentopodata.org/), consultada 2026-10-13.
- Como contexto, una publicación de [PROMPERÚ](https://www.ytuqueplanes.com/destinos/puno/peninsula-de-capachica/comunidad-de-llachon) sitúa Llachón a 74 km al noreste de Puno; un documento de la [Dirección de Hidrografía y Navegación](https://www.dhn.mil.pe/Archivos/avilona_puno/avilonas/2017/12-2017.pdf) menciona unos 12 km por vía terrestre desde Capachica. Esas distancias generales no son sustituto de la ruta calculada ni de topografía.

## Evaluación preliminar de conexión GISEM

Se añadió una consulta a las capas oficiales GISEM de tramos MT, estructuras y SED. El candidato cartográfico más próximo al localizador de Capachica es el tramo ELPU `TMT000011089`, a 98.97 m, cercano a la SED `SE07234`. Ver `entregables/evaluacion_conexion/informe_evaluacion_conexion_gisem.md`, el mapa DXF/PDF/PNG y los JSON fuente en `datos/red_osinergmin/`. Este resultado no acredita tensión, capacidad ni factibilidad; requiere confirmación de Electro Puno. U-01 incorpora la advertencia.
