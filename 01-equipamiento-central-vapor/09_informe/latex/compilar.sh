#!/usr/bin/env bash
# ---------------------------------------------------------------------
# Compilación del expediente (pdfLaTeX + BibTeX)
# Uso:  ./compilar.sh            compila en build/
#       ./compilar.sh --limpia   elimina build/ antes de compilar
# ---------------------------------------------------------------------
set -euo pipefail

cd "$(dirname "$0")"

if [[ "${1:-}" == "--limpia" ]]; then
  rm -rf build
fi

mkdir -p build

echo "[1/4] pdfLaTeX (primera pasada)"
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build main.tex >/dev/null

echo "[2/4] BibTeX"
if [[ -f build/main.aux ]] && grep -q '\\bibdata' build/main.aux; then
  bibtex build/main >/dev/null 2>&1 || echo "  aviso: BibTeX reportó advertencias; revisar build/main.blg"
else
  echo "  omitido: bibliografía desactivada (sin fuentes verificadas todavía)"
fi

echo "[3/4] pdfLaTeX (segunda pasada)"
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build main.tex >/dev/null

echo "[4/4] pdfLaTeX (tercera pasada)"
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build main.tex >/dev/null

echo
echo "PDF generado: $(pwd)/build/main.pdf"
echo
echo "Comprobación rápida de integridad:"
if grep -Eiq "undefined (references|citations)|Reference .* undefined|Citation .* undefined" build/main.log; then
  echo "  ERROR: hay referencias o citas sin resolver."
  grep -Ei "undefined" build/main.log | head -20
  exit 1
else
  echo "  OK: sin referencias ni citas sin resolver."
fi
