

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('dni', models.IntegerField(error_messages={'unique': 'Este DNI ya está registrado.'}, unique=True)),
                ('domicilio', models.CharField(blank=True, max_length=200, null=True)),
                ('ciudad', models.CharField(blank=True, max_length=100, null=True)),
                ('telefono', models.CharField(blank=True, help_text='Número sin 0 ni 15', max_length=10, null=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('foto_perfil', models.ImageField(blank=True, null=True, upload_to='img_clientes/')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('perfil', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='Niñera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('turnos', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Mañana', 'Mañana'), ('Tarde', 'Tarde'), ('Noche', 'Noche')], max_length=50, null=True)),
                ('habilidades', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Cocina', 'Cocina'), ('Maneja', 'Maneja'), ('Limpieza', 'Limpieza'), ('Traslado', 'Traslado')], max_length=50, null=True)),
                ('edades', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('0 - 3 años', '0 - 3 años'), ('4 - 6 años', '4 - 6 años'), ('7 - 10 años', '7 - 10 años'), ('11 - 13 años', '11 - 13 años')], max_length=80, null=True)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('dni', models.IntegerField(blank=True, error_messages={'unique': 'Este DNI ya está registrado.'}, null=True, unique=True)),
                ('fecha_nacimiento', models.DateField(blank=True, default='1990-10-10', null=True)),
                ('ciudad', models.CharField(blank=True, max_length=100, null=True)),
                ('telefono', models.CharField(blank=True, help_text='Número sin 0 ni 15', max_length=10, null=True)),
                ('tarifa_por_hora', models.IntegerField(blank=True, null=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('foto_perfil', models.ImageField(blank=True, null=True, upload_to='img_niñeras/')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('perfil', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Niñera',
                'verbose_name_plural': 'Niñeras',
            },
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField()),
                ('hora', models.IntegerField()),
                ('lugar', models.CharField(max_length=500)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.cliente')),
                ('niñera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.niñera')),
            ],
        ),
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentarista', models.CharField(max_length=200)),
                ('puntaje', models.FloatField(default=0)),
                ('mensaje', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Mensaje',
                'verbose_name_plural': 'Mensajes',
            },
        ),
    ]
