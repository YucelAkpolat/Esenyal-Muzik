from re import search
from django.contrib import admin
from magaza.models import KategoriModel
from magaza.models import YazilarModel
from magaza.models import YorumModel

# Register your models here.
admin.site.register(KategoriModel)

admin.site.register(YorumModel)

class YazilarAdmin(admin.ModelAdmin):
    search_fields=('baslik','icerik')
    list_display=(
        'baslik','olusturulma_tarihi','düzenlenme_tarihi'
    )

admin.site.register(YazilarModel,YazilarAdmin)
