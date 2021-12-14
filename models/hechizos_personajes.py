from sqlalchemy import Table, ForeignKey, Column  # estamos creando las tablas desde aqui
from sqlalchemy.sql.sqltypes import Integer
from config.hogwarts_BD import meta, engine

Tablahechizos_personajes = Table("hechizos_personajes", meta, Column("id_hechizo", Integer, ForeignKey("hechizos.id")),
                    Column("id_personaje", Integer, ForeignKey("personajes.id")))
                             # meta es para saber mas propiedades de la tabla

meta.create_all(engine)