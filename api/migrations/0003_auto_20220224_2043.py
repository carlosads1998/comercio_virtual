# Generated by Django 2.2.9 on 2022-02-24 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20220224_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loja',
            name='nome',
            field=models.CharField(max_length=100),
        ),
    ]
