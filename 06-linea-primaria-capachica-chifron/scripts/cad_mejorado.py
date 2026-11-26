#!/usr/bin/env python3
"""CAD parametrico preliminar Capachica: una escena SVG y un DXF editable.

Los CSV son la fuente de datos. Las coordenadas de planta se conservan en UTM
en ModelSpace; las láminas se representan a escala en Layout A3.
"""
from __future__ import annotations

import csv
import html
import math
import os
import re
import shutil
import subprocess
import zipfile
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "entregables" / "mejorados"
W, H = 420.0, 297.0
FONT = "Arial, sans-serif"
COLORS = {"ink":"#172554", "blue":"#1d4ed8", "teal":"#0f766e", "gray":"#64748b", "light":"#e2e8f0", "red":"#b91c1c", "amber":"#b45309", "green":"#15803d", "white":"#ffffff"}
LAYERS = {
    "LP_EJE_MT":"1D4ED8", "LP_CONT_PEND":"B45309", "LP_VERTICES":"64748B", "LP_ESTRUCTURAS":"172554", "LP_SED":"0F766E",
    "PL_PERFIL_PREL":"64748B", "PL_VERTICES":"B91C1C", "PL_ESTRUCTURAS":"172554", "PL_TABLAS":"334155",
    "U_EXISTENTE_DECL":"64748B", "U_PROYECTADO":"1D4ED8", "U_PENDIENTE":"B45309", "U_TIERRA":"15803D",
    "D_ESTRUCTURA":"172554", "D_AISLAMIENTO":"1D4ED8", "D_HERRAJES":"64748B", "D_COTAS_PEND":"B45309", "D_PAT":"15803D",
    "SHEET":"172554", "SHEET_TEXT":"172554", "SHEET_PENDING":"B91C1C", "SHEET_TABLE":"334155",
}


def read_csv(path: Path):
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def text_xml(v: str) -> str:
    return html.escape(str(v), quote=True)


@dataclass
class Entity:
    kind: str
    layer: str
    args: tuple
    color: str = COLORS["ink"]
    width: float = 0.35
    dash: str = ""


@dataclass
class Scene:
    title: str
    code: str
    scale: str
    entities: list[Entity] = field(default_factory=list)

    def line(self, x1,y1,x2,y2, layer="SHEET", color=None, width=.35, dash=""):
        self.entities.append(Entity("line",layer,(x1,y1,x2,y2),color or COLORS["ink"],width,dash))
    def rect(self,x,y,w,h,layer="SHEET",color=None,width=.35,fill="none"):
        self.entities.append(Entity("rect",layer,(x,y,w,h,fill),color or COLORS["ink"],width))
    def circle(self,x,y,r,layer="SHEET",color=None,width=.35,fill="none"):
        self.entities.append(Entity("circle",layer,(x,y,r,fill),color or COLORS["ink"],width))
    def poly(self,pts,layer,color,width=.7,dash=""):
        self.entities.append(Entity("poly",layer,(tuple(pts),),color,width,dash))
    def text(self,x,y,s,size=2.3,layer="SHEET_TEXT",color=None,bold=False,anchor="start",rotate=0):
        self.entities.append(Entity("text",layer,(x,y,str(s),size,bold,anchor,rotate),color or COLORS["ink"],0))
    def table(self,x,y,width,headers,rows,col_widths=None,row_h=8,font=1.9,header_h=8):
        if not headers: return
        cw=col_widths or [width/len(headers)]*len(headers)
        self.rect(x,y,width,header_h+len(rows)*row_h,"SHEET_TABLE",COLORS["light"],.25,"#ffffff")
        self.rect(x,y,width,header_h,"SHEET_TABLE",COLORS["ink"],.25,"#eff6ff")
        xx=x
        for i,hdr in enumerate(headers):
            self.text(xx+1.5,y+5.2,hdr,font,"SHEET_TEXT",COLORS["ink"],True)
            if i: self.line(xx,y,xx,y+header_h+len(rows)*row_h,"SHEET_TABLE",COLORS["light"],.2)
            xx+=cw[i]
        for ri,row in enumerate(rows):
            yy=y+header_h+(ri+1)*row_h
            self.line(x,yy,x+width,yy,"SHEET_TABLE",COLORS["light"],.2)
            xx=x
            for ci,value in enumerate(row):
                self.text(xx+1.5,yy-row_h/2+font*.35,str(value),font,"SHEET_TEXT",COLORS["ink"],False)
                xx+=cw[ci]

    def frame(self,subtitle,stamp=True):
        self.rect(5,5,410,287,"SHEET",COLORS["ink"],.5,"#ffffff")
        self.rect(8,8,404,281,"SHEET",COLORS["light"],.25,"none")
        self.text(12,16,"LÍNEA PRIMARIA 22.9 kV CAPACHICA – CHIFRÓN",4.0,"SHEET_TEXT",COLORS["ink"],True)
        self.text(12,22,subtitle,2.4,"SHEET_TEXT",COLORS["gray"])
        if stamp:
            self.rect(299,10,109,12,"SHEET_PENDING",COLORS["red"],.45,"#fff7f7")
            self.text(353.5,15,"PRELIMINAR – USO ACADÉMICO",2.1,"SHEET_PENDING",COLORS["red"],True,"middle")
            self.text(353.5,19,"NO APTO PARA CONSTRUCCIÓN",2.1,"SHEET_PENDING",COLORS["red"],True,"middle")
        # Cajetín A3 horizontal.
        self.rect(8,263,404,26,"SHEET",COLORS["ink"],.4,"#ffffff")
        self.line(275,263,275,289,"SHEET",COLORS["ink"],.3)
        self.line(8,276,412,276,"SHEET",COLORS["ink"],.3)
        self.line(340,263,340,276,"SHEET",COLORS["ink"],.3)
        self.line(376,263,376,276,"SHEET",COLORS["ink"],.3)
        self.text(11,269,self.title,2.8,"SHEET_TEXT",COLORS["ink"],True)
        self.text(11,282,"UNA PUNO · FIME · MEC330 · Renzo Mamani Galindo · Rev. P0 · 2026-10-13",1.8,"SHEET_TEXT",COLORS["gray"])
        self.text(278,269,"ESTADO",1.6,"SHEET_TEXT",COLORS["gray"],True)
        self.text(292,269,"PRELIMINAR",2.2,"SHEET_PENDING",COLORS["red"],True)
        self.text(278,282,"ESCALA",1.6,"SHEET_TEXT",COLORS["gray"],True)
        self.text(308,282,self.scale,1.9,"SHEET_TEXT",COLORS["ink"],True)
        self.text(343,269,"LÁMINA",1.6,"SHEET_TEXT",COLORS["gray"],True)
        self.text(358,269,self.code,2.4,"SHEET_TEXT",COLORS["ink"],True)
        self.text(379,269,"FORMATO",1.4,"SHEET_TEXT",COLORS["gray"],True)
        self.text(381,274,"A3",2.0,"SHEET_TEXT",COLORS["ink"],True)

    def svg(self) -> str:
        out=[f'<svg xmlns="http://www.w3.org/2000/svg" width="420mm" height="297mm" viewBox="0 0 420 297">',
             '<rect width="420" height="297" fill="white"/>']
        for e in self.entities:
            a=e.args
            if e.kind=="line":
                x1,y1,x2,y2=a; dash=f' stroke-dasharray="{e.dash}"' if e.dash else ""
                out.append(f'<line x1="{x1:.3f}" y1="{y1:.3f}" x2="{x2:.3f}" y2="{y2:.3f}" stroke="{e.color}" stroke-width="{e.width}"{dash}/>')
            elif e.kind=="rect":
                x,y,w,h,fill=a; out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="{e.color}" stroke-width="{e.width}"/>')
            elif e.kind=="circle":
                x,y,r,fill=a; out.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="{e.color}" stroke-width="{e.width}"/>')
            elif e.kind=="poly":
                points=a[0]; dash=f' stroke-dasharray="{e.dash}"' if e.dash else ""
                pts=" ".join(f"{x:.3f},{y:.3f}" for x,y in points)
                out.append(f'<polyline points="{pts}" fill="none" stroke="{e.color}" stroke-width="{e.width}"{dash}/>')
            elif e.kind=="text":
                x,y,s,size,bold,anchor,rotate=a; rot=f' transform="rotate({rotate} {x} {y})"' if rotate else ""
                weight="700" if bold else "400"
                out.append(f'<text x="{x:.3f}" y="{y:.3f}" font-family="{FONT}" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" fill="{e.color}"{rot}>{text_xml(s)}</text>')
        out.append('</svg>')
        return "\n".join(out)


def load_data():
    s=read_csv(ROOT/"datos/estructuras/planilla_estructuras_lp_capachica.csv")
    v=read_csv(ROOT/"datos/topografia/planilla_vertices_lp.csv")
    p=read_csv(ROOT/"datos/topografia/topografia_coordenadas_PENZD.csv")
    return s,v,p


def route_and_structures(structures, vertices, penzd):
    chain=[]; distance=0.0; last=None
    for r in penzd:
        x,y,z=float(r["Este"]),float(r["Norte"]),float(r["Cota"])
        if last: distance+=math.hypot(x-last[0],y-last[1])
        chain.append((distance,x,y,z,r["Descripcion"]))
        last=(x,y)
    route=[(float(r["progresiva_m"]),float(r["este_m"]),float(r["norte_m"]),float(r["cota_msnm"])) for r in vertices]
    coords=[]
    for st in structures:
        station=float(st["progresiva_m"])
        match=None
        for (d1,x1,y1,z1,_),(d2,x2,y2,z2,_) in zip(chain,chain[1:]):
            if d1-1e-7<=station<=d2+1e-7:
                f=0 if d2==d1 else (station-d1)/(d2-d1)
                match=(x1+f*(x2-x1),y1+f*(y2-y1),z1+f*(z2-z1)); break
        if match is None:
            # The route includes the first point at station zero.
            q=min(chain,key=lambda r:abs(r[0]-station)); match=(q[1],q[2],q[3])
        coords.append({**st,"station":station,"x":match[0],"y":match[1],"z":match[2],"coord_source":"poligonal interpolada"})
    return route,coords,chain


def route_angles(coords):
    """Deflection at supports from the recorded polyline, matching planilla sign."""
    v=read_csv(ROOT/"datos/topografia/planilla_vertices_lp.csv")
    by_station={}
    for i in range(1,len(v)-1):
        a,b,c=v[i-1],v[i],v[i+1]
        ux=float(b["este_m"])-float(a["este_m"]); uy=float(b["norte_m"])-float(a["norte_m"])
        vx=float(c["este_m"])-float(b["este_m"]); vy=float(c["norte_m"])-float(b["norte_m"])
        cross=ux*vy-uy*vx; dot=ux*vx+uy*vy
        # The project CSV uses the opposite sign to the usual E/N cross product.
        by_station[round(float(b["progresiva_m"]),2)]=-math.degrees(math.atan2(cross,dot))
    return [next((ang for sta,ang in by_station.items() if abs(sta-p["station"])<0.025),0.0) for p in coords]


def add_model_data(doc,route,coords,profile=None):
    msp=doc.modelspace()
    for name,color in LAYERS.items():
        if name not in doc.layers: doc.layers.new(name,dxfattribs={"color":7})
    # Exact UTM coordinates, metres. A coordinate polyline and station/support blocks.
    e4=next((p["station"] for p in coords if p["id_estructura"]=="E-04"),0.0)
    before=[(x,y) for s,x,y,z in route if s<=e4+1e-5]
    after=[(x,y) for s,x,y,z in route if s>=e4-1e-5]
    if len(before)>1: msp.add_lwpolyline(before,dxfattribs={"layer":"LP_EJE_MT"})
    if len(after)>1: msp.add_lwpolyline(after,dxfattribs={"layer":"LP_CONT_PEND"})
    for p in coords:
        bname="SAB1" if p["id_estructura"]=="E-04" else "APOYO_MT"
        if bname not in doc.blocks:
            block=doc.blocks.new(bname)
            block.add_circle((0,0),.8,dxfattribs={"layer":"LP_ESTRUCTURAS"})
            block.add_line((-.5,0),(.5,0),dxfattribs={"layer":"LP_ESTRUCTURAS"})
            block.add_line((0,-.5),(0,.5),dxfattribs={"layer":"LP_ESTRUCTURAS"})
            if bname=="SAB1": block.add_circle((0,0),1.8,dxfattribs={"layer":"LP_SED"})
            for tag,dy in (("ID",0.45),("ARMADO",0.2),("PROG",-0.2),("COTA",-0.45)):
                block.add_attdef(tag,insert=(0.9,dy),dxfattribs={"layer":"LP_ESTRUCTURAS","height":0.08})
        ins=msp.add_blockref(bname,(p["x"],p["y"]),dxfattribs={"layer":"LP_SED" if bname=="SAB1" else "LP_ESTRUCTURAS"})
        ins.add_auto_attribs({"ID":p["id_estructura"],"ARMADO":p["armado_dge"],"PROG":f'{p["station"]:.2f}',"COTA":f'{float(p["cota_terreno_msnm"]):.2f}'})
    if profile:
        # Profile ModelSpace: station [m], elevation [m], true source coordinates.
        doc.header["$INSUNITS"]=6
        pr=doc.modelspace()
        pr.add_lwpolyline([(float(r["Progresiva"]),float(r["Cota"])) for r in profile],dxfattribs={"layer":"PL_PERFIL_PREL"})


def add_parametric_library(doc):
    """Attribute-backed, reusable schematic blocks; dimensions are not asserted."""
    lib="CAD_BIBLIOTECA"
    if lib not in doc.layers: doc.layers.new(lib,dxfattribs={"color":8})
    definitions={
        "ARMADO_PS1":("PS-1",[(0,0,0,70),(0,48,-24,48),(0,48,-17,55),(0,48,0,55),(0,48,17,55),(0,48,24,48)]),
        "ARMADO_PA1":("PA-1",[(0,0,0,70),(0,48,-24,48),(0,48,-17,55),(0,48,0,55),(0,48,17,55),(0,48,24,48),(-18,30,-30,20)]),
        "ARMADO_PR1":("PR-1",[(0,0,0,70),(0,48,-24,48),(0,48,-17,55),(0,48,0,55),(0,48,17,55),(0,48,24,48)]),
        "ARMADO_SAB1":("SAB-1",[(-18,0,-18,70),(18,0,18,70),(-18,48,18,48),(-8,34,8,34)]),
        "RETENIDA_REF":("R-1",[(0,0,0,70),(0,48,38,0)]),
        "CIMENTACION_REF":("CIMENTACIÓN",[(0,0,0,70),(-18,0,18,0),(18,0,18,-28),(18,-28,-18,-28),(-18,-28,-18,0)]),
        "PAT3_TIPO":("PAT-3",[(0,0,0,40),(16,0,16,40),(32,0,32,40)]),
    }
    for name,(code,lines) in definitions.items():
        if name in doc.blocks: continue
        b=doc.blocks.new(name)
        for x1,y1,x2,y2 in lines: b.add_line((x1,y1),(x2,y2),dxfattribs={"layer":"0"})
        for i,dy in enumerate((82,78,74)):
            tag=("CODIGO","ESTADO","DIMENSIONES")[i]
            val=code if i==0 else ("ESQUEMÁTICO" if i==1 else "PENDIENTES")
            b.add_attdef(tag,insert=(0,dy),text=val,dxfattribs={"height":2.0,"layer":"0"})
    # Block definitions carry attributes; no hidden inserts distort model extents.


def add_scene_to_modelspace(msp,scene):
    """Expose schematic sheets in ModelSpace as editable CAD geometry (NTS sheets)."""
    for e in scene.entities:
        a=e.args; attrs={"layer":e.layer}
        if e.kind=="line":
            x1,y1,x2,y2=a; msp.add_line((x1,H-y1),(x2,H-y2),dxfattribs=attrs)
        elif e.kind=="rect":
            x,y,w,h,fill=a; msp.add_lwpolyline([(x,H-y),(x+w,H-y),(x+w,H-y-h),(x,H-y-h)],close=True,dxfattribs=attrs)
        elif e.kind=="circle":
            x,y,r,fill=a; msp.add_circle((x,H-y),r,dxfattribs=attrs)
        elif e.kind=="poly":
            pts=a[0]; msp.add_lwpolyline([(x,H-y) for x,y in pts],dxfattribs=attrs)
        elif e.kind=="text":
            x,y,s,size,bold,anchor,rotate=a
            msp.add_text(s,dxfattribs={**attrs,"height":size,"rotation":-rotate}).set_placement((x,H-y))


def export_scene(scene: Scene, path: Path, model=None, profile=None):
    """Write editable DXF paper layout + full-value model geometry."""
    try:
        import ezdxf
    except ImportError as exc:
        raise RuntimeError("ezdxf no está instalado en el entorno virtual") from exc
    doc=ezdxf.new("R2010",setup=True)
    doc.header["$INSUNITS"]=6 if scene.code in {"LP-01","PL-01"} else 4
    for name,color in LAYERS.items():
        if name not in doc.layers:
            try: color_num=ezdxf.colors.rgb2int(tuple(int(color[i:i+2],16) for i in (0,2,4)))
            except Exception: color_num=7
            doc.layers.new(name,dxfattribs={"color":7,"true_color":color_num,"lineweight":25})
    add_parametric_library(doc)
    if model:
        route,structures=model
        add_model_data(doc,route,structures,profile)
    elif profile:
        doc.header["$INSUNITS"]=6
        msp=doc.modelspace()
        msp.add_lwpolyline([(float(r["Progresiva"]),float(r["Cota"])) for r in profile],dxfattribs={"layer":"PL_PERFIL_PREL"})
    elif scene.code not in {"LP-01","PL-01"}:
        add_scene_to_modelspace(doc.modelspace(),scene)
    # Physical sheet geometry is 1:1 mm in paper space.
    layout=doc.layouts.new("A3_PRELIMINAR")
    try: layout.page_setup(size=(420,297),units="mm",margins=(0,0,0,0),label="A3 horizontal")
    except Exception: pass
    for e in scene.entities:
        a=e.args; attrs={"layer":e.layer}
        if e.kind=="line":
            x1,y1,x2,y2=a; layout.add_line((x1,H-y1),(x2,H-y2),dxfattribs=attrs)
        elif e.kind=="rect":
            x,y,w,h,fill=a; layout.add_lwpolyline([(x,H-y),(x+w,H-y),(x+w,H-y-h),(x,H-y-h)],close=True,dxfattribs=attrs)
        elif e.kind=="circle":
            x,y,r,fill=a; layout.add_circle((x,H-y),r,dxfattribs=attrs)
        elif e.kind=="poly":
            points=a[0]; layout.add_lwpolyline([(x,H-y) for x,y in points],dxfattribs=attrs)
        elif e.kind=="text":
            x,y,s,size,bold,anchor,rotate=a
            entity=layout.add_text(s,dxfattribs={**attrs,"height":size,"rotation":-rotate})
            entity.set_placement((x,H-y))
    if scene.code in {"LP-01","PL-01"}:
        # Keep geographic/profile ModelSpace access obvious in file metadata.
        doc.header["$INSUNITS"]=6
    doc.saveas(path)


def convert_svg(svg_path: Path, pdf_path: Path, png_path: Path):
    mutool=shutil.which("mutool")
    if not mutool: raise RuntimeError("mutool no disponible para exportar PDF/PNG desde SVG")
    subprocess.run([mutool,"draw","-q","-F","pdf","-o",str(pdf_path),str(svg_path)],check=True,capture_output=True)
    subprocess.run([mutool,"draw","-q","-r","180","-F","png","-o",str(png_path),str(pdf_path)],check=True,capture_output=True)


def build_lp01(structures,vertices,route,coords):
    sc=Scene("PLANTA DE LÍNEA PRIMARIA Y COORDENADAS","LP-01","H/V ≈ 1:4050")
    sc.frame("TRAZA GEOREFERENCIADA · WGS 84 / UTM ZONA 19S · COORDENADAS DECLARADAS/DERIVADAS")
    sc.text(20,35,"TRAZA POR PROGRESIVAS · E-04 = SAB-1 DECLARADA; E-09 = EXTREMO DOCUMENTADO",2.2,"SHEET_TEXT",COLORS["ink"],True)
    # Map geometry: isotropic scale, coordinates from PENZD; support positions are chainage interpolations.
    gx,gy,gw,gh=22,43,238,203
    sc.rect(gx,gy,gw,gh,"SHEET_TABLE",COLORS["light"],.25,"#fcfdff")
    xs=[p[1] for p in route]; ys=[p[2] for p in route]
    minx,maxx,miny,maxy=min(xs),max(xs),min(ys),max(ys)
    scale=min((gw-24)/(maxx-minx),(gh-22)/(maxy-miny))
    def mp(x,y): return (gx+(gw-(maxx-minx)*scale)/2+(x-minx)*scale, gy+gh-11-(y-miny)*scale)
    routepts=[mp(x,y) for _,x,y,_ in route]
    # Draw two semantically distinct spans, no implication of service past E-04.
    e4=float(next(p["station"] for p in coords if p["id_estructura"]=="E-04"))
    before=[mp(x,y) for s,x,y,z in route if s<=e4+1e-5]
    after=[mp(x,y) for s,x,y,z in route if s>=e4-1e-5]
    if len(before)>1: sc.poly(before,"LP_EJE_MT",COLORS["blue"],1.05)
    if len(after)>1: sc.poly(after,"LP_CONT_PEND",COLORS["amber"],.9,"2 1.5")
    support_stations={round(p["station"],2) for p in coords}
    unassigned=[]
    for station,xm,ym,zm in route[1:-1]:
        if not any(abs(station-ss)<0.03 for ss in support_stations):
            px,py=mp(xm,ym); unassigned.append((station,px,py))
            sc.poly([(px,py-1.3),(px+1.3,py),(px,py+1.3),(px-1.3,py),(px,py-1.3)],"LP_VERTICES",COLORS["red"],.45)
    for i,p in enumerate(coords):
        x,y=mp(p["x"],p["y"]); is_sed=p["id_estructura"]=="E-04"
        sc.circle(x,y,2.0 if is_sed else 1.3,"LP_SED" if is_sed else "LP_ESTRUCTURAS",COLORS["teal"] if is_sed else COLORS["ink"],.5,"#ccfbf1" if is_sed else "#ffffff")
        label=f'{p["id_estructura"]} · {p["station"]:.2f} m'
        dx=3.0 if i%2==0 else -3.0; anchor="start" if dx>0 else "end"
        sc.text(x+dx,y-1.3,label,1.7,"SHEET_TEXT",COLORS["ink"],True,anchor)
        if is_sed: sc.text(x+4,y+4,"SAB-1 / 100 kVA declarada",1.7,"LP_SED",COLORS["teal"],True)
    sc.text(gx+gw-4,gy+8,"N",2.5,"SHEET_TEXT",COLORS["ink"],True,"middle")
    sc.line(gx+gw-4,gy+10,gx+gw-4,gy+23,"SHEET",COLORS["ink"],.6)
    sc.poly([(gx+gw-6,gy+14),(gx+gw-4,gy+10),(gx+gw-2,gy+14)],"SHEET",COLORS["ink"],.6)
    sc.text(20,252,"SÓLIDO: E-01–E-04  ·  TRAZO DECLARADO",1.8,"SHEET_TEXT",COLORS["blue"],True)
    sc.text(20,257,"DISCONTINUO: E-04–E-09 · 511.39 m · CONTINUIDAD PENDIENTE DE DEFINICIÓN FUNCIONAL",1.8,"SHEET_PENDING",COLORS["amber"],True)
    sc.text(20,248,"Escala gráfica aproximada en coordenadas UTM; confirmar impresión al 100%.",1.5,"SHEET_TEXT",COLORS["gray"])
    # Scale bar, 100 m in paper coordinates.
    bar=100*scale; sc.line(30,242,30+bar,242,"SHEET",COLORS["ink"],.65); sc.line(30,240,30,244,"SHEET",COLORS["ink"],.65); sc.line(30+bar,240,30+bar,244,"SHEET",COLORS["ink"],.65); sc.text(30,239,"0",1.5); sc.text(30+bar,239,"100 m",1.5,"SHEET_TEXT",COLORS["ink"],False,"end")
    rows=[]
    angles=route_angles(coords)
    for p,ang in zip(coords,angles):
        rows.append([p["id_estructura"],f'{p["station"]:.2f}',f'{p["x"]:.2f}',f'{p["y"]:.2f}',f'{ang:+.1f}°',p["armado_dge"]])
    sc.text(268,35,"CUADRO DE ESTRUCTURAS / COORDENADAS",2.3,"SHEET_TEXT",COLORS["ink"],True)
    sc.table(268,40,140,["ID","Prog. m","Este m","Norte m","Δ° calc.","Armado"],rows,[20,23,27,29,21,20],row_h=7.7,font=1.5,header_h=8)
    spanrows=[]
    for a,b in zip(coords,coords[1:]): spanrows.append([a["id_estructura"]+"–"+b["id_estructura"],f'{b["station"]-a["station"]:.2f} m',"Declarado por progresivas"])
    sc.text(268,127,"CUADRO DE VANOS",2.1,"SHEET_TEXT",COLORS["ink"],True)
    sc.table(268,131,140,["Tramo","Longitud","Origen"],spanrows,[43,28,69],row_h=7.5,font=1.55,header_h=8)
    sc.text(268,212,"CRITERIO DE DATOS",2.1,"SHEET_TEXT",COLORS["ink"],True)
    notes=["E-01/E-04: puntos declarados en archivos del proyecto.","E-02/E-03 y apoyos no coincidentes con vértice: posición interpolada sobre poligonal PENZD.","Ángulos de apoyo calculados en quiebres coincidentes; convención de signo del archivo fuente.",f"Quiebres sin estructura ID: {', '.join(f'{s:.2f}' for s,_,_ in unassigned[:6])} m; revisar spotting.","Caminos/servidumbre no acreditados. UTM 19S declarado; confirmar EPSG/datum."]
    for i,n in enumerate(notes): sc.text(270,218+i*7,n,1.55,"SHEET_TEXT",COLORS["gray"])
    return sc


def build_pl01(structures,profile):
    sc=Scene("PERFIL LONGITUDINAL PRELIMINAR","PL-01","H 1:2200 · V 1:840 aprox.")
    sc.frame("PERFIL DE REFERENCIA · COTAS DECLARADAS EN VÉRTICES + INTERPOLACIÓN LINEAL INTERMEDIA")
    sc.text(20,35,"NO INCLUYE CATENARIA NI GÁLIBOS: FALTAN VALIDACIÓN DE PERFIL Y DATOS MECÁNICOS TRAZABLES",2.0,"SHEET_PENDING",COLORS["red"],True)
    x0,x1,y0,y1=28,403,48,191
    sc.rect(x0,y0,x1-x0,y1-y0,"SHEET_TABLE",COLORS["light"],.25,"#ffffff")
    xmin,xmax=0,816.60; zmin,zmax=3810,3930
    def pt(s,z): return (x0+(s-xmin)/(xmax-xmin)*(x1-x0), y1-(z-zmin)/(zmax-zmin)*(y1-y0))
    # Grid and labels.
    for s in range(0,817,100):
        x,_=pt(s,zmin); sc.line(x,y0,x,y1,"SHEET_TABLE",COLORS["light"],.2); sc.text(x,y1+4,str(s),1.4,"SHEET_TEXT",COLORS["gray"],False,"middle")
    for z in range(3810,3931,20):
        _,y=pt(0,z); sc.line(x0,y,x1,y,"SHEET_TABLE",COLORS["light"],.2); sc.text(x0-2,y+1,str(z),1.45,"SHEET_TEXT",COLORS["gray"],False,"end")
    vrows=profile
    # The source series consists of points interpolated along lines between vertex elevations.
    sc.poly([pt(float(r["Progresiva"]),float(r["Cota"])) for r in vrows],"PL_PERFIL_PREL",COLORS["gray"],.9,"1.5 1")
    major=read_csv(ROOT/"datos/topografia/planilla_vertices_lp.csv")
    close_groups=[]
    for ri,r in enumerate(major):
        x,y=pt(float(r["progresiva_m"]),float(r["cota_msnm"]))
        sc.circle(x,y,1.15,"PL_VERTICES",COLORS["red"],.4,"#fee2e2")
        # Put very close chainages into a compact, indexed callout strip rather
        # than letting elevation labels collide over the terrain profile.
        station=float(r["progresiva_m"])
        if close_groups and station-close_groups[-1][-1][0] < 52:
            close_groups[-1].append((station,r["nombre"],float(r["cota_msnm"]),x,y))
        else:
            close_groups.append([(station,r["nombre"],float(r["cota_msnm"]),x,y)])
    for group in close_groups:
        for j,(_,name,elev,x,y) in enumerate(group):
            side=-1 if j%2==0 else 1
            label_x=max(x0+1,min(x1-25,x+(4.0 if side>0 else -4.0)))
            label_y=y+(5.0+3.5*(j//2) if side>0 else -3.0-3.5*(j//2))
            anchor="start" if label_x>=x else "end"
            sc.line(x,y,label_x,label_y-1.0,"PL_VERTICES",COLORS["red"],.22)
            sc.text(label_x,label_y,f'{name} {elev:.2f}',1.35,"SHEET_TEXT",COLORS["red"],True,anchor)
    for st in structures:
        x,y=pt(float(st["progresiva_m"]),float(st["cota_terreno_msnm"]))
        sc.line(x,y-3,x,y+2,"PL_ESTRUCTURAS",COLORS["ink"],.7)
        sc.text(x,y+5,st["id_estructura"],1.5,"SHEET_TEXT",COLORS["ink"],True,"middle")
    sc.text(28,198,"Progresiva acumulada (m)",1.5,"SHEET_TEXT",COLORS["gray"])
    sc.text(14,100,"Cota msnm",1.5,"SHEET_TEXT",COLORS["gray"],True,"middle",-90)
    # Identify E04 onward without implying loads or a terminal electrical condition.
    e4=305.21; x,_=pt(e4,zmin); sc.line(x,y0,x,y1,"SHEET_PENDING",COLORS["amber"],.45,"2 1.5")
    sc.text(x+2,y0+5,"E-04 SAB-1 declarada",1.6,"SHEET_PENDING",COLORS["amber"],True)
    sc.rect(x+5,y0+11,x1-x-12,12,"SHEET_PENDING",COLORS["amber"],.35,"#fffbeb")
    sc.text((x+x1)/2,y0+18,"E-04–E-09 · 511.39 m · continuidad funcional pendiente",1.9,"SHEET_PENDING",COLORS["amber"],True,"middle")
    # Table of structures and source elevations.
    rows=[]
    for st in structures:
        rows.append([st["id_estructura"],f'{float(st["progresiva_m"]):.2f}',f'{float(st["cota_terreno_msnm"]):.2f}',f'{float(st["altura_m"]):.1f} m nominal',st["armado_dge"]])
    sc.text(20,204,"CUADRO DE ESTRUCTURAS · ALTURA NOMINAL DECLARADA; EXPOSICIÓN Y SUJECIONES PENDIENTES",1.55,"SHEET_TEXT",COLORS["ink"],True)
    sc.table(20,207,385,["ID","Prog. m","Cota declarada","Poste nominal","Armado declarado"],rows,[27,42,48,84,184],row_h=5.05,font=1.45,header_h=6)
    sc.text(22,261,"DEM/SRTM declarado; ráster/precisión no adjuntos. Intermedios interpolados, no observaciones independientes.",1.25,"SHEET_PENDING",COLORS["red"])
    return sc


def build_u01():
    sc=Scene("DIAGRAMA UNIFILAR DE MEDIA TENSIÓN","U-01","Esquemático · NTS")
    sc.frame("22.9 kV · 3 FASES · 60 Hz · TOPOLOGÍA PROPUESTA / DECLARADA")
    sc.text(20,35,"LEYENDA: DECLARADO EN DATOS  ·  PROPUESTO  ·  PENDIENTE DE SELECCIÓN / COORDINACIÓN",1.9,"SHEET_TEXT",COLORS["ink"],True)
    # Main path left-center with explicit continuation warning.
    sc.line(90,52,90,93,"U_EXISTENTE_DECL",COLORS["gray"],1.2)
    sc.rect(67,42,46,11,"U_EXISTENTE_DECL",COLORS["gray"],.4,"#f1f5f9")
    sc.text(90,46,"PUNTO DE DERIVACIÓN E-01",1.9,"SHEET_TEXT",COLORS["ink"],True,"middle")
    sc.text(90,50,"Equipo/concesionaria: verificar",1.5,"SHEET_TEXT",COLORS["gray"],False,"middle")
    sc.rect(71,65,38,13,"U_PENDIENTE",COLORS["amber"],.5,"#fffbeb")
    sc.text(90,70,"PROTECCIÓN MT",1.9,"SHEET_PENDING",COLORS["amber"],True,"middle")
    sc.text(90,75,"tipo/rating por coordinar",1.6,"SHEET_PENDING",COLORS["amber"],False,"middle")
    sc.line(90,78,90,93,"U_PROYECTADO",COLORS["blue"],1.1)
    sc.line(90,93,90,143,"U_PROYECTADO",COLORS["blue"],2)
    sc.text(94,105,"E-01–E-04 · 305.21 m",1.8,"SHEET_TEXT",COLORS["ink"],True)
    sc.text(94,111,"AAAC 35 mm² declarado",1.7,"SHEET_TEXT",COLORS["gray"])
    # SED tap, transformer and pending protections.
    sc.line(90,125,111,125,"U_PROYECTADO",COLORS["blue"],1.0)
    sc.text(90,121,"E-04",1.7,"SHEET_TEXT",COLORS["teal"],True,"middle")
    sc.rect(111,115,39,20,"U_PENDIENTE",COLORS["amber"],.45,"#fffbeb")
    sc.text(130.5,122,"3× CUT-OUT / FUSIBLE",1.35,"SHEET_PENDING",COLORS["amber"],True,"middle")
    sc.text(130.5,129,"tipo, curva y rating: PENDIENTES",1.2,"SHEET_PENDING",COLORS["amber"],False,"middle")
    sc.line(150,125,173,125,"U_PROYECTADO",COLORS["blue"],1.0)
    sc.rect(173,111,82,39,"U_PROYECTADO",COLORS["blue"],.6,"#eff6ff")
    sc.text(214,118,"SAB-1 · 100 kVA",2.1,"SHEET_TEXT",COLORS["ink"],True,"middle")
    sc.text(214,124,"Dato declarado · relación 22.9 kV",1.55,"SHEET_TEXT",COLORS["gray"],False,"middle")
    sc.text(214,130,"Conexión y protección: pendientes",1.55,"SHEET_PENDING",COLORS["amber"],True,"middle")
    sc.text(214,137,"BT solo como límite de alcance",1.45,"SHEET_TEXT",COLORS["gray"],False,"middle")
    # Arrester is shown as proposed symbol only; no nominal voltage/energy rating selected.
    sc.line(158,125,158,139,"U_PENDIENTE",COLORS["amber"],.65)
    sc.circle(158,143,3,"U_PENDIENTE",COLORS["amber"],.5,"#fffbeb")
    sc.text(158,144,"ZnO",1.15,"SHEET_PENDING",COLORS["amber"],True,"middle")
    sc.line(158,146,158,151,"U_TIERRA",COLORS["green"],.6)
    sc.line(154,151,162,151,"U_TIERRA",COLORS["green"],.5)
    sc.text(166,147,"Pararrayos propuesto; selección pendiente",1.25,"SHEET_PENDING",COLORS["amber"])
    sc.line(255,130,267,130,"SHEET_PENDING",COLORS["red"],.8,"2 1")
    sc.text(269,131,"Límite de expediente MT",1.35,"SHEET_PENDING",COLORS["red"],True)
    # Continuation is explicitly unassigned; it is not shown as a load branch.
    sc.line(90,143,90,199,"U_PENDIENTE",COLORS["amber"],1.3,"3 2")
    sc.rect(52,160,76,26,"U_PENDIENTE",COLORS["amber"],.5,"#fffbeb")
    sc.text(90,167,"E-04–E-09 · 511.39 m",2.0,"SHEET_PENDING",COLORS["amber"],True,"middle")
    sc.text(90,174,"CONTINUIDAD PENDIENTE",1.8,"SHEET_PENDING",COLORS["red"],True,"middle")
    sc.text(90,180,"Sin carga ni función asignada",1.5,"SHEET_TEXT",COLORS["gray"],False,"middle")
    sc.rect(53,199,74,12,"U_EXISTENTE_DECL",COLORS["gray"],.4,"#f1f5f9")
    sc.text(90,207,"E-09 · extremo documentado",1.8,"SHEET_TEXT",COLORS["ink"],True,"middle")
    # Legend/status panel.
    sc.text(273,55,"ESTADO DE INFORMACIÓN",2.3,"SHEET_TEXT",COLORS["ink"],True)
    for i,(color,title,body) in enumerate([
        (COLORS["gray"],"DECLARADO","Punto E-01, SAB-1 100 kVA, longitudes y designación de conductor."),
        (COLORS["blue"],"PROPUESTA DE REPRESENTACIÓN","Esquema de línea y derivación a transformador; validar con concesionaria."),
        (COLORS["amber"],"PENDIENTE","Cut-out, fusible, pararrayos, ratings y coordinación con datos de cortocircuito."),
        (COLORS["red"],"NO RESUELTO","Continuidad E-04–E-09 y cargas/función del tramo."),
    ]):
        y=65+i*32; sc.line(274,y,282,y,color,1.5); sc.text(286,y+1,title,1.8,"SHEET_TEXT",color,True); sc.text(274,y+9,body,1.7,"SHEET_TEXT",COLORS["gray"])
    sc.rect(270,205,132,35,"SHEET_PENDING",COLORS["red"],.4,"#fff7f7")
    sc.text(274,213,"NO HAY COORDINACIÓN DE PROTECCIONES",1.8,"SHEET_PENDING",COLORS["red"],True)
    sc.text(274,221,"Se requieren Scc, curvas de fusibles,",1.7,"SHEET_TEXT",COLORS["gray"])
    sc.text(274,228,"fichas de equipos y criterios de ELPU.",1.7,"SHEET_TEXT",COLORS["gray"])
    return sc


def draw_support_symbol(sc,cx,top,title,kind):
    # Diagrammatic views; not dimensional without approved DGE sheet and assembly list.
    sc.rect(cx-31,top,62,62,"D_ESTRUCTURA",COLORS["light"],.3,"#ffffff")
    sc.text(cx,top+6,title,2.0,"SHEET_TEXT",COLORS["ink"],True,"middle")
    sc.line(cx,top+14,cx,top+53,"D_ESTRUCTURA",COLORS["ink"],1.0)
    if kind in {"PS-1","PA-1"}:
        sc.line(cx-20,top+20,cx+20,top+20,"D_ESTRUCTURA",COLORS["ink"],1.2)
        for dx in [-16,0,16]: sc.circle(cx+dx,top+16,2,"D_AISLAMIENTO",COLORS["blue"],.5,"#dbeafe"); sc.line(cx+dx,top+18,cx+dx,top+20,"D_AISLAMIENTO",COLORS["blue"],.35)
    elif kind=="PR-1":
        sc.line(cx-23,top+20,cx+23,top+20,"D_ESTRUCTURA",COLORS["ink"],1.2)
        for dx in [-16,0,16]: sc.circle(cx+dx,top+17,2,"D_AISLAMIENTO",COLORS["blue"],.5,"#dbeafe")
        sc.line(cx-15,top+22,cx-24,top+31,"D_HERRAJES",COLORS["gray"],.7)
    elif kind=="SAB-1":
        sc.line(cx-25,top+20,cx+25,top+20,"D_ESTRUCTURA",COLORS["ink"],1)
        sc.line(cx-25,top+14,cx-25,top+53,"D_ESTRUCTURA",COLORS["ink"],1)
        sc.rect(cx-11,top+31,22,13,"D_HERRAJES",COLORS["gray"],.6,"#f1f5f9")
        sc.text(cx,top+39,"TRAFO",1.6,"SHEET_TEXT",COLORS["gray"],True,"middle")
    sc.text(cx,top+58,"Dimensiones/montaje: POR DEFINIR",1.4,"SHEET_PENDING",COLORS["amber"],True,"middle")
    # Tiny lateral diagram.
    sx=cx+39
    sc.text(sx,top+10,"LATERAL",1.35,"SHEET_TEXT",COLORS["gray"],True,"middle")
    sc.line(sx,top+17,sx,top+47,"D_ESTRUCTURA",COLORS["ink"],.7)
    sc.line(sx-8,top+21,sx+8,top+21,"D_ESTRUCTURA",COLORS["ink"],.7)
    sc.line(sx-8,top+21,sx-8,top+39,"D_HERRAJES",COLORS["gray"],.5)
    sc.line(sx-8,top+39,sx-20,top+52,"D_HERRAJES",COLORS["gray"],.6,"1 1")


def build_detail(code,title,kinds):
    sc=Scene(title,code,"Esquemático · NTS")
    sc.frame("REPRESENTACIÓN TIPOLÓGICA · DIMENSIONES CONSTRUCTIVAS PENDIENTES DE FUENTE OFICIAL")
    sc.text(20,35,"SÍMBOLOS Y DISPOSICIÓN CONCEPTUAL · NO USAR COMO PLANO DE MONTAJE",2.0,"SHEET_PENDING",COLORS["red"],True)
    positions=[92,210,328]
    material=[]
    for i,kind in enumerate(kinds):
        cx=positions[i]; draw_support_symbol(sc,cx,48,kind,"SAB-1" if kind=="SAB-1" else kind)
        material.append([kind,"1 conjunto (declarado)","dimensiones / norma: verificar"])
    sc.text(22,125,"VISTA DE PLANTA / ARMADO",2.1,"SHEET_TEXT",COLORS["ink"],True)
    # Only symbolic conductor direction and attachment labels.
    for i,kind in enumerate(kinds):
        x=positions[i]
        sc.line(x-27,146,x+27,146,"D_ESTRUCTURA",COLORS["ink"],1.1)
        sc.circle(x-16,146,1.8,"D_AISLAMIENTO",COLORS["blue"],.4,"#dbeafe")
        sc.circle(x,146,1.8,"D_AISLAMIENTO",COLORS["blue"],.4,"#dbeafe")
        sc.circle(x+16,146,1.8,"D_AISLAMIENTO",COLORS["blue"],.4,"#dbeafe")
        sc.text(x,153,"3 fases · punto de sujeción por verificar",1.35,"SHEET_TEXT",COLORS["gray"],False,"middle")
    sc.text(22,166,"LISTA DE COMPONENTES (SIN DIMENSIONES NO SUSTENTADAS)",2.0,"SHEET_TEXT",COLORS["ink"],True)
    rows=[]
    for k in kinds: rows.append([k,"Estructura / aisladores / ferretería", "Validar con lámina DGE aplicable + ELPU"])
    sc.table(22,171,376,["Armado","Familias representadas","Referencia / estado"],rows,[40,125,211],row_h=11,font=1.8,header_h=8)
    sc.text(22,228,"PENDIENTES: código exacto de lámina DGE y revisión; poste/carga; cruceta; aislador; pernos; distancias eléctricas; herrajes; puesta a tierra; criterio de retenida.",1.7,"SHEET_PENDING",COLORS["amber"])
    sc.text(22,238,"Las figuras no atribuyen dimensiones a la DGE. El detalle constructivo debe reemplazarse o cotejarse con el patrón oficial y requerimientos de la concesionaria.",1.65,"SHEET_TEXT",COLORS["gray"])
    return sc


def build_d03():
    sc=Scene("CIMENTACIONES · RETENIDAS · PUESTA A TIERRA","D-03","Esquemático · NTS")
    sc.frame("DETALLES TIPOLÓGICOS · SUELO, CARGAS, GEOMETRÍA Y ENSAYOS PENDIENTES")
    sc.text(20,35,"NO SE GARANTIZA ESTABILIDAD NI RESISTENCIA ELÉCTRICA SIN DATOS DE SITIO",2.0,"SHEET_PENDING",COLORS["red"],True)
    panels=[(18,47,121,127,"CIMENTACIÓN"),(149,47,121,127,"RETENIDA"),(280,47,121,127,"PAT-3")]
    for x,y,w,h,title in panels:
        sc.rect(x,y,w,h,"SHEET_TABLE",COLORS["light"],.35,"#ffffff"); sc.text(x+4,y+7,title,2.0,"SHEET_TEXT",COLORS["ink"],True)
    # Foundation typology, without dimensions.
    sc.line(78,65,78,133,"D_ESTRUCTURA",COLORS["ink"],2.0)
    sc.line(36,98,120,98,"SHEET_TABLE",COLORS["gray"],.6)
    sc.rect(58,97,40,31,"D_COTAS_PEND",COLORS["amber"],.5,"#fffbeb")
    sc.text(78,144,"Dimensiones, suelo y cargas pendientes",1.55,"SHEET_PENDING",COLORS["amber"],True,"middle")
    sc.text(78,153,"No se calcula Sulzberger sin parámetros",1.45,"SHEET_TEXT",COLORS["gray"],False,"middle")
    # Guy wire conceptual.
    sc.line(197,65,197,116,"D_ESTRUCTURA",COLORS["ink"],1.8)
    sc.line(197,80,235,129,"D_HERRAJES",COLORS["gray"],1.2)
    sc.circle(235,129,2,"D_HERRAJES",COLORS["gray"],.5,"#f1f5f9")
    sc.line(158,129,258,129,"SHEET_TABLE",COLORS["gray"],.5)
    sc.text(210,138,"Ángulo, cable, anclaje y tiro pendientes",1.55,"SHEET_PENDING",COLORS["amber"],True,"middle")
    # Three declared electrodes as conceptual symbols, no spacing/layout implied.
    sc.text(340,62,"3 electrodos declarados",1.7,"SHEET_TEXT",COLORS["ink"],True,"middle")
    for x in [307,340,373]:
        sc.line(x,76,x,115,"D_PAT",COLORS["green"],1.6)
        sc.line(x-4,115,x+4,115,"D_PAT",COLORS["green"],.8)
        sc.circle(x,76,1.4,"D_PAT",COLORS["green"],.4,"#dcfce7")
    sc.text(340,124,"Símbolos separados en el dibujo: NO definen espaciamiento",1.38,"SHEET_PENDING",COLORS["amber"],True,"middle")
    sc.text(340,133,"Disposición y enlaces: por confirmar",1.5,"SHEET_PENDING",COLORS["amber"],False,"middle")
    # Parameter tables: explicit blanks/unknowns.
    sc.text(20,188,"REGISTRO DE PARÁMETROS PENDIENTES",2.1,"SHEET_TEXT",COLORS["ink"],True)
    rows=[
        ["Cimentación","Suelo, napa, f'c, geometría y cargas","Estudio geotécnico / estructura"],
        ["Retenida","Resultante, cable, inclinación y anclaje","Cálculo mecánico / ficha de herraje"],
        ["PAT-3","ρ medida, separación, enlace, uniones","Wenner + detalle aprob. + medición final"],
        ["Resistencia PAT","10 Ω es objetivo declarado, no resultado","Medir en puesta en servicio"],
    ]
    sc.table(20,194,380,["Sistema","Dato faltante","Sustento requerido"],rows,[43,143,194],row_h=9,font=1.6,header_h=8)
    sc.text(22,244,"El valor 6.8 Ω de la matriz es un cálculo basado en ρ declarada; no equivale a medición de campo ni garantiza el valor final.",1.65,"SHEET_PENDING",COLORS["red"])
    return sc


def build_all():
    structures,vertices,penzd=load_data()
    route,coords,chain=route_and_structures(structures,vertices,penzd)
    profile=read_csv(ROOT/"datos/topografia/perfil_terreno_redcad.csv")
    scenes=[
        build_lp01(structures,vertices,route,coords),
        build_pl01(structures,profile),
        build_u01(),
        build_detail("D-01","ARMADOS PRIMARIOS DE ALINEAMIENTO Y ÁNGULO",["PS-1","PA-1"]),
        build_detail("D-02","ARMADOS DE RETENCIÓN Y SUBESTACIÓN",["PR-1","SAB-1"]),
        build_d03(),
    ]
    OUT.mkdir(parents=True,exist_ok=True)
    outputs=[]
    for scene in scenes:
        slug=scene.code.replace("-","")
        base=OUT/scene.code
        svg=base.with_suffix(".svg"); dxf=base.with_suffix(".dxf"); pdf=base.with_suffix(".pdf"); png=base.with_suffix(".png")
        svg.write_text(scene.svg(),encoding="utf-8")
        model=(route,coords) if scene.code=="LP-01" else None
        export_scene(scene,dxf,model=model,profile=profile if scene.code=="PL-01" else None)
        convert_svg(svg,pdf,png)
        outputs += [svg.name,dxf.name,pdf.name,png.name]
    # Consolidated package: editable DXF, SVG sources and rendered review sheets.
    zip_path=OUT/"paquete_cad_preliminar.zip"
    with zipfile.ZipFile(zip_path,"w",zipfile.ZIP_DEFLATED) as z:
        for pattern in ("*.dxf","*.svg","*.pdf","*.png"):
            for f in sorted(OUT.glob(pattern)): z.write(f,f.name)
    return outputs+[zip_path.name],coords,route


if __name__=="__main__":
    files,coords,route=build_all()
    print("Generados:")
    for f in files: print(" -",f)
    print(f"Estructuras: {len(coords)}; longitud poligonal: {sum(math.dist((a[1],a[2]),(b[1],b[2])) for a,b in zip(route,route[1:])):.2f} m")
