import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from auditar_trazado import audit


class TrazadoAuditTests(unittest.TestCase):
    def test_length_and_stations_are_internally_consistent(self):
        result = audit()
        checks = {c["id"]: c for c in result["checks"]}
        self.assertEqual(result["structures"], 9)
        self.assertAlmostEqual(result["length_m"], 816.60, places=2)
        self.assertEqual(checks["sum_vanos_vs_longitud"]["status"], "PASS")
        self.assertEqual(checks["progresivas_estructuras"]["status"], "PASS")

    def test_coordinate_chain_agrees_with_declared_vertex_stations(self):
        checks = {c["id"]: c for c in audit()["checks"]}
        self.assertEqual(checks["progresivas_vs_coordenadas"]["status"], "PASS")

    def test_unresolved_sed_continuation_is_never_marked_approved(self):
        checks = {c["id"]: c for c in audit()["checks"]}
        self.assertEqual(checks["sed_y_fin_de_linea"]["status"], "REVIEW")
        self.assertEqual(checks["procedencia_topografia"]["status"], "REVIEW")

    def test_dense_profile_points_are_flagged_when_linearly_interpolated(self):
        checks = {c["id"]: c for c in audit()["checks"]}
        self.assertEqual(checks["densificacion_del_perfil"]["status"], "REVIEW")
        self.assertIn("71 cotas intermedias", checks["densificacion_del_perfil"]["detail"])


if __name__ == "__main__":
    unittest.main()
