# Generated by Django 2.0.2 on 2018-02-18 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projetos', '0002_auto_20180217_1452'),
    ]

    operations = [
        migrations.AddField(
            model_name='pacote',
            name='percent',
            field=models.IntegerField(default=0, verbose_name='Percentual'),
        ),
    ]
