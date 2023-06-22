from django.shortcuts import render
from .models import Menu
from AppLaVecchia.forms import MenuFormulario, BuscaMenuForm

def inicio(request):
    return render(request, "AppLaVecchia/index.html")

def menu(request):
    return render(request, "AppLaVecchia/datos.html")

def reservas(request):
    return render(request, "AppLaVecchia/reservas.html")

def contacto(request):
    return render(request, "AppLaVecchia/contacto.html")

def formulario(request):
    if request.method == 'POST':
        menu = Menu(nombre=request.POST['nombre'],precio=request.POST['precio'])
        menu.save()

        return render(request, 'AppLaVecchia/datos.html')
    
    return render(request,"AppLaVecchia/formulario.html")

def form_con_api(request):
    if request.method == "POST":
        miFormulario = MenuFormulario(request.POST) 
        
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            menu = Menu(nombre=informacion["nombre"], precio=informacion["precio"])

            menu.save()
            return render(request, "AppLaVecchia/index.html")
    else:
        miFormulario = MenuFormulario()

    return render(request, "AppLaVecchia/form_con_api.html", {"miFormulario": miFormulario})

def buscar_form_con_api(request):
    if request.method == "POST":
        miFormulario = BuscaMenuForm(request.POST) 

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            
            menu = Menu.objects.filter(nombre__icontains=informacion["menu"])

            return render(request, "AppLaVecchia/resultados_buscar_form.html", {"menu": menu})
    else:
        miFormulario = BuscaMenuForm()

    return render(request, "AppLaVecchia/buscar_form_con_api.html", {"miFormulario": miFormulario})

