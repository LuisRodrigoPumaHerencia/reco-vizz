from email import message
from importlib.metadata import requires
from pyexpat.errors import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse

from aplicacion.formCaptcha import FormWithCaptcha

from .models import Persona
from .forms import PersonaForm

from werkzeug.security import generate_password_hash, check_password_hash

def index(request):
    return render(request, 'index.html')

def lista(request):
    persona = Persona.objects.all()
    return render(request, 'registro/lista.html', {'personalista': persona})

def registro(request):
    formulario = PersonaForm(request.POST or None)
    

    if formulario.is_valid():
        formulario.save()
        correoawd = formulario.data['correo']
        contrasena = formulario.data['contrasena']
        nuevaContrasena = generate_password_hash(contrasena, 'pbkdf2:sha256',30)
        personaAActualizar = Persona.objects.filter(correo=correoawd)
        personaAActualizar.update(contrasena=nuevaContrasena)
        return redirect('lista')
    return render(request, 'registro/registro.html', {'formulario': formulario})

# def clean_Contraseña(self):
#     data = self.cleaned_data['Contraseña']
#     data = "probando"
#     print("este metodo se ejecuta we")
#     return data

def inicioSesion(request):
    if request.method == 'POST':
        try: 
            form = FormWithCaptcha(request.POST)
            if form.is_valid():
                persona = Persona.objects.get(correo=request.POST['email'])
                if persona != None:
                    if check_password_hash(persona.contrasena, request.POST['password']):
                        return redirect('autentificacion')
                    else: 
                        return redirect('inicioSesion')
                else:
                    return redirect('inicioSesion')
            else:
                return redirect('inicioSesion')
        except Persona.DoesNotExist:
            return redirect('inicioSesion')

    form = FormWithCaptcha()
    return render(request, 'inicioSesion/inicioSesion.html',{'form':form})

def autentifiacion(request):
    if request.method == 'POST':
        form = FormWithCaptcha(request.POST)
        if form.is_valid():
            return redirect('lista')
        else:
            return redirect('autentificacion')

    return render(request, 'inicioSesion/autentificacion.html',{'form':form})

def registroVoz(request):
    return render(request, 'registro/registroVoz.html')

