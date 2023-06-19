from django.shortcuts import redirect, render
from .models import Productos
from .forms import ProductoForm,RegistroUserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
def index(request):
     return render(request, 'index.html')
@login_required
def contacto(request):
     return render(request, 'contacto.html')
@login_required
def galeria(request):
     return render(request, 'galeria.html')
@login_required
def sobreNosotros(request):
     return render(request, 'sobreNosotros.html')



@login_required
def crear(request):
     if request.method=="POST":    
          ProductoForm = ProductoForm(request.POST, request.FILES)    #creamos un objeto de tipo Formulario
          if ProductoForm.is_valid():
               ProductoForm.save()      #similar al insert de sql en función 
               return redirect('tienda')
     else: 
          ProductoForm=ProductoForm()
     return render(request, 'crear.html', {'ProductoForm':ProductoForm})











'''
@login_required
def eliminar(request, id):
  vehiculoEliminado = Vehiculo.objects.get(patente=id)   #select * from Vehiculo where patente=id
      import os
        if ruta_foto != "media/imagenes_bd/noimagen.jpg":
            os.remove(ruta_foto)
     
     vehiculoEliminado.delete()
     return redirect ('otra') '''












'''
@login_required
def modificar(request, id):
     vehiculoModificado=Vehiculo.objects.get(patente=id)
     datos = {
          'form' : VehiculoForm(instance=vehiculoModificado)
     }
     if request.method=='POST':
          formulario = VehiculoForm(data=request.POST, instance=vehiculoModificado)
           try:
            fot = request.FILES['txtfot']

            ruta_foto = "media/"+str(pel.foto)
            import os
            if ruta_foto != "media/imagenes_bd/noimagen.jpg":
                os.remove(ruta_foto)
        except:
            fot = pel.foto

        pel.nombre = nom
        pel.foto = fot
        pel.save()

        pel = Pelicula.objects.all().values()
        datos = {
            'pel' : pel,
            'r' : 'Datos Modificados Correctamente!'
        }
        return render(request, 'listado.html', datos)

    except:
        pel = Pelicula.objects.all().values()
        datos = {
        'plantas' :plantas
        'mensaje de error' : El ID ('+str(id)+') No Existe. Imposible Actualizar!!'
        }
     return render(request, 'modificar.html', datos)'''
















def Tienda(request):
     producto = Productos.objects.all()
     datos={
          'producto':datos
     }
     return render(request, 'mostrar.html', datos)