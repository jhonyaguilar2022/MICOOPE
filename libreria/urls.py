from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

#El usuario entra y accede a la vista de inicio 
urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    #path('bin',views.bin, name='bin'),
    path('bin',views.bin_view, name='bin'),
    path('bin/crear',views.crear, name='crear'),   
    path('bin/editar',views.editar, name='editar'),  
    path('eliminar/<int:id>',views.eliminar, name='eliminar'), 
    path('bin/editar/<int:id>',views.editar, name='editar'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
