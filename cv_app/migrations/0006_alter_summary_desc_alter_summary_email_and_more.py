# Generated by Django 5.0.1 on 2024-01-26 09:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv_app', '0005_alter_education_end_year_alter_education_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='summary',
            name='desc',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='summary',
            name='email',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='summary_email', to='cv_app.contactme'),
        ),
        migrations.AlterField(
            model_name='summary',
            name='name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='summary_name', to='cv_app.aboutme'),
        ),
        migrations.AlterField(
            model_name='summary',
            name='number',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='summary_number', to='cv_app.contactme'),
        ),
        migrations.AlterField(
            model_name='summary',
            name='part',
            field=models.CharField(blank=True, max_length=55, null=True),
        ),
        migrations.AlterField(
            model_name='summary',
            name='place',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='summary_place', to='cv_app.contactme'),
        ),
    ]
