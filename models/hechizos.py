from sqlalchemy import Table, Column  # estamos creando las tablas desde aqui
from sqlalchemy.sql.sqltypes import Integer, String
from config.hogwarts_BD import meta, engine

Tablahechizos = Table("hechizos", meta, Column("id", Integer, primary_key=True),
              Column("hechizo", String(255)),
Column("uso", String(255)))  # meta es para saber mas propiedades de la tabla

meta.create_all(engine)