from django.urls import path
from appmvt.views import listar_familia


urlpatterns = [
    path('familia/', listar_familia, name = "Familia")
]
