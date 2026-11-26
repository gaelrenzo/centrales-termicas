# Fuente de datos GISEM consultada

Fecha/hora de extracción: 2026-10-13 (hora local de consulta; los atributos conservan las fechas publicadas por GISEM).

Portal: https://gisem.osinergmin.gob.pe/menergetico/
Servicio ArcGIS REST: https://gisem.osinergmin.gob.pe/serverosih/rest/services/Electricidad/ELECTRICIDAD/MapServer

Capas consultadas:

- 22 — Tramo Media Tensión: `tramos_mt_gisem_2026-10-13.json`
- 23 — Estructuras MT: `estructuras_mt_gisem_2026-10-13.json`
- 25 — SED: `sed_gisem_2026-10-13.json`

Consulta espacial de intersección, geometría en WGS 84 (EPSG:4326), envolvente `[-69.846,-15.735,-69.769,-15.632]`; análisis métrico en WGS 84 / UTM 19S (EPSG:32719). Respuestas JSON originales conservadas en este directorio. El rectángulo incluye el corredor aproximado con margen y no implica que todo elemento esté eléctricamente conectado al proyecto.

GISEM es una referencia cartográfica. Los campos consultados no acreditan disponibilidad de capacidad, tensión nominal, estado operativo actual ni autorización de empalme. Verificar con Electro Puno y en campo.
