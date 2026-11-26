#!/usr/bin/env python3
"""Produce LP-01/PL-01 reference sheets from the frozen road and DEM sample data."""
import csv,html,math,shutil,subprocess,json,zipfile
from pathlib import Path
import ezdxf
from preparar_traza import utm19s
ROOT=Path(__file__).resolve().parents[1]; DATA=ROOT/'datos/topografia'; OUT=ROOT/'entregables/referencia'
W,H=420,297
rows=list(csv.DictReader((DATA/'estaciones_referencia_100m.csv').open(encoding='utf-8')))
route_raw=json.loads((DATA/'ruta_osrm_osm_2026-10-13.json').read_text())['routes'][0]['geometry']['coordinates']
route_xy=[utm19s(lon,lat) for lon,lat in route_raw]
for r in rows:
    for k in ('progresiva_geodesica_m','longitud_wgs84','latitud_wgs84','este_utm19s_m','norte_utm19s_m','cota_dem_srtm90m_m'): r[k]=float(r[k])
INK='#172554'; BLUE='#1d4ed8'; GRAY='#64748b'; RED='#b91c1c'; AMBER='#b45309'; LIGHT='#e2e8f0'
class Sheet:
 def __init__(self,title,code,scale): self.title=title; self.code=code; self.scale=scale; self.e=[]
 def line(self,x1,y1,x2,y2,c=INK,w=.3,dash=''): self.e.append(('line',(x1,y1,x2,y2),c,w,dash))
 def rect(self,x,y,w,h,c=INK,fill='none'): self.e.append(('rect',(x,y,w,h),c,.3,fill))
 def circle(self,x,y,r,c=INK,fill='white'): self.e.append(('circle',(x,y,r),c,.3,fill))
 def text(self,x,y,t,size=2,c=INK,bold=False,anchor='start'): self.e.append(('text',(x,y,str(t),size,bold,anchor),c,0,''))
 def frame(self,subtitle):
  self.rect(5,5,410,287,INK); self.rect(8,8,404,281,LIGHT)
  self.text(12,16,'LÍNEA PRIMARIA PRELIMINAR · CAPACHICA – LLACHÓN',4,INK,True)
  self.text(12,22,subtitle,2.2,GRAY)
  self.rect(298,10,110,12,RED,'#fff7f7'); self.text(353,15,'PRELIMINAR · REFERENCIA GIS',1.8,RED,True,'middle'); self.text(353,19,'NO APTO PARA CONSTRUCCIÓN',1.8,RED,True,'middle')
  self.rect(8,263,404,26,INK); self.line(275,263,275,289,INK); self.line(8,276,412,276,INK)
  self.text(11,269,self.title,2.6,INK,True); self.text(11,282,'WGS 84 · UTM 19S · Rev. P0 · 2026-10-13 · Ruta OSM + SRTM90m',1.7,GRAY)
  self.text(278,269,'ESTADO  PRELIMINAR',1.7,RED,True); self.text(278,282,'ESCALA  '+self.scale,1.65,INK,True); self.text(362,269,'LÁMINA  '+self.code,1.8,INK,True); self.text(370,282,'A3',1.8,INK,True)
 def svg(self):
  out=[f'<svg xmlns="http://www.w3.org/2000/svg" width="420mm" height="297mm" viewBox="0 0 420 297"><rect width="420" height="297" fill="white"/>']
  for typ,a,c,w,d in self.e:
   if typ=='line':
    x1,y1,x2,y2=a; ds=f' stroke-dasharray="{d}"' if d else ''; out.append(f'<line x1="{x1:.3f}" y1="{y1:.3f}" x2="{x2:.3f}" y2="{y2:.3f}" stroke="{c}" stroke-width="{w}"{ds}/>')
   elif typ=='rect':
    x,y,ww,hh=a; out.append(f'<rect x="{x}" y="{y}" width="{ww}" height="{hh}" fill="{d}" stroke="{c}" stroke-width="{w}"/>')
   elif typ=='circle':
    x,y,r=a; out.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{d}" stroke="{c}" stroke-width="{w}"/>')
   else:
    x,y,t,s,b,anc=a; out.append(f'<text x="{x:.3f}" y="{y:.3f}" font-family="Arial,sans-serif" font-size="{s}" font-weight="{700 if b else 400}" text-anchor="{anc}" fill="{c}">{html.escape(t)}</text>')
  return '\n'.join(out+['</svg>'])
 def dxf(self,path,modelcode):
  doc=ezdxf.new('R2010',setup=True); doc.header['$INSUNITS']=6
  for l,c in [('REF_RUTA',5),('REF_PUNTOS',8),('REF_PERFIL',8),('SHEET',7),('SHEET_TEXT',7),('SHEET_ALERTA',1)]:
   if l not in doc.layers: doc.layers.new(l,dxfattribs={'color':c,'lineweight':25})
  m=doc.modelspace()
  if modelcode=='LP-01':
   m.add_lwpolyline(route_xy,dxfattribs={'layer':'REF_RUTA'})
   for r in rows: m.add_point((r['este_utm19s_m'],r['norte_utm19s_m']),dxfattribs={'layer':'REF_PUNTOS'})
  else:
   m.add_lwpolyline([(r['progresiva_geodesica_m'],r['cota_dem_srtm90m_m']) for r in rows],dxfattribs={'layer':'REF_PERFIL'})
  layout=doc.layouts.new('A3_PRELIMINAR')
  try: layout.page_setup(size=(420,297),units='mm',margins=(0,0,0,0),label='A3 horizontal')
  except Exception: pass
  for typ,a,c,w,d in self.e:
   layer='SHEET_ALERTA' if c in (RED,AMBER) else 'SHEET_TEXT' if typ=='text' else 'SHEET'
   if typ=='line': x1,y1,x2,y2=a; layout.add_line((x1,H-y1),(x2,H-y2),dxfattribs={'layer':layer})
   elif typ=='rect': x,y,ww,hh=a; layout.add_lwpolyline([(x,H-y),(x+ww,H-y),(x+ww,H-y-hh),(x,H-y-hh)],close=True,dxfattribs={'layer':layer})
   elif typ=='circle': x,y,r=a; layout.add_circle((x,H-y),r,dxfattribs={'layer':layer})
   else: x,y,t,s,b,anc=a; layout.add_text(t,dxfattribs={'height':s,'layer':layer}).set_placement((x,H-y))
  doc.saveas(path)

def make_lp():
 s=Sheet('PLANTA DE TRAZA VIAL DE REFERENCIA','LP-01','aprox. 1:47 000'); s.frame('CAPACHICA – LLACHÓN · GEOMETRÍA VIAL OSM · MUESTRAS GIS, NO APOYOS')
 # map with geographic polyline projected to UTM coordinates, true isotropic sheet scale
 x0,y0,x1,y1=22,38,259,247; es=[p[0] for p in route_xy]; ns=[p[1] for p in route_xy]; emin,emax=min(es),max(es); nmin,nmax=min(ns),max(ns)
 sc=min((x1-x0-20)/(emax-emin),(y1-y0-20)/(nmax-nmin)); ox=x0+(x1-x0-(emax-emin)*sc)/2; oy=y0+(y1-y0-(nmax-nmin)*sc)/2
 pts=[(ox+(e-emin)*sc, oy+(nmax-n)*sc) for e,n in route_xy]
 for a,b in zip(pts,pts[1:]): s.line(*a,*b,BLUE,.8)
 for i,r in enumerate(rows):
  if i%10==0 or i in (0,len(rows)-1):
   x=ox+(r['este_utm19s_m']-emin)*sc; y=oy+(nmax-r['norte_utm19s_m'])*sc
   s.circle(x,y,1.1,RED if i in (0,len(rows)-1) else BLUE,'white'); s.text(x+2,y-1,f'{r["progresiva_geodesica_m"]/1000:.1f} km',1.35,INK,True)
 s.text(237,42,'N',2.4,INK,True,'middle'); s.line(237,45,237,58,INK,.5); s.line(234,50,237,45,INK,.5); s.line(240,50,237,45,INK,.5)
 s.text(22,252,'CAPACHICA: −15.642131, −69.830694 · INICIO DE REFERENCIA',1.55,BLUE,True)
 s.text(22,257,'LLACHÓN: −15.722804, −69.783859 · FIN DE REFERENCIA · confirmar punto eléctrico de conexión',1.5,RED,True)
 s.rect(270,34,135,209,LIGHT,'#fcfdff'); s.text(275,41,'COORDENADAS DE CONTROL (UTM 19S)',1.8,INK,True)
 s.text(275,48,'Prog. km       Este m      Norte m',1.8,GRAY,True)
 for j,km in enumerate(range(0,15,2)):
  r=min(rows,key=lambda x:abs(x['progresiva_geodesica_m']-km*1000)); s.text(275,56+j*9,f'{r["progresiva_geodesica_m"]/1000:5.1f}       {r["este_utm19s_m"]:.0f}    {r["norte_utm19s_m"]:.0f}',1.8,INK)
 s.text(275,132,'BASE DE TRAZA',1.8,INK,True)
 for j,t in enumerate(['124 vértices de ruta OSRM/OpenStreetMap.','Longitud de geometría muestreada: 14.201 km.','Longitud informada por OSRM: 14.177 km.','Diferencia geométrica: ~24 m; no usar para metrados.','Muestras cada 100 m: apoyo candidato NO diseñado.','No representa alineamiento aprobado de línea MT.']): s.text(275,139+j*8,t,1.4,GRAY)
 s.text(275,196,'El corredor sigue una ruta vial calculada.',1.4,AMBER,True); s.text(275,202,'Validar acceso, derecho de vía y trazado con',1.4,AMBER); s.text(275,208,'concesionaria y levantamiento de campo.',1.4,AMBER)
 s.text(275,224,'Coordenadas de población: fuente cartográfica web;',1.3,GRAY); s.text(275,230,'centroides/localizadores aproximados.',1.3,GRAY)
 return s

def make_pl():
 s=Sheet('PERFIL DEM DE RECONOCIMIENTO','PL-01','H 1:38 000 · V 1:380 aprox.'); s.frame('SRTM 90 m · ELEVACIÓN DE MODELO DIGITAL, NO TOPOGRAFÍA NI COTAS DE APOYOS')
 x0,y0,x1,y1=30,48,402,205; zmin=3820; zmax=3880; xmin=0; xmax=rows[-1]['progresiva_geodesica_m']
 def p(r): return x0+r['progresiva_geodesica_m']/xmax*(x1-x0),y1-(r['cota_dem_srtm90m_m']-zmin)/(zmax-zmin)*(y1-y0)
 for km in range(0,15,2):
  x=x0+km*1000/xmax*(x1-x0); s.line(x,y0,x,y1,LIGHT,.2); s.text(x,y1+4,str(km),1.35,GRAY,False,'middle')
 for z in range(3820,3881,10):
  y=y1-(z-zmin)/(zmax-zmin)*(y1-y0); s.line(x0,y,x1,y,LIGHT,.2); s.text(x0-2,y+1,str(z),1.35,GRAY,False,'end')
 for a,b in zip(rows,rows[1:]): s.line(*p(a),*p(b),GRAY,.6)
 for r in rows[::5]:
  x,y=p(r); s.circle(x,y,.6,BLUE,'white')
 s.text(30,216,'Progresiva de ruta (km)',1.5,GRAY); s.text(15,125,'Elevación SRTM (msnm)',1.4,GRAY,False,'middle')
 s.rect(30,226,370,25,AMBER,'#fffbeb'); s.text(34,234,'Perfil DEM de reconocimiento (90 m); no interpolar como levantamiento topográfico de diseño.',1.65,AMBER,True)
 s.text(34,242,'Se requiere topografía terrestre de eje, obstáculos y estructuras; correlación vertical del DEM no verificada.',1.5,AMBER)
 s.text(32,57,f'Rango DEM consultado: {min(r["cota_dem_srtm90m_m"] for r in rows):.0f}–{max(r["cota_dem_srtm90m_m"] for r in rows):.0f} m',1.5,INK,True)
 return s

def make_u():
 s=Sheet('DIAGRAMA UNIFILAR DE ALCANCE PRELIMINAR','U-01','NTS'); s.frame('TOPOLOGÍA ELÉCTRICA Y PUNTOS DE INTERFAZ POR DEFINIR')
 s.rect(24,72,94,42,GRAY,'#f1f5f9'); s.text(71,82,'CAPACHICA · ÁREA DE ORIGEN',1.8,INK,True,'middle'); s.text(71,90,'Candidato GISEM: TMT000011089',1.45,AMBER,True,'middle'); s.text(71,97,'SED SE07234 · ~99 m del localizador',1.35,AMBER,True,'middle'); s.text(71,105,'Tensión / capacidad / empalme: verificar',1.3,RED,True,'middle')
 s.line(118,93,294,93,BLUE,1.2); s.text(206,84,'Corredor vial de referencia ≈ 14.2 km',1.9,INK,True,'middle'); s.text(206,101,'Tensión · conductor · apoyos · número de SED: PENDIENTES',1.6,AMBER,True,'middle')
 s.rect(294,72,100,42,RED,'#fff7f7'); s.text(344,83,'LLACHÓN · DESTINO',2,INK,True,'middle'); s.text(344,92,'Localizador de población, no punto de suministro',1.5,AMBER,True,'middle'); s.text(344,101,'Demanda / tensión / SED: PENDIENTES',1.5,RED,True,'middle')
 s.rect(24,136,370,46,LIGHT,'#fcfdff'); s.text(30,146,'EQUIPOS Y COORDINACIÓN',2,INK,True)
 s.text(30,156,'GISEM: TMT000011089 (162.81 m atribuida) y SED SE07234 próximos al localizador de Capachica.',1.65,AMBER,True)
 s.text(30,167,'Candidato cartográfico; tensión, capacidad, operación y factibilidad de empalme no verificadas.',1.65,RED,True)
 s.text(24,205,'Antes de cerrar el unifilar: confirmar tensión y punto de alimentación con Electro Puno; levantar demanda y',1.7,GRAY)
 s.text(24,213,'definir ubicación de subestación/es y configuración conforme a factibilidad de servicio y normas aplicables.',1.7,GRAY)
 return s

def make_detail(code,title,labels):
 s=Sheet(title,code,'NTS · esquemático'); s.frame('DETALLES TIPOLÓGICOS DE REFERENCIA · SIN DIMENSIONES CONSTRUCTIVAS APROBADAS')
 xs=[82,210,338]
 for x,label in zip(xs,labels):
  s.rect(x-45,43,90,124,LIGHT,'#ffffff'); s.text(x,52,label,2.1,INK,True,'middle')
  s.line(x,65,x,132,INK,2.2); s.line(x-27,81,x+27,81,BLUE,1.4)
  for dx in (-19,0,19): s.circle(x+dx,77,2,BLUE,'#dbeafe')
  if 'RETEN' in label or 'ÁNGULO' in label: s.line(x,95,x+34,142,GRAY,.9)
  if 'SUBESTACIÓN' in label:
   s.line(x-26,86,x-26,130,INK,1); s.line(x+26,86,x+26,130,INK,1); s.rect(x-15,105,30,17,GRAY,'#f1f5f9'); s.text(x,116,'TRAFO?',1.4,AMBER,True,'middle')
  s.text(x,151,'TIPOLÓGICO',1.5,AMBER,True,'middle')
 s.text(24,181,'ELEMENTOS REPRESENTADOS',2,INK,True)
 s.rect(24,187,370,36,LIGHT,'#ffffff')
 s.text(29,197,'Poste, cruceta y tres fases como símbolo de estudio; aisladores y ferretería por seleccionar.',1.7,GRAY)
 s.text(29,208,'Código DGE, geometría, distancias eléctricas, cargas, materiales y metrados: POR VERIFICAR.',1.7,RED,True)
 s.text(24,239,'No atribuir dimensiones ni aplicabilidad a una lámina DGE sin identificar y verificar su edición oficial.',1.6,AMBER,True)
 return s

def make_d03():
 s=Sheet('CIMENTACIONES · RETENIDAS · PUESTA A TIERRA','D-03','NTS · esquemático'); s.frame('TIPOLOGÍA DE ANÁLISIS · NO CONSTRUCTIVA')
 boxes=[(22,'CIMENTACIÓN'),(156,'RETENIDA'),(290,'PUESTA A TIERRA')]
 for x,label in boxes: s.rect(x,48,112,118,LIGHT,'#ffffff'); s.text(x+56,58,label,1.8,INK,True,'middle')
 s.line(78,69,78,124,INK,2); s.rect(58,109,40,25,AMBER,'#fffbeb'); s.text(78,145,'geotecnia/cargas pendientes',1.4,RED,True,'middle')
 s.line(212,69,212,124,INK,2); s.line(212,88,247,135,GRAY,1.3); s.circle(247,135,2,GRAY,'#f1f5f9'); s.text(212,145,'tiro/anclaje pendientes',1.4,RED,True,'middle')
 s.text(346,82,'PAT: geometría',1.5,GRAY,False,'middle'); s.text(346,92,'electrodos/cantidad',1.5,GRAY,False,'middle'); s.text(346,102,'resistividad y enlaces',1.5,GRAY,False,'middle'); s.text(346,120,'PENDIENTES',1.8,RED,True,'middle')
 s.text(24,187,'DATOS PARA CÁLCULO Y DETALLE',2,INK,True)
 for i,t in enumerate(['Geotecnia, nivel freático, geometría y cargas del apoyo.','Fuerzas de conductor/viento, cable de retenida, anclaje y herrajes.','Resistividad de suelo, esquema PAT y medición de resistencia.','No se declara estabilidad, resultado Sulzberger ni resistencia PAT.']): s.text(28,199+i*10,'• '+t,1.65,AMBER if i<3 else RED, i==3)
 return s

def main():
 OUT.mkdir(parents=True,exist_ok=True)
 sheets=(make_lp(),make_pl(),make_u(),make_detail('D-01','ARMADOS: SUSPENSIÓN Y ÁNGULO',['SUSPENSIÓN','ÁNGULO','DESVÍO']),make_detail('D-02','ARMADOS: RETENCIÓN Y SUBESTACIÓN',['RETENCIÓN','ANCLAJE','SUBESTACIÓN']),make_d03())
 for sh in sheets:
  base=OUT/sh.code
  svg=base.with_suffix('.svg'); svg.write_text(sh.svg(),encoding='utf-8')
  sh.dxf(base.with_suffix('.dxf'),sh.code)
  subprocess.run(['mutool','draw','-q','-F','pdf','-o',str(base.with_suffix('.pdf')),str(svg)],check=True)
  subprocess.run(['mutool','draw','-q','-r','180','-F','png','-o',str(base.with_suffix('.png')),str(base.with_suffix('.pdf'))],check=True)
 package=OUT/'paquete_capachica_llachon_preliminar.zip'
 with zipfile.ZipFile(package,'w',zipfile.ZIP_DEFLATED) as z:
  for sh in sheets:
   for ext in ('.dxf','.pdf','.png','.svg'):
    p=OUT/(sh.code+ext); z.write(p,p.name)
  for p in (DATA/'estaciones_referencia_100m.csv',DATA/'metadatos_traza.json',DATA/'ruta_osrm_osm_2026-10-13.json',ROOT/'README.md',ROOT/'proyecto.yaml',ROOT/'requirements-cad.txt',ROOT/'documentacion/criterios_de_traza.md',ROOT/'documentacion/informe_base_geoespacial.md',ROOT/'scripts/preparar_traza.py',ROOT/'scripts/generar_planos_referencia.py',ROOT/'tests/test_geodata.py'):
   z.write(p,p.relative_to(ROOT).as_posix())
 print('Generadas seis láminas A3 en DXF/PDF/PNG/SVG; ruta de referencia',f'{rows[-1]["progresiva_geodesica_m"]:.2f}','m')
if __name__=='__main__': main()
