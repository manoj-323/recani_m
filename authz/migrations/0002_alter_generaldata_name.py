# Generated by Django 5.0.6 on 2024-06-11 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generaldata',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
