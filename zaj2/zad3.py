from sqlalchemy import create_engine, delete, table
from sqlalchemy import select, Table, MetaData

def insert_student(connection, table, name, age, grade):
    result = connection.execute(table.insert(),[
        {'name':name, 'age':age, 'grade':grade},
    ])
    conn.commit()

def query_student_by_id(connection, table, id):
    query = select(table.c.id, table.c.name, table.c.age, table.c.grade).where(table.c.id == id)
    output = connection.execute(query)
    results = output.fetchall()
    return results

def update_student(connection, table, id, name, age, grade):
    result = connection.execute(table.update().where(table.c.id==id),[
        {'name':name, 'age':age, 'grade':grade},
    ])
    conn.commit()

def delete_student_by_id(connection, table, id):
    stm = table.delete().where(table.c.id > 2)
    connection.execute(stm)
    conn.commit()

engine = create_engine('sqlite:///census.sqlite')
meta = MetaData()
conn = engine.connect()
students = Table('students', meta, autoload_with=engine)

print(query_student_by_id(conn, students,1))
update_student(conn, students,1, 'Adam', 12, 5.4)
delete_student_by_id(conn, students,1)
insert_student(conn, students, 'Jeff', 15, 3.4)

query = select(students.c.id, students.c.name, students.c.age, students.c.grade)
output = conn.execute(query)
results = output.fetchall()

for i in range(len(results)): 
    print(f'{results[i][0]} {results[i][1]} {results[i][2]} {results[i][3]}')
