# Generated by Django 4.1.1 on 2022-10-17 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_mensaje_comentarista_alter_mensaje_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='descripcion',
            field=models.TextField(blank=True, null=True),
        ),
    ]
