from sqlalchemy import create_engine
from sqlalchemy import select, Table, MetaData

engine = create_engine('sqlite:///census.sqlite', echo=True)

meta = MetaData()

students = Table('students', meta, autoload_with=engine)

conn = engine.connect()
query = select(students.c.id, students.c.name, students.c.age, students.c.grade)
output = conn.execute(query)
results = output.fetchall()

for i in range(len(results)): 
    print(f'{results[i][0]} {results[i][1]} {results[i][2]} {results[i][3]}')
