# Generated by Django 2.2 on 2020-04-03 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chat',
            old_name='reqname',
            new_name='reciever',
        ),
        migrations.RenameField(
            model_name='chat',
            old_name='reqid',
            new_name='recieverid',
        ),
        migrations.RenameField(
            model_name='chat',
            old_name='user',
            new_name='sender',
        ),
    ]