from django.urls import path
from .views import index,tienda,sobreNosotros,contacto,galeria

urlpatterns=[
    path('', index, name="index"),
    path('tienda/', tienda, name="tienda"),
    path('sobreNosotros/', sobreNosotros, name="sobreNosotros"),
    path('contacto/', contacto, name="contacto"),
    path('galeria/', galeria, name="galeria"),
    
    
    
]