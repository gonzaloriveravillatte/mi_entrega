from django.http import HttpResponse
from datetime import datetime

def saludo (request):
    return HttpResponse ("Bienvenidos")

def prueba (request):
    return HttpResponse ("""
    <html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Pruba de que el html anda bien</h1>
</body>
</html>"""                 
         )
    
def dia_de_hoy (request):
    dia = datetime.now()
    respuesta = f"el dia de hoy es {dia}"
    return HttpResponse (respuesta)

def saluda_con_nombre (request,nombre):
    saludo = f"Hola {nombre}"
    return HttpResponse (saludo)