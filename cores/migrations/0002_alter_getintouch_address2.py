# Generated by Django 4.2 on 2024-06-24 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cores', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='getintouch',
            name='address2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
