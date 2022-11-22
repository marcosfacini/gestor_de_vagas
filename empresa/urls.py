from django.urls import path
from . import views

urlpatterns = [
    path('nova_empresa/', views.nova_empresa, name="nova_empresa"),
    path('empresas/',views.empresas, name='empresas'),
    path('excluir_empresa/<int:id>', views.excluir_empresa, name='excluir_empresa'),
    path('empresa_unica/<int:id>', views.empresa_unica, name="empresa_unica"),
    path('deletar_vaga/<int:id_vaga>', views.deletar_vaga, name='deletar_vaga'),
    path('tecnologias/', views.tecnologias, name='tecnologias'),
    path('nova_tech/', views.nova_tech, name='nova_tech'),
]