from sqlalchemy import Table, Column  # estamos creando las tablas desde aqui
from sqlalchemy.sql.sqltypes import Integer, String, Boolean
from config.hogwarts_BD import meta, engine


TablaUser = Table("users", meta, Column("id", Integer, primary_key=True),
                Column("username", String(50), unique=True),
                Column("password", String(255)),
                Column("is_active", Boolean, default=True))


meta.create_all(engine)