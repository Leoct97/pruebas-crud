from typing import Union
from fastapi import FastAPI,HTTPException
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
    return (datos)


@app.post("/insertar", response_model=articulo)
def insert(articulo: articulo): 
    conn = pyodbc.connect(connectionString)
    cursor = conn.cursor()
    query = "insert into articulos (id, nombre, precio) values (?,?,?)"
    cursor.execute(query, (articulo.id, articulo.name, articulo.precio))
    conn.commit()
    cursor.close()
    return articulo



@app.get("/inventario")
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
    dato2 = json.dumps(dato2)
    cursor.close()
    return dato2
