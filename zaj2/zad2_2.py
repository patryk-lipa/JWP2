from sqlalchemy import create_engine
from sqlalchemy import Table, MetaData

engine = create_engine('sqlite:///census.sqlite', echo=True)

meta = MetaData()

students = Table('students', meta, autoload_with=engine)

conn = engine.connect()
result = conn.execute(students.insert(),[
    {'name':'John', 'age':12, 'grade':5.0},
    {'name':'Bob', 'age':13, 'grade':4.0},
    {'name':'Alice', 'age':14, 'grade':3.0}
])

conn.commit()

