# Figuras del PDF

Archivos gráficos listos para incluir en el documento. Es una carpeta de
**salida**: las fuentes editables viven en `../../../06_diagramas/`.

## 1. Nomenclatura

```
FIG-NN_nombre.pdf
```

Ejemplo: `FIG-07_caldera_acuotubular.pdf`.

## 2. Cómo se llena

1. Crear o editar la fuente en `../../../06_diagramas/` (TikZ, SVG, Mermaid o
   Draw.io).
2. Si es TikZ, se puede incluir directamente desde el capítulo sin pasar por
   esta carpeta.
3. Si es SVG, exportar a PDF vectorial:

   ```bash
   inkscape --export-type=pdf FIG-NN_nombre.svg --export-filename=figuras/FIG-NN_nombre.pdf
   ```

4. Incluir en el capítulo con `\includegraphics` y su `\caption`/`\label`.

## 3. Reglas

1. Solo PDF vectorial o formatos raster de alta resolución; no capturas de
   pantalla.
2. El nombre del archivo coincide con el código `FIG-NN` del inventario.
3. La leyenda indica «Fuente: elaboración propia» o «adaptado de SRC-NNN».
4. No se edita aquí la figura: se corrige en la fuente y se vuelve a exportar.
5. Los archivos generados se versionan solo si son parte de una figura aprobada.

## 4. Qué no va aquí

- Fuentes `.svg`, `.tex`, `.mmd` o `.drawio` (van en `06_diagramas/`).
- Fotografías sin licencia o sin fuente identificada.
- Imágenes temporales o de prueba.

## 5. Estado

Carpeta vacía (solo `.gitkeep`). Las figuras se generarán al desarrollar los
capítulos y los diagramas.
