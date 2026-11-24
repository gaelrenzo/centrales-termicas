# Bibliografía del trabajo

## 1. Archivos

| Archivo | Contenido |
|---|---|
| `fuentes.bib` | Base BibTeX propia del trabajo (vacía hasta verificar fuentes) |
| `../../09_informe/latex/bibliografia.bib` | Base que compila el expediente |
| `../00_gestion/REGISTRO_FUENTES.md` | Registro `SRC-NNN` con estado y datos extraídos |

La base del expediente y la de este directorio deben mantenerse equivalentes; al
cerrar cada capítulo se sincronizan y se registra el cambio.

## 2. Reglas de la base

1. Solo entradas `VERIFICADA` o `CONSULTADA`.
2. Datos transcritos del documento, sin deducciones.
3. Clave `primerAutorAnioPalabraClave`.
4. Campo `note` con `SRC-NNN` y fecha de verificación.
5. Sin entradas huérfanas: toda entrada se cita en el texto.
6. Sin citas sin entrada: toda cita existe en la base.

## 3. Verificación antes de compilar

```bash
# Citas sin resolver y entradas no usadas
grep -i "warning" ../09_informe/latex/build/main.blg || echo "Sin advertencias"

# Entradas declaradas
grep -c "^@" fuentes.bib
```

## 4. Estado

| Métrica | Valor |
|---|---|
| Entradas en la base | 0 |
| Fuentes verificadas | 0 |
| Fuentes pendientes | 0 |

> Base vacía intencionalmente: no se ha consultado ningún documento todavía.
