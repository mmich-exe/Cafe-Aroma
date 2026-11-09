from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_carta, name='lista_carta'),
    path('cafe/<int:pk>/', views.detalle_cafe, name='detalle_cafe'),
    path('cafe/nuevo/', views.crear_cafe, name='crear_cafe'),
    path('cafe/<int:pk>/editar/', views.editar_cafe, name='editar_cafe'),
    path('cafe/<int:pk>/eliminar/', views.eliminar_cafe, name='eliminar_cafe'),
]