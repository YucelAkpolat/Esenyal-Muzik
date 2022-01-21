from tabnanny import verbose
from django.db import models


class IletisimModel(models.Model):
    email = models.EmailField(max_length=250)
    isim_soyisim = models.CharField(max_length=150)
    olusturulma_tarihi = models.DateField(auto_now_add=True)
    mesaj = models.TextField()


    class Meta:
        db_table = 'iletisim'
        verbose_name ='İletişim'
        verbose_name_plural = 'iletişim'

    def __str__(self):
        return self.email
    
