from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:""@localhost:3306/hogwartsapp")

meta = MetaData() #se importa para tener esta propieda en models/user.py

conexion = engine.connect()

