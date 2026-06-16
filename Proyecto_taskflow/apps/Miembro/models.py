from django.db import models

class Miembro(models.Model):
    ESTADO_CHOICES = [
        (True, 'Activo'),
        (False, 'Inactivo'),
    ]

    nombre_completo = models.CharField(max_length=150)
    rol_empresa = models.CharField(max_length=100)
    correo_electronico = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)
    fecha_ingreso = models.DateField()
    departamento = models.CharField(max_length=100)
    horas_disponibles_semana = models.PositiveIntegerField()
    habilidad_principal = models.CharField(max_length=100)
    estado_activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre_completo

    class Meta:
        verbose_name = 'Miembro'
        verbose_name_plural = 'Miembros'