# Generated by Django 5.0.1 on 2024-01-28 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cv_app', '0013_alter_projectimages_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projectimages',
            old_name='portfolio',
            new_name='img_portfolio',
        ),
    ]
