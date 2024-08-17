from django.shortcuts import render, get_object_or_404, redirect
from apps.galeria.models import Fotografia
from django.contrib import messages
from apps.galeria.forms import FotografiaForms

def index(request):
          if not request.user.is_authenticated:
                    messages.success(request, 'Faça login')
                    return redirect('login')

          fotografias = Fotografia.objects.order_by("-data").filter(publicada=True)
          return render(request, 'galeria/index.html', {"cards": fotografias})


def imagem(request, foto_id):
          fotografia = get_object_or_404(Fotografia, pk= foto_id)
          return render(request, 'galeria/imagem.html', {"fotografia":fotografia})


def buscar(request):
          if not request.user.is_authenticated:
                    messages.success(request, 'Faça login')
                    return redirect('login')
                    
          fotografias = Fotografia.objects.order_by("-data").filter(publicada=True)
          if "buscar" in request.GET:
                    nome_a_buscar = request.GET['buscar']
                    if nome_a_buscar: 
                              fotografias = fotografias.filter(nome__icontains=nome_a_buscar)

          return render(request, 'galeria/index.html', {"cards": fotografias})


def new_image(request):          
          if not request.user.is_authenticated:
                    messages.success(request, 'Faça login')
                    return redirect('login')
          form = FotografiaForms
          if request.method == 'POST':
                    form = FotografiaForms(request.POST, request.FILES)
                    if form.is_valid():
                              form.save()
                              messages.success(request, 'Nova fotografia cadastrada!')
                              return redirect('index')                        
                              
          return render(request, "galeria/crud/new_image.html", {'form':form} )


def edit_image(request, foto_id):
          #capturando informações do banco de dados
          fotografia = Fotografia.objects.get(id=foto_id)
          #criando o forms com o q foi feito antes e passando as informações preexistentes
          form = FotografiaForms(instance=fotografia)
          #esse trecho verifica se o método da requisição é POST e, se for o caso, cria uma instância do formulário FotografiaForms com os dados enviados no POST
          if request.method == 'POST':
                    form = FotografiaForms(request.POST, request.FILES, instance=fotografia)
                    if form.is_valid():
                              form.save()
                              messages.success(request, 'fotografia alterada!')
                              return redirect('index') 

          return render(request, "galeria/crud/edit_image.html", {'form':form, 'foto_id':foto_id})

def delet_image(request, foto_id):
          #capturando informações do banco de dados
          fotografia = Fotografia.objects.get(id=foto_id)
          #deletar
          fotografia.delete()
          #redirecionando para o index
          return redirect('index')


def filtro(request, categoria):
    fotografias = Fotografia.objects.order_by("data").filter(publicada=True, categoria=categoria)

    return render(request, 'galeria/index.html', {"cards": fotografias})