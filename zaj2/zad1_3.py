from sqlalchemy import create_engine, Column, Integer, String, distinct, text
from sqlalchemy import inspect, Table, MetaData, select, func
from sqlalchemy.util import warn

engine = create_engine('sqlite:///census.sqlite')

inspector = inspect(engine)
table_names = inspector.get_table_names()
print(table_names)

connection = engine.connect()

metadata = MetaData()
census = Table('census', metadata, autoload_with=engine)

new_york = 'New York'

stmt = select(
    func.sum(census.c.pop2008)
).where(census.c.state == new_york).where(census.c.sex == 'M')
results = connection.execute(stmt).fetchall()
print(f'{new_york} Males in 2008: {results[0][0]}')

stmt = select(
    func.sum(census.c.pop2008)
).where(census.c.state == new_york).where(census.c.sex == 'F')
results = connection.execute(stmt).fetchall()
print(f'{new_york} Females in 2008: {results[0][0]}')

