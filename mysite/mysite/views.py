from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.template import Template, Context
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

# Funcion para invocar templates. No olvidar de Importar las clases al comienzo de las views con: from django.template import Template,context
def invoca_template (request):
    mihtml = open('G:/Mi unidad/Phyton/Entregas/Entrega3/mi_entrega/mysite/mysite/Templates/template1.html') #OJO usar / en lugar de \ Abre el archivo del template
    plantilla = Template(mihtml.read()) # es una instancia de la clase template donde leemos lo que esta en a variable anterior
    mihtml.close() #es una buena practica cerrar la conexion con el html
   
    miContexto = Context()
    documento1 = plantilla.render(miContexto)
   
    return HttpResponse (documento1)