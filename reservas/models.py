from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Recurso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    capacidad = models.IntegerField(default=1)

    def __str__(self):
        return self.nombre

class Reserva(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    recurso = models.ForeignKey(Recurso, on_delete=models.CASCADE)
    inicio = models.DateTimeField()
    fin = models.DateTimeField()
    creada_el = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.recurso.nombre}"

    # Lógica para evitar solapamiento de fechas (El "Reto" del PDF)
    def clean(self):
        if self.inicio >= self.fin:
            raise ValidationError("La fecha de inicio debe ser anterior a la de fin.")
        
        # Buscamos si hay otra reserva que choque
        choque = Reserva.objects.filter(
            recurso=self.recurso,
            inicio__lt=self.fin,
            fin__gt=self.inicio
        ).exclude(pk=self.pk).exists()

        if choque:
            raise ValidationError(f"La '{self.recurso}' ya está reservada en este horario.")