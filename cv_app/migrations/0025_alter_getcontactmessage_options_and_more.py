# Generated by Django 5.0.1 on 2024-01-30 16:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cv_app', '0024_rename_contactmessage_getcontactmessage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='getcontactmessage',
            options={'verbose_name_plural': '1Get Contact Model'},
        ),
        migrations.RenameField(
            model_name='leftside',
            old_name='skype_link',
            new_name='github_link',
        ),
        migrations.RenameField(
            model_name='leftside',
            old_name='twitter_link',
            new_name='telegram_link',
        ),
    ]
