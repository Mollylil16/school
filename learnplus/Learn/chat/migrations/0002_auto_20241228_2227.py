# Generated by Django 2.2.12 on 2024-12-28 21:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salon',
            name='classe',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='class_room', to='school.Classe'),
        ),
    ]
