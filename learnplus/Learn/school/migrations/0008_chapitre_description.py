# Generated by Django 2.2.8 on 2020-04-28 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0007_remove_cours_duree'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapitre',
            name='description',
            field=models.TextField(default='Description du chapitre'),
        ),
    ]