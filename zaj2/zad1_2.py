from sqlalchemy import create_engine
from sqlalchemy import inspect, Table, MetaData, select, func

engine = create_engine('sqlite:///census.sqlite')

inspector = inspect(engine)
table_names = inspector.get_table_names()
print(table_names)

connection = engine.connect()

metadata = MetaData()
census = Table('census', metadata, autoload_with=engine)

new_york = 'New York'
alaska = 'Alaska'

stmt = select(
    func.sum(census.c.pop2008)
).where(census.c.state == new_york)
results = connection.execute(stmt).fetchall()
print(f'{new_york} 2008: {results[0][0]}')

stmt = select(
    func.sum(census.c.pop2000)
).where(census.c.state == new_york)
results = connection.execute(stmt).fetchall()
print(f'{new_york} 2000: {results[0][0]}')

stmt = select(
    func.sum(census.c.pop2008)
).where(census.c.state == alaska)
results = connection.execute(stmt).fetchall()
print(f'{alaska} 2008: {results[0][0]}')

stmt = select(
    func.sum(census.c.pop2000)
).where(census.c.state == alaska)
results = connection.execute(stmt).fetchall()
print(f'{alaska} 2000: {results[0][0]}')
