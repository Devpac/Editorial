# Editorial

La fábrica de novelas: el método (orquestador, ventanas de trabajo, lecturas), las plantillas de oficio y los paquetes de género. Cada saga nace de aquí y lleva su propia copia montada. Aquí no se escribe ninguna obra.

## Estructura

```
ARRANQUE.md                 cómo se empieza una saga, cómo se pone al día y cómo se publica
VERSION · CHANGELOG.md      la versión de la fábrica y su historia (las reglas no llevan historia)
fabrica/
├── metodo/                 orquestador, encargos, lecturas, plantillas de fase
├── oficio/                 bases de oficio, válidas para cualquier novela
├── romance/                lo común a todo romance (la pareja primero)
└── generos/
    └── dark_romance/       plantillas de género y adendas sobre el oficio
herramientas/
├── nueva_saga.py           prepara el repo de una saga nueva (fabrica/ montada, LEEME, publicacion/)
├── montar.py               compone la fábrica plana para un género (y pone al día la de una saga)
├── sincronizar_preset.py   regenera las ranuras de PLANTILLA_PRESET desde las plantillas
└── partir_v2.py            traza del reparto inicial (paso 1)
plantilla_saga/             lo que lleva una saga nueva además de la fábrica
maquetador/                 de los capítulos a EPUB, interior PDF, cubiertas y ficha de KDP
cirugia/                    la separación de la fábrica (v3.0): guía, registros y la migración de MyP
auditorias/                 auditorías de la fábrica
historia/                   origen y restos de modelos anteriores (no se montan)
```

Para empezar una saga: `ARRANQUE.md`.

## Estado

- **Paso 1 (28-10-2026):** el MODELO_DarkRomance v2.0 de `Devpac/Dark` (`fcd6839`), repartido en capas sin cambios. El montaje es idéntico byte a byte al original (`historia/ORIGEN.md`). Todavía arrastra lo que encontró la auditoría.
- **Paso 2 (28-10-2026): Fábrica v3.0.** La cirugía de la auditoría: la fábrica ya no lleva valores de ninguna obra (`CHANGELOG.md`, `cirugia/`). Auditada después de operar (`auditorias/2026-10-28_v3/`) y corregida: 72 hallazgos, 67 resueltos, 5 dejados así a propósito, ninguno pendiente. Lo que el preset de MyP tiene que recibir al migrar: `cirugia/MIGRACION_MyP.md`.
- **Paso 3 (29-10-2026): arranque y maquetador.** `ARRANQUE.md`, `plantilla_saga/` y `herramientas/nueva_saga.py`: una saga nueva se prepara con un comando, con la fábrica montada en `fabrica/` (y su sello de versión) y la obra en la raíz. El maquetador vive aquí, sin la configuración de ninguna obra; la de cada libro va en `publicacion/` de su saga.
- **Siguiente:** el manual de producción, y la prueba de fuego con la segunda saga.
- *Madera y Pólvora* termina su libro 1 con la v2.0 de Dark y migra a esta fábrica al abrir el libro 2.
