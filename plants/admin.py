from django.contrib import admin
from .models import Category, Plant , Review

# Enregistrement des modèles dans l'interface d'administration

admin.site.register(Category)
admin.site.register(Plant)
admin.site.register(Review)



