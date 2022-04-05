from django.shortcuts import render
from django.http import HttpResponse
from appmvt.models import Familia

# Create your views here.


def listar_familia(request):

    lista = Familia.objects.all()
    print(lista)

    return render(request,"appmvt/base.html",{"familia":lista}) 