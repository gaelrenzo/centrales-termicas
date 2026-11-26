#!/usr/bin/env python3
"""Evaluate proximity of official GISEM assets to Capachica-Llachón route.

Proximity is a GIS screening only; it does not establish voltage, capacity,
operating status or authorization to connect.
"""
import csv, json, math
from pathlib import Path
import ezdxf, html, subprocess
from preparar_traza import utm19s

ROOT=Path(__file__).resolve().parents[1]
GIS=ROOT/'datos/red_osinergmin'
OUT=ROOT/'entregables/evaluacion_conexion'
ROUTE=json.loads((ROOT/'datos/topografia/ruta_osrm_osm_2026-10-13.json').read_text())['routes'][0]['geometry']['coordinates']
ORIGIN=utm19s(-69.830694,-15.642131)
DEST=utm19s(-69.783859,-15.722804)

def read(name): return json.loads((GIS/name).read_text())['features']
def xy_geom(g):
    if 'paths' in g: return [[utm19s(*p) for p in path] for path in g['paths']]
    if 'x' in g: return [utm19s(g['x'],g['y'])]
    return []
def dist_point_seg(p,a,b):
    dx=b[0]-a[0]; dy=b[1]-a[1]; den=dx*dx+dy*dy
    t=0 if den==0 else max(0,min(1,((p[0]-a[0])*dx+(p[1]-a[1])*dy)/den))
    q=(a[0]+t*dx,a[1]+t*dy)
    return math.hypot(p[0]-q[0],p[1]-q[1]),q
def nearest_line(p,lines,min_len=0):
    best=None
    for f in lines:
        at=f['attributes']; paths=xy_geom(f['geometry'])
        try:
            if float(at.get('LONGITUD') or 0)<min_len: continue
        except (TypeError,ValueError): pass
        for path in paths:
            for a,b in zip(path,path[1:]):
                d,q=dist_point_seg(p,a,b)
                if best is None or d<best[0]: best=(d,q,at)
    return best
def nearest_asset(p,features,codekey):
    best=None
    for f in features:
        at=f['attributes']; g=f['geometry']; q=utm19s(g['x'],g['y']); d=math.dist(p,q)
        if best is None or d<best[0]: best=(d,q,at)
    return best
def main():
    OUT.mkdir(parents=True,exist_ok=True)
    lines=read('tramos_mt_gisem_2026-10-13.json'); poles=read('estructuras_mt_gisem_2026-10-13.json'); seds=read('sed_gisem_2026-10-13.json')
    stub0=nearest_line(ORIGIN,lines); line0=nearest_line(ORIGIN,lines,min_len=20); sed0=nearest_asset(ORIGIN,seds,'CODSED')
    line1=nearest_line(DEST,lines,min_len=20); sed1=nearest_asset(DEST,seds,'CODSED')
    # Sample the reference road at 100 m from existing route stations.
    rows=list(csv.DictReader((ROOT/'datos/topografia/estaciones_referencia_100m.csv').open(encoding='utf-8')))
    sample=[]
    for r in rows:
        p=(float(r['este_utm19s_m']),float(r['norte_utm19s_m']))
        d,q,a=nearest_line(p,lines,min_len=20)
        sample.append({'progresiva_m':float(r['progresiva_geodesica_m']),'distancia_red_mt_m':d,'codigo_tramo':a.get('CODTRAMOMT',''),'tipo_red':a.get('CODTIPORED',''),'propiedad':a.get('PROPIEDAD',''),'fecha_puesta_servicio':a.get('FECPUESTASERVICIO',''),'este_punto_cercano_m':q[0],'norte_punto_cercano_m':q[1]})
    with (OUT/'proximidad_red_mt_muestras_100m.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=sample[0].keys()); w.writeheader(); w.writerows(sample)
    def asset_row(label,res,code):
        d,q,a=res
        return {'referencia':label,'codigo':a.get(code,''),'etiqueta':a.get('ETIQUETACAMPO',''),'empresa':a.get('CODEMP',''),'fecha':a.get('FECPUESTASERVICIO',''),'este_utm19s_m':q[0],'norte_utm19s_m':q[1],'distancia_al_localizador_m':d,'sistema':a.get('SISTEMA0',a.get('SISTEMA','')),'codigo_tramo':''}
    result={'fecha_consulta':'2026-10-13','fuente':'Osinergmin GISEM ArcGIS REST; capas 22 Tramo Media Tensión, 23 Estructuras MT, 25 SED','crs':'WGS 84 / UTM 19S (EPSG:32719)','origen_capachica_localizador':{'lon':-69.830694,'lat':-15.642131,'este':ORIGIN[0],'norte':ORIGIN[1]},'destino_llachon_localizador':{'lon':-69.783859,'lat':-15.722804,'este':DEST[0],'norte':DEST[1]},'activos_cercanos':{'tramo_mt_capachica':asset_row('Más cercano al localizador Capachica',line0,'CODTRAMOMT'),'sed_capachica':asset_row('SED más cercana a Capachica',sed0,'CODSED'),'tramo_mt_llachon':asset_row('Más cercano al localizador Llachón',line1,'CODTRAMOMT'),'sed_llachon':asset_row('SED más cercana a Llachón',sed1,'CODSED')},'conteos_consulta':{'tramos_mt':len(lines),'estructuras_mt':len(poles),'sed':len(seds)},'estado':'CRIBADO DE PROXIMIDAD; no es factibilidad ni diseño de conexión'}
    # Add attributes for nearest mapped line and pole around Capachica.
    result['activos_cercanos']['tramo_mt_capachica'].update({'codigo_tramo':line0[2].get('CODTRAMOMT'),'tipo_red':line0[2].get('CODTIPORED'),'propiedad':line0[2].get('PROPIEDAD'),'longitud_atributo_m':line0[2].get('LONGITUD'),'punto_mas_cercano_este_m':line0[1][0],'punto_mas_cercano_norte_m':line0[1][1],'criterio':'tramo con longitud atribuida >= 20 m; se excluye stub cartográfico de 0.99 m'})
    result['activos_cercanos']['tramo_mt_llachon'].update({'codigo_tramo':line1[2].get('CODTRAMOMT'),'tipo_red':line1[2].get('CODTIPORED'),'propiedad':line1[2].get('PROPIEDAD'),'longitud_atributo_m':line1[2].get('LONGITUD'),'punto_mas_cercano_este_m':line1[1][0],'punto_mas_cercano_norte_m':line1[1][1]})
    nearp=nearest_asset(ORIGIN,poles,'CODESTRUCTURA'); result['activos_cercanos']['estructura_mt_capachica']=asset_row('Estructura MT más cercana',nearp,'CODESTRUCTURA')
    result['activos_cercanos']['stub_mas_cercano_capachica']=asset_row('Stub MT cartográfico más cercano',stub0,'CODTRAMOMT')
    result['activos_cercanos']['stub_mas_cercano_capachica'].update({'codigo_tramo':stub0[2].get('CODTRAMOMT'),'longitud_atributo_m':stub0[2].get('LONGITUD'),'nota':'geometría de 0.99 m coincidente con la SED; no usar como tramo de empalme sin aclaración de la concesionaria'})
    (OUT/'evaluacion_conexion_gisem.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
    md=['# Evaluación preliminar del punto de conexión con GISEM','',f"Consulta: {result['fecha_consulta']} · CRS de análisis: {result['crs']}.",'','## Resultado de proximidad','']
    for k,v in result['activos_cercanos'].items(): md.append(f"- **{v['referencia']}**: {v['codigo'] or v.get('codigo_tramo')} ({v['empresa']}); UTM 19S E {v['este_utm19s_m']:.2f} m, N {v['norte_utm19s_m']:.2f} m; separación del localizador {v['distancia_al_localizador_m']:.1f} m; fecha registrada {v['fecha'] or 'no informada'}.")
    md += ['',f"Consulta del corredor: {len(lines)} tramos MT, {len(poles)} estructuras y {len(seds)} SED dentro del rectángulo de búsqueda.",'','## Interpretación y decisión provisional','','El activo que debe investigarse primero es el tramo **TMT000011089** (162.81 m de longitud atribuida), a 99.0 m del localizador de Capachica y próximo a la SED SE07234. GISEM también muestra un tramo de solo 0.99 m (TMT001868169) coincidente con la SED; se separa del candidato para no tomar ese stub como línea de alimentación. Este hallazgo **no prueba** tensión de 22.9 kV, capacidad disponible, circuito alimentador ni autorización. La recomendación es pedir a Electro Puno factibilidad de suministro/empalme con los códigos y coordenadas antes de fijar una línea nueva de 14 km.','', 'La ruta vial Capachica–Llachón se conserva como corredor de estudio. Las distancias calculadas contra su eje son proximidades cartográficas a la red GISEM, no alineamiento, vanos, estructuras, derecho de vía ni servidumbre.','', '## Pendientes para declarar punto de conexión','','1. Confirmación de Electro Puno del alimentador, tensión nominal, fases, conductor y estado operativo del tramo candidato.','2. Capacidad y caída de tensión con demanda/proyección de Llachón, cortocircuito y coordinación de protecciones.','3. Coordenada autorizada de empalme y levantamiento topográfico del acceso/traza hasta dicho punto.','4. Función de SED cercanas, cargas conectadas y posibilidad de conexión directa o necesidad de nueva subestación.','5. Validación en campo de poste/estructura, propiedad, accesibilidad y servidumbre.','', 'GISEM se usa como referencia cartográfica oficial; su información es referencial y requiere validación con la concesionaria. No es plano ejecutivo ni aprobación de conexión.','']
    (OUT/'informe_evaluacion_conexion_gisem.md').write_text('\n'.join(md),encoding='utf-8')
    # Lightweight A3 SVG/PDF/PNG and an editable DXF with true UTM coordinates.
    allpts=[utm19s(*p) for p in ROUTE]
    for f in lines:
        for path in xy_geom(f['geometry']): allpts.extend(path)
    for f in seds: allpts.append(utm19s(f['geometry']['x'],f['geometry']['y']))
    e0=min(p[0] for p in allpts); e1=max(p[0] for p in allpts); n0=min(p[1] for p in allpts); n1=max(p[1] for p in allpts)
    sx,sy=230/(e1-e0),225/(n1-n0); scale=min(sx,sy); ox,oy=22,35
    mapw=(e1-e0)*scale; maph=(n1-n0)*scale
    def screen(p): return ox+(p[0]-e0)*scale, 258-(p[1]-n0)*scale
    svg=['<svg xmlns="http://www.w3.org/2000/svg" width="420mm" height="297mm" viewBox="0 0 420 297"><rect width="420" height="297" fill="white"/>']
    svg += ['<rect x="5" y="5" width="410" height="287" fill="none" stroke="#172554"/>','<text x="12" y="16" font-size="4" font-family="Arial" font-weight="bold">GISEM · CRIBADO DE RED MT CAPACHICA–LLACHÓN</text>','<text x="12" y="23" font-size="2.2" font-family="Arial" fill="#b91c1c">PRELIMINAR · PROXIMIDAD CARTOGRÁFICA · NO ES FACTIBILIDAD DE CONEXIÓN</text>']
    for f in lines:
        for path in xy_geom(f['geometry']):
            pts=' '.join(f'{screen(p)[0]:.2f},{screen(p)[1]:.2f}' for p in path)
            svg.append(f'<polyline points="{pts}" fill="none" stroke="#dc2626" stroke-width="0.45" opacity="0.65"/>')
    pts=' '.join(f'{screen(p)[0]:.2f},{screen(p)[1]:.2f}' for p in [utm19s(*p) for p in ROUTE])
    svg.append(f'<polyline points="{pts}" fill="none" stroke="#2563eb" stroke-width="0.8"/>')
    for f in seds:
        x,y=screen(utm19s(f['geometry']['x'],f['geometry']['y'])); svg.append(f'<rect x="{x-0.7:.2f}" y="{y-0.7:.2f}" width="1.4" height="1.4" fill="#16a34a" stroke="#14532d" stroke-width="0.2"/>')
    for p,color,label,dx,dy in [(ORIGIN,'#f59e0b','CAPACHICA',3,-2),(DEST,'#7c3aed','LLACHÓN',3,-2),(line0[1],'#dc2626','TRAMO MT',3,4)]:
        x,y=screen(p); svg.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="1.5" fill="{color}" stroke="#111827" stroke-width="0.3"/><text x="{x+dx:.2f}" y="{y+dy:.2f}" font-size="1.6" font-family="Arial">{label}</text>')
    svg += ['<rect x="275" y="34" width="130" height="220" fill="#f8fafc" stroke="#cbd5e1"/>','<text x="280" y="43" font-size="2.5" font-family="Arial" font-weight="bold">PUNTO A INVESTIGAR</text>',f'<text x="280" y="52" font-size="2" font-family="Arial">MT: {html.escape(str(line0[2].get("CODTRAMOMT")))}</text>',f'<text x="280" y="59" font-size="2" font-family="Arial">Longitud GISEM: {html.escape(str(line0[2].get("LONGITUD")))} m</text>',f'<text x="280" y="66" font-size="2" font-family="Arial">Separación: {line0[0]:.1f} m al localizador</text>',f'<text x="280" y="73" font-size="2" font-family="Arial">Punto próximo UTM E {line0[1][0]:.0f}</text>',f'<text x="280" y="80" font-size="2" font-family="Arial">N {line0[1][1]:.0f}</text>',f'<text x="280" y="89" font-size="2" font-family="Arial">SED: {html.escape(str(sed0[2].get("ETIQUETACAMPO")))} / {html.escape(str(sed0[2].get("CODSED")))}</text>','<text x="280" y="98" font-size="2" font-family="Arial">TMT001868169 (0.99 m) coincide</text>','<text x="280" y="105" font-size="2" font-family="Arial">con SED; no tratar como troncal.</text>','<text x="280" y="117" font-size="2" font-family="Arial" font-weight="bold">LIMITACIÓN</text>','<text x="280" y="125" font-size="1.8" font-family="Arial">No consta en estas capas la tensión,</text>','<text x="280" y="132" font-size="1.8" font-family="Arial">capacidad o factibilidad de empalme.</text>','<text x="280" y="143" font-size="1.8" font-family="Arial">Confirmar con Electro Puno antes</text>','<text x="280" y="150" font-size="1.8" font-family="Arial">de diseñar nueva línea MT.</text>']
    svg += ['<line x1="12" y1="268" x2="26" y2="268" stroke="#dc2626" stroke-width="0.8"/><text x="29" y="269" font-size="1.8">Tramo MT GISEM</text>','<line x1="75" y1="268" x2="89" y2="268" stroke="#2563eb" stroke-width="0.9"/><text x="92" y="269" font-size="1.8">Ruta vial OSRM/OSM</text>','<rect x="147" y="266.5" width="3" height="3" fill="#16a34a"/><text x="153" y="269" font-size="1.8">SED GISEM</text>',f'<text x="12" y="278" font-size="1.8" font-family="Arial">Consulta 2026-10-13 · 171 tramos MT · 362 estructuras · 49 SED · WGS84 / UTM 19S (EPSG:32719)</text>','<text x="12" y="285" font-size="1.8" font-family="Arial" fill="#b91c1c">La cartografía no informa aquí capacidad disponible ni autorización; confirmar con Electro Puno.</text>','</svg>']
    svgpath=OUT/'mapa_red_gisem_corredor.svg'; svgpath.write_text('\n'.join(svg),encoding='utf-8')
    subprocess.run(['mutool','draw','-q','-F','pdf','-o',str(OUT/'mapa_red_gisem_corredor.pdf'),str(svgpath)],check=True)
    subprocess.run(['mutool','draw','-q','-r','160','-F','png','-o',str(OUT/'mapa_red_gisem_corredor.png'),str(OUT/'mapa_red_gisem_corredor.pdf')],check=True)
    doc=ezdxf.new('R2010'); doc.header['$INSUNITS']=6; m=doc.modelspace()
    for name,color in [('GIS_MT',1),('RUTA_REFERENCIA',5),('GIS_SED',3),('PUNTO_CANDIDATO',30),('ETIQUETAS',7)]: doc.layers.new(name,dxfattribs={'color':color})
    for f in lines:
        for path in xy_geom(f['geometry']):
            if len(path)>1: m.add_lwpolyline(path,dxfattribs={'layer':'GIS_MT'})
    m.add_lwpolyline([utm19s(*p) for p in ROUTE],dxfattribs={'layer':'RUTA_REFERENCIA'})
    for f in seds:
        p=utm19s(f['geometry']['x'],f['geometry']['y']); m.add_circle(p,3,dxfattribs={'layer':'GIS_SED'})
    for p,label in [(ORIGIN,'CAPACHICA'),(DEST,'LLACHON'),(line0[1],'CANDIDATO MT')]:
        m.add_circle(p,5,dxfattribs={'layer':'PUNTO_CANDIDATO'}); m.add_text(label,dxfattribs={'height':5,'layer':'ETIQUETAS'}).set_placement((p[0]+8,p[1]+8))
    doc.saveas(OUT/'mapa_red_gisem_corredor.dxf')
    print(json.dumps(result['activos_cercanos'],ensure_ascii=False,indent=2))
if __name__=='__main__': main()
