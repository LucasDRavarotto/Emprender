# Generated by Django 5.1.1 on 2024-10-13 19:01

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('descripcion', models.TextField(default='Sin descripción disponible')),
                ('imagen_seccion', models.ImageField(blank=True, default='default_image.png', null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('titulo', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('imagen_seccion', models.ImageField(blank=True, default='default_image.png', null=True, upload_to='')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('categoria', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='post.category')),
            ],
        ),
    ]
