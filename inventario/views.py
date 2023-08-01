from django.shortcuts import render,redirect,get_object_or_404

from .models import Productos,Categoria
from .forms import ProductoForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def main(request):
    productos= Productos.objects.all()
    categoria=Categoria.objects.all()
    formulario=ProductoForm()
    context={'productos':productos,'categoria':categoria,'formulario':formulario}
    return render (request,'listado.html',context)

@login_required
def crearProducto (request):
    formulario = ProductoForm(request.POST)
    if formulario.is_valid():
        formulario.save()
        return redirect("main")

@login_required
def eliminarProducto(request,id):
    Producto=Productos.objects.get(id=id)
    Producto.delete()
    return redirect('main')

@login_required
def editarProducto(request,id):
    producto=get_object_or_404(Productos,id=id)
    if request.method == 'GET':
        formulario=ProductoForm(instance=producto)
        ctx={'formulario':formulario,'producto':producto}
        return render(request,'editar.html',ctx)
    
    elif request.method=='POST':
            formulario=ProductoForm(request.POST,instance=producto)
            if formulario.is_valid():
                formulario.save()
                return redirect('main')
    
def principal(request):
    productos= Productos.objects.all()
    categoria=Categoria.objects.all()
    
    context={'productos':productos,'categoria':categoria}
    return render (request,'principal.html',context)