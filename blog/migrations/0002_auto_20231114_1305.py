# Generated by Django 2.2.28 on 2023-11-14 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipement',
            name='taille_max',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='equipement',
            name='disponibilite',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='equipement',
            name='photo',
            field=models.CharField(max_length=2000),
        ),
    ]