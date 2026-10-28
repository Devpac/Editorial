# Editorial

La fábrica de novelas: el método (orquestador, ventanas de trabajo, lecturas), las plantillas de oficio y los paquetes de género. Cada saga nace de aquí y lleva su propia copia montada. Aquí no se escribe ninguna obra.

## Estructura

```
fabrica/
├── metodo/                 orquestador, encargos, lecturas, plantillas de fase
├── oficio/                 bases de oficio, válidas para cualquier novela
├── romance/                lo común a todo romance (la pareja primero)
└── generos/
    └── dark_romance/       plantillas de género y adendas sobre el oficio
herramientas/
├── montar.py               compone la fábrica plana para un género
├── sincronizar_preset.py   regenera las ranuras de PLANTILLA_PRESET desde las plantillas
└── partir_v2.py            traza del reparto inicial (paso 1)
cirugia/                    la separación de la fábrica (paso 2): guía, registros y la migración de MyP
CHANGELOG.md                historia de la fábrica (las reglas no llevan historia)
historia/                   origen y restos de modelos anteriores (no se montan)
auditorias/                 auditorías de la fábrica
```

Para obtener la fábrica que leen las ventanas:

```
python herramientas/montar.py --genero dark_romance --destino <carpeta>
```

## Estado

- **Paso 1 (28-10-2026):** el MODELO_DarkRomance v2.0 de `Devpac/Dark` (`fcd6839`), repartido en capas sin cambios. El montaje es idéntico byte a byte al original (`historia/ORIGEN.md`). Todavía arrastra lo que encontró la auditoría.
- **Paso 2 (28-10-2026): Fábrica v3.0.** La cirugía de la auditoría: la fábrica ya no lleva valores de ninguna obra (`CHANGELOG.md`, `cirugia/`). Lo que el preset de MyP tiene que recibir al migrar: `cirugia/MIGRACION_MyP.md`.
- **Siguiente:** el manual de producción y la plantilla de saga nueva.
- *Madera y Pólvora* termina su libro 1 con la v2.0 de Dark y migra a esta fábrica al abrir el libro 2.
