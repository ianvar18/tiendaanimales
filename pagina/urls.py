from django.urls import path
from . import views

urlpatterns = [
    path ('', views.index, name='index'), 
    path ('Accesorios', views.Accesorios, name='Accesorios'),  
    path ('Comidas', views.Comidas, name='Comidas'),
    path ('Juguetes', views.Juguetes, name='Juguetes'),
    path ('Snacks', views.Snacks, name='Snacks'),
    path ('Registro/', views.Registro, name='Registro'),    
    path ('crud', views.crud, name='crud'),
    path ('productosAdd', views.productosAdd, name='productosAdd'),
    path ('productos_del/<str:pk>', views.productos_del, name='productos_del'),
    path ('productos_findEdit/<str:pk>', views.productos_findEdit, name='productos_findEdit'),
    path ('productosUpdate', views.productosUpdate, name='productosUpdate'),
]
