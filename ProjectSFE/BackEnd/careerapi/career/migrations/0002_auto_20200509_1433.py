# Generated by Django 3.0.5 on 2020-05-09 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='external_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
