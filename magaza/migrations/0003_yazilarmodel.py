# Generated by Django 3.1.5 on 2022-01-21 09:50

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('magaza', '0002_auto_20220121_1244'),
    ]

    operations = [
        migrations.CreateModel(
            name='YazilarModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resim', models.ImageField(upload_to='yazı_resimleri')),
                ('baslik', models.CharField(max_length=50)),
                ('icerik', models.TextField()),
                ('olusturulma_tarihi', models.DateField(auto_now=True)),
                ('düzenlenme_tarihi', models.DateField(auto_now=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='baslik', unique=True)),
                ('kategoriler', models.ManyToManyField(related_name='yazi', to='magaza.KategoriModel')),
                ('yazar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='yazilar', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Yazi',
                'verbose_name_plural': 'Yazilar',
                'db_table': 'Yazi',
            },
        ),
    ]
