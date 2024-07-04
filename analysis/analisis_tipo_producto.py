from generators.generar_tipo_producto import generar_tipo_producto
import pandas as pd

def analizarDatos():
    datos=generar_tipo_producto()
    tabla=pd.DataFrame(datos,columns=["Plan","Categoria"])
    tabla.to_csv("./data/tipo_producto_apple.csv",index=False)
analizarDatos()
