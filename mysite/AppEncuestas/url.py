from django.urls import path #
from .views import *

from mysite.views import saludo, prueba, dia_de_hoy,saluda_con_nombre,invoca_template

urlpatterns = [

    path("saludar/", saludo),
    path("prueba/", prueba),
    path("fecha/", dia_de_hoy),
    path("saluda-nombre/<nombre>", saluda_con_nombre), # el /<name> es el parametro que le voy a pasar (viene de la funcion), que lo pongo directo en la url. Si quiero invocar esta funcion debere escribir la url/name
    path("probando-template/", invoca_template),

]