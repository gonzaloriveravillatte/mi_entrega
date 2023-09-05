from django.db import models

# Create your models here.

class Entrevistadores(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
   

class Entrevistados(models.Model):
    nombre = models.CharField(max_length=40)
    hombre = models.BooleanField(default=False)
    mujer = models.BooleanField(default=False)

class Encuestas(models.Model):
    OPCIONES = (
        ('verdadero', 'Verdadero'),
        ('falso', 'Falso'),
        ('nulo', 'Nulo'),
    )

    Pregunta1 = models.CharField(
        max_length=10,
        choices=OPCIONES,
        default='nulo',  # Establece 'nulo' como valor por defecto
    )

    Pregunta2 = models.CharField(
            max_length=10,
            choices=OPCIONES,
            default='nulo',  # Establece 'nulo' como valor por defecto
    )

