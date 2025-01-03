# Generated by Django 2.2.12 on 2024-12-28 21:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instructor', '0005_instructor_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructor',
            name='ville',
            field=models.CharField(default='Abobo', max_length=255),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='classe',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='instructors', to='school.Classe'),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='images/instructors/'),
        ),
    ]
