from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    
    # Rotas user
    path('user/login/', views.login_user, name='login_user'),
    path('user/cadastro/', views.cadastro_user, name='cadastro_user'),
    path('user/welcome/', views.welcome_user, name='welcome_user'),

    
    # rotas freteiro
    path('motorista/login/', views.login_freteiro, name='login_freteiro'),
    path('motorista/cadastro/', views.cadastro_freteiro, name='cadastro_freteiro'),
    path('motorista/welcome/', views.welcome_freteiro, name='welcome_freteiro'),
    
    
    # admininstração
    path('suporte/usuarios/', views.listar_usuarios_geral, name='listar_usuarios_geral'), #listar todos os usuarios e freteiros
    path('suporte/<str:tipo>/<int:id>/editar/', views.update_geral, name='update_geral'), #listar todos os usuarios e freteiros
    path('suporte/<str:tipo>/<int:id>/excluir/', views.excluir_geral, name='excluir_geral'), #listar todos os usuarios e freteiros




    



]