from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import Usuarios
from django.contrib.auth import logout
# Create your views here.

# funcion que creara un usuario en la pagina de registro, tendra un if/else en caso de que el metodo post este correcto junto con los datos solicitados, lo guardara en el modelo de Usuarios y se generara de manera exitosa
def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Usuarios.objects.create(user=user)
            return redirect('/login/')
    else:
        form = UserCreationForm()
    return render(request, 'perfilUsuario/registro.html', {
        'form': form
    })
    
def logout_view(request):
    logout(request)
    return redirect('index')