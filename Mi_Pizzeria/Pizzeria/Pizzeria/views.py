from django.shortcuts import render

def index(request):
    restaurante = {
        'nombre': 'Restaurante LaVecchia',
        'descripcion': 'Disfruta de nuestra deliciosa comida en un ambiente acogedor.',
        'menu': ['Plato 1', 'Plato 2', 'Plato 3'],
        'direccion': 'Roque Grasera, Montevideo, Uruguay',
        'telefono': '123-456-789',
        'email': 'lavecchia@gmail.com'
    }
    return render(request, 'index.html', {'restaurante': restaurante})