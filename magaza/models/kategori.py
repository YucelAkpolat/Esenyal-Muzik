from enum import unique
from tabnanny import verbose
from django.db import models
from autoslug import AutoSlugField


class KategoriModel(models.Model):
    isim = models.CharField(max_length=30, blank=True, null=True)
    slug =  AutoSlugField(populate_from='isim',unique=True)


    class Meta:
     db_table = 'Kategori'
     verbose_name_plural = 'Kategoriler'
     verbose_name = 'Kategori'

    def __str__(self):
        return self.isim 