from sqlalchemy import create_engine
from sqlalchemy import inspect, Table, MetaData, select

engine = create_engine('sqlite:///census.sqlite')

inspector = inspect(engine)
table_names = inspector.get_table_names()
print(table_names)

connection = engine.connect()

metadata = MetaData()
census = Table('census', metadata, autoload_with=engine)

query = select(census.c.state).distinct()
output = connection.execute(query)
results = output.fetchall()
print(results)
