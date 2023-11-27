from django.contrib import admin
from .models import Usuario, Taller, Inscripcion

admin.site.register(Usuario),
admin.site.register(Taller),
admin.site.register(Inscripcion)
