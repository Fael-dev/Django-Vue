# Generated by Django 3.0.4 on 2020-03-23 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='foto',
            field=models.ImageField(upload_to='media/img', verbose_name='Foto'),
        ),
    ]
