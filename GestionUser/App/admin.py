from pyexpat.errors import messages

from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Reporter)

#On aura toute la personnalisation de l'affichage du modele article cote admin
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('headline', 'reporter', 'pub_date','created_at','updated_at', 'est_valide')
    '''fields = (
        ('headline', 'reporter'),
        ('pub_date', 'created_at', 'updated_at')
    )'''
    fieldsets = (
        (None, {'fields': ('headline','reporter')}),
        ('Dates', {'fields': ('pub_date', 'created_at', 'updated_at')}),
        ('state', {'fields': ('est_valide',)})
    )
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ['headline', 'reporter']
    list_filter = ('headline', 'reporter')
    actions = ['set_to_valid', 'set_to_no_valid']
    def set_to_valid(self, request, queryset):
        queryset.update(est_valide=True)
    set_to_valid.short_description = 'Validate'

    def set_to_no_valid(self,request, queryset):
        row_no_valid= queryset.filter(est_valide=False)
        if row_no_valid.count()>0:
            messages.error(request,"%s This article is already no valid"%row_no_valid.count())
        else:
            rows_update=queryset.update(est_valide=False)
            if rows_update==1:
                message="1 article was successfully added !"
            else:
                message="%s articles were"%rows_update
            self.message_user(request,level='success', message='%s successfully marked as not valid'% message)

    #radio_fields = {'reporter': admin.VERTICAL}
#admin.site.register(Article, ArticleAdmin)