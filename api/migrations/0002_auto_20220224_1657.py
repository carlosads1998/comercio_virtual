# Generated by Django 2.2.9 on 2022-02-24 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loja',
            name='valor',
            field=models.DecimalField(decimal_places=2, max_digits=20),
        ),
    ]
