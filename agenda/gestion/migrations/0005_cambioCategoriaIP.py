# Generated by Django 4.0.3 on 2022-04-07 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0004_descpticionNUlleable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tareas',
            name='categoria',
            field=models.CharField(choices=[('TODO', 'TO_DO'), ('IP', 'IN_PROGRESS'), ('DONE', 'DONE'), ('CANCELLED', 'CANCELLED')], default='TODO', max_length=45),
        ),
    ]
