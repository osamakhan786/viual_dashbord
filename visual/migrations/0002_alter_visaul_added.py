# Generated by Django 5.0.6 on 2024-05-23 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visual', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visaul',
            name='added',
            field=models.CharField(max_length=100),
        ),
    ]
