import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings

# Create your models here.

class Encuesta(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    titulo = models.CharField(_("Titulo"), max_length=100, unique=True)
    descripcion = models.TextField(_("Descripcion"), null=True, blank=True)
    creado = models.DateTimeField(verbose_name=_(
        'Fecha y hora de creación'),auto_now_add=True)
    actualizado = models.DateTimeField(verbose_name= _(
        'Fecha y hora de actualizacion'), auto_now= True)

    class Meta:
        verbose_name = _("Encuesta")
        verbose_name_plural = _("Encuestas")

    def __str__(self):
        return self.titulo
    

class Pregunta(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    encuesta = models.ForeignKey("Encuesta", verbose_name=_("encuesta"), on_delete=models.CASCADE)
    pregunta = models.TextField(_("Pregunta?"))
    pregunta_previa = models.ForeignKey("self", verbose_name=_("Pregunta previa"), null=True, 
                                        blank=True, on_delete=models.CASCADE, related_name="previa")
    pregunta_sgte = models.ForeignKey("self", verbose_name=_("Pregunta siguiente"), null=True,
                                      blank=True, on_delete=models.CASCADE, related_name="siguiente")
    creado = models.DateTimeField(verbose_name=_(
        'Fecha y hora de creación'), auto_now_add=True)
    actualizado = models.DateTimeField(verbose_name=_(
        'Fecha y hora de actualizacion'), auto_now=True)

    class Meta:
        verbose_name = _("Pregunta")
        verbose_name_plural = _("Preguntas")

    def __str__(self):
        return "{}".format(self.pregunta)


class Respuesta(models.Model):
    OPCIONES = (
        ("DE_ACUERDO", "De acuerdo"),
        ("EN_DESACUERDO", "En desacuerdo"),
        ("NO_SABE", "No sabe/no opina")
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_(
        "Usuario"), on_delete=models.CASCADE)
    pregunta = models.ForeignKey("Pregunta", verbose_name=_("pregunta"), on_delete=models.CASCADE)
    respuesta = models.CharField(
        _("Respuesta"), max_length=50, choices=OPCIONES)
    creado = models.DateTimeField(verbose_name=_(
        'Fecha y hora de creación'), auto_now_add=True)
    actualizado = models.DateTimeField(verbose_name=_(
        'Fecha y hora de actualizacion'), auto_now=True)

    class Meta:
        verbose_name = _("Respuesta")
        verbose_name_plural = _("Respuestas")

    def __str__(self):
        return "{}".format(self.id)
