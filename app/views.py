from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario, Freteiro
from datetime import date
from django.contrib import messages
from .forms import UsuarioForm, FreteiroForm

# Create your views here.
def index(request):
    return render(request, 'index.html')



# Seção Usuário
def login_user(request):
    return render(request, 'tela_user.html', {'active': 'usuario'})    

def cadastro_user(request):
    if request.method == 'POST':
        novo_usuario = Usuario()
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        tel = request.POST.get('tel')
        cpf = request.POST.get('cpf')
        
        # juntar os dados e formar a data_nascimento
        dia = request.POST.get('dia')
        mes = request.POST.get('mes')
        ano = request.POST.get('ano')
        
        data_nascimento = f"{ano}-{mes}-{dia}"
        novo_usuario.data_nascimento = data_nascimento
    
    
        novo_usuario.nome = nome
        novo_usuario.email = email
        novo_usuario.senha = senha
        novo_usuario.tel = tel
        novo_usuario.cpf = cpf
        
        novo_usuario.save()
        
        # verificar o que já foi cadastrado até o momento.
        # usuarios = { Usuario.objects.all() }
        # return render(request, 'listar_usuarios.html', {'usuarios': usuarios})
        return redirect('welcome_user')   

        
    return render(request, 'tela_cadastro_usuario.html')   
      

# @login_required
def welcome_user(request):
    return render(request, 'tela_inicial_usuario.html') 

# Seção freteiro
def login_freteiro(request):
    return render(request, 'tela_motorista.html', {'active': 'motorista'})

def welcome_freteiro(request):
    return render(request, 'tela_inicial_freteiro.html') 



def cadastro_freteiro(request):
    novo_freteiro = Freteiro()
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        tel = request.POST.get('tel')
        cpf = request.POST.get('cpf')
        cidade = request.POST.get('cidade')
        estado = request.POST.get('estado')
        # juntar os dados e formar a data_nascimento
        dia = request.POST.get('dia')
        mes = request.POST.get('mes')
        ano = request.POST.get('ano')
        
        if dia and mes and ano:
            try:
                data_nascimento = date(int(ano), int(mes), int(dia))
            except ValueError:
                data_nascimento = None  
        else:
            data_nascimento = None
            
        if not nome or not email or not senha or not cpf:
            return render(request, 'tela_cadastro_freteiro.html', {
                'erro': 'Preencha todos os campos obrigatórios.'
            })
        novo_freteiro.data_nascimento = data_nascimento

        novo_freteiro.nome = nome
        novo_freteiro.email = email
        novo_freteiro.senha = senha
        novo_freteiro.tel = tel
        novo_freteiro.cpf = cpf
        novo_freteiro.cidade = cidade
        novo_freteiro.estado = estado
    
        novo_freteiro.save()    
        return redirect('welcome_freteiro')

    return render(request, 'tela_cadastro_freteiro.html')  


# Administração geral
def listar_usuarios_geral(request):
    query = request.GET.get('q', '')  # pega o valor do campo de pesquisa

    if query:
        # Filtra por nome ou email contendo o texto
        usuarios = Usuario.objects.filter(
            nome__icontains=query
        ) | Usuario.objects.filter(
            email__icontains=query
        )
        freteiros = Freteiro.objects.filter(
            nome__icontains=query
        ) | Freteiro.objects.filter(
            email__icontains=query
        )
    else:
        
        freteiros = Freteiro.objects.all()
        usuarios = Usuario.objects.all()
        
    return render(request, 'administrar_usuarios.html', {
        'freteiros': freteiros,
        'usuarios': usuarios,
        'query': query
    })
        


def update_geral(request, id, tipo):
    if tipo == 'freteiro':
        post = get_object_or_404(Freteiro, id=id)
        form_class = FreteiroForm
    elif tipo == 'usuario':
        post = get_object_or_404(Usuario, id=id)
        form_class = UsuarioForm
    else:
        return redirect('listar_usuarios_geral')

    form = form_class(request.POST or None, request.FILES or None, instance=post)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('listar_usuarios_geral')

    return render(request, 'update.html', {
        'form': form,
        'tipo': tipo,
        'post': post
    })


def excluir_geral(request, id, tipo):
    if tipo == 'freteiro':
        post = get_object_or_404(Freteiro, id=id) #xconsulta de freteiro
    elif tipo == 'usuario':
        post = get_object_or_404(Usuario, id=id) # consulta de usuario
    else:
        return redirect('listar_usuarios_geral')

    if request.method == 'POST':
        post.delete()
        return redirect('listar_usuarios_geral')

    return render(request, 'delete.html', {
        'post': post,
        'tipo': tipo
    })
    
def listar_por_cidade(request, cidade):
    freteiros = Freteiro.objects.filter(cidade__iexact=cidade)
    return render(request, 'listar_por_cidade.html', {'freteiros': freteiros, 'cidade': cidade})
  

