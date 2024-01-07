from fastapi.responses import JSONResponse
from fastapi import FastAPI
from conexion import datos
from conexion import connectionString
from pydantic import BaseModel
import json
import pyodbc

app = FastAPI()
    
class articulo(BaseModel):
    id: int
    name: str
    precio: int
    
    
@app.get("/obtener")
def read():
    conn = pyodbc.connect(connectionString)
    cursor = conn.cursor()
    sql_query = "select * from articulos"
    cursor = conn.cursor()
    cursor.execute(sql_query)
    select = cursor.fetchall()
    dato2 = [dict(zip(["ïd", "nombre", "precio"],row)) for row in select]
    return JSONResponse(content=dato2)

@app.post("/insertar/articulo", response_model=articulo)
def insert(articulo: articulo): 
    conn = pyodbc.connect(connectionString)
    cursor = conn.cursor()
    query = "insert into articulos (id, nombre, precio) values (?,?,?)"
    cursor.execute(query, (articulo.id, articulo.name, articulo.precio))
    conn.commit()
    cursor.close()
    return articulo

@app.get("/lista/inventario")
def obtener(id: int):
    conn = pyodbc.connect(connectionString)
    cursor = conn.cursor()
    query = "exec inventarios ?"
    cursor.execute(query, (id))
    results = cursor.fetchall()
    dato2 = [dict(zip(["nombre", "precio", "stock", "fecha_alta"],
                      [row[0], row[1], row[2], row[3].isoformat()])) 
             for row in results
             ]
    cursor.close()
    return JSONResponse(content=dato2)


@app.delete("/delete")
def delete(id: int):
    conn = pyodbc.connect(connectionString)
    cursor = conn.cursor()
    query = "delete articulos where id = ?"
    cursor.execute(query, (id))
    cursor.commit()
    cursor.close()
    return id


@app.put("/actualizar")
def update(id: int, precio: int):
    conn = pyodbc.connect(connectionString)
    cursor = conn.cursor()
    query = "update articulos set precio = ? where id = ?"
    cursor.execute(query, (precio, id))
    cursor.commit()
    cursor.close()
    return id


@app.post("/insertar/stock")
def newinv(id: int, stock: int):
    conn = pyodbc.connect(connectionString)
    cursor = conn.cursor()
    query = "insert into inventario(id_articulo,fecha,stock) values (?,getdate(),?)"
    cursor.execute(query, (id, stock))
    cursor.commit()
    cursor.close()
    return JSONResponse(content=id)

@app.put("/actualizar/articulo")
def updateinv(id: int, precio: int):
    conn = pyodbc.connect(connectionString)
    cursor = conn.cursor()
    query = "update articulos set precio = ? where id = ?"
    cursor.execute(query, (precio, id))
    cursor.commit()
    cursor.close()
    return id