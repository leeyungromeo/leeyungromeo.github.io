# Generated by Django 3.2.8 on 2022-02-20 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20220220_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commande',
            name='adress_text',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='commande',
            name='numero_gsm',
            field=models.IntegerField(default=0),
        ),
    ]