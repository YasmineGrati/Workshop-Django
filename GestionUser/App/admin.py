from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Reporter)

#On aura toute la personnalisation de l'affichage du modele article cote admin
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('headline', 'reporter', 'pub_date','created_at','updated_at', 'est_valide')
    fields = (
        ('headline', 'reporter'),
        ('pub_date', 'created_at', 'updated_at')
    )
    readonly_fields = ('created_at', 'updated_at')
#admin.site.register(Article, ArticleAdmin)