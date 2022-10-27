# Generated by Django 4.1.2 on 2022-10-27 02:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('permission', '0004_alter_postmanager_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmanager',
            name='post',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='permission.post'),
        ),
        migrations.AlterField(
            model_name='postmanager',
            name='status',
            field=models.CharField(choices=[('RJ', 'REJECT'), ('AP', 'APPROVE'), ('W', 'Waiting')], default='Waiting', max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_blogger',
            field=models.BooleanField(default=False, help_text='Can update posts'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_manager',
            field=models.BooleanField(default=False, help_text='Can approve posts'),
        ),
    ]
