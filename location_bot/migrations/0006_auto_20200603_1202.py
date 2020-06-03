# Generated by Django 3.0.6 on 2020-06-03 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location_bot', '0005_auto_20200602_2233'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Messages',
        ),
        migrations.RemoveField(
            model_name='vk_sender',
            name='key',
        ),
        migrations.RemoveField(
            model_name='vk_sender',
            name='messages',
        ),
        migrations.RemoveField(
            model_name='vk_sender',
            name='messages_count',
        ),
        migrations.AddField(
            model_name='vk_sender',
            name='message',
            field=models.TextField(blank=True),
        ),
    ]