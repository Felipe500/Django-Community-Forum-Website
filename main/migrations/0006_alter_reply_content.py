# Generated by Django 3.2.6 on 2021-10-01 17:40

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_comment_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='content',
            field=tinymce.models.HTMLField(),
        ),
    ]
