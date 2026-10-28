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
└── partir_v2.py            traza del reparto inicial (paso 1)
historia/                   origen y restos de modelos anteriores (no se montan)
auditorias/                 auditorías de la fábrica
```

Para obtener la fábrica que leen las ventanas:

```
python herramientas/montar.py --genero dark_romance --destino <carpeta>
```

## Estado

- **Paso 1 (28-10-2026):** el MODELO_DarkRomance v2.0 de `Devpac/Dark` (`fcd6839`), repartido en capas sin cambios. El montaje es idéntico byte a byte al original (`historia/ORIGEN.md`). Todavía arrastra lo que encontró la auditoría.
- **Siguiente:** la cirugía de la auditoría (`auditorias/2026-10-28_separacion/`), el manual de producción y la plantilla de saga nueva.
- *Madera y Pólvora* termina su libro 1 con la v2.0 de Dark y migra a esta fábrica al abrir el libro 2.
