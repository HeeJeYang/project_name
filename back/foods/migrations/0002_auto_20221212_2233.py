# Generated by Django 3.2.13 on 2022-12-12 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='image',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='menu',
            name='recipe',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='foods.recipe'),
        ),
    ]
