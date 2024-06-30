from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistroForm
from .models import Categoria, Producto

def index(request):
    context = {}
    return render(request, 'pagina/index.html', context)

def Accesorios(request):
    accesorios = Categoria.objects.get(categoria='Accesorios')
    productos_accesorios = Producto.objects.filter(id_categoria=accesorios)

    return render(request, 'pagina/Accesorios.html', {'productos': productos_accesorios})

def Comidas(request):
    comidas = Categoria.objects.get(categoria='Comidas')
    productos_comidas = Producto.objects.filter(id_categoria=comidas)
    return render(request, 'pagina/Comidas.html', {'productos': productos_comidas})

def Juguetes(request):
    juguetes = Categoria.objects.get(categoria='Juguetes')
    productos_juguetes = Producto.objects.filter(id_categoria=juguetes)
    return render(request, 'pagina/Juguetes.html', {'productos': productos_juguetes})

def Snacks(request):
    snack = Categoria.objects.get(categoria='Snack')
    productos_snack = Producto.objects.filter(id_categoria=snack)
    return render(request, 'pagina/Snacks.html', {'productos': productos_snack})

def Registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Ya se registró!')  # Mensaje de éxito
            return redirect('Accesorios')  # Redirige a la página de Accesorios o donde desees
    else:
        form = RegistroForm()
    
    return render(request, 'pagina/Registro.html', {'form': form})

def admin(request):
    productos = Producto.objects.all()
    context = {"productos": productos}
    return render(request, 'pagina/admin.html', context)

def crud(request):
    productos = Producto.objects.all()
    context = {'productos': productos}
    return render(request, 'pagina/admin_list.html', context)

from django.shortcuts import render, redirect
from .forms import RegistroForm
from .models import Categoria, Producto

def productosAdd(request):
    if request.method == "POST":
        # Obtener datos del formulario
        id_producto = request.POST["id_producto"]
        nombre_producto = request.POST["nombre_producto"]
        precio = request.POST["precio"]
        id_categoria = request.POST["categoria"]

        # Obtener objeto de categoría
        objCategoria = Categoria.objects.get(id_categoria=id_categoria)

        # Crear objeto Producto
        nuevo_producto = Producto(
            id_producto=id_producto,
            nombre_producto=nombre_producto,
            precio=precio,
            id_categoria=objCategoria,
            activo=True
        )

        # Manejar la carga de la imagen
        if 'foto' in request.FILES:
            nuevo_producto.foto = request.FILES['foto']

        nuevo_producto.save()

        # Obtener productos y categorías para el contexto
        productos = Producto.objects.all()
        categorias = Categoria.objects.all()
        context = {
            'mensaje': "¡Producto Añadido!",
            'productos': productos,
            'categorias': categorias
        }
        return render(request, 'pagina/admin_add.html', context)
    
    else:
        # Si no es método POST, mostrar el formulario vacío
        productos = Producto.objects.all()
        categorias = Categoria.objects.all()
        context = {
            'productos': productos,
            'categorias': categorias
        }
        return render(request, 'pagina/admin_add.html', context)


def productos_del(request, pk):
    context = {}
    try:
        producto = Producto.objects.get(id_producto=pk)
        producto.delete()
        mensaje = "¡Producto Eliminado!"
        productos = Producto.objects.all()
        context = {'productos': productos, 'mensaje': mensaje}
        return render(request, 'pagina/admin_list.html', context)
    except Producto.DoesNotExist:
        mensaje = "¡Error! Producto no existe"
        productos = Producto.objects.all()
        context = {'productos': productos, 'mensaje': mensaje}
        return render(request, 'pagina/admin_list.html', context)
    
def productos_findEdit(request, pk):
    if pk != "":
        try:
            producto = Producto.objects.get(id_producto=pk)
            categorias = Categoria.objects.all()
            context = {'producto': producto, 'categorias': categorias}
            return render(request, 'pagina/admin_edit.html', context)
        except Producto.DoesNotExist:
            context = {'mensaje': "¡Error! Producto no existe"}
            return render(request, 'pagina/admin_list.html', context)
        
def productosUpdate(request):
    if request.method == "POST":
        id_producto = request.POST.get("id_producto")
        nombre_producto = request.POST.get("nombre_producto")
        precio = request.POST.get("precio")
        id_categoria = request.POST.get("categoria")

        print(f"id_producto: {id_producto}")
        print(f"nombre_producto: {nombre_producto}")
        print(f"precio: {precio}")
        print(f"id_categoria: {id_categoria}")

        if None in [id_producto, nombre_producto, precio, id_categoria]:
            categorias = Categoria.objects.all()
            productos = Producto.objects.all()
            context = {
                'mensaje': "¡Error! Faltan datos en el formulario.",
                'categorias': categorias,
                'productos': productos
            }
            return render(request, 'pagina/admin_list.html', context)

        objCategoria = Categoria.objects.get(id_categoria=id_categoria)

        producto = Producto.objects.get(id_producto=id_producto)
        producto.nombre_producto = nombre_producto
        producto.precio = precio
        producto.id_categoria = objCategoria
        producto.save()

        categorias = Categoria.objects.all()
        context = {
            'mensaje': "¡Producto Actualizado!",
            'categorias': categorias,
            'producto': producto
        }
        return render(request, 'pagina/admin_edit.html', context)
    else:
        productos = Producto.objects.all()
        context = {'productos': productos}
        return render(request, 'pagina/admin_list.html', context)
