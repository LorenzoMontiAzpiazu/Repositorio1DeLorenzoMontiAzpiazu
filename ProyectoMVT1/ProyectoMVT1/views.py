from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from App.models import Familiares

def familiares(request, nombre, numero_tel, fecha_nac):
    
    familiares = Familiares(nombre=nombre, numero_tel=numero_tel, fecha_nac=fecha_nac)
    familiares.save()

    return HttpResponse(f"""
        <p>nombre: {familiares.nombre} - numero: {familiares.numero_tel} - fecha_nac: {familiares.fecha_nac} 
    """)

def lista_familiares(request):
    
    lista = Familiares.objects.all()

    return render(request,'lista_familiares.html', {'lista_familiares': lista})

