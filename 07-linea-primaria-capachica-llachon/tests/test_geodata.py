import csv, json, math
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from preparar_traza import utm19s

def test_wgs84_utm19s_control_points():
    e,n=utm19s(-69.830694,-15.642131)
    assert abs(e-410963.591)<0.01 and abs(n-8270475.406)<0.01
    e,n=utm19s(-69.783859,-15.722804)
    assert abs(e-416016.796)<0.01 and abs(n-8261570.425)<0.01

def test_reference_samples_route_progression_and_dem():
    rows=list(csv.DictReader((ROOT/'datos/topografia/estaciones_referencia_100m.csv').open()))
    meta=json.loads((ROOT/'datos/topografia/metadatos_traza.json').read_text())
    assert len(rows)==144
    stations=[float(r['progresiva_geodesica_m']) for r in rows]
    assert stations[0]==0 and stations[-1]==meta['sampled_geometry_chainage_m']
    assert all(a<b for a,b in zip(stations,stations[1:]))
    assert abs(stations[-1]-14201.31)<.02
    assert all('NO ES APOYO' in r['clasificacion'] for r in rows)
    assert all(r['cota_dem_srtm90m_m'] for r in rows)
    geo=json.loads((ROOT/'datos/topografia/traza_referencia.geojson').read_text())
    assert len(geo['features'])==145
    assert geo['features'][0]['geometry']['type']=='LineString'

def test_reference_cad_outputs_and_dxf_audit():
    import ezdxf
    out=ROOT/'entregables/referencia'
    for sheet in ('LP-01','PL-01','U-01','D-01','D-02','D-03'):
        for ext in ('.dxf','.pdf','.png','.svg'): assert (out/f'{sheet}{ext}').is_file()
        d=ezdxf.readfile(out/f'{sheet}.dxf'); assert not d.audit().errors
        assert 'A3_PRELIMINAR' in d.layouts
    lp=ezdxf.readfile(out/'LP-01.dxf')
    assert lp.header['$INSUNITS']==6
    assert len(lp.modelspace().query("LWPOLYLINE[layer=='REF_RUTA']"))==1
    route=lp.modelspace().query("LWPOLYLINE[layer=='REF_RUTA']")[0]
    assert len(route)==124
    pl=ezdxf.readfile(out/'PL-01.dxf')
    assert len(pl.modelspace().query("LWPOLYLINE[layer=='REF_PERFIL']"))==1
    import zipfile
    with zipfile.ZipFile(out/'paquete_capachica_llachon_preliminar.zip') as z:
        assert all(f'{s}{ext}' in z.namelist() for s in ('LP-01','PL-01','U-01','D-01','D-02','D-03') for ext in ('.dxf','.pdf','.png','.svg'))
