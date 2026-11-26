"""Regresiones de datos y archivos para las láminas CAD preliminares."""
from pathlib import Path
import sys
import math
import zipfile

import ezdxf
import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import cad_mejorado as cad


@pytest.fixture(scope="module")
def generated():
    files, coords, route = cad.build_all()
    return files, coords, route


def test_nine_supports_and_chainage_length(generated):
    _, coords, route = generated
    assert [p["id_estructura"] for p in coords] == [f"E-{i:02d}" for i in range(1, 10)]
    assert coords[-1]["station"] == pytest.approx(816.60)
    assert coords[3]["station"] == pytest.approx(305.21)
    assert coords[-1]["station"] - coords[3]["station"] == pytest.approx(511.39)
    assert sum(math.dist((a[1], a[2]), (b[1], b[2])) for a, b in zip(route, route[1:])) == pytest.approx(816.60, abs=.02)


def test_outputs_pdf_png_dxf_and_zip(generated):
    files, _, _ = generated
    out = ROOT / "entregables" / "mejorados"
    assert len([f for f in files if f.endswith(".svg")]) == 6
    for sheet in ("LP-01", "PL-01", "U-01", "D-01", "D-02", "D-03"):
        for ext in (".dxf", ".pdf", ".png", ".svg"):
            p = out / f"{sheet}{ext}"
            assert p.is_file() and p.stat().st_size > 500
        assert (out / f"{sheet}.pdf").read_bytes().startswith(b"%PDF")
        assert (out / f"{sheet}.png").read_bytes().startswith(b"\x89PNG\r\n\x1a\n")
    with zipfile.ZipFile(out / "paquete_cad_preliminar.zip") as z:
        assert all(f"{s}{ext}" in z.namelist() for s in ("LP-01", "PL-01", "U-01", "D-01", "D-02", "D-03") for ext in (".dxf", ".svg", ".pdf", ".png"))


def test_dxf_structure_layers_blocks_units_and_audit(generated):
    out = ROOT / "entregables" / "mejorados"
    required = set(cad.LAYERS) | {"CAD_BIBLIOTECA"}
    expected_blocks = {"ARMADO_PS1", "ARMADO_PA1", "ARMADO_PR1", "ARMADO_SAB1", "RETENIDA_REF", "CIMENTACION_REF", "PAT3_TIPO"}
    for sheet in ("LP-01", "PL-01", "U-01", "D-01", "D-02", "D-03"):
        doc = ezdxf.readfile(out / f"{sheet}.dxf")
        assert required <= {layer.dxf.name for layer in doc.layers}
        assert expected_blocks <= {block.name for block in doc.blocks}
        assert doc.header["$INSUNITS"] == (6 if sheet in ("LP-01", "PL-01") else 4)
        assert "A3_PRELIMINAR" in doc.layouts
        audit = doc.audit()
        assert not audit.errors
        assert len(doc.layouts.get("A3_PRELIMINAR")) > 20
    doc = ezdxf.readfile(out / "LP-01.dxf")
    assert len([e for e in doc.modelspace().query("INSERT") if e.dxf.layer in {"LP_ESTRUCTURAS", "LP_SED"}]) == 9
    pl = ezdxf.readfile(out / "PL-01.dxf")
    assert len(pl.modelspace().query("LWPOLYLINE[layer=='PL_PERFIL_PREL']")) == 1


def test_sheet_content_and_preliminary_status(generated):
    out = ROOT / "entregables" / "mejorados"
    for sheet in ("LP-01", "PL-01", "U-01", "D-01", "D-02", "D-03"):
        svg = (out / f"{sheet}.svg").read_text(encoding="utf-8")
        assert "PRELIMINAR" in svg and "NO APTO PARA CONSTRUCCIÓN" in svg
    assert "511.39 m" in (out / "LP-01.svg").read_text(encoding="utf-8")
    assert "511.39 m" in (out / "PL-01.svg").read_text(encoding="utf-8")
    assert "511.39 m" in (out / "U-01.svg").read_text(encoding="utf-8")
    assert "3 electrodos declarados" in (out / "D-03.svg").read_text(encoding="utf-8")


def test_layout_text_tables_titles_and_sheet_bounds(generated):
    out = ROOT / "entregables" / "mejorados"
    for sheet in ("LP-01", "PL-01", "U-01", "D-01", "D-02", "D-03"):
        doc = ezdxf.readfile(out / f"{sheet}.dxf")
        layout = doc.layouts.get("A3_PRELIMINAR")
        texts = list(layout.query("TEXT"))
        assert len(texts) >= 35
        assert any(sheet in text.dxf.text for text in texts)
        assert any("PRELIMINAR" in text.dxf.text for text in texts)
        # Main sheet frame/table entities are 1:1 millimetres on A3 landscape.
        for entity in layout:
            if entity.dxftype() == "TEXT":
                x, y = entity.dxf.insert.x, entity.dxf.insert.y
                assert -1 <= x <= 421 and -1 <= y <= 298
            elif entity.dxftype() == "LINE":
                for point in (entity.dxf.start, entity.dxf.end):
                    assert -1 <= point.x <= 421 and -1 <= point.y <= 298
        assert doc.header["$INSUNITS"] in (4, 6)
