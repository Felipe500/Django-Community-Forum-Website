# Generated by Django 3.2.9 on 2021-12-05 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20211205_1034'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='descricao_arquivo1',
            field=models.CharField(default='arquivo1', max_length=50),
        ),
        migrations.AddField(
            model_name='post',
            name='descricao_arquivo2',
            field=models.CharField(default='arquivo2', max_length=50),
        ),
        migrations.AddField(
            model_name='post',
            name='descricao_arquivo3',
            field=models.CharField(default='arquivo3', max_length=50),
        ),
    ]
