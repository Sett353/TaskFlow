from django.db import models
from django.contrib.auth.models import User
import os


class Comentario(models.Model):

    tarea = models.IntegerField()

    autor = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    texto_comentario = models.TextField()

    fecha_publicacion = models.DateField(
        auto_now_add=True
    )

    hora_publicacion = models.TimeField(
        auto_now_add=True
    )

    editado = models.BooleanField(
        default=False
    )

    archivo_adjunto = models.FileField(
        upload_to='comentarios/',
        blank=True,
        null=True
    )

    tipo_archivo = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    visibilidad_cliente = models.BooleanField(
        default=True
    )

    def save(self, *args, **kwargs):

        if self.archivo_adjunto:

            extension = os.path.splitext(
                self.archivo_adjunto.name
            )[1]

            self.tipo_archivo = extension.upper()

        super().save(*args, **kwargs)

    def __str__(self):

        return f"Comentario {self.id}"