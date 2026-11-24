# Ficha de fuente

> Copiar a `00_gestion/REGISTRO_FUENTES.md` como una entrada nueva.
> Identificador único e irrepetible: `SRC-NNN`.
> No completar campos por deducción: si no está en el documento, se deja vacío.

## SRC-NNN

| Campo | Valor |
|---|---|
| Identificador | SRC-NNN |
| Tipo | Norma / Libro / Artículo / Informe técnico / Catálogo / Manual / Tesis / Web oficial |
| Autor(es) u organismo | |
| Título exacto | |
| Edición / versión / revisión | |
| Editorial o entidad | |
| Año | |
| Volumen / número | |
| Páginas consultadas | |
| DOI / ISBN / número de norma | |
| URL oficial | |
| Fecha de consulta | AAAA-MM-DD |
| Idioma | |
| Estado | PENDIENTE / CONSULTADA / VERIFICADA / DESCARTADA |
| Ubicación del documento | (enlace oficial o ubicación física; nunca archivo protegido en el repo) |
| Capítulos donde se usa | |
| Datos extraídos | (qué valores concretos se tomaron: tablas, páginas, figuras) |
| Observaciones | (vigencia, limitaciones, posibles conflictos con otras fuentes) |

## Verificación

- [ ] Autor/organismo confirmado en el documento.
- [ ] Título transcrito literalmente.
- [ ] Año y edición confirmados.
- [ ] Identificador (DOI/ISBN/norma) confirmado o declarado ausente.
- [ ] Datos extraídos localizados en la página/sección indicada.
- [ ] Sin conflicto no resuelto con otra fuente del expediente.

## Entrada BibTeX asociada

```bibtex
@misc{claveSRCnnn,
  author = {},
  title  = {},
  year   = {},
  note   = {SRC-NNN}
}
```
