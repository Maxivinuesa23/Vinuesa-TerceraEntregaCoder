# Generated by Django 5.2 on 2025-04-25 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alumno_fecha_nacimiento'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatares'),
        ),
    ]
