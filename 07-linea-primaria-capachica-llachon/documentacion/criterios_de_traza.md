# Criterios de la traza de referencia

## Qué representa

El itinerario se solicitó a OSRM para automóvil entre los localizadores cartográficos de Capachica y Llachón (nodos OpenStreetMap). Es una línea vial de reconocimiento. No identifica el punto de conexión de media tensión, el extremo de una red existente, una ubicación de transformador ni un eje eléctrico aprobado.

El servicio devolvió 124 coordenadas de geometría y 14,177.3 m de distancia de ruta. La suma geodésica entre los 124 vértices es 14,201.31 m. Para que el resultado sea reproducible, se conserva la respuesta original y se calcula la progresiva de las muestras sobre esa geometría WGS84. Los puntos se generan cada 100 m, con un punto final adicional; no son estacado topográfico.

Las coordenadas UTM se transforman con la serie Transversa de Mercator del elipsoide WGS84, hemisferio sur, zona 19, falso norte 10,000,000 m, falso este 500,000 m y factor 0.9996 (EPSG:32719).

## Elevación

Se consultó OpenTopoData con dataset SRTM90m para las 144 muestras. La superficie raster tiene resolución nominal aproximada de 90 m; consultas cada 100 m no significan precisión vertical de 100 m ni levantamiento. El perfil solo es DEM de reconocimiento y no debe usarse para flechas/gálibos, diseño de postes o metrados.

## Conflictos de longitud

Una fuente de navegación consultada indica aproximadamente 12 km por carretera entre Capachica y Llachón. La ruta de este trabajo da 14.18–14.20 km según algoritmo/medición de geometría. La diferencia puede deberse a puntos inicial/final distintos, camino y método de medición. Se registra para reconciliación, no se escoge silenciosamente un dato como definitivo.
