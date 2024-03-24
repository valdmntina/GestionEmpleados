from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='inicio'),
    path('salario/', views.salario, name='salario'),
    path('save_salario/', views.save_salario, name='save_salario'),
    path('trabajo/', views.trabajo, name='puestotrabajo'),
    path('save_trabajo/', views.save_trabajo, name='save_trabajo'),
    path('lista/', views.lista_salario, name='lista_salario'), 
    path('id/<int:id>/', views.id_salario, name="id_salario")
]
