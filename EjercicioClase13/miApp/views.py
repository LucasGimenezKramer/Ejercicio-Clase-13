from django.shortcuts import render
from django.template import Template, Context
from django.http import HttpResponse

def mostrar_index(request):
    estudiantes = [
        {"nombre": "Juan", "apellido": "Perez", "calificaciones" : [
            {"materia": "Matematica", "nota": 8},
            {"materia": "Historia", "nota": 6},
            {"materia": "Programacion", "nota": 10}
        ]},
        {"nombre": "Lucas", "apellido": "Gimenez", "calificaciones" : [
            {"materia": "Matematica", "nota": 5},
            {"materia": "Historia", "nota": 7},
            {"materia": "Programacion", "nota": 5}
        ]},
        {"nombre": "Maria", "apellido": "Gonzalez", "calificaciones" : []}
    ]

    ruta = "C:/Users/Familia/Desktop/proyectosdjango/EjercicioClase13/miApp/templates/index.html"
    doc_externo = open(ruta)
    plantilla = Template(doc_externo.read())
    doc_externo.close()
    contexto = Context({"estudiantes": estudiantes})  
    return HttpResponse(plantilla.render(contexto))
