from sqlalchemy import Table, Column, ForeignKey  # estamos creando las tablas desde aqui
from sqlalchemy.sql.sqltypes import Integer, String
from config.hogwarts_BD import meta, engine

Tablapersonajes = Table("personajes", meta, Column("id", Integer, primary_key=True),
              Column("personaje", String(255)),
Column("casa_hogwarts", String(255)),
Column("descripcion", String(1000)),
Column("progenitor", Integer, ForeignKey("personajes.id")),
Column("hijos", String(255)),
Column("fecha_nacimiento", String(255)),
Column("imagen", String(255)))  # meta es para saber mas propiedades de la tabla

meta.create_all(engine)