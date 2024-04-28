from sqlalchemy import Float, create_engine, Column, Integer, String
from sqlalchemy import select, Table, MetaData

engine = create_engine('sqlite:///census.sqlite')

meta = MetaData()

students = Table(
   'students', meta, 
   Column('id', Integer, primary_key = True), 
   Column('name', String), 
   Column('age', Integer), 
   Column('grade', Float), 
)
meta.create_all(engine)

