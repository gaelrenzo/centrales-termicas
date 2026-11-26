#!/usr/bin/env python3
"""Chequeos geométricos reproducibles del trazado Capachica–Chifrón.

Este validador comprueba consistencia interna de los CSV. No certifica que las
coordenadas o cotas provengan de un levantamiento de campo.
"""
from __future__ import annotations

import csv
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "datos"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def audit() -> dict[str, object]:
    structures = read_csv(DATA / "estructuras/planilla_estructuras_lp_capachica.csv")
    vertices = read_csv(DATA / "topografia/planilla_vertices_lp.csv")
    penzd = read_csv(DATA / "topografia/topografia_coordenadas_PENZD.csv")
    checks: list[dict[str, object]] = []

    stations = [float(r["progresiva_m"]) for r in structures]
    ids = [r["id_estructura"] for r in structures]
    spans = [b - a for a, b in zip(stations, stations[1:])]
    span_sum = sum(spans)
    expected_length = stations[-1] - stations[0]
    checks.append({
        "id": "sum_vanos_vs_longitud",
        "status": "PASS" if abs(span_sum - expected_length) <= 0.02 else "FAIL",
        "detail": f"Suma calculada {span_sum:.2f} m; longitud por progresivas {expected_length:.2f} m.",
    })
    checks.append({
        "id": "progresivas_estructuras",
        "status": "PASS" if len(ids) == 9 and len(set(ids)) == len(ids) and all(b > a for a, b in zip(stations, stations[1:])) else "FAIL",
        "detail": f"{len(ids)} IDs únicos; secuencia estrictamente creciente: {all(b > a for a, b in zip(stations, stations[1:]))}.",
    })

    # El CSV PENZD carece de columna de progresiva; se reconstruye la abscisa
    # acumulando distancias UTM. Esto solo comprueba coherencia geométrica.
    chain = 0.0
    chain_at_label: dict[str, float] = {}
    previous = None
    for row in penzd:
        point = (float(row["Este"]), float(row["Norte"]))
        if previous is not None:
            chain += math.dist(point, previous)
        previous = point
        chain_at_label[row["Descripcion"]] = chain
    vertex_deltas = []
    for row in vertices:
        name = row["nombre"]
        if name in chain_at_label:
            vertex_deltas.append(abs(float(row["progresiva_m"]) - chain_at_label[name]))
    max_delta = max(vertex_deltas, default=float("inf"))
    checks.append({
        "id": "progresivas_vs_coordenadas",
        "status": "PASS" if vertex_deltas and max_delta <= 0.05 else "FAIL",
        "detail": f"Máxima diferencia entre progresiva declarada y distancia UTM acumulada en vértices coincidentes: {max_delta:.3f} m.",
    })

    vertex_count = len(vertices)
    checks.append({
        "id": "vertices_vs_apoyos",
        "status": "INFO",
        "detail": f"Hay {vertex_count} puntos/vértices topográficos y {len(structures)} estructuras. No son conjuntos equivalentes: los vértices intermedios no tienen tipo de apoyo asignado.",
    })

    anchor_indices = [i for i, row in enumerate(penzd) if row["Descripcion"] != "TN"]
    interpolation_residuals = []
    for ia, ib in zip(anchor_indices, anchor_indices[1:]):
        z0, z1 = float(penzd[ia]["Cota"]), float(penzd[ib]["Cota"])
        count = ib - ia
        for i in range(ia + 1, ib):
            fraction = (i - ia) / count
            expected_z = z0 + (z1 - z0) * fraction
            interpolation_residuals.append(abs(float(penzd[i]["Cota"]) - expected_z))
    max_profile_residual = max(interpolation_residuals, default=float("inf"))
    checks.append({
        "id": "densificacion_del_perfil",
        "status": "REVIEW",
        "detail": f"{len(interpolation_residuals)} cotas intermedias difieren como máximo {max_profile_residual:.3f} m de una interpolación lineal entre puntos rotulados como vértices. No son evidencia de observaciones independientes del terreno.",
    })

    sed = next((r for r in structures if r["id_estructura"] == "E-04"), None)
    if sed:
        remaining = stations[-1] - float(sed["progresiva_m"])
        checks.append({
            "id": "sed_y_fin_de_linea",
            "status": "REVIEW",
            "detail": f"E-04 está declarada SAB-1/SED; la traza sigue {remaining:.2f} m hasta E-09. Los datos no identifican carga, función eléctrica ni límite de propiedad aguas abajo; la continuidad queda sin justificar.",
        })

    # proyecto.yaml identifica DEM/SRTM, pero no se adjunta el raster ni su
    # resolución/procesamiento. No es evidencia de levantamiento topográfico.
    checks.append({
        "id": "procedencia_topografia",
        "status": "REVIEW",
        "detail": f"proyecto.yaml declara DEM/SRTM; hay {len(penzd)} puntos interpolados/exportados, pero no se adjuntan raster, resolución, metadatos de procesamiento, datum vertical ni validación contra campo. Es perfil preliminar, no levantamiento de replanteo.",
    })

    return {"structures": len(structures), "vertices": vertex_count, "length_m": expected_length, "checks": checks}


def render_markdown(result: dict[str, object]) -> str:
    rows = [
        "# Auditoría reproducible de trazado y datos de entrada",
        "",
        "> Resultado de consistencia interna. No es aprobación de diseño ni validación de levantamiento topográfico.",
        "",
        f"- Estructuras listadas: {result['structures']}",
        f"- Puntos/vértices: {result['vertices']}",
        f"- Longitud por progresivas: {result['length_m']:.2f} m",
        "",
        "| Control | Estado | Evidencia |",
        "|---|---|---|",
    ]
    for c in result["checks"]:  # type: ignore[index]
        rows.append(f"| {c['id']} | **{c['status']}** | {c['detail']} |")
    rows += [
        "",
        "## Conclusión sobre E-04 y E-09",
        "",
        "La planilla sitúa la SAB-1 de 100 kVA en E-04 (prog. 0+305.21) y define E-09 como terminal de la misma traza (0+816.60). No se encuentra un diagrama de derivaciones, carga aguas abajo de E-04, concesión de continuidad ni explicación de la función del tramo E-04–E-09. La inconsistencia no se resuelve con los archivos disponibles. Hasta recibir esa definición, planta, perfil y unifilar deben tratar el tramo E-04–E-09 como alcance y topología pendientes de confirmar.",
        "",
        "## Datos requeridos antes de emitir planos verificables",
        "",
        "1. Para perfil ejecutivo: levantamiento de campo con archivo nativo, puntos, método, fecha, equipo, precisión y datum vertical; coordenadas/cotas de cada estructura y obstáculo. Si se conserva DEM/SRTM, adjuntar raster, resolución y método y rotular el perfil como preliminar.",
        "2. Confirmación del propietario/concesionaria sobre el punto de derivación, el recorrido E-01–E-09, la función del tramo después de E-04 y el límite del proyecto.",
        "3. Ficha certificada del AAAC instalado/propuesto y memoria de cambio de estado que respalde tensión y flecha para cada vano e hipótesis climática.",
        "4. Datos de corto circuito y curvas/fichas de fusibles y pararrayos para coordinación; resistividad medida en el emplazamiento y medición de PAT al terminar la obra.",
        "5. Geotecnia, cargas de diseño verificadas, fichas de postes/anclajes y parámetros necesarios para validar cimentaciones y retenidas.",
        "",
        "Las cotas de estructura y progresivas del CSV se conservan como datos declarados. Aunque `proyecto.yaml` declara DEM/SRTM, el ráster no está adjunto y las 71 cotas intermedias siguen casi exactamente rectas entre vértices; no se puede reconstruir ni acreditar un perfil de terreno observado con el paquete revisado. Las comprobaciones geométricas solo verifican relaciones entre archivos y no convierten esos datos en observaciones de campo.",
        "",
    ]
    return "\n".join(rows)


if __name__ == "__main__":
    result = audit()
    out = ROOT / "documentacion/auditoria_datos_trazado.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(render_markdown(result), encoding="utf-8")
    print(render_markdown(result))
