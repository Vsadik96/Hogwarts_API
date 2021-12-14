from sqlalchemy import Table, Column  # estamos creando las tablas desde aqui
from sqlalchemy.sql.sqltypes import Integer, String
from config.hogwarts_BD import meta, engine

Tablapeliculas = Table("peliculas", meta, Column("id", Integer, primary_key=True),
              Column("titulo", String(255)),
Column("fecha_lanzamiento", String(255)),
Column("director", String(255)),
Column("descripcion", String(1000)),
Column("imagen", String(255)))  # meta es para saber mas propiedades de la tabla

meta.create_all(engine)