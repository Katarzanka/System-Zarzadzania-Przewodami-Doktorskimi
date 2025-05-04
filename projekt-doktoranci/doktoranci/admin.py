from django.contrib import admin

# Register your models here.

from .models import Doktorant

@admin.register(Doktorant)
class DoktorantAdmin(admin.ModelAdmin):
    list_display = ('imie', 'nazwisko', 'temat_pracy', 'status')



from .models import ProfilUzytkownika

@admin.register(ProfilUzytkownika)
class ProfilUzytkownikaAdmin(admin.ModelAdmin):
    list_display = ('user', 'rola')

