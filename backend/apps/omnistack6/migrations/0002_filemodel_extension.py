# Generated by Django 3.2 on 2022-03-29 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('omnistack6', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='filemodel',
            name='extension',
            field=models.CharField(blank=True, max_length=10, verbose_name='File extension'),
        ),
    ]
