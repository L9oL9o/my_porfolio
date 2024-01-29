# Generated by Django 5.0.1 on 2024-01-29 11:12

import django.db.models.deletion
import mptt.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv_app', '0019_remove_projectimages_slug_portfolio_client_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='level',
            field=models.PositiveIntegerField(default='0', editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='portfolio',
            name='lft',
            field=models.PositiveIntegerField(default='0', editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='portfolio',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='cv_app.portfolio'),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='rght',
            field=models.PositiveIntegerField(default='0', editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='portfolio',
            name='tree_id',
            field=models.PositiveIntegerField(db_index=True, default='0', editable=False),
            preserve_default=False,
        ),
    ]
