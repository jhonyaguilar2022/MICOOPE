from django.urls import path
from . import views

#El usuario entra y accede a la vista de inicio 
urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('bin',views.bin, name='bin'),
    path('bin/crear',views.crear, name='crear'),   
    path('bin/editar',views.editar, name='editar'),  
]
