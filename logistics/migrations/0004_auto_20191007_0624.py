# Generated by Django 2.2 on 2019-10-06 21:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logistics', '0003_auto_20191007_0541'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staffschedule',
            old_name='name',
            new_name='staff',
        ),
    ]
