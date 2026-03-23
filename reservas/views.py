from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import ValidationError
from .models import Recurso, Reserva
from .forms import ReservaForm
from datetime import timedelta

@login_required
def lista_recursos(request):
    recursos = Recurso.objects.all()
    mis_reservas = Reserva.objects.filter(usuario=request.user).order_by('-inicio')
    
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            recurso = form.cleaned_data['recurso']
            inicio_base = form.cleaned_data['inicio']
            fin_base = form.cleaned_data['fin']
            es_recurrente = form.cleaned_data['repetir_4_semanas']
            
            cantidad = 4 if es_recurrente else 1
            
            try:
                for i in range(cantidad):
                    nueva_inicio = inicio_base + timedelta(weeks=i)
                    nueva_fin = fin_base + timedelta(weeks=i)
                    
                    reserva = Reserva(
                        usuario=request.user,
                        recurso=recurso,
                        inicio=nueva_inicio,
                        fin=nueva_fin
                    )
                    
                    reserva.full_clean()
                    reserva.save()
                
                messages.success(request, '¡Reserva confirmada con éxito!')
                return redirect('lista_recursos')

            except ValidationError as e:
                if hasattr(e, 'message_dict'):
                    mensaje_error = e.message_dict.get('__all__', [str(e)])[0]
                else:
                    mensaje_error = str(e)
                
                messages.error(request, f"No se pudo reservar: {mensaje_error}")
                return redirect('lista_recursos') 
                
            except Exception as e:
                messages.error(request, f"Error inesperado: {str(e)}")
                return redirect('lista_recursos')
    else:
        form = ReservaForm()

    return render(request, 'reservas/lista.html', {
        'recursos': recursos, 
        'form': form, 
        'mis_reservas': mis_reservas
    })

@login_required
def eliminar_reserva(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk, usuario=request.user)
    reserva.delete()
    messages.info(request, 'La reserva ha sido cancelada.')
    return redirect('lista_recursos')