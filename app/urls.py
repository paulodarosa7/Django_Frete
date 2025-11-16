from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    
    # Rotas user
    path('user/login/', views.login_user, name='login_user'),
    path('user/cadastro/', views.cadastro_user, name='cadastro_user'),
    path('user/welcome/', views.welcome_user, name='welcome_user'),
    
    path('user/perfil/<int:id>/', views.perfil_user, name='perfil_user'),
    # path('user/logout/', views.logout, name='logout'),
    
    
    #solicitar frete
    # path('user/fretes/historico/', views.fretes_solicitados, name='fretes_solicitados'),
    path('user/<int:id>/fretes/solicitar/', views.solicitar_frete, name='solicitar_frete'),
    path('user/<int:id>/frete/concluido/', views.frete_concluido, name='frete_concluido'),
    path('user/fretes/status/', views.status_frete, name='status_frete'),

    # path('user/<int:id>/frete/<int:id>/editar', views.solicitar_frete, name='solicitar_frete'),

    

    
    # rotas freteiro
    path('motorista/login/', views.login_freteiro, name='login_freteiro'),
    path('motorista/cadastro/', views.cadastro_freteiro, name='cadastro_freteiro'),
    path('motorista/welcome/', views.welcome_freteiro, name='welcome_freteiro'),
    
    # path('motorista/perfil/<int:id>/', views.perfil_freteiro, name='perfil_freteiro'),
    # path('motorista/logout/', views.logout, name='logout'),
    
    
    # aceitar frete
    path('motorista/fretes/disponiveis/', views.fretes_disponiveis, name='fretes_disponiveis'),
    path('motorista/frete/<int:frete_id>/aceitar/', views.aceitar_frete, name='aceitar_frete'),
    path('motorista/fretes/status/', views.status_frete, name='status_frete_freteiro'),
    
    # gestão de fretes
    path('fretes/', views.listar_fretes, name='listar_fretes'),
    path('fretes/<int:id>/atualizar/', views.atualizar_frete, name='atualizar_frete'),
    path('fretes/<int:id>/cancelar/', views.cancelar_frete, name='cancelar_frete'),
    path('fretes/<int:id>/excluir/', views.excluir_frete, name='excluir_frete'),

    
    # admininstração
    path('suporte/usuarios/', views.listar_usuarios_geral, name='listar_usuarios_geral'), #listar todos os usuarios e freteiros
    path('suporte/<str:tipo>/<int:id>/editar/', views.update_geral, name='update_geral'), #listar todos os usuarios e freteiros
    path('suporte/<str:tipo>/<int:id>/excluir/', views.excluir_geral, name='excluir_geral'), #listar todos os usuarios e freteiros




    



]