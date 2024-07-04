import random

def generar_tipo_producto():
    planes = ['Música','TV','Aplicaciones','PC','Celulares','Tablets','Accesorios']
    datos=[]
    for producto in planes:   
        plan={}
        categoria=random.choice(["Plus", "Basic", "Mega"])
        plan=[producto,categoria]
        datos.append(plan)
    return datos
print(generar_tipo_producto())
