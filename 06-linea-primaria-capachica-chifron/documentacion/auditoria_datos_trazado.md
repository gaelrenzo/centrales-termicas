# Auditoría reproducible de trazado y datos de entrada

> Resultado de consistencia interna. No es aprobación de diseño ni validación de levantamiento topográfico.

- Estructuras listadas: 9
- Puntos/vértices: 13
- Longitud por progresivas: 816.60 m

| Control | Estado | Evidencia |
|---|---|---|
| sum_vanos_vs_longitud | **PASS** | Suma calculada 816.60 m; longitud por progresivas 816.60 m. |
| progresivas_estructuras | **PASS** | 9 IDs únicos; secuencia estrictamente creciente: True. |
| progresivas_vs_coordenadas | **PASS** | Máxima diferencia entre progresiva declarada y distancia UTM acumulada en vértices coincidentes: 0.003 m. |
| vertices_vs_apoyos | **INFO** | Hay 13 puntos/vértices topográficos y 9 estructuras. No son conjuntos equivalentes: los vértices intermedios no tienen tipo de apoyo asignado. |
| densificacion_del_perfil | **REVIEW** | 71 cotas intermedias difieren como máximo 0.005 m de una interpolación lineal entre puntos rotulados como vértices. No son evidencia de observaciones independientes del terreno. |
| sed_y_fin_de_linea | **REVIEW** | E-04 está declarada SAB-1/SED; la traza sigue 511.39 m hasta E-09. Los datos no identifican carga, función eléctrica ni límite de propiedad aguas abajo; la continuidad queda sin justificar. |
| procedencia_topografia | **REVIEW** | proyecto.yaml declara DEM/SRTM; hay 84 puntos interpolados/exportados, pero no se adjuntan raster, resolución, metadatos de procesamiento, datum vertical ni validación contra campo. Es perfil preliminar, no levantamiento de replanteo. |

## Conclusión sobre E-04 y E-09

La planilla sitúa la SAB-1 de 100 kVA en E-04 (prog. 0+305.21) y define E-09 como terminal de la misma traza (0+816.60). No se encuentra un diagrama de derivaciones, carga aguas abajo de E-04, concesión de continuidad ni explicación de la función del tramo E-04–E-09. La inconsistencia no se resuelve con los archivos disponibles. Hasta recibir esa definición, planta, perfil y unifilar deben tratar el tramo E-04–E-09 como alcance y topología pendientes de confirmar.

## Datos requeridos antes de emitir planos verificables

1. Para perfil ejecutivo: levantamiento de campo con archivo nativo, puntos, método, fecha, equipo, precisión y datum vertical; coordenadas/cotas de cada estructura y obstáculo. Si se conserva DEM/SRTM, adjuntar raster, resolución y método y rotular el perfil como preliminar.
2. Confirmación del propietario/concesionaria sobre el punto de derivación, el recorrido E-01–E-09, la función del tramo después de E-04 y el límite del proyecto.
3. Ficha certificada del AAAC instalado/propuesto y memoria de cambio de estado que respalde tensión y flecha para cada vano e hipótesis climática.
4. Datos de corto circuito y curvas/fichas de fusibles y pararrayos para coordinación; resistividad medida en el emplazamiento y medición de PAT al terminar la obra.
5. Geotecnia, cargas de diseño verificadas, fichas de postes/anclajes y parámetros necesarios para validar cimentaciones y retenidas.

Las cotas de estructura y progresivas del CSV se conservan como datos declarados. Aunque `proyecto.yaml` declara DEM/SRTM, el ráster no está adjunto y las 71 cotas intermedias siguen casi exactamente rectas entre vértices; no se puede reconstruir ni acreditar un perfil de terreno observado con el paquete revisado. Las comprobaciones geométricas solo verifican relaciones entre archivos y no convierten esos datos en observaciones de campo.
