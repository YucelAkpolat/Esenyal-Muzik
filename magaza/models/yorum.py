from tabnanny import verbose
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

from magaza.models.yazi import YazilarModel


class YorumModel(models.Model):
    yazan = models.ForeignKey(User, on_delete=models.CASCADE,related_name='yorum')
    yazi = models.ForeignKey(YazilarModel,on_delete=models.CASCADE,related_name='yorumlar')
    yorum = models.TextField()
    olusturulma_tarihi = models.DateField(auto_now_add=True)
    guncellenme_tarihi = models.DateField(auto_now=True)


    class Meta:
        db_table = 'yorum'
        verbose_name ='Yorum'
        verbose_name_plural='Yorumlar'

    def __str__(self):
        return self.yazan.username
    
    