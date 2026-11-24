# Entregables

Versiones finales aprobadas. Esta carpeta es la única donde se versionan PDF y
presentaciones terminadas.

## 1. Convención de nombres

```
AAA-MM-DD_CT01_EquipamientoCentralVapor_vX.Y.Z.pdf
AAA-MM-DD_CT01_Presentacion_vX.Y.Z.pdf
```

- `CT01`: código del trabajo.
- `vX.Y.Z`: versión semántica del documento.
- No se sobrescribe un entregable publicado: se agrega una versión nueva.

## 2. Requisitos para incorporar un entregable

1. El expediente está compilado desde `../09_informe/latex/main.tex` sin errores
   ni referencias rotas.
2. Todos los capítulos involucrados están en `APROBADO`.
3. La auditoría de `../00_gestion/CONTROL_CALIDAD.md` está cerrada.
4. Se actualiza `CHANGELOG.md` y se etiqueta la versión en Git.

## 3. Contenido actual

| Archivo | Descripción | Estado |
|---|---|---|
| — | Sin entregables aprobados todavía | — |

El PDF de compilación vive en `../09_informe/latex/build/main.pdf` y **no** se
copia aquí hasta cumplir los requisitos anteriores.

## 4. Verificación de un entregable

```bash
pdfinfo entregable.pdf | grep -E "Pages|Page size"
pdftotext entregable.pdf - | grep -c "PENDIENTE"   # debe ser 0
```

La segunda comprobación busca avisos de estado que no deben llegar a la versión
final.
