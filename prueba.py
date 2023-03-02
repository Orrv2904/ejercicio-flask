import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, scoped_session
load_dotenv()

if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")


engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

nombre = None
apellido = None

#consulta = text("INSERT INTO usuarios(nombre, apellido) VALUES(:nombre, :apellido)")
# print(consulta)
# db.execute(consulta, {"nombre": nombre, "apellido" :apellido})
# print(db.execute("SELECT * FROM usuarios"))
consulta2 = text("SELECT * FROM usuarios")

omar=db.execute(consulta2).fetchall()

#print(db.execute(consulta2).fetchall())
print(omar[0][2]) #imprime la posicion de lo que almacena la variable



#para imprimir un registro unico
consulta3 = text("SELECT * FROM usuarios WHERE id=18")
print(db.execute(consulta3).fetchone())

consulta4 = text("UPDATE usuarios SET nombre = 'KEVIN', apellido = 'GUADAMUZ' WHERE id=17") 

selectupdate = text("SELECT * FROM usuarios WHERE id=17")
print(db.execute(selectupdate).fetchall())

contador = 0
datos = {'nombre':["Hamlet","Ally","Justin","Santiago"], 'apellido':["Aburto","Mora","Campos","Ocampo"]}
for i in datos.items():
    # print(datos[i][0])
    print(i[1][contador])
    contador = contador + 1
    

db.commit()
db.close()