# Generated by Django 5.1.4 on 2024-12-27 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_profile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]