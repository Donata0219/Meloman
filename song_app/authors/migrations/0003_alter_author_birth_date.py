# Generated by Django 4.2.1 on 2023-05-22 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0002_alter_author_birth_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='birth_date',
            field=models.DateField(help_text='iveskite data', null=True),
        ),
    ]