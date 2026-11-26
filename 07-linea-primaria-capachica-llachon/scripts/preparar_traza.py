#!/usr/bin/env python3
"""Prepara estaciones de referencia sobre la ruta vial OSM Capachica-Llachón.

Las estaciones son muestras geométricas cada 100 m; NO son ubicaciones de postes.
Datum horizontal WGS84, proyección UTM 19S (EPSG:32719). Elevación SRTM90m
se obtiene de OpenTopoData si hay red; es DEM de reconocimiento, no topografía.
"""
import csv, json, math, urllib.parse, urllib.request
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SRC=ROOT/'datos/topografia/ruta_osrm_osm_2026-10-13.json'
OUT=ROOT/'datos/topografia'

# WGS84 / UTM central meridian zone 19S; EPSG:32719.
def utm19s(lon,lat):
    a=6378137.0; f=1/298.257223563; k0=.9996
    e2=f*(2-f); ep2=e2/(1-e2); lon0=math.radians(-69)
    phi=math.radians(lat); lam=math.radians(lon)
    n=a/math.sqrt(1-e2*math.sin(phi)**2)
    t=math.tan(phi)**2; c=ep2*math.cos(phi)**2
    A=math.cos(phi)*(lam-lon0)
    M=a*((1-e2/4-3*e2**2/64-5*e2**3/256)*phi
      -(3*e2/8+3*e2**2/32+45*e2**3/1024)*math.sin(2*phi)
      +(15*e2**2/256+45*e2**3/1024)*math.sin(4*phi)
      -(35*e2**3/3072)*math.sin(6*phi))
    easting=500000+k0*n*(A+(1-t+c)*A**3/6+(5-18*t+t*t+72*c-58*ep2)*A**5/120)
    northing=10000000+k0*(M+n*math.tan(phi)*(A**2/2+(5-t+9*c+4*c*c)*A**4/24+(61-58*t+t*t+600*c-330*ep2)*A**6/720))
    return easting,northing

def hav(a,b):
    r=6371008.8; p1,p2=math.radians(a[1]),math.radians(b[1]); dp=p2-p1; dl=math.radians(b[0]-a[0])
    h=math.sin(dp/2)**2+math.cos(p1)*math.cos(p2)*math.sin(dl/2)**2
    return 2*r*math.asin(math.sqrt(h))

def resample(coords,spacing=100):
    cumulative=[0.0]
    for a,b in zip(coords,coords[1:]): cumulative.append(cumulative[-1]+hav(a,b))
    total=cumulative[-1]; stations=[float(i) for i in range(0,int(total//spacing)*spacing+1,spacing)]
    if total-stations[-1]>.01: stations.append(total)
    out=[]; j=0
    for s in stations:
        while j<len(cumulative)-2 and cumulative[j+1]<s: j+=1
        d=cumulative[j+1]-cumulative[j]; f=0 if d==0 else (s-cumulative[j])/d
        a,b=coords[j],coords[j+1]
        out.append((s,a[0]+f*(b[0]-a[0]),a[1]+f*(b[1]-a[1])))
    return out,total

def elevations(points):
    vals=[None]*len(points)
    for start in range(0,len(points),50):
        chunk=points[start:start+50]
        loc='|'.join(f'{lat:.7f},{lon:.7f}' for _,lon,lat in chunk)
        url='https://api.opentopodata.org/v1/srtm90m?'+urllib.parse.urlencode({'locations':loc})
        req=urllib.request.Request(url,headers={'User-Agent':'Academic preliminary Capachica-Llachon study'})
        data=json.load(urllib.request.urlopen(req,timeout=40))
        for j,r in enumerate(data.get('results',[])): vals[start+j]=r.get('elevation')
    return vals

def main():
    data=json.loads(SRC.read_text()); route=data['routes'][0]
    raw=route['geometry']['coordinates']; points,total=resample(raw)
    try: elev=elevations(points); elev_source='OpenTopoData API / SRTM 90 m'
    except Exception as e:
        elev=[None]*len(points); elev_source=f'No disponible: {type(e).__name__}'
    path=OUT/'estaciones_referencia_100m.csv'
    with path.open('w',newline='',encoding='utf-8') as f:
        w=csv.writer(f); w.writerow(['id_muestra','progresiva_geodesica_m','longitud_wgs84','latitud_wgs84','este_utm19s_m','norte_utm19s_m','cota_dem_srtm90m_m','clasificacion'])
        for i,((s,lon,lat),z) in enumerate(zip(points,elev)):
            e,n=utm19s(lon,lat)
            w.writerow([f'M{i:03d}',f'{s:.2f}',f'{lon:.7f}',f'{lat:.7f}',f'{e:.3f}',f'{n:.3f}','' if z is None else f'{z:.1f}','MUESTRA DE RUTA; NO ES APOYO NI VERTICE DE LEVANTAMIENTO'])
    features=[{'type':'Feature','properties':{'name':'Ruta vial OSRM Capachica-Llachon','status':'referencia; no alineamiento electrico','route_distance_osrm_m':route['legs'][0]['distance'],'geometry_chainage_m':round(total,2)},'geometry':{'type':'LineString','coordinates':raw}}]
    for i,((s,lon,lat),z) in enumerate(zip(points,elev)):
        e,n=utm19s(lon,lat)
        features.append({'type':'Feature','properties':{'id':f'M{i:03d}','station_m':round(s,2),'easting_utm19s_m':round(e,3),'northing_utm19s_m':round(n,3),'elevation_srtm90m_m':z,'classification':'route sample; not a pole'},'geometry':{'type':'Point','coordinates':[lon,lat]}})
    (OUT/'traza_referencia.geojson').write_text(json.dumps({'type':'FeatureCollection','name':'Capachica-Llachon reference route','features':features},ensure_ascii=False)+'\n')
    features=[{'type':'Feature','properties':{'name':'Ruta vial OSRM Capachica-Llachon','status':'referencia; no alineamiento electrico','route_distance_osrm_m':route['legs'][0]['distance'],'geometry_chainage_m':round(total,2)},'geometry':{'type':'LineString','coordinates':raw}}]
    for i,((s,lon,lat),z) in enumerate(zip(points,elev)):
        e,n=utm19s(lon,lat)
        features.append({'type':'Feature','properties':{'id':f'M{i:03d}','station_m':round(s,2),'easting_utm19s_m':round(e,3),'northing_utm19s_m':round(n,3),'elevation_srtm90m_m':z,'classification':'route sample; not a pole'},'geometry':{'type':'Point','coordinates':[lon,lat]}})
    (OUT/'traza_referencia.geojson').write_text(json.dumps({'type':'FeatureCollection','name':'Capachica-Llachon reference route','features':features},ensure_ascii=False)+'\n')
    summary={'route_engine':'OSRM public routing service','map_data':'OpenStreetMap contributors','source_route_distance_m':route['legs'][0]['distance'],'sampled_geometry_chainage_m':round(total,2),'route_vertices_osrm':len(raw),'samples':len(points),'spacing_m':100,'crs':'WGS 84 / UTM zone 19S (EPSG:32719)','elevation_source':elev_source,'status':'PRELIMINAR; route to be reviewed and field surveyed','electrical_network_context':'Osinergmin 2024 report shows feeder 5025/network serving Capachica and includes Llachon in regional MT topology; exact local tie-in and asset status unverified','endpoint_capachica_wgs84':{'lon':raw[0][0],'lat':raw[0][1]},'endpoint_llachon_wgs84':{'lon':raw[-1][0],'lat':raw[-1][1]}}
    (OUT/'metadatos_traza.json').write_text(json.dumps(summary,indent=2,ensure_ascii=False)+'\n')
    print(json.dumps(summary,indent=2,ensure_ascii=False))
if __name__=='__main__': main()
