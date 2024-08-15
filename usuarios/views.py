from django.shortcuts import render, redirect
from usuarios.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User 
from django.contrib import auth
from django.contrib import messages

def login(request):
        form = LoginForms()
        if request.method == 'POST':
                form = LoginForms(request.POST)

                if form.is_valid():
                        nome = form['nome_login'].value()
                        senha = form['senha'].value()

                        usuario = auth.authenticate(
                                request,
                                username=nome,
                                password=senha
                        )
                        if usuario is not None:
                                auth.login(request, usuario)
                                messages.success(request, f'{nome} logado com sucesso!')
                                return redirect('index')
                        else:
                                messages.error(request, 'Erro ao efetuar login')
                                return redirect('login')


        return render(request, "usuarios/login.html", {"form": form})

def cadastro(request):
    form = CadastroForms()

    if request.method == 'POST': 
        form = CadastroForms(request.POST)

        if form.is_valid():# validação do formulário
            if form["senha_1"].value() != form["senha_2"].value(): #validação de senhas iguais
                messages.error(request, 'As senhas são diferentes!')
                return redirect ('cadastro')

            nome=form['nome_cadastro'].value() #armazenando as informações do forms em variáveis
            email=form['email'].value()
            senha=form['senha_1'].value()

            if User.objects.filter(username=nome).exists(): #verificação se o usuário existe
                messages.error(request, 'Usuário existente')
                return redirect('cadastro')

            usuario = User.objects.create_user( #criamos esse novo usuário com as informações inseridas no formulário.
                username=nome,
                email=email,
                password=senha
            )
            usuario.save()
            messages.success(request, 'Login feito vom sucesso!')
            return redirect('login')

    return render(request, 'usuarios/cadastro.html', {'form': form})


def logout(request):
        auth.logout(request)
        messages.success(request, "Logout efeituado")
        return redirect('login')