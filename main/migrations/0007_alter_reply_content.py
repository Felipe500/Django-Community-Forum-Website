# Generated by Django 3.2.6 on 2021-10-02 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_reply_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='content',
            field=models.TextField(),
        ),
    ]
