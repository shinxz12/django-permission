# Generated by Django 4.1.2 on 2022-10-27 02:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('permission', '0005_alter_postmanager_post_alter_postmanager_status_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogger',
            options={'permissions': [('search_blogger', 'Can search blogger')]},
        ),
    ]