# Generated by Django 5.0.1 on 2024-01-28 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv_app', '0008_remove_projectimages_project_id_project_images_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectimages',
            name='name',
            field=models.CharField(blank=True, max_length=550, null=True),
        ),
    ]
