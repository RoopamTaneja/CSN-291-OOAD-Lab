# Generated by Django 4.2.5 on 2023-11-03 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_data', '0009_alter_credential_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='credential',
            name='strength',
            field=models.CharField(default='', max_length=50),
        ),
    ]
