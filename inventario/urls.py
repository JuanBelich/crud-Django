from django.contrib import admin
from django.urls import path
from inventario.views import main,crearProducto,eliminarProducto,principal,editarProducto
from django.contrib.auth import views

urlpatterns = [
    path('',principal,name='principal'),
    path('crear/',crearProducto,name='crear'),
    path('eliminar/<id>',eliminarProducto,name='eliminar'),
    path('main/',main,name='main'),
    path('editar/<id>',editarProducto,name='editar'),
    path('login/',views.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/',views.LogoutView.as_view(),name='logout')
]